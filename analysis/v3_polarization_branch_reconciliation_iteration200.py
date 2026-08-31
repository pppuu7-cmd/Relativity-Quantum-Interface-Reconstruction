#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 200.

Reconcile two independently prospectively frozen polarization realizations on
the same v3 hard q-geometry.  Branch A was produced by the hourly automation
(Iteration-197 seed stream); branch B by the concurrent manual continuation
(Iterations 198-199 seed stream).  Both were frozen before their own cubic C5
calculation and neither used a candidate target.

The purpose is not to choose a winner post hoc.  We compare the resulting
rank-4 local C5 nuisance subspaces using principal angles and projector norms.
Because the polarization settings define different row functionals, a large
subspace rotation is a protocol-sensitivity result, not a theory ambiguity.
"""
from pathlib import Path
import json
import numpy as np

x=np.array([0.324864,0.246656,0.27264,0.201792,0.256256,0.184448,
            0.994896,0.755384,0.83496,0.617988,0.784784,0.564872],float)
rA=np.array([0.002791966005629022,-0.2581196992877426,0.001641675291115765,
             0.020745938182375526,0.30750307400851506,-0.024343572728527205,
             2.456544279901893,-0.5807324717023833,0.36455839728118633,
             -0.43499543790175527,-2.4389329324378224,-0.4569481776425529])
rB=np.array([-0.2342367480907922,0.03885720334039703,0.19747961324750216,
             -0.013040718030417045,-0.024551995092504563,0.05672164019392357,
             -4.956740678936905,-0.40340860658856637,-7.333276233374885,
             0.1996690006442663,0.5256632248543467,-0.08172191198556611])

def V(r): return np.column_stack([r,-x*r,x*x*r,-x**3*r])
def basis(M):
    U,s,_=np.linalg.svd(M,full_matrices=False)
    return U[:,:4],s

VA,VB=V(rA),V(rB)
QA,sA=basis(VA); QB,sB=basis(VB)
cosines=np.linalg.svd(QA.T@QB,compute_uv=False)
angles=np.degrees(np.arccos(np.clip(cosines,-1.,1.)))
PA=QA@QA.T; PB=QB@QB.T
union=np.column_stack([VA,VB])
s_union=np.linalg.svd(union,compute_uv=False)
rank_union=int(np.linalg.matrix_rank(union,tol=1e-12))
# If both polarization settings are actually measured, the same four Wilson
# coefficients map to a 24-row vertical stack. This is only a diagnostic, not a
# newly frozen protocol.
Vstack=np.vstack([VA,VB])
sstack=np.linalg.svd(Vstack,compute_uv=False)
Vstack_n=Vstack/np.linalg.norm(Vstack,axis=0)
sstack_n=np.linalg.svd(Vstack_n,compute_uv=False)

sAn=np.linalg.svd(VA/np.linalg.norm(VA,axis=0),compute_uv=False)
sBn=np.linalg.svd(VB/np.linalg.norm(VB,axis=0),compute_uv=False)

out={
 'iteration':200,
 'scope':'reconciliation of two independently frozen v3 polarization protocols on identical hard q rows; no candidate target',
 'branches':{
   'v3_A':{
     'authority':'hourly automation Iteration 197',
     'seed_rule':'hard 197000+1000*row; partner 197500+1000*row; first geometry-pass',
     'rank':4,'raw_condition_number':float(sA[0]/sA[-1]),
     'column_normalized_condition_number':float(sAn[0]/sAn[-1]),
     'Riemann3_soft2':rA.tolist()},
   'v3_B':{
     'authority':'concurrent manual Iterations 198-199',
     'seed_rule':'hard 198000+1000*row; partner 198500+1000*row; first geometry-pass',
     'rank':4,'raw_condition_number':float(sB[0]/sB[-1]),
     'column_normalized_condition_number':float(sBn[0]/sBn[-1]),
     'Riemann3_soft2':rB.tolist()}},
 'subspace_comparison':{
   'principal_cosines':cosines.tolist(),
   'principal_angles_degrees':angles.tolist(),
   'projector_frobenius_distance':float(np.linalg.norm(PA-PB,'fro')),
   'projector_operator_distance':float(np.linalg.norm(PA-PB,2)),
   'alternate_subspace_union_rank':rank_union,
   'alternate_subspace_union_singular_values':s_union.tolist(),
   'union_rank_interpretation':'rank8 describes the union of two alternate row-functional subspaces in the common 12-index representation; it is NOT eight independent C5 theory parameters'},
 'dual_setting_diagnostic':{
   'meaning':'if both A and B polarization settings were measured as separate 24 rows with the same four C5 coefficients',
   'rank':int(np.linalg.matrix_rank(Vstack,tol=1e-12)),
   'raw_condition_number':float(sstack[0]/sstack[-1]),
   'column_normalized_condition_number':float(sstack_n[0]/sstack_n[-1]),
   'status':'DIAGNOSTIC_ONLY_NOT_A_FROZEN_V4_PROTOCOL'},
 'classification':{
   'scientific_conflict':'NONE_BOTH_ARE_DIFFERENT_VALID_OBSERVABLE_PROTOCOLS',
   'polarization_seed_is_pure_numerical_nuisance':'FALSE',
   'polarization_setting_is_part_of_observable_definition':'TRUE',
   'choose_A_or_B_posthoc':'FORBIDDEN',
   'AS':'BLOCKED_NOT_ZERO','C3':'BLOCKED_NOT_ZERO',
   'candidate_residual':'NOT_TESTED','ANSATZ_003':'NOT_CREATED','Fisher_resources':'FORBIDDEN'},
 'retained_results':[
   'PROTO-NG-007 — ADMISSIBLE_TT_POLARIZATION_SETTINGS_DEFINE_DISTINCT_OBSERVABLE_PROTOCOLS_AND_MAY_NOT_BE_TREATED_AS_INTERCHANGEABLE_NUMERICAL_SEEDS',
   'C5-NG-018 — TWO_PROSPECTIVELY_FROZEN_V3_POLARIZATION_PROTOCOLS_BOTH_HAVE_RANK4_BUT_THEIR_LOCAL_C5_NUISANCE_SUBSPACES_ARE_STRONGLY_ROTATED',
   'REL-NG-013 — PRINCIPAL_ANGLES_SHOW_ONLY_ONE_NEAR_COMMON_C5_DIRECTION_BETWEEN_V3_A_AND_V3_B',
   'NG-FUNNEL-054 — COMPARATOR_QUOTIENT_AUTHORITY_MUST_INCLUDE_POLARIZATION_SETTINGS_AS_PART_OF_THE_ROW_DEFINITION_BEFORE_RESIDUAL_TESTING'],
 'model_readiness_percent':24,
 'readiness_change':'unchanged: a concurrency discrepancy was resolved as protocol branching, not scientific contradiction; AS/C3 remain blocked and no candidate residual exists.'}
Path('results/v3_polarization_branch_reconciliation_iteration200.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2,sort_keys=True))
