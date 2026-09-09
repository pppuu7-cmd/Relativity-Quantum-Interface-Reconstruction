#!/usr/bin/env python3
"""Iter665: fail-closed authority scan plus prospective non-collinear soft-family freeze.
No Candidate values are read. This gate removes the Iter662 axial Rz(pi/2) stabilizer but does NOT define W[D_s K2].
"""
from pathlib import Path
from fractions import Fraction as F
import json, re
ROOT=Path(__file__).resolve().parents[2]
fail=[]
# Required prior raw-valid committed authorities. Exact filenames are frozen from their authority commits.
for name in [
 'candidate_gravity/results/iteration662_plus_tt_quarter_turn_selection_rule_authority.json',
 'candidate_gravity/results/iteration663_transverse_soft_ward_authority.json',
 'candidate_gravity/results/iteration664_null_ward_transverse_no_go.json']:
 p=ROOT/name
 if not p.exists(): fail.append('missing:'+name)
 else:
  d=json.loads(p.read_text())
  if d.get('scientific_gate_pass') is not True: fail.append('nonpass:'+name)
# Broad discovery remains fail-closed, but known historical mentions are semantically classified rather than
# promoted merely because a keyword occurs. These paths were read directly after the first Iter665 audit:
# Iter142/145 are external/comparator design locks; Iter146 is an on-shell C5 comparator discussion;
# Iter237 explicitly says the soft theorem alone does NOT supply the causal/source-completed identity;
# Iter664/current bookkeeping state absence of same-parent transverse authority.
patterns=[re.compile(x,re.I) for x in [r'transverse\s+soft\s+theorem',r'soft\s+graviton\s+theorem',r'\bBMS\b',r'asymptotic\s+identity']]
hits=[]
for p in (ROOT/'candidate_gravity').rglob('*'):
 if not p.is_file() or p.suffix.lower() not in {'.md','.json','.py','.txt'}: continue
 sp=str(p.relative_to(ROOT))
 if 'iteration665' in sp.lower() or 'iteration_665' in sp.lower(): continue
 try: txt=p.read_text(errors='ignore')
 except Exception: continue
 for pat in patterns:
  if pat.search(txt): hits.append({'path':sp,'pattern':pat.pattern}); break
reviewed_nonauthority_paths={
 'candidate_gravity/POST_GAUSSIAN_PROTOCOL_ITERATION145.md',
 'candidate_gravity/C5_FINITE_TANGENT_ITERATION146.md',
 'candidate_gravity/ONSHELL_RETARDED_OBSERVABLE_IDENTITY_AUDIT_ITERATION237.md',
 'candidate_gravity/landscape/RQIR_NONLINEAR_COMPARATOR_AUDIT_ITERATION142.md',
 'candidate_gravity/recovery/CURRENT_QG_FRONT.md',
 'candidate_gravity/recovery/RECOVERY_DELTA_ITERATION_664.md',
 'candidate_gravity/results/iteration664_null_ward_transverse_no_go.json',
 'candidate_gravity/verification/iteration664_null_ward_transverse_no_go.py',
 'candidate_gravity/research_log/2026-09-09_iteration_664.md'
}
unknown_hits=[h for h in hits if h['path'] not in reviewed_nonauthority_paths]
authority_hits=unknown_hits
v=F(1,3)
gamma2=F(1,1)/(F(1,1)-v*v)
rz_stabilizes_hard=(v==0)
soft_null=True
hard_timelike=(gamma2-(v*v*gamma2)==1)
if authority_hits: fail.append('new transverse-soft authority candidate requires semantic review')
if rz_stabilizes_hard: fail.append('noncollinear redesign failed: axial stabilizer retained')
if not soft_null or not hard_timelike: fail.append('kinematic contract algebra drift')
out={
 'iteration':665,'date':'2026-09-09','MODEL_READINESS':'24%',
 'classification':('BLOCKED_ITER665_NO_COMMITTED_SAME_PARENT_TRANSVERSE_SOFT_THEOREM_FOUND__NONCOLLINEAR_SOFT_FAMILY_FROZEN__ITER662_AXIAL_SELECTION_STABILIZER_REMOVED__W_DS_K2_STILL_UNDEFINED__NON_RESIDUAL' if not fail else 'FAIL_ITER665_PROSPECTIVE_SOFT_REDESIGN_AUDIT'),
 'scientific_gate_pass':not fail,'failures':fail,'blocked':not fail,
 'authority_scan':{'patterns':[p.pattern for p in patterns],'all_hits':hits,'reviewed_nonauthority_paths':sorted(reviewed_nonauthority_paths),'authority_candidate_hits':authority_hits,'same_parent_transverse_soft_authority_found':bool(authority_hits),'semantic_rule':'keyword mention is not authority; unexpected paths fail closed for direct review'},
 'frozen_contract':{
   'name':'MSSC001-CLOSED-SK-NONCOLLINEAR-SOFT-KIN-V1','v_x':'1/3','gamma_squared':'9/8',
   'q_hard':'(sqrt(9*s/8), sqrt(s/8), 0, 0)','q_soft':'-epsilon*(1,0,0,1)','q_other':'-q_hard-q_soft',
   'q_hard_squared':'s','q_soft_squared':'0','operation_order':'fixed epsilon>0 -> D_s=Disc_s/(2*pi*i) -> epsilon->0+',
   'candidate_values_used':False,'Rz_pi_over_2_stabilizes_full_kinematics':rz_stabilizes_hard,
   'purpose':'remove Iter662 axial odd-spin stabilizer prospectively; not a definition of transverse W'},
 'native_soft_Tcut':'BLOCKED_ADDITIONAL_TRANSVERSE_SOFT_INPUT_REQUIRED','source_born_subtraction':'NOT_PERFORMED','zero_fill':False,
 'ANSATZ_003':'FORBIDDEN','Fisher_resources':'FORBIDDEN',
 'exact_next_gate':'Iteration666: Ward-controlled mixed-soft observable construction. Use the authoritative longitudinal diffeomorphism Ward map to define a soft insertion in its image/cokernel-controlled sector, then test whether the resulting same-parent closed-SK Gamma3/Gamma2 relation is nontrivial and compatible with the Iter665 non-collinear kinematics. Do not use the frozen plus-TT W and do not form a comparator residual until a matched observable is explicit.'}
p=ROOT/'candidate_gravity/results/iteration665_prospective_noncollinear_soft_redesign.json'; p.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print(json.dumps(out,indent=2,sort_keys=True))
if fail: raise SystemExit(2)
