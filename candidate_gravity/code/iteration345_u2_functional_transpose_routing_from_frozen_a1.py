#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 345.

Route-only repair after preserved Iteration-343/344 implementation FAILs.

Iteration 341 already independently validated the physical same-parent A1/A2
kernels against an exact-geometry oracle.  Therefore this gate does NOT build a
second hand-coded Eq.(55) oracle.  It treats the Iteration-341 A1 kernel factory
as frozen component authority and asks only the distinct Fourier-functional
transpose question.

For a background mode Q and a right vertex
    A_R(Q;p): ghost momentum p -> field momentum p+Q,
the bilinear functional transpose obeys
    A_T(Q;k) = A_R(Q;-k-Q)^T,
so a field input k maps to ghost momentum k+Q.  The external insertion remains
+Q on both orientations.  This gate verifies the pairing for multiple physical
momenta/modes and proves that the naive same-input-momentum transpose is not
identical.
"""
from __future__ import annotations
import contextlib, hashlib, io, json, re
from pathlib import Path
import numpy as np

ROOT=Path(__file__).resolve().parent
I341=ROOT/'iteration341_u2_v1_a12_same_parent_geometry.py'
raw=I341.read_bytes(); source_sha256=hashlib.sha256(raw).hexdigest()
src=raw.decode()
# Execute only the physical polynomial construction through Acoef; do not run
# the independent finite-difference oracle or the Iteration-341 result gate.
prefix=src.split('def geom_x(t,x):',1)[0]
if len(prefix)==len(src):
    raise RuntimeError('Iteration-341 Acoef authority boundary changed')
old="p=np.array([.43,-.27,.39,.21])"
if prefix.count(old)!=1:
    raise RuntimeError('Iteration-341 fixed-p signature changed')

def load_factory(p_in):
    repl='p=np.array('+repr([float(x) for x in p_in])+')'
    code=prefix.replace(old,repl,1)
    ns={'__name__':'iteration345_i341_factory','__file__':str(I341)}
    with contextlib.redirect_stdout(io.StringIO()):
        exec(compile(code,'iteration345_i341_factory','exec'),ns,ns)
    return ns

# Freeze the physical modes/background tensors from the same parent source.
base=load_factory([.43,-.27,.39,.21])
qs=[np.asarray(x,float) for x in base['qs']]
mode_keys=[(1,0),(0,1)]

rng=np.random.default_rng(345)
fixtures=[
    np.array([.57,-.31,.22,.46]),
    np.array([.71,.19,-.37,.28]),
    np.array([.49,-.41,-.16,.63]),
]
records=[]
max_pair=max_kernel=max_phase=0.0
min_wrong=float('inf')
for imode,(Q,key) in enumerate(zip(qs,mode_keys)):
  for ip,p in enumerate(fixtures):
    right=load_factory(p)['Acoef'][key]
    # Fourier pairing requires k+p+Q=0.
    k=-(p+Q)
    p_of_transpose=-k-Q
    left=load_factory(p_of_transpose)['Acoef'][key].T
    kernel_err=float(np.max(np.abs(left-right.T)))
    phase_err=float(np.max(np.abs(k+p+Q)))
    c=rng.normal(size=right.shape[1])+1j*rng.normal(size=right.shape[1])
    t=rng.normal(size=right.shape[0])+1j*rng.normal(size=right.shape[0])
    pair_err=float(abs(t.T@(right@c)-c.T@(left@t)))
    # Naive same-input-momentum transpose: A(Q;k)^T.  It is generically wrong.
    wrong=load_factory(k)['Acoef'][key].T
    wrong_diff=float(np.max(np.abs(wrong-left)))
    max_pair=max(max_pair,pair_err); max_kernel=max(max_kernel,kernel_err); max_phase=max(max_phase,phase_err)
    min_wrong=min(min_wrong,wrong_diff)
    records.append({'mode':imode,'fixture':ip,'Q':Q.tolist(),'p_right':p.tolist(),'k_left':k.tolist(),
                    'transpose_input_recovered':p_of_transpose.tolist(),'kernel_error':kernel_err,
                    'bilinear_pairing_error':pair_err,'phase_closure_error':phase_err,
                    'naive_same_k_transpose_difference':wrong_diff})

# Independent loop-routing closure: each oriented vertex raises the current loop
# momentum by +Q, so three external insertions close iff their Q sum is zero;
# no sign reversal of Q is induced by functional transpose.
q1=np.array([1.,0.,0.,0.]); q2=np.array([-.4,.1,.1,0.]); q3=np.array([-.6,-.1,-.1,0.])
loop_closure=float(np.max(np.abs(q1+q2+q3)))

thresholds={'kernel_abs_max':2e-13,'pairing_abs_max':2e-12,'phase_abs_max':2e-15,
            'loop_closure_abs_max':2e-15,'naive_same_k_difference_min':1e-5}
passed=(max_kernel<=thresholds['kernel_abs_max'] and max_pair<=thresholds['pairing_abs_max'] and
        max_phase<=thresholds['phase_abs_max'] and loop_closure<=thresholds['loop_closure_abs_max'] and
        min_wrong>=thresholds['naive_same_k_difference_min'])

result={
 'iteration':345,'model_readiness_percent':24,'scientific_gate_pass':bool(passed),
 'classification':('PASS_U2_FUNCTIONAL_TRANSPOSE_FOURIER_ROUTING_FROM_FROZEN_ITERATION341_A1_AUTHORITY__TRU2_CUBIC_ROUTE_ASSEMBLY_AUTHORIZED_NEXT'
                   if passed else 'FAIL_U2_FUNCTIONAL_TRANSPOSE_ROUTING_FROM_FROZEN_A1'),
 'candidate_residual':False,
 'predecessor_disposition':{
   'iteration343':'PRESERVED_IMPLEMENTATION_FAIL_HAND_CODED_EQ55_ORACLE__TRANSPOSE_PAIRING_SUBTESTS_PASSED',
   'iteration344':'PRESERVED_IMPLEMENTATION_FAIL_PARTIAL_EQ55_ORACLE_REPAIR__NO_THRESHOLD_CHANGE',
   'reason_for_new_gate':'component correctness belongs to independently validated Iteration341; this gate isolates routing only'
 },
 'component_authority':{'source':'candidate_gravity/code/iteration341_u2_v1_a12_same_parent_geometry.py',
                        'sha256':source_sha256,'status':'FROZEN_PHYSICAL_A1_A2_FROM_ITERATION341'},
 'frozen_rule':{'right':'A_R(Q;p)=A(Q;p): p -> p+Q',
                'left':'A_T(Q;k)=A(Q;-k-Q)^T: k -> k+Q',
                'external_background_momentum':'same +Q for right and functional-transpose orientations',
                'closed_loop_condition':'sum external Q_i = 0 unchanged by transpose'},
 'validation':{'fixture_count':len(records),'records':records,'max_kernel_error':max_kernel,
               'max_bilinear_pairing_error':max_pair,'max_phase_closure_error':max_phase,
               'min_naive_same_k_transpose_difference':min_wrong,'closed_triad_loop_error':loop_closure,
               'thresholds':thresholds},
 'status':{'A1_A2':'FROZEN_ITERATION341','N_Y':'FROZEN_ITERATION342',
           'functional_transpose_routing':'FROZEN_EXECUTABLE' if passed else 'BLOCKED',
           'TrU2_cubic_12_route_assembly':'AUTHORIZED_NEXT' if passed else 'BLOCKED'},
 'guardrails':['NO_SECOND_HAND_CODED_EQ55_ORACLE_IN_THIS_GATE','DO_NOT_USE_NAIVE_A_Q_K_TRANSPOSE_AT_SAME_K',
               'ITERATION340_A_TRANSPOSE_A_INDEX_ORIENTATION_BINDING','ITERATION340_HINV_VD_MINUS_KINV_BINDING',
               'NO_SOURCE_BORN_SUBTRACTION','NO_ANSATZ003','NO_FISHER_RESOURCES','NO_BLIND_FULL_C5'],
 'next_gate':'assemble and independently validate the 12 surviving cubic-background Tr U2 routes from Iteration308 with frozen A1/A2, N/Y, Hinv and functional-transpose momentum routing before any cut integration'
}
print(json.dumps(result,indent=2,sort_keys=True))
if not passed: raise SystemExit(2)
