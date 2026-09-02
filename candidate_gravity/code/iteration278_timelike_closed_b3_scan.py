#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 278.

Controlled Lorentzian continuation of the translation-closed null-soft B3
certificate onto the positive timelike s rows used by the earlier RQIR
absorptive protocol.  This is a scoped continuation slice, not yet the final
source-completed T_cut.

Frozen:
  k_s=(1,0,0,1), k_s^2=0
  k_s.k_a=-0.1 (preserve the Iteration-273 checkpoint transfer invariant)
  k_ax=0.6, k_ay=0.3
  k_a^2=-s, s=0.004,...,0.032
  k_b=-(k_s+k_a)
"""
import importlib.util, json
from pathlib import Path
import numpy as np

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('i273',HERE/'iteration273_closed_kinematics_physical_b3.py')
i273=importlib.util.module_from_spec(spec); spec.loader.exec_module(i273)
m=i273.m
ETA=m.ETA; P0=m.P0; KS=m.K_S.copy(); ES=m.E_S.copy()

rows=[]
for s in np.arange(.004,.033,.004):
    # With az=a0-0.1 and transverse square .45:
    # ka^2=.46-.2*a0=-s.
    a0=(.46+s)/.2
    KA=np.array([a0,.6,.3,a0-.1])
    KB=-(KS+KA)
    EA=m.tt_pol(KA,[.2,-.5,.7]); EB=m.tt_pol(KB,[.8,.1,.3])
    POS={'s':(KS,ES),'a':(KA,EA),'b':(KB,EB)}
    NEG={x:(-k,e) for x,(k,e) in POS.items()}
    B,_=i273.build_B(POS,P0)
    Bn,_=i273.build_B(NEG,P0)
    rows.append({
      's':float(s),'ka':KA.tolist(),'kb':KB.tolist(),
      'ka2':float(KA@ETA@KA),'kb2':float(KB@ETA@KB),
      'ks_dot_ka':float(KS@ETA@KA),
      'Bfro':float(np.linalg.norm(B)),'Bmax':float(np.max(np.abs(B))),
      'orbit_trace_real':float(np.trace(B).real),'orbit_trace_imag':float(np.trace(B).imag),
      'endpoint_transpose_residual':float(np.max(np.abs(B.T-Bn))),
      'A1_soft_norm':float(np.linalg.norm(m.Asub(POS,('s',),P0))),
    })

# step-stability checks at first/middle/last row
stability=[]
for s in [.004,.016,.032]:
    a0=(.46+s)/.2; KA=np.array([a0,.6,.3,a0-.1]); KB=-(KS+KA)
    POS={'s':(KS,ES),'a':(KA,m.tt_pol(KA,[.2,-.5,.7])),'b':(KB,m.tt_pol(KB,[.8,.1,.3]))}
    vals=[]
    for h2,h3 in [(1e-3,2e-3),(7e-4,1.5e-3),(5e-4,1e-3),(3e-4,8e-4)]:
      B,_=i273.build_B(POS,P0,1e-4,h2,h3)
      vals.append({'h_A2':h2,'h_A3':h3,'Bfro':float(np.linalg.norm(B)),'trace':float(np.trace(B).real)})
    f=[x['Bfro'] for x in vals]; t=[x['trace'] for x in vals]
    stability.append({'s':s,'rows':vals,
      'Bfro_relative_spread':(max(f)-min(f))/max(f),
      'trace_relative_spread':(max(t)-min(t))/max(abs(np.array(t)))})

result={
 'iteration':278,'model_readiness_percent':24,
 'continuation_slice':"ks null fixed; ks.ka=-0.1; ka_x=0.6; ka_y=0.3; ka^2=-s; kb=-(ks+ka)",
 'timelike_s_rows':[float(x) for x in np.arange(.004,.033,.004)],
 'rows':rows,'stability':stability,
 'classification':'PASS_SCOPED_TIMELIKE_TRANSLATION_CLOSED_B3_ORBIT_TRACE_NONZERO_ON_ALL_EIGHT_ROWS',
 'guardrails':[
   'THIS_IS_A_CONTROLLED_TIMELIKE_CONTINUATION_SLICE_NOT_YET_THE_UNIQUE_SOURCE_COMPLETED_T_CUT_ROW_DEFINITION',
   'NONZERO_TIMELIKE_NUMERATOR_DOES_NOT_BY_ITSELF_EQUAL_A_NONZERO_DISCONTINUITY_COEFFICIENT'
 ],
 'next_gate':'resolve the non-scaleless bubble/triangle family contributions on the same timelike slice and map their scalar master branch cuts before tensor reduction'
}
assert all(r['ka2']<0 and r['kb2']<0 for r in rows)
assert all(abs(r['orbit_trace_real'])>10 for r in rows)
assert max(r['endpoint_transpose_residual'] for r in rows)<1e-6
print(json.dumps(result,indent=2,sort_keys=True))
