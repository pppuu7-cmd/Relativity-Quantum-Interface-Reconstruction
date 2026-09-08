#!/usr/bin/env python3
"""Iteration 589: same-action normalization bridge between MSSC-001 K1 and mixed K2.

This gate is prospectively frozen before any K1+K2 Ward-block cancellation is
evaluated.  It removes a relative-factor ambiguity that would otherwise allow a
spurious cancellation.  Both kernels are derived from the SAME Iter218/Iter583
scalar parent action

  S_phi = -1/2 int sqrt(-g)[g^{mu nu} d_mu phi d_nu phi + m^2 phi^2],
  g = eta + kappa h, eta=(+---).

Using contravariant scalar momenta p,p' and covectors p_c=eta p, the quadratic
scalar inverse-kernel convention is

  K[g] = - p'_c (sqrt(-g) g^{-1}) p_c + m^2 sqrt(-g).

Then the first variation is

  K1(h;p',p) = -p'_c a1(h) p_c + m^2 b1(h)
              = (1/2) h_{mu nu} V^{mu nu}(p',p),

where V is exactly the Iter218/Iter587 one-graviton tensor.  Therefore no extra
relative factor may be inserted into the mixed second variation

  K2(h1,h2;p',p) = -p'_c bt(h1,h2) p_c + m^2 bs(h1,h2),

with bt,bs exactly the raw-valid Iter584 mixed geometric coefficients.

No source-tree value, Born subtraction, comparator quotient or residual is
computed here.
"""
from __future__ import annotations
import contextlib, hashlib, io, json
from pathlib import Path
import numpy as np

ROOT=Path(__file__).resolve().parents[1]
CROOT=ROOT/'candidate_gravity'/'code'
ETA=np.diag([1.,-1.,-1.,-1.])
MASS=0.7
LEGS=('s','a','b')
TOL=2e-12


def mdot(a,b):
    return float(np.asarray(a,float)@ETA@np.asarray(b,float))


def first_coeff(h):
    H=ETA@h; trH=float(np.trace(H))
    b1=0.5*trH
    a1=b1*ETA-ETA@h@ETA
    return a1,b1


def mixed_coeff(h1,h2):
    H1=ETA@h1; H2=ETA@h2
    t1=float(np.trace(H1)); t2=float(np.trace(H2))
    bs=t1*t2/4.0-float(np.trace(H1@H2))/2.0
    bt=(ETA@h1@ETA@h2@ETA + ETA@h2@ETA@h1@ETA
        -0.5*t1*(ETA@h2@ETA)-0.5*t2*(ETA@h1@ETA)+bs*ETA)
    return bt,bs


def V(pp,p):
    d=mdot(pp,p)
    return np.outer(pp,p)+np.outer(p,pp)-ETA*(d-MASS*MASS)


def K1(h,pp,p):
    a1,b1=first_coeff(h); ppc=ETA@pp; pc=ETA@p
    return -float(ppc@a1@pc)+MASS*MASS*b1


def K2(h1,h2,pp,p):
    bt,bs=mixed_coeff(h1,h2); ppc=ETA@pp; pc=ETA@p
    return -float(ppc@bt@pc)+MASS*MASS*bs


def main():
    failures=[]

    # Verify exact algebraic normalization K1=(1/2)h.V and the Iter218 Ward
    # identity on deterministic generic off-shell probes.
    rng=np.random.default_rng(589218)
    max_k1_match=0.; max_ward_match=0.
    for i in range(24):
        x=rng.normal(size=(4,4)); h=.1*(x+x.T)/2
        p=rng.normal(size=4); pp=rng.normal(size=4)
        lhs=K1(h,pp,p); rhs=0.5*float(np.sum(h*V(pp,p)))
        e=abs(lhs-rhs); max_k1_match=max(max_k1_match,e)
        if e>TOL: failures.append(f'probe {i}: K1 half-hV normalization mismatch {e}')

        q=pp-p; xi=rng.normal(size=4); qc=ETA@q; xic=ETA@xi
        hg=np.outer(qc,xic)+np.outer(xic,qc)
        ward_vec=(mdot(pp,pp)-MASS*MASS)*p-(mdot(p,p)-MASS*MASS)*pp
        lhsw=K1(hg,pp,p); rhsw=float(xic@ward_vec)
        ew=abs(lhsw-rhsw); max_ward_match=max(max_ward_match,ew)
        if ew>TOL: failures.append(f'probe {i}: pure-gauge K1 Ward mismatch {ew}')

    # Inherit the exact Iter368 three-mode fixture rather than retyping the
    # polarizations; this is the same fixture bound by Iter588.
    p368=CROOT/'iteration368_tru1sq_timelike_full_prepruning_routing.py'
    src=p368.read_text(); marker='# Cache expensive same-parent blocks by routed loop momentum.'
    if src.count(marker)!=1: raise SystemExit('iteration368 setup boundary drift')
    ns={'__name__':'iteration589_parent368_fixture','__file__':str(p368)}
    with contextlib.redirect_stdout(io.StringIO()):
        exec(compile(src.split(marker,1)[0],str(p368),'exec'),ns,ns)
    if tuple(ns['LEGS'])!=LEGS: raise SystemExit(('leg order drift',ns['LEGS']))
    M=ns['M']

    fixture=[]
    for singleton in LEGS:
        pair=tuple(x for x in LEGS if x!=singleton)
        q=np.asarray(M[singleton][0],float); p=-0.5*q; pp=+0.5*q
        k2=K2(np.asarray(M[pair[0]][1],float),np.asarray(M[pair[1]][1],float),pp,p)
        fixture.append({'singleton':singleton,'pair':list(pair),'source_q2':mdot(q,q),
                        'K2_mixed_same_action_normalization':float(k2)})

    if not np.all(np.isfinite([x['K2_mixed_same_action_normalization'] for x in fixture])):
        failures.append('nonfinite fixture K2 value')

    classification=('PASS_MSSC001_K1_K2_SAME_ACTION_NORMALIZATION_CONTRACT__NON_RESIDUAL'
                    if not failures else 'FAIL_MSSC001_K1_K2_NORMALIZATION_CONTRACT')
    result={
      'iteration':589,'date':'2026-09-08','model_readiness_percent':24,
      'classification':classification,'scientific_gate_pass':not failures,'failures':failures,
      'parent_action':'Iter218/Iter583 MSSC-001 scalar action; eta=(+---); m=0.7',
      'normalization_contract':{
        'inverse_kernel':'K[g]=-p_prime_cov (sqrt(-g) g^-1) p_cov + m^2 sqrt(-g)',
        'K1':'-p_prime_cov a1(h) p_cov + m^2 b1(h) = (1/2) h_{mu nu} V^{mu nu}',
        'K2':'-p_prime_cov bt(h1,h2) p_cov + m^2 bs(h1,h2)',
        'relative_factor_rule':'K1 and K2 are first and mixed-second derivatives of one K[g]; no independent factor/sign is permitted',
        'Iter584_bs':'trH1*trH2/4 - Tr(H1 H2)/2',
        'Iter584_bt':'E h1 E h2 E + E h2 E h1 E -(trH1/2)E h2 E -(trH2/2)E h1 E + bs E'
      },
      'audit':{'generic_probe_count':24,'max_K1_minus_half_hV_abs':max_k1_match,
               'max_pure_gauge_Ward_abs':max_ward_match,'tolerance':TOL},
      'iter368_iter588_fixture_K2_values':fixture,
      'interpretation':'The relative K1/K2 normalization is fixed by the same covariant scalar inverse kernel before any cancellation test; a later Ward PASS cannot be manufactured by choosing an extra factor of two or sign.',
      'explicit_nonclaims':['not a full K1+K2 Ward cancellation test','not a source tree value','not a comparator residual','not Candidate-Gravity model PASS/FAIL','not a novelty certificate'],
      'source_born_subtraction':'NOT_PERFORMED','ANSATZ_003':'FORBIDDEN','Fisher_resources':'FORBIDDEN',
      'next_gate_if_pass':'using exactly this normalization plus Iter588 singleton/pair routing and both block orientations, assemble the full same-fixture K1-G-K2 + K2-G-K1 source response and test the off-shell Ward identity including inverse-propagator RHS before any Iter582 mapping/comparator quotient'
    }
    out=ROOT/'results'/'iteration589_source_k1_k2_normalization'; out.mkdir(parents=True,exist_ok=True)
    rp=out/'result.json'; rp.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    sha=hashlib.sha256(rp.read_bytes()).hexdigest()
    audit={'iteration':589,'result_sha256':sha,'failures':failures,
           'classification':'PASS_RAW_AUTHORITY_AUDIT_ITER589_K1_K2_NORMALIZATION' if not failures else 'FAIL_RAW_AUTHORITY_AUDIT_ITER589_K1_K2_NORMALIZATION'}
    (out/'authority_audit.json').write_text(json.dumps(audit,indent=2,sort_keys=True)+'\n')
    print(json.dumps(result,indent=2,sort_keys=True))
    if failures: raise SystemExit(2)

if __name__=='__main__': main()
