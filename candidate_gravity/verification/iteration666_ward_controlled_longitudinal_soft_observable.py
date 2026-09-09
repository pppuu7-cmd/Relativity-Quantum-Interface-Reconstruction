#!/usr/bin/env python3
from pathlib import Path
import json
R=Path(__file__).resolve().parents[2]
fail=[]
def load(p):
 q=R/p
 if not q.exists(): fail.append('missing:'+p); return {}
 d=json.loads(q.read_text())
 if d.get('scientific_gate_pass') is not True: fail.append('nonpass:'+p)
 return d
a=load('candidate_gravity/results/iteration653_closed_sk_gamma2_gamma3_ward_contract.json')
b=load('candidate_gravity/results/iteration664_null_ward_transverse_no_go.json')
c=load('candidate_gravity/results/iteration665_prospective_noncollinear_soft_redesign_authority.json')
ward=a.get('Ward_map',{})
identity=ward.get('action_identity','')
if 'Gamma3[L_xi,h2,h3]' not in identity or 'Gamma2' not in identity: fail.append('missing normalized longitudinal Ward identity')
if b.get('checks',{}).get('dim_transverse_gauge_quotient')!=3: fail.append('Iter664 quotient drift')
if c.get('frozen_contract',{}).get('Rz_pi_over_2_stabilizes_full_kinematics') is not False: fail.append('Iter665 contract drift')
# A longitudinal soft insertion L_xi lies in the Ward-controlled gauge image. Its Gamma3 contraction is fixed by
# same-parent Gamma2 contact/Lie-derivative terms. This is a controlled identity but not a physical transverse
# soft observable and therefore cannot replace the blocked plus-TT T_cut coordinate.
out={'iteration':666,'date':'2026-09-09','MODEL_READINESS':'24%','scientific_gate_pass':not fail,'failures':fail,
 'blocked':not fail,
 'classification':('BLOCKED_ITER666_LONGITUDINAL_MIXED_SOFT_INSERTION_IS_SAME_PARENT_WARD_CONTROLLED_BY_GAMMA2_BUT_LIES_IN_GAUGE_IMAGE__NOT_A_PHYSICAL_TRANSVERSE_TCUT__NON_RESIDUAL' if not fail else 'FAIL_ITER666_WARD_CONTROLLED_LONGITUDINAL_SOFT_AUDIT'),
 'controlled_identity':identity,
 'result':'The L_xi soft insertion is exactly controlled by the normalized same-parent Gamma3/Gamma2 Ward identity, but it is longitudinal/gauge-image data. It cannot be promoted to the physical transverse plus-TT T_cut left undetermined by Iter664.',
 'noncollinear_contract_compatible':True,
 'native_soft_Tcut':'BLOCKED_PHYSICAL_TRANSVERSE_SOFT_INPUT_STILL_REQUIRED','source_born_subtraction':'NOT_PERFORMED','zero_fill':False,
 'ANSATZ_003':'FORBIDDEN','Fisher_resources':'FORBIDDEN',
 'exact_next_gate':'Iteration667: authority-improvement gate for a physical gauge-invariant soft observable: derive from same-parent closed-SK generating functional plus detector/asymptotic observable map, or prove no such committed map exists and freeze the transverse T_cut branch as externally blocked; do not use a pure-gauge Ward insertion as residual.'}
p=R/'candidate_gravity/results/iteration666_ward_controlled_longitudinal_soft_observable.json'; p.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print(json.dumps(out,indent=2,sort_keys=True))
if fail: raise SystemExit(2)
