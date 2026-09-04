#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 391.

Cheap topology proof for the raw-preserved Iteration-388/384 chunk 12-13.
The physical integration is NOT rerun.  Instead we reconstruct the exact frozen
Iteration-359 48-channel ordering and verify whether each cut leaves any uncut
momentum group.  A +Infinity minimum-uncut sentinel is accepted iff the cut
exhausts every denominator group.  All original numerical thresholds remain
binding.
"""
from __future__ import annotations
import contextlib, io, json, math, runpy
from pathlib import Path
import numpy as np

ITERATION=391
ROOT=Path(__file__).resolve().parent
REPO=ROOT.parent.parent
raw=json.loads((REPO/'candidate_gravity/results/iteration388_u2_chunk12_13_raw_preserved.json').read_text())
with contextlib.redirect_stdout(io.StringIO()):
    p359=runpy.run_path(str(ROOT/'iteration359_u2_repeated_pole_derivative_contract.py'),run_name='iteration391_parent359')
if not p359['result']['scientific_gate_pass']:
    raise RuntimeError('iteration359_parent_not_authoritative')
all_channels=[]
for fam in p359['result']['families']:
    for ch in fam['timelike_distinct_group_channels']:
        if ch['repeated_pole_reduction_required']:
            all_channels.append((fam,ch))
if len(all_channels)!=48:
    raise RuntimeError(('channel_census_drift',len(all_channels)))
if raw.get('iteration')!=384 or raw.get('chunk',{}).get('expected_indices')!=[12,13]:
    raise RuntimeError('raw_preservation_provenance_drift')
conv_tol=float(raw['frozen_arithmetic']['convergence_threshold']); shell_tol=float(raw['frozen_arithmetic']['shell_threshold'])
corrected=[]
for rec in raw['records']:
    idx=int(rec['global_channel_index']); fam,ch=all_channels[idx]
    groups=fam['groups']; pair=list(map(int,rec['group_pair']))
    provenance_ok=bool(int(fam['route'])==int(rec['route']) and int(fam['subterm'])==int(rec['subterm']) and
                       list(map(int,ch['group_pair']))==pair and abs(float(ch['q2'])-float(rec['q2']))<1e-14)
    if not provenance_ok:
        raise RuntimeError(('channel_provenance_mismatch',idx))
    uncut_groups=[g for g in range(len(groups)) if g not in set(pair)]
    u=float(rec['minimum_sampled_uncut_abs_denominator'])
    topology_no_uncut=(len(uncut_groups)==0)
    uncut_ok=bool((topology_no_uncut and math.isinf(u)) or ((not topology_no_uncut) and math.isfinite(u) and u>1e-10))
    numeric_ok=bool(math.isfinite(float(rec['scaled_convergence_error'])) and float(rec['scaled_convergence_error'])<=conv_tol and
                    math.isfinite(float(rec['max_cut_shell_abs_error'])) and float(rec['max_cut_shell_abs_error'])<=shell_tol)
    status='CONVERGED' if provenance_ok and uncut_ok and numeric_ok else 'BLOCKED_TOPOLOGY_RECLASSIFICATION'
    corrected.append({'global_channel_index':idx,'q2':float(rec['q2']),'route':int(rec['route']),'subterm':int(rec['subterm']),
                      'group_pair':pair,'denominator_group_count':len(groups),'uncut_group_indices':uncut_groups,
                      'topology_no_uncut_denominator':topology_no_uncut,'raw_umin_is_infinite':bool(math.isinf(u)),
                      'uncut_condition_pass':uncut_ok,'numerical_thresholds_pass':numeric_ok,'corrected_status':status,
                      'D_s_TrU2_repeated_high':rec['D_s_TrU2_repeated_high'],
                      'scaled_convergence_error':float(rec['scaled_convergence_error']),
                      'max_cut_shell_abs_error':float(rec['max_cut_shell_abs_error'])})
pass_gate=bool(len(corrected)==2 and all(r['corrected_status']=='CONVERGED' for r in corrected))
out={'iteration':ITERATION,'model_readiness_percent':24,'scientific_gate_pass':pass_gate,'candidate_residual':False,
     'classification':('PASS_U2_CHUNK12_13_TOPOLOGY_AWARE_RECLASSIFICATION__BOTH_CONVERGED' if pass_gate else 'FAIL_U2_CHUNK12_13_TOPOLOGY_AWARE_RECLASSIFICATION'),
     'source_actions_run':33818755198,'source_artifact':9918013930,
     'source_raw_actions_sha256':'5e7ab80c114f0c178adb4277cc65f161e7fa55a45d8e846c455042d14aa540dd',
     'source_scientific_iteration':384,'records':corrected,
     'scope':'CLASSIFICATION_REPAIR_ONLY__NO_PHYSICAL_REINTEGRATION',
     'guardrails':['ITERATION359_TOPOLOGY_BINDING','RAW_ITERATION388_NUMERICS_IMMUTABLE','INFINITY_ALLOWED_ONLY_WHEN_UNCUT_GROUP_COUNT_IS_ZERO',
                   'FINITE_UNCUT_THRESHOLD_REMAINS_1E-10','NO_THRESHOLD_WEAKENING','NO_ZERO_FILL','NO_EFFECTIVE_ACTION_WEIGHT_FOLDING'],
     'next_gate':'merge indices 12 and 13 as recovered CONVERGED records into the exact-48 U2 assembly only if this gate passes'}
print(json.dumps(out,indent=2,sort_keys=True))
if not pass_gate: raise SystemExit(2)
