#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 285.

Actual denominator-stripped same-parent numerator oracle and held-out basis audit.
This iteration supersedes the *minimal 9/50 scalar basis* claim of Iterations
283-284 while retaining their exact degree ceilings (bubble <=4, triangle <=6).

The key distinction is that denominator topology does not exhaust numerator
kinematics: the frozen same-parent numerator also contains the null-soft leg and
TT polarization tensors.  Therefore a basis built only from l^2 and l.q_i can
be incomplete even when the denominator family has only one or two q_i.
"""
import importlib.util, itertools, json
from pathlib import Path
from collections import Counter, defaultdict
import numpy as np

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('i273',HERE/'iteration273_closed_kinematics_physical_b3.py')
i273=importlib.util.module_from_spec(spec); spec.loader.exec_module(i273)
m=i273.m
ETA=m.ETA; M=i273.POS; LEGS=('s','a','b'); R0=-ETA.copy()
KS=M['s'][0]; KA=M['a'][0]; KB=M['b'][0]

def mdot(x,y): return float(np.array(x)@ETA@np.array(y))
def vk(v): return tuple(np.round(np.array(v,float),12))
def ksum(legs): return sum((M[x][0] for x in legs),np.zeros(4))

def qdescs(legs,base):
    legs=tuple(legs); base=np.array(base,float)
    if len(legs)==0:
        return [{'kind':'Q0','legs':legs,'base':base,'den':[base]}]
    if len(legs)==1:
        x=legs[0]
        return [{'kind':'Q1','legs':legs,'base':base,'den':[base+M[x][0],base]}]
    x,y=legs
    return [
      {'kind':'Q2_seq_xy','legs':legs,'base':base,'den':[base+M[x][0]+M[y][0],base+M[y][0],base]},
      {'kind':'Q2_seq_yx','legs':legs,'base':base,'den':[base+M[x][0]+M[y][0],base+M[x][0],base]},
      {'kind':'Q2_contact','legs':legs,'base':base,'den':[base+M[x][0]+M[y][0],base]},
    ]

def descriptors():
    out=[]
    for ass in itertools.product('LMR',repeat=3):
      L=tuple(LEGS[i] for i,a in enumerate(ass) if a=='L')
      A=tuple(LEGS[i] for i,a in enumerate(ass) if a=='M')
      R=tuple(LEGS[i] for i,a in enumerate(ass) if a=='R')
      if not A or A==('s',): continue
      for ld in qdescs(L,ksum(R)+ksum(A)):
       for rd in qdescs(R,np.zeros(4)):
        den=ld['den']+rd['den']; mult=Counter(vk(v) for v in den)
        counts=tuple(sorted(mult.values(),reverse=True))
        vv=[np.array(v) for v in mult]
        pairq=tuple(sorted(round(mdot(vv[j]-vv[i],vv[j]-vv[i]),12)
                           for i in range(len(vv)) for j in range(i+1,len(vv))))
        rep=np.array(next(v for v,n in mult.items() if n==2))
        if counts==(2,1,1):
          inc=tuple(sorted(round(mdot(np.array(v)-rep,np.array(v)-rep),12)
                           for v,n in mult.items() if n==1))
          fam='triangle'; sector=f'tri_{inc}'
        elif counts==(2,1):
          fam={0.0:'bubble_null',0.21:'bubble_b',0.41:'bubble_a'}[pairq[0]]; sector=fam
        elif counts==(2,): fam='single_scaleless'; sector=fam
        else: raise RuntimeError((counts,pairq))
        out.append({'L':L,'A':A,'R':R,'ld':ld,'rd':rd,'den':den,'rep':rep,'family':fam,'sector':sector})
    return out
D=descriptors(); assert len(D)==23

N1C={}; N2C={}; AC={}
def pk(p): return tuple(np.round(np.array(p,float),11))
def n1(x,p):
    k=(x,pk(p));
    if k not in N1C: N1C[k]=m.N1(M,x,np.array(p,float))
    return N1C[k]
def n2(x,y,p):
    k=(x,y,pk(p));
    if k not in N2C: N2C[k]=m.N2(M,x,y,np.array(p,float))
    return N2C[k]
def aa(legs,p):
    k=(tuple(legs),pk(p));
    if k not in AC: AC[k]=m.Asub(M,legs,np.array(p,float))
    return AC[k]

def qnum(d,p):
    arg=np.array(p)+d['base']; legs=d['legs']
    if d['kind']=='Q0': return R0
    if d['kind']=='Q1': return -R0@n1(legs[0],arg)@R0
    x,y=legs
    if d['kind']=='Q2_seq_xy': return R0@n1(x,arg+M[y][0])@R0@n1(y,arg)@R0
    if d['kind']=='Q2_seq_yx': return R0@n1(y,arg+M[x][0])@R0@n1(x,arg)@R0
    if d['kind']=='Q2_contact': return -R0@n2(x,y,arg)@R0
    raise RuntimeError(d['kind'])

def bnum(d,p):
    return qnum(d['ld'],p)@aa(d['A'],np.array(p)+ksum(d['R']))@qnum(d['rd'],p)

def p2(p): return mdot(p,p)
def dprod(d,p):
    z=1.0
    for v in d['den']: z*=p2(np.array(p)+v)
    return z

# Primitive oracle exact cross-check against the translation-closed B3 object.
B=np.zeros((4,4),complex)
for d in D: B += bnum(d,i273.P0)/dprod(d,i273.P0)
oracle_crosscheck={
 'trace':float(np.trace(B).real), 'fro':float(np.linalg.norm(B)),
 'matrix_residual_vs_iteration273':float(np.max(np.abs(B-i273.B)))
}

# Canonical orientation: repeated propagator is already p^2 for all closed
# non-scaleless branches.  Branches with simple shifts -q are reflected p=-l
# before sector summation, so every bubble uses l^4(l+q)^2.
def simples(d):
    mult=Counter(vk(v) for v in d['den'])
    return [np.array(v) for v,n in mult.items() if n==1]
def same(a,b,tol=1e-10): return np.max(np.abs(np.array(a)-np.array(b)))<tol

def bubble_trace(fam,q,l):
    z=0j
    for d in [x for x in D if x['family']==fam]:
      u=simples(d)[0]
      if same(u,q): p=l
      elif same(u,-q): p=-np.array(l)
      else: raise RuntimeError((fam,u,q))
      z+=np.trace(bnum(d,p))
    return float(z.real)

PAIR={
 'tri_(0.0, 0.21)':(-KS,KB),
 'tri_(0.0, 0.41)':(-KS,KA),
 'tri_(0.21, 0.41)':(-KA,KB),
}
def pairmatch(s,q1,q2):
    return (same(s[0],q1) and same(s[1],q2)) or (same(s[1],q1) and same(s[0],q2))
def tri_trace(sec,l):
    q1,q2=PAIR[sec]; z=0j
    for d in [x for x in D if x['sector']==sec]:
      s=simples(d)
      if pairmatch(s,q1,q2): p=l
      elif pairmatch(s,-q1,-q2): p=-np.array(l)
      else: raise RuntimeError((sec,s))
      z+=np.trace(bnum(d,p))
    return float(z.real)

BE=[(a,b) for a in range(3) for b in range(4-2*a+1)]
TE=[(a,b,c) for a in range(4) for b in range(6-2*a+1) for c in range(6-2*a-b+1)]
MON4=[(e0,e1,e2,e3) for e0 in range(5) for e1 in range(5-e0)
      for e2 in range(5-e0-e1) for e3 in range(5-e0-e1-e2)]
MON6=[(e0,e1,e2,e3) for e0 in range(7) for e1 in range(7-e0)
      for e2 in range(7-e0-e1) for e3 in range(7-e0-e1-e2)]
assert len(BE)==9 and len(TE)==50 and len(MON4)==70 and len(MON6)==210

def b9(q,l):
    return np.array([(mdot(l,l)**a)*(mdot(l,q)**b) for a,b in BE])
def t50(q1,q2,l):
    return np.array([(mdot(l,l)**a)*(mdot(l,q1)**b)*(mdot(l,q2)**c) for a,b,c in TE])
def mon(exps,l):
    l=np.array(l); return np.array([np.prod([l[i]**e[i] for i in range(4)]) for e in exps])
def fitmetric(X,H,y,z):
    c=np.linalg.lstsq(X,y,rcond=None)[0]; r=H@c-z
    return {'train_rank':int(np.linalg.matrix_rank(X)),'basis_size':int(X.shape[1]),
            'condition_number':float(np.linalg.cond(X)),
            'heldout_max_abs':float(np.max(np.abs(r))),
            'heldout_rms':float(np.sqrt(np.mean(r*r))),
            'heldout_rel_max':float(np.max(np.abs(r))/max(np.max(np.abs(z)),1e-30))}

def bubble_audit(fam,q,seed):
    rng=np.random.default_rng(seed); tr=rng.uniform(-1.15,1.15,(82,4)); ho=rng.uniform(-1.25,1.25,(28,4))
    y=np.array([bubble_trace(fam,q,l) for l in tr]); z=np.array([bubble_trace(fam,q,l) for l in ho])
    return {'topology_only_9':fitmetric(np.array([b9(q,l) for l in tr]),np.array([b9(q,l) for l in ho]),y,z),
            'full_coordinate_degree4_70':fitmetric(np.array([mon(MON4,l) for l in tr]),np.array([mon(MON4,l) for l in ho]),y,z)}

bubbles={'bubble_a':bubble_audit('bubble_a',KA,285),'bubble_b':bubble_audit('bubble_b',KB,286)}

# One triangle sector is sufficient to falsify the topology-only 50 basis and
# to certify existence of a conservative complete degree<=6 reconstruction.
sec='tri_(0.0, 0.41)'; q1,q2=PAIR[sec]
rng=np.random.default_rng(287); tr=rng.uniform(-1.05,1.05,(88,4)); ho=rng.uniform(-1.15,1.15,(30,4))
y=np.array([tri_trace(sec,l) for l in tr]); z=np.array([tri_trace(sec,l) for l in ho])
tri50=fitmetric(np.array([t50(q1,q2,l) for l in tr]),np.array([t50(q1,q2,l) for l in ho]),y,z)
rng=np.random.default_rng(2881); tr=rng.uniform(-.95,.95,(232,4)); ho=rng.uniform(-1.05,1.05,(36,4))
y=np.array([tri_trace(sec,l) for l in tr]); z=np.array([tri_trace(sec,l) for l in ho])
tri210=fitmetric(np.array([mon(MON6,l) for l in tr]),np.array([mon(MON6,l) for l in ho]),y,z)

result={
 'iteration':285,'model_readiness_percent':24,
 'oracle_crosscheck':oracle_crosscheck,
 'degree_bounds_retained':{'bubble':4,'triangle':6},
 'bubbles':bubbles,
 'triangle_test_sector':sec,
 'triangle_topology_only_50':tri50,
 'triangle_full_coordinate_degree6_210':tri210,
 'classification':'PASS_ACTUAL_NUMERATOR_ORACLE_AND_FAIL_TOPOLOGY_ONLY_9_50_BASIS_WITH_COMPLETE_70_210_RECONSTRUCTION_CERTIFICATES',
 'supersedes':'Iterations 283-284 minimal 9/50 numerator-basis sufficiency; exact degree ceilings and denominator canonicalization remain valid',
 'guardrail':'DENOMINATOR TOPOLOGY DOES NOT REMOVE SOFT-MOMENTUM_OR_TT-POLARIZATION DEPENDENCE FROM THE NUMERATOR',
 'candidate_residual':False,
 'next_gate':286,
}
assert oracle_crosscheck['matrix_residual_vs_iteration273']<1e-10
assert bubbles['bubble_a']['topology_only_9']['heldout_rel_max']>.5
assert bubbles['bubble_b']['topology_only_9']['heldout_rel_max']>.5
assert bubbles['bubble_a']['full_coordinate_degree4_70']['heldout_rel_max']<1e-6
assert bubbles['bubble_b']['full_coordinate_degree4_70']['heldout_rel_max']<1e-6
assert tri50['heldout_rel_max']>1.0
assert tri210['heldout_rel_max']<1e-7
print(json.dumps(result,indent=2,sort_keys=True))
