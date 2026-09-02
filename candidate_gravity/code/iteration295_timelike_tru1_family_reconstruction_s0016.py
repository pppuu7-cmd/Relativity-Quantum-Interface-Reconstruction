#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 295.

Directly reconstruct all non-scaleless weight-completed [Tr U1]_{sab} family
numerators at the frozen timelike row s=0.016.  External momenta and TT
polarizations are timelike-row data themselves; no spacelike coefficient set is
continued by rotating denominators.

This script intentionally mirrors the exact Iteration-292 primitive Q/A/Y
construction, but builds it for the timelike model M(s=0.016).  Canonical loop
routing uses only p=sigma*l+delta with sigma=+/-1.
"""
import importlib.util, itertools, json
from collections import Counter, defaultdict
from pathlib import Path
import numpy as np

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('i273',HERE/'iteration273_closed_kinematics_physical_b3.py')
i273=importlib.util.module_from_spec(spec); spec.loader.exec_module(i273)
m=i273.m
ETA=m.ETA; P0=m.P0.copy(); KS=m.K_S.copy(); ES=m.E_S.copy(); R0=-ETA.copy(); LEGS=('s','a','b')
S=0.016
a0=(.46+S)/.2
KA=np.array([a0,.6,.3,a0-.1]); KB=-(KS+KA)
M={'s':(KS,ES),'a':(KA,m.tt_pol(KA,[.2,-.5,.7])),'b':(KB,m.tt_pol(KB,[.8,.1,.3]))}


def mdot(x,y): return float(np.asarray(x)@ETA@np.asarray(y))
def ksum(legs): return sum((M[x][0] for x in legs),np.zeros(4))
def pk(p): return tuple(np.round(np.asarray(p,float),11))
def p2(p): return mdot(p,p)

def ycoef(legs,h=2e-5):
    legs=tuple(legs)
    if not legs: return m.y_down([],[])
    modes=[M[x] for x in legs]; out=np.zeros((4,4),complex)
    for sig in itertools.product([-1,1],repeat=len(legs)):
        out += np.prod(sig)*m.y_down([z*h for z in sig],modes)
    return out/(2*h)**len(legs)
YC={}
def yy(legs):
    k=tuple(legs)
    if k not in YC: YC[k]=ycoef(k)
    return YC[k]

N1C={}; N2C={}; AC={}
def n1(x,p):
    k=(x,pk(p))
    if k not in N1C: N1C[k]=m.N1(M,x,np.asarray(p,float))
    return N1C[k]
def n2(x,y,p):
    k=(x,y,pk(p))
    if k not in N2C: N2C[k]=m.N2(M,x,y,np.asarray(p,float))
    return N2C[k]
def aa(legs,p):
    k=(tuple(legs),pk(p))
    if k not in AC: AC[k]=m.Asub(M,legs,np.asarray(p,float))
    return AC[k]

def qdescs(legs,base):
    legs=tuple(legs); base=np.asarray(base,float)
    if len(legs)==0: return [{'kind':'Q0','legs':legs,'base':base,'den':[base]}]
    if len(legs)==1:
        x=legs[0]; return [{'kind':'Q1','legs':legs,'base':base,'den':[base+M[x][0],base]}]
    x,y=legs
    return [
      {'kind':'Q2_seq_xy','legs':legs,'base':base,'den':[base+M[x][0]+M[y][0],base+M[y][0],base]},
      {'kind':'Q2_seq_yx','legs':legs,'base':base,'den':[base+M[x][0]+M[y][0],base+M[x][0],base]},
      {'kind':'Q2_contact','legs':legs,'base':base,'den':[base+M[x][0]+M[y][0],base]},
    ]
def qnum(d,p):
    arg=np.asarray(p)+d['base']; legs=d['legs']
    if d['kind']=='Q0': return R0
    if d['kind']=='Q1': return -R0@n1(legs[0],arg)@R0
    x,y=legs
    if d['kind']=='Q2_seq_xy': return R0@n1(x,arg+M[y][0])@R0@n1(y,arg)@R0
    if d['kind']=='Q2_seq_yx': return R0@n1(y,arg+M[x][0])@R0@n1(x,arg)@R0
    if d['kind']=='Q2_contact': return -R0@n2(x,y,arg)@R0
    raise RuntimeError(d['kind'])


def signature(global_den):
    # Multiplicity pattern + all pairwise invariant separations +, for raised
    # triangles, invariants from the repeated point uniquely identify the family.
    keys=[tuple(np.round(v,12)) for v in global_den]
    mult=Counter(keys); pts=[np.asarray(k,float) for k in mult]
    counts=tuple(sorted(mult.values(),reverse=True))
    pair=tuple(sorted(round(mdot(pts[j]-pts[i],pts[j]-pts[i]),12)
                      for i in range(len(pts)) for j in range(i+1,len(pts))))
    repeated=None
    if 2 in mult.values():
        rp=np.asarray(next(k for k,n in mult.items() if n==2),float)
        repeated=tuple(sorted(round(mdot(np.asarray(k,float)-rp,np.asarray(k,float)-rp),12)
                              for k,n in mult.items() if n==1))
    if counts==(2,): fam='single_scaleless'
    elif counts==(2,1): fam='raised_bubble'
    elif counts==(2,1,1): fam='raised_triangle'
    elif counts==(1,1): fam='ordinary_bubble'
    elif counts==(1,1,1): fam='ordinary_triangle'
    else: raise RuntimeError((counts,pair,repeated))
    return fam,counts,pair,repeated

D=[]
for ydeg in (0,1,2):
  for Ylegs in itertools.combinations(LEGS,ydeg):
    Blegs=tuple(x for x in LEGS if x not in Ylegs)
    if not Blegs: continue
    yshift=ksum(Ylegs)
    for ass in itertools.product('LMR',repeat=len(Blegs)):
      L=tuple(Blegs[i] for i,a in enumerate(ass) if a=='L')
      A=tuple(Blegs[i] for i,a in enumerate(ass) if a=='M')
      R=tuple(Blegs[i] for i,a in enumerate(ass) if a=='R')
      if not A or A==('s',): continue
      for ld in qdescs(L,ksum(R)+ksum(A)):
       for rd in qdescs(R,np.zeros(4)):
        den=[yshift+v for v in ld['den']+rd['den']]
        fam,counts,pair,repeated=signature(den)
        D.append({'Y':Ylegs,'B':Blegs,'L':L,'A':A,'R':R,'ld':ld,'rd':rd,
                  'yshift':yshift,'den':den,'family':fam,'counts':counts,
                  'pair':pair,'repeated':repeated})

def numerator(d,p):
    bp=np.asarray(p)+d['yshift']
    return np.trace(qnum(d['ld'],bp) @ aa(d['A'],bp+ksum(d['R'])) @ qnum(d['rd'],bp) @ yy(d['Y']))

def dprod(d,p):
    z=1.0
    for v in d['den']: z*=p2(np.asarray(p)+v)
    return z

# Direct cross-check at P0.
def Bcoef(legs,p,h1=1e-4,h2=5e-4,h3=1e-3):
    legs=tuple(legs); out=np.zeros((4,4),complex)
    for ass in itertools.product('LMR',repeat=len(legs)):
      L=tuple(legs[i] for i,a in enumerate(ass) if a=='L')
      A=tuple(legs[i] for i,a in enumerate(ass) if a=='M')
      R=tuple(legs[i] for i,a in enumerate(ass) if a=='R')
      if not A or A==('s',): continue
      out += m.term(M,L,A,R,np.asarray(p),h1,h2,h3)
    return out
direct=0j
for ydeg in (0,1,2):
  for Ylegs in itertools.combinations(LEGS,ydeg):
    Blegs=tuple(x for x in LEGS if x not in Ylegs)
    if not Blegs: continue
    direct += np.trace(Bcoef(Blegs,P0+ksum(Ylegs))@yy(Ylegs))
primitive=sum(numerator(d,P0)/dprod(d,P0) for d in D)

# Group by exact denominator signature; determine scaleless families from all
# external squared separations zero.
groups=defaultdict(list)
for d in D:
    key=(d['family'],d['pair'],d['repeated'])
    groups[key].append(d)

def is_scaleless(key):
    fam,pair,repeated=key
    if fam=='single_scaleless': return True
    return all(abs(x)<1e-11 for x in pair)
NON=[k for k in groups if not is_scaleless(k)]

# Canonical affine loop routing.
def same_ms(a,b,tol=2e-10):
    aa=sorted((np.asarray(x,float) for x in a),key=lambda z:tuple(np.round(z,12)))
    bb=sorted((np.asarray(x,float) for x in b),key=lambda z:tuple(np.round(z,12)))
    return len(aa)==len(bb) and all(np.max(np.abs(x-y))<tol for x,y in zip(aa,bb))
def route(d,target):
    for sig in (1.0,-1.0):
      for v in d['den']:
       for t in target:
        delta=sig*np.asarray(t)-np.asarray(v)
        got=[sig*(delta+np.asarray(x)) for x in d['den']]
        if same_ms(got,target): return sig,delta
    raise RuntimeError(('route',d['family'],d['pair'],d['repeated']))

DEG={'ordinary_bubble':2,'ordinary_triangle':4,'raised_bubble':4,'raised_triangle':6}
def exponents(deg):
    return [(a,b,c,d) for a in range(deg+1) for b in range(deg+1-a)
            for c in range(deg+1-a-b) for d in range(deg+1-a-b-c)]
def mon(exps,l):
    return np.array([np.prod([l[i]**e[i] for i in range(4)]) for e in exps],float)

def key_name(k):
    fam,pair,rep=k
    def fmt(x): return ('%.6g'%x).replace('-','m').replace('.','p')
    return fam+'__pair_'+'_'.join(fmt(x) for x in pair)+'__rep_'+('none' if rep is None else '_'.join(fmt(x) for x in rep))

def fit_group(k,seed):
    ds=groups[k]; target=[np.asarray(v,float) for v in ds[0]['den']]
    rr=[route(d,target) for d in ds]
    def f(l):
      z=0j
      for d,(sig,delta) in zip(ds,rr): z += numerator(d,sig*np.asarray(l)+delta)
      return z
    deg=DEG[k[0]]; exps=exponents(deg); n=len(exps); rng=np.random.default_rng(seed)
    tr=rng.uniform(-.92,.92,(n+18,4)); ho=rng.uniform(-1.08,1.08,(max(28,n//7),4))
    yc=np.array([f(x) for x in tr]); zc=np.array([f(x) for x in ho])
    X=np.array([mon(exps,x) for x in tr]); H=np.array([mon(exps,x) for x in ho])
    c=np.linalg.lstsq(X,yc.real,rcond=None)[0]; res=H@c-zc.real
    return {'family':k[0],'pair_invariants':list(k[1]),'repeated_vertex_invariants':None if k[2] is None else list(k[2]),
      'degree_ceiling':deg,'basis_size':n,'rank':int(np.linalg.matrix_rank(X)),
      'condition_number':float(np.linalg.cond(X)),'primitive_branch_count':len(ds),
      'route_reflection_count':sum(sig<0 for sig,_ in rr),
      'heldout_max_abs':float(np.max(np.abs(res))),
      'heldout_relative_max':float(np.max(np.abs(res))/max(np.max(np.abs(zc.real)),1e-30)),
      'max_oracle_imag_abs':float(max(np.max(np.abs(yc.imag)),np.max(np.abs(zc.imag)))),
      'canonical_denominator_shifts':[np.asarray(v).tolist() for v in target],
      'monomial_exponents':[list(e) for e in exps],'coefficients':[float(x) for x in c]}

rows={key_name(k):fit_group(k,2950+i) for i,k in enumerate(sorted(NON,key=key_name))}
maxrel=max(v['heldout_relative_max'] for v in rows.values()); maximag=max(v['max_oracle_imag_abs'] for v in rows.values())
fullrank=all(v['rank']==v['basis_size'] for v in rows.values())
cls=('PASS_DIRECT_TIMELIKE_S0016_WEIGHT_COMPLETED_TRU1_ALL_FAMILY_NUMERATOR_RECONSTRUCTION'
     if len(rows)==8 and fullrank and maxrel<3e-5 and maximag<3e-5 else
     'BLOCKED_TIMELIKE_S0016_TRU1_FAMILY_RECONSTRUCTION')
result={
 'iteration':295,'model_readiness_percent':24,'s':S,
 'kinematics':{'ks2':mdot(KS,KS),'ka2':mdot(KA,KA),'kb2':mdot(KB,KB),'ks_dot_ka':mdot(KS,KA)},
 'primitive_branch_count':len(D),'non_scaleless_family_count':len(rows),
 'direct_trace_at_P0':{'real':float(direct.real),'imag':float(direct.imag)},
 'primitive_reconstruction_at_P0':{'real':float(primitive.real),'imag':float(primitive.imag)},
 'primitive_vs_direct_abs_residual':float(abs(primitive-direct)),
 'families':rows,'max_heldout_relative_error':maxrel,'max_oracle_imag_abs':maximag,
 'classification':cls,'candidate_residual':False,
 'guardrails':[
   'NUMERATOR_COEFFICIENTS_ARE_RECONSTRUCTED_DIRECTLY_AT_TIMELIKE_S0016',
   'NO_SPACELIKE_NUMERATOR_COEFFICIENT_ANALYTIC_CONTINUATION_IS_ASSUMED',
   'NEXT_STEP_MAY_EVALUATE_PLUS_MINUS_I0_DR_MASTERS_WITH_THESE_FIXED_TIMELIKE_NUMERATORS'
 ],
 'next_gate':'perform common-normalization DR tensor/Laurent plus-minus-i0 reduction of these eight direct timelike families and extract the e=1,c=2 TrU1 discontinuity/pole structure'
}
assert abs(mdot(KA,KA)+S)<1e-12 and abs(mdot(KB,KB)+(S+.2))<1e-12
assert len(D)==36 and abs(primitive-direct)<2e-5
assert cls.startswith('PASS_DIRECT'),result
print(json.dumps(result,indent=2,sort_keys=True))
