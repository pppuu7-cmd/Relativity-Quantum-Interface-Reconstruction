#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 291.

Audit the exact relation between the weighted symmetric kernel

    B = U1 W = Q A Q

used in Iterations 260--289 and the actual one-loop insertion trace Tr U1.
Since W^{-1}=Y_down, the physical operator is U1 = B Y_down.  Therefore the
mixed cubic background coefficient of Tr U1 is NOT trace(B3) when Y_down is
background dependent.

On the frozen translation-closed Iteration-273 kinematics, construct B1/B2/B3
with exact routed convolution bookkeeping and Y_down coefficients through
second mixed order, then evaluate the complete cubic coefficient

 [Tr U1]_{sab} = tr(B3 Y0)
                + tr(B2[sa](p+kb) Y1[b])
                + tr(B2[sb](p+ka) Y1[a])
                + tr(B2[ab](p+ks) Y1[s])
                + tr(B1[s](p+ka+kb) Y2[ab])
                + tr(B1[a](p+ks+kb) Y2[sb])
                + tr(B1[b](p+ks+ka) Y2[sa]).

The B1[s] term should vanish on the frozen null-TT soft leg.  This script is a
provenance/weight-completion certificate only; no loop integration is done.
"""
import importlib.util, itertools, json
from pathlib import Path
import numpy as np

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('i273',HERE/'iteration273_closed_kinematics_physical_b3.py')
i273=importlib.util.module_from_spec(spec); spec.loader.exec_module(i273)
m=i273.m
POS=i273.POS; P0=i273.P0.copy(); LEGS=('s','a','b')


def ksum(legs):
    return sum((POS[x][0] for x in legs),np.zeros(4))


def Bcoef(legs,p,h1=1e-4,h2=5e-4,h3=1e-3):
    """Mixed coefficient of B=QAQ for distinct named external legs."""
    legs=tuple(legs); out=np.zeros((4,4),complex); rows=[]
    for assign in itertools.product('LMR',repeat=len(legs)):
        L=tuple(legs[i] for i,a in enumerate(assign) if a=='L')
        Md=tuple(legs[i] for i,a in enumerate(assign) if a=='M')
        R=tuple(legs[i] for i,a in enumerate(assign) if a=='R')
        if not Md: continue
        # Q3 is never needed because A0=0; for <=3 total legs this is safe.
        T=m.term(POS,L,Md,R,p,h1,h2,h3)
        out+=T; rows.append((L,Md,R))
    return out,rows


def Ycoef(legs,h=2e-5):
    """Mixed coefficient of Y_down=sqrt(|g|) g for 0,1,2 distinct legs."""
    legs=tuple(legs)
    if not legs:
        return m.y_down([],[])
    modes=[POS[x] for x in legs]
    out=np.zeros((4,4),complex)
    for sig in itertools.product([-1,1],repeat=len(legs)):
        out += np.prod(sig)*m.y_down([s*h for s in sig],modes)
    return out/(2*h)**len(legs)

Y0=Ycoef(())
Y1={x:Ycoef((x,)) for x in LEGS}
Y2={tuple(sorted((x,y))):Ycoef((x,y)) for x,y in itertools.combinations(LEGS,2)}

B3,_=Bcoef(LEGS,P0)
B2={}
for x,y in itertools.combinations(LEGS,2):
    other=next(z for z in LEGS if z not in (x,y))
    # Rightmost Y1[other] acts first and shifts the B input momentum.
    B2[(x,y)],_=Bcoef((x,y),P0+POS[other][0])
B1={}
for z in LEGS:
    others=tuple(x for x in LEGS if x!=z)
    B1[z],_=Bcoef((z,),P0+ksum(others))

components={}
components['B3_Y0']=np.trace(B3@Y0)
for x,y in itertools.combinations(LEGS,2):
    other=next(z for z in LEGS if z not in (x,y))
    components[f'B2_{x}{y}_Y1_{other}']=np.trace(B2[(x,y)]@Y1[other])
for z in LEGS:
    others=tuple(x for x in LEGS if x!=z)
    key=tuple(sorted(others))
    components[f'B1_{z}_Y2_{others[0]}{others[1]}']=np.trace(B1[z]@Y2[key])

complete=sum(components.values())
old_proxy=np.trace(B3)
flat_weight=np.trace(B3@Y0)
weight_dressing=complete-flat_weight

# Analytic TT first-order expectation Y1=e and soft B1=0 are useful regressions.
y1_err=max(float(np.max(np.abs(Y1[x]-POS[x][1]))) for x in LEGS)
soft_b1=float(np.linalg.norm(B1['s']))

result={
 'iteration':291,
 'model_readiness_percent':24,
 'identity':'U1 = B Y_down with B=U1 W=Q A Q',
 'translation_closed':bool(np.max(np.abs(ksum(LEGS)))<1e-14),
 'old_proxy_trace_B3':{'real':float(old_proxy.real),'imag':float(old_proxy.imag)},
 'flat_weight_trace_B3_Y0':{'real':float(flat_weight.real),'imag':float(flat_weight.imag)},
 'weight_dressing_sum':{'real':float(weight_dressing.real),'imag':float(weight_dressing.imag)},
 'complete_cubic_trace_U1_at_fixed_loop_momentum':{'real':float(complete.real),'imag':float(complete.imag)},
 'components':{k:{'real':float(v.real),'imag':float(v.imag),'abs':float(abs(v))} for k,v in components.items()},
 'Y0':np.real_if_close(Y0).tolist(),
 'max_Y1_minus_TT_polarization_abs':y1_err,
 'soft_B1_fro':soft_b1,
 'provenance':{
   'B3_background_degree':3,
   'B3_EOM_degree':1,
   'effective_action_sector':'linear-EOM connection sector -(i/2) Tr U1 dressed to total curvature/background order 3',
   'not_equal_to':'cubic-EOM sector +(i/2)Tr(U1 U2)-(i/6)Tr(U1^3)'
 },
 'classification':'PASS_EXACT_U1_TRACE_WEIGHT_COMPLETION_FORMULA_AND_B3_EOM_DEGREE_PROVENANCE',
 'candidate_residual':False,
 'guardrails':[
   'ITERATIONS278_289_TRACE_B3_RESULTS_ARE_WEIGHTED_KERNEL_PROXY_RESULTS_NOT_TR_U1_AUTHORITY',
   'DO_NOT_USE_TRACE_B3_MASTER_COEFFICIENTS_AS_THE_LINEAR_EOM_EFFECTIVE_ACTION_SECTOR_BEFORE_YDOWN_WEIGHT_COMPLETION',
   'DO_NOT_CONFUSE_BACKGROUND_CUBIC_B3_WITH_EOM_DEGREE3_COMPOSITE_TRACES'
 ],
 'next_gate':'reconstruct the p-dependent complete [Tr U1]_{sab} numerator with Y_down convolution terms, then redo denominator-family/tensor/IR-pole audit for the e=1,c=2 sector before source projection; e=2 and e=3 connection sectors remain separately open'
}
assert result['translation_closed']
assert y1_err < 2e-8
assert soft_b1 < 2e-7
print(json.dumps(result,indent=2,sort_keys=True))
