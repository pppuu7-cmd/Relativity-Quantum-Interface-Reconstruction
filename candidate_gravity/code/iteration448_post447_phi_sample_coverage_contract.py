#!/usr/bin/env python3
"""Iteration 448: prospective coverage/promotion contract for the active post-447 phi/sample MP slab.

This audit is deliberately independent of the numerical outcome of run 33928248369.
It freezes how that outcome may be interpreted before the raw artifact exists.
"""
from __future__ import annotations
import ast, json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = ROOT / 'post447_class3_phi_sample_mp_stage.py'
text = SRC.read_text()
tree = ast.parse(text)
vals = {}
for node in tree.body:
    if isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
        name = node.targets[0].id
        if name in {'MASS_U','MASS_V','Z_SAMPLES','NPHI','RADIAL_HS','MP_LEVELS'}:
            vals[name] = ast.literal_eval(node.value)

required = {'MASS_U','MASS_V','Z_SAMPLES','NPHI','RADIAL_HS','MP_LEVELS'}
missing = sorted(required - vals.keys())
if missing:
    raise SystemExit(('active_stage_binding_missing', missing))

sample_rows = len(vals['Z_SAMPLES']) * int(vals['NPHI'])
parent_evaluations = sample_rows * len(vals['MP_LEVELS']) * len(vals['RADIAL_HS']) * 2
assert sample_rows == 48
assert parent_evaluations == 576
assert tuple(vals['MP_LEVELS']) == (80,120)
assert tuple(vals['RADIAL_HS']) == (2.0e-3,1.0e-3,5.0e-4)
assert tuple(vals['Z_SAMPLES']) == (-0.86,0.0,0.86)
assert vals['MASS_U'] == vals['MASS_V'] == 5.0e-6

result = {
  'iteration': 448,
  'classification': 'PASS_PROSPECTIVE_PHI_SAMPLE_COVERAGE_PROMOTION_BARRIER__NON_PROMOTING',
  'scientific_gate_pass': True,
  'promotes_physical_coordinate': False,
  'MODEL_READINESS': '24%',
  'readiness_change_pp': 0,
  'bound_active_run': 33928248369,
  'active_scope': {
    'mass_points': [[vals['MASS_U'], vals['MASS_V']]],
    'z_samples': list(vals['Z_SAMPLES']),
    'phi_nodes': vals['NPHI'],
    'radial_hs': list(vals['RADIAL_HS']),
    'precision_digits': list(vals['MP_LEVELS']),
    'required_output_sample_rows': sample_rows,
    'direct_parent_mp_evaluations': parent_evaluations,
  },
  'frozen_interpretation': {
    'if_active_stage_pass': 'REPRESENTATIVE_SLAB_PRECISION_PASS__NON_PROMOTING; next gate is extension to every remaining frozen z support point at the same mass corner, then every frozen mass-node family required by index-2 F(u,v), with unchanged thresholds/nodes.',
    'if_active_stage_blocked': 'NUMERICAL_SAMPLE_LAYER_BLOCKED__NON_PROMOTING; localize first failing z/phi/radial sample at unchanged mass point and conventions; no resampling, threshold weakening, or precision cherry-picking.',
    'full_F_promotion_requirement': 'Only explicit exhaustive coverage of the frozen Iteration-407 z/phi/radial support at every frozen mass node entering the index-2 F(u,v) derivative may be called full-F precision provenance closure.',
    'forbidden_inferences': [
      'PASS of 48 rows is not full-z closure',
      'PASS at u=v=+5e-6 is not mass-family closure',
      'PASS of sample generation is not radial/mass-derivative physical D_s authority',
      'No coverage percentage may be inferred until the full frozen support denominator is enumerated from source',
    ],
  },
  'guardrails': [
    'NO_PHYSICAL_DS_PROMOTION','NO_THRESHOLD_WEAKENING','NO_Z_RESAMPLING','NO_PHI_ESCALATION',
    'NO_RADIAL_NODE_CHANGE','NO_MASS_NODE_CHANGE','NO_ZERO_FILL','NO_ANSATZ003','NO_FISHER_RESOURCES'
  ],
}
print(json.dumps(result, indent=2, sort_keys=True))
