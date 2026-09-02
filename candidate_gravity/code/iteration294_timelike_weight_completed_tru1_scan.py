#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 294.

Evaluate the actual weight-completed mixed cubic Tr U1 coefficient directly on
the frozen Iteration-278 timelike translation-closed slice.  This avoids using
a spacelike numerator coefficient set while analytically rotating only scalar
denominators.

Frozen slice:
  k_s^2=0, k_s.k_a=-0.1,
  k_a^2=-s, k_b=-(k_s+k_a), hence k_b^2=-(s+0.2),
  s=0.004,...,0.032.
"""
import importlib.util, itertools, json
from pathlib import Path
import numpy as np

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('i273',HERE/'iteration273_closed_kinematics_physical_b3.py')
i273=importlib.util.module_from_spec(spec); spec.loader.exec_module(i273)
m=i273.m
ETA=m.ETA; P0=m.P0.copy(); KS=m.K_S.copy(); ES=m.E_S.copy(); LEGS=('s','a','b')


def ksum(M,legs): return sum((M[x][0] for x in legs),np.zeros(4))
def ycoef(M,legs,h=2e-5):
    legs=tuple(legs)
    if not legs: return m.y_down([],[])
    modes=[M[x] for x in legs]; out=np.zeros((4,4),complex)
    for sig in itertools.product([-1,1],repeat=len(legs)):
        out += np.prod(sig)*m.y_down([z*h for z in sig],modes)
    return out/(2*h)**len(legs)
def Bcoef(M,legs,p,h1=1e-4,h2=5e-4,h3=1e-3):
    legs=tuple(legs); out=np.zeros((4,4),complex)
    for ass in itertools.product('LMR',repeat=len(legs)):
        L=tuple(legs[i] for i,a in enumerate(ass) if a=='L')
        A=tuple(legs[i] for i,a in enumerate(ass) if a=='M')
        R=tuple(legs[i] for i,a in enumerate(ass) if a=='R')
        if not A or A==('s',): continue
        out += m.term(M,L,A,R,np.asarray(p),h1,h2,h3)
    return out

def complete_trace(M,p,h1=1e-4,h2=5e-4,h3=1e-3):
    comps={}; total=0j
    for ydeg in (0,1,2):
      for Ylegs in itertools.combinations(LEGS,ydeg):
        Blegs=tuple(x for x in LEGS if x not in Ylegs)
        if not Blegs: continue
        X=np.trace(Bcoef(M,Blegs,np.asarray(p)+ksum(M,Ylegs),h1,h2,h3) @ ycoef(M,Ylegs))
        comps[f"B{len(Blegs)}_{''.join(Blegs)}_Y{ydeg}_{''.join(Ylegs) or '0'}"]=X
        total += X
    return total,comps

rows=[]; MODELS={}
for s in np.arange(.004,.033,.004):
    a0=(.46+s)/.2
    KA=np.array([a0,.6,.3,a0-.1]); KB=-(KS+KA)
    EA=m.tt_pol(KA,[.2,-.5,.7]); EB=m.tt_pol(KB,[.8,.1,.3])
    M={'s':(KS,ES),'a':(KA,EA),'b':(KB,EB)}; MODELS[round(float(s),3)]=M
    B3=Bcoef(M,LEGS,P0); total,comps=complete_trace(M,P0)
    Y0=ycoef(M,())
    rows.append({
      's':float(s),'ka2':float(KA@ETA@KA),'kb2':float(KB@ETA@KB),
      'translation_residual':float(np.max(np.abs(ksum(M,LEGS)))),
      'old_proxy_trace_B3':float(np.trace(B3).real),
      'flat_weight_trace_B3Y0':float(np.trace(B3@Y0).real),
      'complete_TrU1_cubic':float(total.real),
      'complete_TrU1_imag_abs':float(abs(total.imag)),
      'weight_dressing':float((total-np.trace(B3@Y0)).real),
      'components':{k:float(v.real) for k,v in comps.items()},
      'A1_soft_norm':float(np.linalg.norm(m.Asub(M,('s',),P0)))
    })

stability=[]
for s in (.004,.016,.032):
    M=MODELS[round(s,3)]; vals=[]
    for h2,h3 in [(1e-3,2e-3),(7e-4,1.5e-3),(5e-4,1e-3),(3e-4,8e-4)]:
        z,_=complete_trace(M,P0,1e-4,h2,h3)
        vals.append({'h_A2':h2,'h_A3':h3,'complete_TrU1_cubic':float(z.real)})
    a=np.array([x['complete_TrU1_cubic'] for x in vals])
    stability.append({'s':s,'rows':vals,
      'relative_spread':float((a.max()-a.min())/max(np.max(np.abs(a)),1e-30))})

minabs=min(abs(r['complete_TrU1_cubic']) for r in rows)
maxspread=max(x['relative_spread'] for x in stability)
cls=('PASS_SCOPED_TIMELIKE_TRANSLATION_CLOSED_WEIGHT_COMPLETED_TRU1_NONZERO_ALL_ROWS'
     if minabs>1e-4 and maxspread<2e-3 else
     'BLOCKED_TIMELIKE_WEIGHT_COMPLETED_TRU1_STABILITY')
result={
 'iteration':294,'model_readiness_percent':24,
 'continuation_slice':'ks null fixed; ks.ka=-0.1; ka_x=0.6; ka_y=0.3; ka^2=-s; kb=-(ks+ka)',
 'timelike_s_rows':[float(x) for x in np.arange(.004,.033,.004)],
 'rows':rows,'stability':stability,
 'minimum_abs_complete_TrU1':float(minabs),'max_step_relative_spread':float(maxspread),
 'classification':cls,'candidate_residual':False,
 'guardrails':[
   'THIS_IS_THE_ACTUAL_WEIGHT_COMPLETED_TRU1_FIXED_LOOP_MOMENTUM_NUMERATOR_NOT_YET_ITS_INTEGRATED_DISCONTINUITY',
   'TIMELIKE_NUMERATOR_COEFFICIENTS_SHOULD_BE_RECONSTRUCTED_DIRECTLY_ON_THE_CUT_SLICE_BEFORE_PLUS_MINUS_I0_MASTER_EVALUATION',
   'NONZERO_TRU1_NUMERATOR_IS_NOT_A_CANDIDATE_RESIDUAL'
 ],
 'next_gate':'after Iteration293 structural basis certification, reconstruct complete family coefficients directly at a frozen timelike row (start s=0.016) and evaluate DR plus/minus-i0 cuts without rotating only the denominators'
}
assert all(r['ka2']<0 and r['kb2']<0 for r in rows)
assert all(r['translation_residual']<1e-13 for r in rows)
assert max(r['A1_soft_norm'] for r in rows)<2e-7
assert cls.startswith('PASS_SCOPED'), result
print(json.dumps(result,indent=2,sort_keys=True))
