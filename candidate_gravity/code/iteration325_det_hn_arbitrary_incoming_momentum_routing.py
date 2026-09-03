#!/usr/bin/env python3
"""RQIR Iteration 325: arbitrary-incoming-momentum H/N numerator routing certificate.

This gate reuses the frozen Iteration-317 ghost and Iteration-319 graviton
same-parent derivations, but re-evaluates them at every distinct cumulative
incoming loop momentum p+Q required by an ordered closed-triad cubic trace.
For each momentum state, the polynomial coefficient factory is independently
checked against its exact-geometry oracle.  No missing coefficient is zero-filled.

Scope: numerator-routing certificate only.  No physical determinant coefficient,
denominator-family reduction, Source/Born subtraction, comparator residual,
ANSATZ-003, Fisher or resource inference is produced here.
"""
from __future__ import annotations
import contextlib, io, itertools, json, pathlib, re
import numpy as np

ROOT=pathlib.Path(__file__).resolve().parents[2]
GHOST=ROOT/'candidate_gravity/code/iteration317_det_ghost_three_mode_routing.py'
GRAV=ROOT/'candidate_gravity/code/iteration319_det_graviton_three_mode_routing.py'

# Use the first two frozen non-collinear modes of each authority script and impose
# q3=-(q1+q2) before any geometry is constructed.  Closure makes the three q's
# linearly dependent by construction; amplitude variables remain independent.
BASE_P={
 'ghost':np.array([0.70,-0.40,0.20,0.60]),
 'graviton':np.array([0.61,-0.33,0.24,0.52]),
}
BASE_Q={
 'ghost':[np.array([0.30,-0.20,0.40,0.10]),np.array([-0.10,0.50,0.20,-0.30])],
 'graviton':[np.array([0.27,-0.19,0.31,0.11]),np.array([-0.13,0.37,0.17,-0.29])],
}

def patch_and_exec(path: pathlib.Path, pvec: np.ndarray):
    src=path.read_text()
    # Override the hard-coded incoming momentum immediately after its assignment;
    # also close the triad before any routed coefficient is constructed.
    marker="\nZERO=(0,0,0)" if 'iteration317_' in path.name else "\ndef deg(a):"
    inject=("\np=np.array("+repr([float(x) for x in pvec])+")"
            "\nqs[2]=-(qs[0]+qs[1])")
    if marker not in src:
        raise RuntimeError(f'patch marker absent in {path}')
    src=src.replace(marker,inject+marker,1)
    ns={'__name__':'__rqir_iteration325_embedded__','__file__':str(path)}
    with contextlib.redirect_stdout(io.StringIO()):
        exec(compile(src,str(path),'exec'),ns,ns)
    return ns

def unique_shift_states(qs):
    z=np.zeros(4); q1,q2,q3=qs
    candidates=[z,q1,q2,q3,q1+q2,q1+q3,q2+q3]
    out=[]
    for x in candidates:
        if not any(np.max(np.abs(x-y))<1e-14 for y in out): out.append(x)
    return out

def sector_result(kind,path):
    q1,q2=BASE_Q[kind]; qs=[q1,q2,-(q1+q2)]
    closure=float(np.max(np.abs(sum(qs,np.zeros(4)))))
    states=unique_shift_states(qs)
    runs=[]; all_ok=True
    for Q in states:
        pin=BASE_P[kind]+Q
        ns=patch_and_exec(path,pin)
        IND=ns['IND']; deg=ns['deg']; errors=ns['errs'] if kind=='graviton' else ns['errors']
        maxdeg={n:max(float(errors[a]) for a in IND if deg(a)==n) for n in range(4)}
        threshold=ns['threshold']
        oracle_ok=all(maxdeg[n] < threshold[n] for n in range(4))
        target=ns['H'] if kind=='graviton' else ns['N']
        # Explicitly inspect all physical insertion orders relevant to e=0,c<=3.
        required=[a for a in IND if 1 <= deg(a) <= 3]
        finite=all(np.isfinite(target[a]).all() for a in required)
        nontrivial=any(float(np.max(np.abs(target[a])))>1e-12 for a in required)
        all_ok &= oracle_ok and finite and nontrivial
        runs.append({
          'Q':[float(x) for x in Q], 'incoming_p':[float(x) for x in pin],
          'oracle_pass':bool(oracle_ok),'finite_required_HN123':bool(finite),
          'nontrivial_required_HN123':bool(nontrivial),
          'max_abs_error_by_degree':{str(n):maxdeg[n] for n in range(4)},
          'threshold_by_degree':{str(n):float(threshold[n]) for n in range(4)},
          'mixed_111_norm':float(np.max(np.abs(target[(1,1,1)]))),
        })
    # Six permutations must map insertion starts into the certified shift-state set.
    route_checks=[]
    for perm in itertools.permutations(range(3)):
        cum=np.zeros(4); starts=[]
        for r in perm:
            starts.append(cum.copy()); cum=cum+qs[r]
        covered=all(any(np.max(np.abs(s-u))<1e-14 for u in states) for s in starts)
        route_checks.append({'order':[int(x) for x in perm],
                             'trace_closure_max_abs':float(np.max(np.abs(cum))),
                             'all_incoming_states_certified':bool(covered)})
        all_ok &= covered and np.max(np.abs(cum))<1e-14
    return {'closed_triad_max_abs':closure,'distinct_incoming_shift_states':len(states),
            'shift_state_validations':runs,'ordered_route_checks':route_checks,
            'sector_pass':bool(all_ok)}

ghost=sector_result('ghost',GHOST)
grav=sector_result('graviton',GRAV)
ok=ghost['sector_pass'] and grav['sector_pass']
result={
 'iteration':325,'model_readiness_percent':24,'scientific_gate_pass':bool(ok),
 'classification':('PASS_HN123_ARBITRARY_INCOMING_MOMENTUM_CLOSED_TRIAD_ROUTING_CERTIFICATE' if ok else 'FAIL_HN123_ARBITRARY_INCOMING_MOMENTUM_CLOSED_TRIAD_ROUTING_CERTIFICATE'),
 'scope':{'determinant_sector':'e=0,c<=3','trace':'closed non-collinear q1,q2,q3=-(q1+q2)',
          'purpose':'certify frozen H1/H2/H3 and N1/N2/N3 at every distinct p+Q incoming state used by ordered cubic routes'},
 'ghost':ghost,'graviton':grav,
 'physical_status':{
   'shifted_denominator_routing':'FROZEN_ITERATION_324',
   'arbitrary_incoming_HN123':'CERTIFIED_FOR_CLOSED_TRIAD_ROUTE_STATES' if ok else 'BLOCKED_FAIL',
   'physical_cubic_determinant_trace':'NEXT_DEPENDENT_GATE_NOT_COMPUTED',
   'physical_U2':'BLOCKED_UNCHANGED'},
 'candidate_residual':False,
 'guardrails':['UNSUPPORTED_IS_BLOCKED_NOT_ZERO_FILLED','NO_PHYSICAL_DETERMINANT_COEFFICIENT_CLAIMED_HERE','NO_SOURCE_BORN_SUBTRACTION','NO_ANSATZ003','NO_FISHER_RESOURCES','NO_BLIND_HEAVY_FULL_C5'],
 'next_gate':('assemble the first physical shifted cubic determinant trace using Iteration-324 denominators and the certified p+Q H/N numerator insertions; then classify denominator families and pole/cut origin before any matched-observable subtraction' if ok else 'preserve FAIL and repair arbitrary-incoming H/N routing without weakening frozen oracle thresholds')
}
print(json.dumps(result,indent=2,sort_keys=True))
