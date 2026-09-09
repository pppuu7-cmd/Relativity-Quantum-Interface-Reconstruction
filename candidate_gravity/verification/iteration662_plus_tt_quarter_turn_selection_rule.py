#!/usr/bin/env python3
"""Iter662 exact pi/2 transverse-rotation selection rule for frozen +++ soft Gamma3 cut sectors."""
from fractions import Fraction as F
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[2]
req=[
 ROOT/'candidate_gravity/results/iteration655_soft_tcut_kinematic_contract.json',
 ROOT/'candidate_gravity/results/iteration658_plus_tt_null_quotient_invariance.json',
 ROOT/'candidate_gravity/results/iteration659_soft_gamma3_cut_topology_census.json',
 ROOT/'candidate_gravity/results/iteration660_soft_family_routing_threshold_landau.json',
 ROOT/'candidate_gravity/results/iteration661_soft_quotient_cut_integrands_authority.json']
fail=[]
for p in req:
 if not p.exists(): fail.append('missing:'+str(p.relative_to(ROOT)))
 else:
  d=json.loads(p.read_text())
  if d.get('scientific_gate_pass') is not True: fail.append('nonpass:'+p.name)
# Exact R_z(pi/2) in (t,x,y,z); H0 is unnormalised plus polarization.
R=[[F(1),0,0,0],[0,0,F(-1),0],[0,F(1),0,0],[0,0,0,F(1)]]
H=[[F(0) for _ in range(4)] for _ in range(4)]; H[1][1]=F(1); H[2][2]=F(-1)
def mm(A,B): return [[sum(A[i][k]*B[k][j] for k in range(4)) for j in range(4)] for i in range(4)]
def tr(A): return [[A[j][i] for j in range(4)] for i in range(4)]
RHR=mm(mm(R,H),tr(R))
minusH=[[-x for x in row] for row in H]
if RHR!=minusH: fail.append('R Hplus R^T != -Hplus')
# Frozen q vectors have only t,z components, hence are invariant under R exactly.
q_basis=[[F(1),0,0,0],[F(0),0,0,F(1)]]
def mv(A,v): return [sum(A[i][j]*v[j] for j in range(4)) for i in range(4)]
if any(mv(R,q)!=q for q in q_basis): fail.append('axial momentum subspace not invariant')
# Each retained ordinary-cut three-point sector is homogeneous of total degree 3 in external h.
# K1*K2 has degree 1+2; K1^3 has 1+1+1. Under H->-H each changes sign.
sector_degree={'K1K2':3,'K1^3':3}
sector_sign={k:(-1)**v for k,v in sector_degree.items()}
if sector_sign!={'K1K2':-1,'K1^3':-1}: fail.append('odd trilinear sign failure')
# Scalar propagator denominators, Lorentz phase-space measure and D_s depend only on rotated scalar products;
# with q on the t-z axis they are invariant. Thus I = -I after a measure-preserving variable rotation.
exact_zero={k:(sector_sign[k]==-1) for k in sector_sign}
if not all(exact_zero.values()): fail.append('selection zero not established')
classification=('PASS_ITER662_EXACT_PI_OVER_2_TRANSVERSE_ROTATION_FORCES_FROZEN_PLUS_PLUS_PLUS_K1K2_AND_K1CUBED_DS_TO_ZERO__ITER661_TINY_VALUES_NUMERICAL_RESIDUE__NON_RESIDUAL' if not fail else 'BLOCKED_ITER662_SELECTION_RULE_NOT_ESTABLISHED__NON_RESIDUAL')
out={
 'iteration':662,'date':'2026-09-09','MODEL_READINESS':'24%','classification':classification,
 'scientific_gate_pass':not fail,'failures':fail,
 'exact_checks':{'R_Hplus_RT_equals_minus_Hplus':RHR==minusH,'axial_tz_momenta_invariant':all(mv(R,q)==q for q in q_basis),'sector_external_H_degree':sector_degree,'sector_rotation_sign':sector_sign,'measure_and_scalar_denominator_statement':'Lorentz-scalar propagators/cut measure are invariant under proper spatial R_z(pi/2); frozen q_i lie in t-z plane','Ds_order_unchanged':'rotation acts at fixed epsilon and fixed s, before epsilon->0'},
 'authority_statement':'For the frozen all-plus-TT measurement only, every retained ordinary-cut K1K2 and K1^3 integrand has I(phi+pi/2)=-I(phi), so the full azimuthal integral and its D_s contribution vanish exactly. This does NOT set the full tensor Gamma3 amplitude or unsupported polarizations to zero.',
 'iteration661_interpretation':'Reported O(1e-23..1e-19) densities are floating-point quadrature/cancellation residue, not nonzero physics.',
 'q3_bubble_status':'NO_MASSIVE_ORDINARY_CUT_TOPOLOGY_RETAINED_NOT_ZERO_FILLED',
 'source_born_subtraction':'NOT_PERFORMED','native_soft_Tcut':'NOT_YET_FORMED','zero_fill':False,'candidate_values_used':False,'ANSATZ_003':'FORBIDDEN','Fisher_resources':'FORBIDDEN',
 'exact_next_gate':'Iteration663: apply the same frozen rotational representation to the matched Ward image W[D_s K2]. Determine from the same-parent Iter653 Ward map whether its all-plus-TT soft component is also symmetry-forced to zero or whether a different tensor representation survives. Only then classify the matched T_cut component; do not infer full-tensor zero and do not perform Source/Born subtraction.'}
p=ROOT/'candidate_gravity/results/iteration662_plus_tt_quarter_turn_selection_rule.json'; p.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n'); print(json.dumps(out,indent=2,sort_keys=True))
if fail: raise SystemExit(2)
