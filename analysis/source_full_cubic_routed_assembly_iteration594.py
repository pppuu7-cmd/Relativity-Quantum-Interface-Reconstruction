#!/usr/bin/env python3
"""Iteration 594: full same-action routed MSSC cubic source assembly audit.

This is the first fixture-level assembly after Iter593 that keeps all three
families required by the exact inverse-kernel identity:

  d_abc G = -G Kabc G
            + sum_6(G Ki G Kjk G)
            - sum_6(G Ki G Kj G Kk G).

The purpose is deliberately narrower than the next nonlinear Ward gate: prove
that the complete routed object can be assembled on the exact Iter368/588
three-mode fixture with the Iter589 normalization, with momentum closure,
finite propagators, inherited K3 convergence, and permutation symmetry.  No
source-to-Iter582 map, Born subtraction, comparator quotient, ANSATZ-003,
Fisher or resources is permitted here.
"""
from __future__ import annotations
import contextlib, io, itertools, json, math
from pathlib import Path
import numpy as np

ITERATION=594
ROOT=Path(__file__).resolve().parents[1]
CROOT=ROOT/'candidate_gravity'/'code'
ETA=np.diag([1.,-1.,-1.,-1.])
MASS=0.7
LEGS=('s','a','b')
PROBES=[np.array([.43,-.27,.39,.21]),np.array([.61,.19,-.31,.47])]
# Inherited, not tuned to Iter594 outputs:
CLOSURE_TOL=1e-14                 # Iter368
K3_LAST_STEP_TOL=2e-7             # Iter590
PERMUTATION_SPREAD_TOL=2e-7        # same numerical envelope as inherited K3 FD tolerance
K3_STEPS=(2e-2,1e-2,5e-3)


def mdot(v):
    v=np.asarray(v,float); return float(v@ETA@v)


def first_coeff(h):
    H=ETA@h; trH=float(np.trace(H))
    return 0.5*trH*ETA-ETA@h@ETA,0.5*trH


def mixed_coeff(h1,h2):
    H1=ETA@h1; H2=ETA@h2
    t1=float(np.trace(H1)); t2=float(np.trace(H2))
    bs=t1*t2/4.0-float(np.trace(H1@H2))/2.0
    bt=(ETA@h1@ETA@h2@ETA + ETA@h2@ETA@h1@ETA
        -0.5*t1*(ETA@h2@ETA)-0.5*t2*(ETA@h1@ETA)+bs*ETA)
    return bt,bs


def K1(h,pp,p):
    a1,b1=first_coeff(h); ppc=ETA@pp; pc=ETA@p
    return -float(ppc@a1@pc)+MASS*MASS*b1


def K2(h1,h2,pp,p):
    bt,bs=mixed_coeff(h1,h2); ppc=ETA@pp; pc=ETA@p
    return -float(ppc@bt@pc)+MASS*MASS*bs


def G(p):
    return 1.0/(MASS*MASS-mdot(p))


def exact_scalar_K(eps,hs,p):
    g=ETA.copy()
    for e,h in zip(eps,hs): g += float(e)*h
    det=float(np.linalg.det(g))
    if det>=0: raise RuntimeError('left Lorentzian determinant branch')
    s=math.sqrt(-det); gi=np.linalg.inv(g); pc=ETA@p
    return -float(pc@(s*gi)@pc)+MASS*MASS*s


def K3_mixed(hs,p,step):
    tot=0.0
    for signs in itertools.product((-1,1),repeat=3):
        tot += float(np.prod(signs))*exact_scalar_K([step*x for x in signs],hs,p)
    return tot/(8.0*step**3)


def assemble(order,qs,hs,p0,k3_step):
    """Assemble the exact three families with routed scalar propagators."""
    order=tuple(order); g0=G(p0)
    k3=K3_mixed([hs[x] for x in order],p0,k3_step)
    direct=-g0*k3*g0

    pair_terms=[]
    pair_rows=[]
    for singleton in order:
        pair=tuple(x for x in order if x!=singleton)
        qpair=qs[pair[0]]+qs[pair[1]]

        # Pair acts first: p0 -> p0+qpair -> p0.
        p1=p0+qpair
        z1=(g0*K1(hs[singleton],p0,p1)*G(p1)
            *K2(hs[pair[0]],hs[pair[1]],p1,p0)*g0)
        # Singleton acts first: p0 -> p0+q_singleton -> p0.
        p2=p0+qs[singleton]
        z2=(g0*K2(hs[pair[0]],hs[pair[1]],p0,p2)*G(p2)
            *K1(hs[singleton],p2,p0)*g0)
        pair_terms.extend((z1,z2))
        pair_rows.append({'singleton':singleton,'pair':list(pair),
                          'K1_after_K2':float(z1),'K2_after_K1':float(z2),
                          'pair_first_internal_K0':float(MASS*MASS-mdot(p1)),
                          'singleton_first_internal_K0':float(MASS*MASS-mdot(p2))})

    triple_terms=[]
    for perm in itertools.permutations(order):
        p=p0.copy(); amp=g0; internal=[]
        for x in perm:
            pp=p+qs[x]
            amp*=K1(hs[x],pp,p); p=pp
            inv=MASS*MASS-mdot(p); internal.append(float(inv)); amp*=1.0/inv
        triple_terms.append({'order':list(perm),'value':float(amp),'routed_K0':internal})

    triple_sum=float(sum(x['value'] for x in triple_terms))
    full=float(direct+sum(pair_terms)-triple_sum)
    return {'K3_mixed':float(k3),'direct_minus_GK3G':float(direct),
            'six_K1K2_sum':float(sum(pair_terms)),
            'six_K1cubed_sum_before_minus':triple_sum,
            'full_dabcG':full,'K1K2_rows':pair_rows,'K1cubed_rows':triple_terms}


def main():
    failures=[]
    # Inherit exact Iter368/588 fixture rather than retype polarizations.
    p368=CROOT/'iteration368_tru1sq_timelike_full_prepruning_routing.py'
    src=p368.read_text(); marker='# Cache expensive same-parent blocks by routed loop momentum.'
    if src.count(marker)!=1: raise SystemExit('iteration368 setup boundary drift')
    ns={'__name__':'iteration594_parent368_fixture','__file__':str(p368)}
    with contextlib.redirect_stdout(io.StringIO()):
        exec(compile(src.split(marker,1)[0],str(p368),'exec'),ns,ns)
    if tuple(ns['LEGS'])!=LEGS: raise SystemExit(('leg order drift',ns['LEGS']))
    M=ns['M']; qs={x:np.asarray(M[x][0],float) for x in LEGS}; hs={x:np.asarray(M[x][1],float) for x in LEGS}
    closure=float(np.max(np.abs(sum((qs[x] for x in LEGS),np.zeros(4)))))
    if closure>CLOSURE_TOL: failures.append(f'fixture momentum closure {closure}')

    probe_results=[]
    for p0 in PROBES:
        k3vals=[K3_mixed([hs[x] for x in LEGS],p0,h) for h in K3_STEPS]
        k3_last=abs(k3vals[-1]-k3vals[-2])
        if k3_last>K3_LAST_STEP_TOL:
            failures.append(f'K3 inherited convergence failed at {p0.tolist()}: {k3_last}')

        canonical=assemble(LEGS,qs,hs,p0,K3_STEPS[-1])
        perm=[]
        for order in itertools.permutations(LEGS):
            z=assemble(order,qs,hs,p0,K3_STEPS[-1])
            perm.append({'order':list(order),'full_dabcG':z['full_dabcG']})
        spread=float(max(x['full_dabcG'] for x in perm)-min(x['full_dabcG'] for x in perm))
        if spread>PERMUTATION_SPREAD_TOL:
            failures.append(f'full cubic permutation spread {spread} at {p0.tolist()}')

        routed_inv=[]
        for row in canonical['K1K2_rows']:
            routed_inv.extend([abs(row['pair_first_internal_K0']),abs(row['singleton_first_internal_K0'])])
        for row in canonical['K1cubed_rows']:
            routed_inv.extend(abs(x) for x in row['routed_K0'][:-1])
        min_internal=float(min(routed_inv))
        if not (min_internal>0 and np.isfinite(min_internal)):
            failures.append(f'nonfinite/on-pole internal scalar propagator at {p0.tolist()}')

        probe_results.append({'p0':p0.tolist(),'K0_external':float(MASS*MASS-mdot(p0)),
                              'K3_steps':list(K3_STEPS),'K3_values':[float(x) for x in k3vals],
                              'K3_last_step_difference':float(k3_last),
                              'permutation_spread':spread,'minimum_abs_internal_K0':min_internal,
                              'canonical_assembly':canonical,'permutations':perm})

    classification=('PASS_FULL_SAME_ACTION_ROUTED_CUBIC_SOURCE_ASSEMBLY_AND_PERMUTATION_SYMMETRY__NON_WARD_NON_RESIDUAL'
                    if not failures else 'FAIL_FULL_SAME_ACTION_ROUTED_CUBIC_SOURCE_ASSEMBLY')
    result={
      'iteration':594,'date':'2026-09-08','model_readiness_percent':24,
      'classification':classification,'scientific_gate_pass':not failures,'failures':failures,
      'parent_authorities':['Iter588 exact three-mode routing','Iter589 same-action K1/K2 normalization',
                            'Iter590 exact d_abc(K^-1) family identity','Iter593 split-invariance requirement'],
      'identity':'d_abc G = -G Kabc G + sum_6(G Ki G Kjk G) - sum_6(G Ki G Kj G Kk G)',
      'fixture_momentum_closure_max_abs':closure,
      'thresholds_inherited':{'closure_max':CLOSURE_TOL,'K3_last_step_max':K3_LAST_STEP_TOL,
                              'permutation_spread_max':PERMUTATION_SPREAD_TOL},
      'probe_results':probe_results,
      'key_result':'the full routed source object containing K3 + six K1/K2 placements + six ordered K1^3 chains is explicitly assembled, finite away from sampled scalar poles, and permutation-symmetric within the inherited K3 numerical envelope',
      'scope':'ASSEMBLY_AND_PERMUTATION_SYMMETRY_ONLY',
      'explicit_nonclaims':['not the nonlinear Ward contraction yet','not Candidate-Gravity consistency PASS/FAIL',
                            'not source-to-Iter582 matching','not comparator identity','not a comparator-subtracted residual',
                            'not a novelty certificate'],
      'source_born_subtraction':'NOT_PERFORMED','candidate_residual':False,
      'ANSATZ_003':'FORBIDDEN','Fisher_resources':'FORBIDDEN',
      'next_gate_if_pass':'derive and prospectively freeze the full source-level pure-gauge contraction/Iter587 inverse-propagator RHS for this exact routed 13-term object, then evaluate that nonlinear Ward identity without removing K3 or K1^3; only after Ward closure may a full-observable source-to-Iter582 map be attempted'
    }
    out=ROOT/'candidate_gravity'/'results'; out.mkdir(parents=True,exist_ok=True)
    (out/'iteration594_full_cubic_routed_assembly.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps(result,indent=2,sort_keys=True))
    if failures: raise SystemExit(2)

if __name__=='__main__': main()
