#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 292.

Exact primitive denominator census for the weight-completed mixed cubic trace
[Tr U1]_{sab} with U1=B Y_down, B=Q A Q.

The rightmost local Y insertion acts first.  It adds no propagator but shifts
the input momentum of the lower-background-order B block.  We enumerate all
primitive Q0/Q1/Q2 recursion branches, classify denominator multiplicities and
external invariant sectors, and cross-check the primitive sum against a direct
matrix evaluation at the frozen Iteration-273 checkpoint.
"""
import importlib.util, itertools, json
from collections import Counter
from pathlib import Path
import numpy as np

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('i273',HERE/'iteration273_closed_kinematics_physical_b3.py')
i273=importlib.util.module_from_spec(spec); spec.loader.exec_module(i273)
m=i273.m
ETA=m.ETA; M=i273.POS; LEGS=('s','a','b'); P0=i273.P0.copy(); R0=-ETA.copy()


def mdot(x,y): return float(np.asarray(x)@ETA@np.asarray(y))
def vk(v): return tuple(np.round(np.asarray(v,float),12))
def ksum(legs): return sum((M[x][0] for x in legs),np.zeros(4))
def p2(p): return mdot(p,p)
def pk(p): return tuple(np.round(np.asarray(p,float),11))

# Local Y_down coefficients.
def ycoef(legs,h=2e-5):
    legs=tuple(legs)
    if not legs: return m.y_down([],[])
    modes=[M[x] for x in legs]; out=np.zeros((4,4),complex)
    for sig in itertools.product([-1,1],repeat=len(legs)):
        out += np.prod(sig)*m.y_down([s*h for s in sig],modes)
    return out/(2*h)**len(legs)

YC={}
def yy(legs):
    k=tuple(legs)
    if k not in YC: YC[k]=ycoef(k)
    return YC[k]

# Primitive Q descriptors, as frozen in the Iteration-285 oracle.
def qdescs(legs,base):
    legs=tuple(legs); base=np.asarray(base,float)
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

# Numerator caches for primitive denominator stripping.
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

def qnum(d,p):
    arg=np.asarray(p)+d['base']; legs=d['legs']
    if d['kind']=='Q0': return R0
    if d['kind']=='Q1': return -R0@n1(legs[0],arg)@R0
    x,y=legs
    if d['kind']=='Q2_seq_xy': return R0@n1(x,arg+M[y][0])@R0@n1(y,arg)@R0
    if d['kind']=='Q2_seq_yx': return R0@n1(y,arg+M[x][0])@R0@n1(x,arg)@R0
    if d['kind']=='Q2_contact': return -R0@n2(x,y,arg)@R0
    raise RuntimeError(d['kind'])

# Enumerate Y/B partitions and primitive Q recursion branches.
def classify(global_den):
    mult=Counter(vk(v) for v in global_den)
    counts=tuple(sorted(mult.values(),reverse=True))
    vv=[np.asarray(v) for v in mult]
    pairq=tuple(sorted(round(mdot(vv[j]-vv[i],vv[j]-vv[i]),12)
                       for i in range(len(vv)) for j in range(i+1,len(vv))))
    if counts==(2,): return 'single_scaleless','single_scaleless',counts,pairq
    if counts==(2,1):
        q2=pairq[0]
        lab={0.0:'raised_bubble_null',0.21:'raised_bubble_b',0.41:'raised_bubble_a'}[q2]
        return 'raised_bubble',lab,counts,pairq
    if counts==(2,1,1):
        rep=np.asarray(next(v for v,n in mult.items() if n==2))
        inc=tuple(sorted(round(mdot(np.asarray(v)-rep,np.asarray(v)-rep),12)
                         for v,n in mult.items() if n==1))
        return 'raised_triangle',f'raised_tri_{inc}',counts,pairq
    if counts==(1,1):
        q2=pairq[0]
        lab={0.0:'ordinary_bubble_null',0.21:'ordinary_bubble_b',0.41:'ordinary_bubble_a'}[q2]
        return 'ordinary_bubble',lab,counts,pairq
    if counts==(1,1,1):
        assert max(abs(a-b) for a,b in zip(pairq,(0.0,0.21,0.41)))<1e-9, pairq
        return 'ordinary_triangle','ordinary_tri_(0.0,0.21,0.41)',counts,pairq
    raise RuntimeError((counts,pairq))

D=[]
for ydeg in (0,1,2):
    for Ylegs in itertools.combinations(LEGS,ydeg):
        Blegs=tuple(x for x in LEGS if x not in Ylegs)
        if not Blegs: continue  # B0=0
        yshift=ksum(Ylegs)
        for ass in itertools.product('LMR',repeat=len(Blegs)):
            L=tuple(Blegs[i] for i,a in enumerate(ass) if a=='L')
            A=tuple(Blegs[i] for i,a in enumerate(ass) if a=='M')
            R=tuple(Blegs[i] for i,a in enumerate(ass) if a=='R')
            if not A or A==('s',): continue
            for ld in qdescs(L,ksum(R)+ksum(A)):
                for rd in qdescs(R,np.zeros(4)):
                    local_den=ld['den']+rd['den']
                    global_den=[yshift+v for v in local_den]
                    fam,sec,counts,pairq=classify(global_den)
                    D.append({'Y':Ylegs,'B':Blegs,'L':L,'A':A,'R':R,
                              'ld':ld,'rd':rd,'yshift':yshift,'den':global_den,
                              'family':fam,'sector':sec,'counts':counts,'pairq':pairq})

# Primitive denominator-stripped trace numerator and denominator product.
def numerator(d,p):
    bp=np.asarray(p)+d['yshift']
    Bn=qnum(d['ld'],bp) @ aa(d['A'],bp+ksum(d['R'])) @ qnum(d['rd'],bp)
    return np.trace(Bn @ yy(d['Y']))
def dprod(d,p):
    z=1.0
    for v in d['den']: z*=p2(np.asarray(p)+v)
    return z

primitive_sum=sum(numerator(d,P0)/dprod(d,P0) for d in D)

# Direct matrix coefficient from exact routed Q/A kernels, independent of denominator stripping.
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
        if not Blegs or Blegs==('s',): continue
        direct += np.trace(Bcoef(Blegs,P0+ksum(Ylegs)) @ yy(Ylegs))

cnt=Counter(d['sector'] for d in D)
famcnt=Counter(d['family'] for d in D)
scaleless={'single_scaleless','raised_bubble_null','ordinary_bubble_null'}
non_scaleless=sum(n for k,n in cnt.items() if k not in scaleless)
by_ydeg=Counter(len(d['Y']) for d in D)

result={
 'iteration':292,'model_readiness_percent':24,
 'translation_closed':bool(np.max(np.abs(ksum(LEGS)))<1e-14),
 'primitive_branch_count':len(D),
 'primitive_branch_count_by_Y_degree':dict(sorted(by_ydeg.items())),
 'family_counts':dict(sorted(famcnt.items())),
 'sector_counts':dict(sorted(cnt.items())),
 'scaleless_sectors':sorted(scaleless),
 'non_scaleless_primitive_branch_count':int(non_scaleless),
 'new_weight_dressing_topologies':['ordinary_bubble','ordinary_triangle'],
 'direct_complete_trace_at_p0':{'real':float(direct.real),'imag':float(direct.imag)},
 'primitive_denominator_reconstruction_at_p0':{'real':float(primitive_sum.real),'imag':float(primitive_sum.imag)},
 'primitive_vs_direct_abs_residual':float(abs(primitive_sum-direct)),
 'classification':'PASS_EXACT_WEIGHT_COMPLETED_TRU1_DENOMINATOR_CENSUS_AND_PRIMITIVE_RECONSTRUCTION',
 'candidate_residual':False,
 'guardrails':[
   'YDOWN_IS_LOCAL_AND_ADDS_NO_PROPAGATOR_BUT_CHANGES_ROUTING_AND_NUMERATOR_CONTRACTION',
   'OLD_RAISED_ONLY_FAMILY_CENSUS_IS_INCOMPLETE_FOR_TRU1_AFTER_WEIGHT_COMPLETION',
   'ORDINARY_BUBBLE_AND_ORDINARY_TRIANGLE_FAMILIES_MUST_BE_INCLUDED_BEFORE_TENSOR_REDUCTION'
 ],
 'next_gate':'fit and held-out validate complete polynomial numerator bases for every non-scaleless raised and ordinary family of [Tr U1]_{sab}; only then perform DR tensor/Laurent reduction'
}
assert result['translation_closed']
assert len(D)==36, len(D)
assert by_ydeg[0]==23 and by_ydeg[1]==11 and by_ydeg[2]==2, by_ydeg
assert non_scaleless==32, non_scaleless
assert result['primitive_vs_direct_abs_residual']<2e-5, result['primitive_vs_direct_abs_residual']
print(json.dumps(result,indent=2,sort_keys=True))
