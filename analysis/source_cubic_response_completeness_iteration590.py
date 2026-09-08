#!/usr/bin/env python3
"""Iteration 590: cubic MSSC-001 source-response completeness audit.

Before calling the six frozen K1-G-K2 / K2-G-K1 placements a *complete* cubic
source response, audit the universal third mixed derivative of an inverse
operator and the actual Iter368/Iter588 MSSC fixture.  For

    K(e)=K0 + sum_i e_i K_i + sum_{i<j} e_i e_j K_ij
             + e_a e_b e_c K_abc,
    G(e)=K(e)^-1,

the exact mixed derivative d_a d_b d_c G|0 contains three families:
  (i)  - G K_abc G,
  (ii) + all six G K_i G K_jk G / G K_jk G K_i G placements,
  (iii)- all six G K_i G K_j G K_k G permutations.

Thus the six K1/K2 placements are a well-defined scoped subset, but are not the
full third inverse-kernel response unless K3 and K1^3 are independently shown
to project out of the frozen T_cut observable.  This iteration does NOT decide
that later projection question; it prevents an unsupported omission.
"""
from __future__ import annotations
import contextlib, hashlib, io, itertools, json, math
from pathlib import Path
import numpy as np

ROOT=Path(__file__).resolve().parents[1]
CROOT=ROOT/'candidate_gravity'/'code'
ETA=np.diag([1.,-1.,-1.,-1.])
MASS=0.7
LEGS=('s','a','b')


def mdot(v):
    v=np.asarray(v,float); return float(v@ETA@v)


def first_coeff(h):
    H=ETA@h; trH=float(np.trace(H))
    return 0.5*trH*ETA-ETA@h@ETA, 0.5*trH


def K1(h,pp,p):
    a1,b1=first_coeff(h); ppc=ETA@pp; pc=ETA@p
    return -float(ppc@a1@pc)+MASS*MASS*b1


def flat_G(p):
    # Iter589 K0(p,p)=m^2-p^2 in the frozen (+---) convention.
    return 1.0/(MASS*MASS-mdot(p))


def exact_scalar_K(eps,hs,p):
    """Exact same-action diagonal scalar kernel for total external momentum 0."""
    g=ETA.copy()
    for e,h in zip(eps,hs): g += float(e)*h
    det=float(np.linalg.det(g))
    if det>=0: raise RuntimeError('left Lorentzian determinant branch')
    s=math.sqrt(-det); gi=np.linalg.inv(g); pc=ETA@p
    return -float(pc@(s*gi)@pc)+MASS*MASS*s


def mixed3_scalar(hs,p,step):
    tot=0.0
    for signs in itertools.product((-1,1),repeat=3):
        tot += float(np.prod(signs))*exact_scalar_K([step*x for x in signs],hs,p)
    return tot/(8.0*step**3)


def universal_inverse_regression():
    rng=np.random.default_rng(590031)
    A=rng.normal(size=(3,3)); K0=A.T@A+2.0*np.eye(3); G=np.linalg.inv(K0)
    K1s=[0.08*rng.normal(size=(3,3)) for _ in range(3)]
    K2s={(0,1):0.04*rng.normal(size=(3,3)),(0,2):0.04*rng.normal(size=(3,3)),(1,2):0.04*rng.normal(size=(3,3))}
    K3=0.02*rng.normal(size=(3,3))

    def exact(e):
        K=K0.copy()
        for i in range(3): K += float(e[i])*K1s[i]
        for (i,j),x in K2s.items(): K += float(e[i]*e[j])*x
        K += float(e[0]*e[1]*e[2])*K3
        return np.linalg.inv(K)

    full=-G@K3@G
    pair_only=np.zeros_like(G)
    for i in range(3):
        pair=tuple(sorted(j for j in range(3) if j!=i)); P=K2s[pair]
        z=G@K1s[i]@G@P@G + G@P@G@K1s[i]@G
        full += z; pair_only += z
    triple_only=np.zeros_like(G)
    for perm in itertools.permutations(range(3)):
        z=G@K1s[perm[0]]@G@K1s[perm[1]]@G@K1s[perm[2]]@G
        full -= z; triple_only += z

    steps=[0.03,0.015,0.0075]
    errors=[]
    for h in steps:
        fd=np.zeros_like(G)
        for signs in itertools.product((-1,1),repeat=3):
            fd += float(np.prod(signs))*exact(np.asarray(signs,float)*h)
        fd /= 8.0*h**3
        errors.append(float(np.max(np.abs(fd-full))))
    return {
      'matrix_dimension':3,'steps':steps,'max_abs_errors_to_full_formula':errors,
      'full_formula_frobenius_norm':float(np.linalg.norm(full)),
      'six_K1K2_subset_frobenius_norm':float(np.linalg.norm(pair_only)),
      'omitted_full_minus_K1K2_frobenius_norm':float(np.linalg.norm(full-pair_only)),
      'K3_piece_frobenius_norm':float(np.linalg.norm(G@K3@G)),
      'K1cubed_piece_frobenius_norm':float(np.linalg.norm(triple_only)),
      'convergence_ratio_coarse_to_fine':float(errors[0]/errors[-1]) if errors[-1] else float('inf')
    }


def main():
    failures=[]
    # Bind the raw-valid Iter589 normalization authority.
    p589=ROOT/'results'/'iteration589_source_k1_k2_normalization'/'result.json'
    raw589=p589.read_bytes(); sha589=hashlib.sha256(raw589).hexdigest()
    if sha589!='90cd8591f34deb9a7c0d49a21d554bc8f776c5c2fdbef30cbcd88455b2a0dfad':
        raise SystemExit(('iteration589 raw sha drift',sha589))
    r589=json.loads(raw589)
    if r589.get('classification')!='PASS_MSSC001_K1_K2_SAME_ACTION_NORMALIZATION_CONTRACT__NON_RESIDUAL' or r589.get('failures')!=[]:
        raise SystemExit('iteration589 prerequisite not raw-valid PASS')

    u=universal_inverse_regression()
    if not (u['max_abs_errors_to_full_formula'][2] < u['max_abs_errors_to_full_formula'][0]/8.0):
        failures.append('universal inverse third-derivative finite-difference convergence failed')
    if not u['omitted_full_minus_K1K2_frobenius_norm']>1e-8:
        failures.append('universal omitted K3/K1cubed control unexpectedly vanished')

    # Inherit exact Iter368 fixture momenta/polarizations.
    p368=CROOT/'iteration368_tru1sq_timelike_full_prepruning_routing.py'
    src=p368.read_text(); marker='# Cache expensive same-parent blocks by routed loop momentum.'
    if src.count(marker)!=1: raise SystemExit('iteration368 setup boundary drift')
    ns={'__name__':'iteration590_parent368_fixture','__file__':str(p368)}
    with contextlib.redirect_stdout(io.StringIO()):
        exec(compile(src.split(marker,1)[0],str(p368),'exec'),ns,ns)
    if tuple(ns['LEGS'])!=LEGS: raise SystemExit(('leg order drift',ns['LEGS']))
    M=ns['M']; qs=[np.asarray(M[x][0],float) for x in LEGS]; hs=[np.asarray(M[x][1],float) for x in LEGS]
    if np.max(np.abs(sum(qs,np.zeros(4))))>2e-15: raise SystemExit('Iter368 fixture momentum closure drift')

    steps=[1e-2,5e-3,2.5e-3]
    fixture=[]
    for si,singleton in enumerate(LEGS):
        p0=-0.5*qs[si]
        k3vals=[mixed3_scalar(hs,p0,h) for h in steps]
        k3fine=float(k3vals[-1]); k3conv=float(abs(k3vals[-1]-k3vals[-2]))
        if abs(k3fine)<=1e-9: failures.append(f'{singleton}: actual fixture K3 unexpectedly zero')
        if k3conv>2e-7: failures.append(f'{singleton}: K3 mixed-derivative convergence too weak {k3conv}')

        # Evaluate the six K1^3 scalar-chain permutations on the same closed
        # three-mode fixture.  This is a nonzero-support diagnostic only; it is
        # not yet assigned to the retarded T_cut discontinuity.
        chains=[]; min_abs_inv=float('inf')
        for perm in itertools.permutations(range(3)):
            p=p0.copy(); amp=1.0
            for n,idx in enumerate(perm):
                pp=p+qs[idx]; amp*=K1(hs[idx],pp,p); p=pp
                if n<2:
                    inv=MASS*MASS-mdot(p); min_abs_inv=min(min_abs_inv,abs(inv)); amp*=1.0/inv
            chains.append({'order':[LEGS[i] for i in perm],'value':float(amp)})
        chain_sum=float(sum(x['value'] for x in chains))
        if abs(chain_sum)<=1e-10: failures.append(f'{singleton}: six-permutation K1cubed support unexpectedly zero')
        if min_abs_inv<=1e-6: failures.append(f'{singleton}: K1cubed diagnostic sampled near scalar pole {min_abs_inv}')
        fixture.append({'singleton_role':singleton,'p0':p0.tolist(),
                        'K3_mixed_steps':steps,'K3_mixed_values':k3vals,'K3_fine':k3fine,'K3_last_step_difference':k3conv,
                        'K1cubed_six_permutation_sum':chain_sum,'minimum_abs_internal_K0':float(min_abs_inv),
                        'K1cubed_permutations':chains})

    classification=('PASS_CUBIC_SOURCE_RESPONSE_COMPLETENESS_AUDIT__K1K2_ONLY_IS_SCOPED_NOT_FULL'
                    if not failures else 'FAIL_CUBIC_SOURCE_RESPONSE_COMPLETENESS_AUDIT')
    result={
      'iteration':590,'date':'2026-09-08','model_readiness_percent':24,
      'classification':classification,'scientific_gate_pass':not failures,'failures':failures,
      'parent_authorities':['Iter589 same-action K1/K2 normalization','Iter588 fixture routing','Iter218/583 MSSC-001 parent action'],
      'universal_identity':'d_abc G = -G Kabc G + sum_6(G Ki G Kjk G) - sum_6(G Ki G Kj G Kk G), G=K^-1',
      'universal_regression':u,
      'fixture_K3_and_K1cubed_support':fixture,
      'key_scope_result':'the six frozen K1/K2 placements are not by themselves the full third mixed inverse-kernel response; K3 and K1^3 have nonzero same-action support on the exact fixture',
      'projection_status':{
        'K3_under_hard_channel_Discontinuity':'NOT_YET_PROVEN_TO_PROJECT_OUT',
        'K1cubed_under_frozen_linked_T_cut':'NOT_YET_CLASSIFIED',
        'K1K2_only_as_complete_source_response':'NOT_AUTHORIZED_YET'
      },
      'important_nonclaim':'This does not say K3 or K1^3 survive the final retarded hard-channel T_cut. A local K3 may have zero discontinuity and other terms may be assigned/cancelled by the frozen linked observable, but that exclusion must be demonstrated rather than assumed.',
      'source_born_subtraction':'NOT_PERFORMED','candidate_residual':False,'ANSATZ_003':'FORBIDDEN','Fisher_resources':'FORBIDDEN',
      'next_gate_if_pass':'derive/freeze the T_cut origin projection for K3 and K1cubed on the Iter368/582 fixture. If K3 is local-analytic under D_s, prove D_s K3=0 in the frozen convention; independently classify the K1cubed chain against the existing linked K2/Ward bookkeeping. Only after those origin-accounting tests may the K1/K2 subset be called complete and used for the nonlinear Ward cancellation.'
    }
    out=ROOT/'results'/'iteration590_source_cubic_response_completeness'; out.mkdir(parents=True,exist_ok=True)
    rp=out/'result.json'; rp.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    sha=hashlib.sha256(rp.read_bytes()).hexdigest()
    audit={'iteration':590,'result_sha256':sha,'failures':failures,
           'classification':'PASS_RAW_AUTHORITY_AUDIT_ITER590_CUBIC_COMPLETENESS' if not failures else 'FAIL_RAW_AUTHORITY_AUDIT_ITER590_CUBIC_COMPLETENESS'}
    (out/'authority_audit.json').write_text(json.dumps(audit,indent=2,sort_keys=True)+'\n')
    print(json.dumps(result,indent=2,sort_keys=True))
    if failures: raise SystemExit(2)

if __name__=='__main__': main()
