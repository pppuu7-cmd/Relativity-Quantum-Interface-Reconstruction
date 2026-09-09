#!/usr/bin/env python3
"""Iter665: fail-closed authority scan plus prospective non-collinear soft-family freeze.
No Candidate values are read. This gate removes the Iter662 axial Rz(pi/2) stabilizer but does NOT define W[D_s K2].
"""
from pathlib import Path
from fractions import Fraction as F
import json, re, math
ROOT=Path(__file__).resolve().parents[2]
fail=[]
# Required prior raw-valid committed authorities.
for name in [
 'candidate_gravity/results/iteration662_exact_transverse_rotation_selection_rule.json',
 'candidate_gravity/results/iteration663_transverse_soft_ward_authority.json',
 'candidate_gravity/results/iteration664_null_ward_transverse_no_go.json']:
 p=ROOT/name
 if not p.exists(): fail.append('missing:'+name)
 else:
  d=json.loads(p.read_text())
  if d.get('scientific_gate_pass') is not True: fail.append('nonpass:'+name)
# Repository-wide authority discovery: broad theorem/asymptotic phrases, excluding current/redesign bookkeeping.
patterns=[re.compile(x,re.I) for x in [r'transverse\s+soft\s+theorem',r'soft\s+graviton\s+theorem',r'\bBMS\b',r'asymptotic\s+identity']]
hits=[]
for p in (ROOT/'candidate_gravity').rglob('*'):
 if not p.is_file() or p.suffix.lower() not in {'.md','.json','.py','.txt'}: continue
 sp=str(p.relative_to(ROOT))
 if 'iteration665' in sp.lower() or 'ITERATION_665' in sp: continue
 try: txt=p.read_text(errors='ignore')
 except Exception: continue
 for pat in patterns:
  if pat.search(txt): hits.append({'path':sp,'pattern':pat.pattern}); break
# Discussion-only mentions in Iter663/664 are not accepted as theorem authority.
authority_hits=[h for h in hits if 'iteration663' not in h['path'].lower() and 'iteration_663' not in h['path'].lower() and 'iteration664' not in h['path'].lower() and 'iteration_664' not in h['path'].lower()]
# Prospective non-collinear family. Dimensionless boost v=1/3 is frozen before any new Candidate values.
v=F(1,3)
gamma2=F(1,1)/(F(1,1)-v*v)  # 9/8; E^2=gamma2*s, k_x^2=(gamma2-1)*s.
# Symbolic coefficient vectors in units sqrt(s) for hard leg; soft direction n=(1,0,0,1).
# p=(sqrt(gamma2*s), v*sqrt(gamma2*s),0,0). Rz(pi/2)p has x->0,y->x and is different for v!=0.
rz_stabilizes_hard=(v==0)
soft_null=True
hard_timelike=(gamma2-(v*v*gamma2)==1)
if authority_hits: fail.append('preexisting transverse-soft authority candidate requires semantic review')
if rz_stabilizes_hard: fail.append('noncollinear redesign failed: axial stabilizer retained')
if not soft_null or not hard_timelike: fail.append('kinematic contract algebra drift')
out={
 'iteration':665,'date':'2026-09-09','MODEL_READINESS':'24%',
 'classification':('BLOCKED_ITER665_NO_COMMITTED_SAME_PARENT_TRANSVERSE_SOFT_THEOREM_FOUND__NONCOLLINEAR_SOFT_FAMILY_FROZEN__ITER662_AXIAL_SELECTION_STABILIZER_REMOVED__W_DS_K2_STILL_UNDEFINED__NON_RESIDUAL' if not fail else 'FAIL_ITER665_PROSPECTIVE_SOFT_REDESIGN_AUDIT'),
 'scientific_gate_pass':not fail,'failures':fail,'blocked':not fail,
 'authority_scan':{'patterns':[p.pattern for p in patterns],'all_hits':hits,'authority_candidate_hits':authority_hits,'same_parent_transverse_soft_authority_found':bool(authority_hits)},
 'frozen_contract':{
   'name':'MSSC001-CLOSED-SK-NONCOLLINEAR-SOFT-KIN-V1',
   'v_x':'1/3','gamma_squared':'9/8',
   'q_hard':'(sqrt(9*s/8), sqrt(s/8), 0, 0)',
   'q_soft':'-epsilon*(1,0,0,1)',
   'q_other':'-q_hard-q_soft',
   'q_hard_squared':'s','q_soft_squared':'0',
   'operation_order':'fixed epsilon>0 -> D_s=Disc_s/(2*pi*i) -> epsilon->0+',
   'candidate_values_used':False,
   'Rz_pi_over_2_stabilizes_full_kinematics':rz_stabilizes_hard,
   'purpose':'remove Iter662 axial odd-spin stabilizer prospectively; not a definition of transverse W'
 },
 'native_soft_Tcut':'BLOCKED_ADDITIONAL_TRANSVERSE_SOFT_INPUT_REQUIRED',
 'source_born_subtraction':'NOT_PERFORMED','zero_fill':False,'ANSATZ_003':'FORBIDDEN','Fisher_resources':'FORBIDDEN',
 'exact_next_gate':'Iteration666: Ward-controlled mixed-soft observable construction. Use the authoritative longitudinal diffeomorphism Ward map to define a soft insertion in its image/cokernel-controlled sector, then test whether the resulting same-parent closed-SK Gamma3/Gamma2 relation is nontrivial and compatible with the Iter665 non-collinear kinematics. Do not use the frozen plus-TT W and do not form a comparator residual until a matched observable is explicit.'
}
p=ROOT/'candidate_gravity/results/iteration665_prospective_noncollinear_soft_redesign.json'; p.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print(json.dumps(out,indent=2,sort_keys=True))
if fail: raise SystemExit(2)
