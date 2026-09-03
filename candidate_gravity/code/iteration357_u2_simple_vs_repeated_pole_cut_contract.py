#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 357.

Freeze a fail-closed cut contract for the 42 Iteration-356 U2 families.
Ordinary simple-cut substitution is authorized only when all propagator momentum
factors are simple. Repeated-pole families are typed for derivative/distributional
reduction and are not numerically cut in this gate.
"""
from __future__ import annotations
import contextlib, io, json, runpy
from collections import Counter
from pathlib import Path

ITERATION=357
ROOT=Path(__file__).resolve().parent
with contextlib.redirect_stdout(io.StringIO()):
    P=runpy.run_path(str(ROOT/'iteration356_u2_family_origin_topology_classification.py'), run_name='iteration357_parent356')
records=P['records']

out=[]; simple=0; repeated=0; simple_channels=0; repeated_channels=0
for r in records:
    # Iteration 356 already freezes direct timelike channels and repeated status.
    chans=r['timelike_pair_channels']
    if r['has_repeated_pole_momentum']:
        repeated+=1; repeated_channels+=len(chans)
        status='REPEATED_POLE_DERIVATIVE_DISTRIBUTIONAL_REDUCTION_REQUIRED__SIMPLE_CUT_FORBIDDEN'
    else:
        simple+=1; simple_channels+=len(chans)
        status='ORDINARY_SIMPLE_CUT_CHANNELS_AUTHORIZED_FOR_NEXT_NUMERATOR_ON_SHELL_GATE'
    out.append({'route':r['route'],'subterm':r['subterm'],'propagator_count':r['propagator_count'],
                'direct_timelike_channel_count':len(chans),'cut_contract':status,
                'timelike_pair_channels':chans})

passed=bool(len(out)==42 and simple==12 and repeated==30 and all(x['direct_timelike_channel_count']>0 for x in out))
result={
 'iteration':ITERATION,'model_readiness_percent':24,'scientific_gate_pass':passed,'candidate_residual':False,
 'classification':('PASS_U2_SIMPLE_VS_REPEATED_POLE_CUT_CONTRACT__12_SIMPLE_FAMILIES_NEXT__30_REPEATED_FAMILIES_DISTRIBUTIONAL_BLOCKED' if passed else 'FAIL_U2_SIMPLE_REPEATED_POLE_CUT_CONTRACT'),
 'census':{'families':42,'ordinary_simple_cut_families':simple,'repeated_pole_families':repeated,
           'ordinary_simple_timelike_pair_channels':simple_channels,'repeated_pole_timelike_pair_channels':repeated_channels},
 'families':out,
 'scope':'CUT_METHOD_TYPING_ONLY__NO_DISCONTINUITY_INTEGRATION',
 'guardrails':['REPEATED_POLE_NEVER_TREATED_AS_SIMPLE_CUT','NO_ZERO_FILL','NO_SOURCE_BORN_SUBTRACTION','NO_ANSATZ003','NO_FISHER_RESOURCES','NO_BLIND_FULL_C5'],
 'next_gate':'evaluate numerator-on-shell regularity and uncut-denominator separation only for the 12 ordinary-simple families on each typed timelike pair channel; repeated-pole families remain BLOCKED pending explicit derivative/distributional reduction'
}
print(json.dumps(result,indent=2,sort_keys=True))
if not passed: raise SystemExit(2)
