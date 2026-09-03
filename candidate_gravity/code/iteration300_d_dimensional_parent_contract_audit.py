#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 300.

Static + algebraic audit of the minimum same-parent D-dimensional continuation
contract required to remove the Iteration-297/299 evanescent ambiguity.

This does not invent evanescent coefficients. It identifies which layers of the
current executable parent are intrinsically four-dimensional and freezes the
minimum fail-closed implementation/validation contract for a future D-aware
parent or explicit scheme-conversion map.
"""
from pathlib import Path
import json, re

HERE=Path(__file__).resolve().parent
FILES={
  'parent270': HERE/'iteration270_vd_physical_b3_nonzero.py',
  'timelike295': HERE/'iteration295_timelike_tru1_family_reconstruction_s0016.py',
  'dr296': HERE/'iteration296_timelike_tru1_bubble_dr_laurent.py',
}
texts={k:p.read_text(encoding='utf-8') for k,p in FILES.items()}

checks={}
checks['parent_eta_is_explicit_4d']=bool(re.search(r"ETA\s*=\s*np\.diag\(\[-1\.,1\.,1\.,1\.\]\)",texts['parent270']))
checks['parent_has_range4_internal_contractions']='range(4)' in texts['parent270']
checks['parent_has_explicit_rank6_4d_fieldspace_tensor']='np.zeros((4,4,4,4,4,4)' in texts['parent270']
checks['parent_tt_uses_3d_cross_product']='np.cross' in texts['parent270']
checks['timelike295_full_coordinate_loop_basis_4d']='for d in range(deg+1-a-b-c)' in texts['timelike295']
checks['dr296_uses_4d_minkowski_laplacian']='for mu in range(4)' in texts['dr296']
checks['dr296_measure_is_D_continued']='D2=2.0-eps' in texts['dr296']
checks['dr296_declares_4d_numerator_scheme_guard']='FOUR_D_NUMERATOR_D_MEASURE' in texts['dr296']

required_true=list(checks)
assert all(checks[k] for k in required_true),checks

# Algebraic order requirement imported from Iteration 299.
# If the master has pole order p, finite C0 needs numerator Taylor orders N_j
# through j=p; subleading pole delta^-m needs j through p-m.
order_requirements={}
for p in (0,1,2,3):
    order_requirements[str(p)]={
      'highest_numerator_delta_order_needed_for_finite_C0':p,
      'highest_pole_protected_by_N0_only':0 if p==0 else p,
      'subleading_pole_requires_evanescent_data':False if p<=1 else True,
    }

contract={
  'regulator_convention':[
    'Freeze whether external physical momenta/polarizations are kept in a four-dimensional barred subspace while all internal Lorentz traces and loop contractions are D-dimensional, or choose a different explicit convention.',
    'Do not mix conventions across K2 and Gamma3 comparator pieces.'
  ],
  'internal_parent_algebra':[
    'Replace explicit internal range(4)/4x4 contraction logic by a D-aware symbolic contraction layer or derive an exact finite scheme-conversion map.',
    'Re-derive the field-space metric/Christoffel and orbit operator at arbitrary D; do not assume the D=4 numerical Christoffel coefficients are sufficient away from D=4.',
    'Carry D dependence through Nhat, N1, N2, Q1, Q2, A, Y_down and trace contractions before Laurent expansion.'
  ],
  'evanescent_order':[
    'Determine actual Laurent pole order family-by-family first.',
    'For a simple nonzero pole, retain the numerator through O(D-4) to promote the finite term.',
    'For a double pole, retain through O((D-4)^2) for the finite term and through O(D-4) even for the subleading single pole.',
    'If the relevant discontinuity is pole-free, record that the pole-times-evanescent mechanism does not require higher numerator orders for that finite cut, without promoting unrelated full finite terms.'
  ],
  'regression_and_validation':[
    'At delta=0 reproduce the frozen Iteration-295 eight-family numerator coefficients/primitive reconstruction within its certified numerical envelope.',
    'Reproduce Iteration-291/292 trace-weight and denominator identities at D=4.',
    'Validate D-derivative coefficients independently (symbolic identity or two independent small-delta evaluations); no one-sided finite-difference authority alone.',
    'Use fail-closed scientific artifact sentinel/schema validation from Iteration 298.'
  ],
  'promotion':[
    'No same-parent finite C5 comparator coordinate is promoted until this contract or an explicit equivalent scheme-conversion map is satisfied.',
    'Protected Laurent coefficients may be promoted only under the Iteration-299 pole-order theorem.'
  ]
}

result={
 'iteration':300,
 'model_readiness_percent':24,
 'classification':'PASS_D_DIMENSIONAL_PARENT_GAP_LOCALIZED_AND_IMPLEMENTATION_CONTRACT_FROZEN__NUMERICAL_D_CONTINUATION_STILL_BLOCKED',
 'candidate_residual':False,
 'source_files':{k:str(p.relative_to(HERE.parent.parent)) for k,p in FILES.items()},
 'hardcoded_4d_checks':checks,
 'pole_order_to_required_numerator_order':order_requirements,
 'minimum_d_dimensional_contract':contract,
 'guardrails':[
   'DO_NOT_TREAT_D_DIMENSIONAL_MEASURE_ALONE_AS_A_D_DIMENSIONAL_PARENT',
   'DO_NOT_REPLACE_MISSING_EVANESCENT_PARENT_COEFFICIENTS_BY_ZERO',
   'D4_REGRESSION_IS_NECESSARY_NOT_SUFFICIENT_FOR_D_DIMENSIONAL_AUTHORITY',
   'K2_AND_GAMMA3_MUST_SHARE_THE_SAME_REGULATOR_AND_EXTERNAL_STATE_CONVENTION'
 ],
 'next_gate':'implement the first D-aware parent sublayer needed by the observed Laurent pole order (or freeze an explicit finite scheme-conversion map); use corrected Iteration296 to decide whether bubble-cut finite coefficients need O(D-4) numerator data before spending effort on them'
}
print(json.dumps(result,indent=2,sort_keys=True))
