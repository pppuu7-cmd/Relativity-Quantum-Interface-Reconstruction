#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 356.

Classify the 42 distinct physical additive U2 families left by Iteration 355 by
massless propagator topology and kinematic cut origin before any discontinuity
integration.  This gate does not evaluate a cut.
"""
from __future__ import annotations
import contextlib, io, json, runpy
from pathlib import Path
import numpy as np

ITERATION=356
ROOT=Path(__file__).resolve().parent
with contextlib.redirect_stdout(io.StringIO()):
    P=runpy.run_path(str(ROOT/'iteration355_u2_heldout_physical_numerator_transport.py'), run_name='iteration356_parent355')

raw=P['raw']; enumerate_subterms=P['enumerate_subterms']; mdot=P['mdot']
pref=np.array([.43,-.27,.39,.21])
tol=2e-12
records=[]; cut_capable=0; noncut=0; repeated=0
for rid,a in enumerate(raw):
    for s in enumerate_subterms(a,pref):
        props=s['props']
        # Convert absolute propagator momenta p+offset to offsets from common loop p.
        offsets=[(sp,np.asarray(k,float)-pref) for sp,k in props]
        pair_channels=[]
        for i in range(len(offsets)):
            for j in range(i+1,len(offsets)):
                delta=offsets[j][1]-offsets[i][1]
                q2=float(np.real(mdot(delta)))
                if q2 < -tol:
                    pair_channels.append({'i':i,'j':j,'q2':q2,'delta':delta.tolist(),'type':'TIMELIKE_TWO_LINE_CUT_CANDIDATE'})
        unique={tuple(np.round(off,12)) for _,off in offsets}
        has_repeated=len(unique)<len(offsets)
        if has_repeated: repeated+=1
        capable=bool(pair_channels)
        cut_capable+=int(capable); noncut+=int(not capable)
        origin=('CUT_CAPABLE_REPEATED_POLE_TOPOLOGY' if capable and has_repeated else
                'CUT_CAPABLE_SIMPLE_DISTINCT_POLE_TOPOLOGY' if capable else
                'NO_DIRECT_TIMELIKE_TWO_LINE_CUT__LOCAL_SCALELESS_RATIONAL_OR_HIGHER_ANALYSIS_REQUIRED')
        records.append({'route':rid,'subterm':s['subterm'],'propagator_count':len(props),
                        'ghost_count':sum(sp=='ghost' for sp,_ in props),'graviton_count':sum(sp=='graviton' for sp,_ in props),
                        'distinct_momentum_offsets':len(unique),'has_repeated_pole_momentum':has_repeated,
                        'direct_timelike_cut_capable':capable,'origin_classification':origin,'timelike_pair_channels':pair_channels})

passed=bool(len(records)==42 and cut_capable+noncut==42)
result={
 'iteration':ITERATION,'model_readiness_percent':24,'scientific_gate_pass':passed,'candidate_residual':False,
 'classification':('PASS_U2_42_FAMILY_KINEMATIC_ORIGIN_AND_PROPAGATOR_TOPOLOGY_CLASSIFICATION__CUT_INTEGRATION_NEXT_ONLY_FOR_TYPED_CHANNELS' if passed else 'FAIL_U2_FAMILY_ORIGIN_TOPOLOGY_CLASSIFICATION'),
 'census':{'families':42,'cut_capable_families':cut_capable,'no_direct_timelike_cut_families':noncut,'families_with_repeated_pole_momentum':repeated},
 'thresholds':{'timelike_pair_q2_max':-tol},'families':records,
 'scope':'KINEMATIC_ORIGIN_AND_PROPAGATOR_TOPOLOGY_ONLY__NO_DISCONTINUITY_INTEGRATION',
 'guardrails':['NO_DENOMINATOR_ONLY_FAMILY_MERGE','ITERATION355_42_DISTINCT_FAMILIES_BINDING','REPEATED_POLES_TYPED_SEPARATELY','NO_SOURCE_BORN_SUBTRACTION','NO_ANSATZ003','NO_FISHER_RESOURCES','NO_BLIND_FULL_C5'],
 'next_gate':'for cut-capable families, build channel-resolved normalized Tr U2 discontinuity with repeated-pole channels handled by explicit derivative/distributional reduction rather than simple-cut substitution; preserve no-direct-cut families separately'
}
print(json.dumps(result,indent=2,sort_keys=True))
if not passed: raise SystemExit(2)
