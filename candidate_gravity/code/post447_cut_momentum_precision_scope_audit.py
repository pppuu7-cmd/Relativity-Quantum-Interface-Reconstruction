#!/usr/bin/env python3
"""RQIR post-447 collision-safe precision-scope audit.

Purpose: distinguish arithmetic closure on frozen representative parent momenta
from continuous arbitrary-precision provenance on the actual Iteration-407 cut
sample momenta p(z,phi,u,v).  This is source/provenance only, non-promoting, and
runs in parallel with the already-active Iteration-407 spectral-algebra stage.

No authoritative iteration number is claimed here to avoid races with automatic
research.  No physical threshold, routing, numerator, node, sign, or
normalization is changed.
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
C=ROOT/'candidate_gravity/code'
R=ROOT/'candidate_gravity/results'

p436=C/'iteration436_iter270_n1_multiprecision_closure.py'
p437=C/'iteration437_iter270_q1_multiprecision_closure.py'
p438=C/'iteration438_iter270_a_finite_multiprecision_core.py'
p440=C/'iteration440_iter270_acoef_asub_multiprecision_closure.py'
p446=C/'postparent_contraction_precision_stage.py'
p407=C/'iteration407_tru1sq_channel4_analytic_spectral_reduction.py'
p431=C/'iteration431_channel2_cut_kinematic_h1_sensitivity.py'

texts={p.name:p.read_text() for p in (p436,p437,p438,p440,p446,p407,p431)}

checks={
 'iter436_explicit_P0_scope': "for M=POS, legs s/a/b, P0 and h=3e-5" in texts[p436.name] and "ns['P0']" in texts[p436.name],
 'iter437_q1_evaluator_hardcodes_P0': "p=np.asarray(base['P0'],float)" in texts[p437.name],
 'iter438_frozen_P0_scope': "base['P0']" in texts[p438.name] and "26 signed finite-amplitude nodes" in texts[p438.name],
 'iter440_Acoef_mp_hardcodes_P0': "A_finite_mp([mp.mpf(s)*h for s in sig],modes,base['P0'],total_shift)" in texts[p440.name],
 'iter446_uses_parent_binary_Q0_Q1_Asub': "LEGS=ns['LEGS']; M=ns['M']; PROBES=ns['PROBES']; Q0=ns['Q0']; Q1=ns['Q1']; Asub=ns['Asub']" in texts[p446.name],
 'iter446_mp_only_after_parent_values': "mats=[mp_matrix_from_parent(x)" in texts[p446.name],
 'iter446_representative_PROBES_scope': "for probe_index,p0 in enumerate(PROBES)" in texts[p446.name],
 'iter407_continuous_cut_sample_map': "p0=-a+alpha*q+rho*unit_from(z,phi)" in texts[p407.name] and "stripped_limit_massive(alpha,rho*unit_from(z,phi))" in texts[p407.name],
 'iter407_phi_grid_varies_phi': "for m in range(MEAN_NPHI)" in texts[p407.name],
 'iter407_mass_nodes_vary_u_v': "for i,u in enumerate(nodes)" in texts[p407.name] and "for j,v in enumerate(nodes)" in texts[p407.name],
 'manual_cut_audit_exhibits_actual_cut_p': "p=-a+alpha*q+(1.0+sign*h)*vec" in texts[p431.name],
}
if not all(checks.values()):
    raise SystemExit(('source_scope_drift',checks))

# Bind the auto-research authority files fail-closed.  Their PASS remains valid;
# this audit only narrows what those PASS statements logically certify.
s436=json.loads((R/'iteration436_n1_multiprecision_closure_summary.json').read_text())
s438=json.loads((R/'iteration438_a_finite_multiprecision_core_summary.json').read_text())
s440=json.loads((R/'iteration440_acoef_asub_multiprecision_closure_summary.json').read_text())
s446=json.loads((R/'iteration446_postparent_contraction_precision.json').read_text())
s447=json.loads((R/'iteration447_downstream_precision_boundary_audit.json').read_text())
prereq=all(x.get('scientific_gate_pass') is True for x in (s436,s438,s440,s446,s447))
if not prereq: raise SystemExit('auto_research_prerequisite_not_passed')

result={
 'stage':'POST447_CUT_MOMENTUM_PARENT_PRECISION_SCOPE_AUDIT__UNNUMBERED_COLLISION_SAFE',
 'classification':'PASS_REPRESENTATIVE_PARENT_MP_DOES_NOT_YET_EQUAL_CONTINUOUS_CUT_MOMENTUM_MP__NON_PROMOTING',
 'scientific_gate_pass':True,
 'promotes_physical_coordinate':False,
 'MODEL_READINESS':'24%',
 'readiness_change_pp':0,
 'source_checks':checks,
 'retained_auto_research_authority':{
   'iteration436':s436.get('classification'),
   'iteration438':s438.get('classification'),
   'iteration440':s440.get('classification'),
   'iteration446':s446.get('classification'),
   'iteration447':s447.get('classification'),
 },
 'scope_distinction':{
   'certified_parent_arithmetic':'valid on the explicitly frozen representative parent inputs/nodes tested by Iterations 436-446',
   'not_yet_certified':'continuous arbitrary-precision recomputation of Q0/Q1/Acoef/Asub and the traced stripped numerator at every actual Iteration-407 p(z,phi,u,v) sample',
   'reason':'the 436-440 multiprecision evaluators explicitly bind P0/frozen representative momenta, while the 446 post-parent stage converts already-computed parent matrices to mpmath before products/trace; Iteration 407 generates different p continuously from mass and angular variables',
 },
 'scientific_interpretation':(
   'All prior raw PASS results are retained.  They establish strong local/representative numerical closure and make a gross parent arithmetic defect unlikely. '
   'However they are not a proof of continuous cut-sample parent precision provenance.  Therefore, after the active spectral-algebra stage is raw-consumed, '
   'the next non-duplicative numerical gate should evaluate the complete class-3 stripped numerator at prospectively frozen actual cut-sample momenta at 80 and 120 digits, '
   'using generalized arbitrary-precision Q0/Q1/Acoef/Asub at those same momenta rather than recasting binary64 parent matrices.'
 ),
 'prospective_next_numerical_gate':{
   'target':'double-double index 2 / class 3 / q^2=-1',
   'sample_geometry':'actual Iteration-407 fixed-mass cut p(z,phi,u,v)',
   'precision_digits':[80,120],
   'must_preserve':['parent dynamics','class-3 routing','h1=1e-4','radial Richardson nodes 2e-3,1e-3,5e-4','physical mass nodes','numerator','sign','normalization'],
   'must_not_do':['reuse binary64 Q0/Q1/Acoef/Asub as mp inputs','smaller/adaptive h','threshold weakening','angular-grid escalation','zero fill'],
   'status':'PROSPECTIVE_ONLY__NO_PHYSICAL_ACCEPTANCE_RULE_CHANGED'
 },
 'guardrails':['NO_AUTHORITATIVE_ITERATION_NUMBER_REUSE','DO_NOT_INVALIDATE_436_446_PASS','NO_PHYSICAL_DS_PROMOTION','NO_THRESHOLD_WEAKENING','NO_SMALLER_MASS_STEP','NO_ZERO_FILL','NO_ANSATZ003','NO_FISHER_RESOURCES']
}
print(json.dumps(result,indent=2,sort_keys=True))
