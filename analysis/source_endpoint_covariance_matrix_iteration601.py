#!/usr/bin/env python3
"""Iteration 601: derive and validate scalar endpoint/covariance matrix realization.

This is the exact next gate from Iter600.  It does not rerun the cubic Ward rows.
It fixes only the row/column realization of the frozen Fourier scalar rule

  Delta_xi phi(k) = int xi(l) (k-l)_rho phi(k-l),

for the operator kernel convention used by Iter597/599.

For a single gauge mode q with row momentum p_r=p_c+q:
  R_rc = xi . p_c            (right/column scalar endpoint)
  L_rc = - xi . p_r          (left/row dual scalar endpoint)

The Green-function covariance identity is therefore
  Delta G - R G - G L = 0,
not Delta G - T G - G T^T = 0.

The mandatory acceptance test is the Iter587 one-leg anchor on all three exact
symmetric routes p=-q/2, p'=+q/2 and all four xi basis vectors.  No thresholds,
fixture, source action, Fourier rule, or Candidate-Gravity q2 grouping are changed.
"""
from __future__ import annotations
import hashlib, json
from pathlib import Path
import numpy as np
import nonlinear_ward_full_response_iteration597 as base

ITERATION=601
ROOT=Path(__file__).resolve().parents[1]
TOL=2e-11
LEGS=base.LEGS
XI_BASIS=base.XI_BASIS


def symmetric_route(q):
    q=np.asarray(q,float)
    return -0.5*q,+0.5*q


def build_endpoint_generators(g,xi,inds,pos,ps):
    n=len(inds)
    R=np.zeros((n,n),complex)
    L=np.zeros((n,n),complex)
    sh=base.MODE[g]
    for c in inds:
        r=(c[0]+sh[0],c[1]+sh[1])
        if r in pos:
            pc=np.asarray(ps[c],float)
            pr=np.asarray(ps[r],float)
            # Frozen Fourier rule acting on the right scalar column.
            R[pos[r],pos[c]]=xi@(base.ETA@pc)
            # The left scalar is the dual row endpoint.  Its physical momentum
            # enters with the opposite orientation in the bilinear kernel.
            L[pos[r],pos[c]]=-xi@(base.ETA@pr)
    return R,L


def corrected_anchor(g,xi,p0,hs,qs):
    inds,pos,ps=base.lattice(p0,qs)
    modes=base.needed_modes(inds)
    A,B,dA,dB=base.metric_and_variation_grids(0.0,0.0,g,*tuple(x for x in LEGS if x!=g),xi,hs,qs)
    Ac={m:base.coeff_from_grid(A,m) for m in modes}
    Bc={m:base.coeff_from_grid(B,m) for m in modes}
    dAc={m:base.coeff_from_grid(dA,m) for m in modes}
    dBc={m:base.coeff_from_grid(dB,m) for m in modes}
    K=base.build_K_from_coeffs(Ac,Bc,inds,ps)
    dK=base.build_K_from_coeffs(dAc,dBc,inds,ps)
    G=np.linalg.inv(K)
    dG=-G@dK@G
    R,L=build_endpoint_generators(g,xi,inds,pos,ps)
    C=dG-R@G-G@L
    c=(0,0); sh=base.MODE[g]; r=(sh[0],sh[1])
    return C[pos[r],pos[c]],dG[pos[r],pos[c]],(R@G)[pos[r],pos[c]],(G@L)[pos[r],pos[c]],K,G,inds,pos,ps


def main():
    failures=[]
    front=(ROOT/'candidate_gravity'/'recovery'/'CURRENT_QG_FRONT.md').read_text()
    if 'Latest authoritative research iteration: **600**' not in front:
        raise SystemExit('Iter600 front authority not current at Iter601 freeze')
    qs,hs=base.inherit_fixture()
    rows=[]
    max_res=0.0
    max_old_prediction=0.0
    for g in LEGS:
        p0,pp=symmetric_route(qs[g])
        for ix,xi in enumerate(XI_BASIS):
            val,dg,rg,gl,K,G,inds,pos,ps=corrected_anchor(g,xi,p0,hs,qs)
            ab=float(abs(val)); max_res=max(max_res,ab)
            sh=base.MODE[g]; c=(0,0); r=(sh[0],sh[1])
            # Reconstruct the old Iter599 endpoint realization to verify the
            # Iter600 residual is exactly the omitted left endpoint.
            Told=base.build_T(g,xi,inds,pos,ps)
            old=dg-(Told@G)[pos[r],pos[c]]-(G@Told.T)[pos[r],pos[c]]
            missing=(G@build_endpoint_generators(g,xi,inds,pos,ps)[1])[pos[r],pos[c]]
            pred=float(abs(old-missing))
            max_old_prediction=max(max_old_prediction,pred)
            if ab>TOL: failures.append(f'corrected anchor {g}/xi{ix}={ab}')
            if pred>TOL: failures.append(f'old residual not explained by missing left endpoint {g}/xi{ix}: {pred}')
            rows.append({
              'gauge_leg':g,'xi_basis':ix,'p':p0.tolist(),'pprime':pp.tolist(),
              'corrected_covariance_residual_abs':ab,
              'deltaG_rc':[float(dg.real),float(dg.imag)],
              'right_endpoint_RG_rc':[float(rg.real),float(rg.imag)],
              'left_endpoint_GL_rc':[float(gl.real),float(gl.imag)],
              'old_iter599_covariance_rc':[float(old.real),float(old.imag)],
              'old_minus_missing_left_abs':pred,
            })
    result={
      'iteration':ITERATION,'date':'2026-09-08','model_readiness_percent':24,
      'classification':('PASS_SCALAR_ENDPOINT_COVARIANCE_MATRIX_REALIZATION_REPRODUCES_ITER587_ANCHOR__NON_RESIDUAL'
                        if not failures else 'FAIL_SCALAR_ENDPOINT_COVARIANCE_MATRIX_REALIZATION'),
      'scientific_gate_pass':not failures,'failures':failures,
      'frozen_fourier_rule':'Delta_xi phi(k)=int xi(l)(k-l)_rho phi(k-l)',
      'matrix_realization':{
        'right_column':'R_rc = xi . p_c for p_r=p_c+q',
        'left_row_dual':'L_rc = - xi . p_r for p_r=p_c+q',
        'green_covariance':'Delta G - R G - G L = 0',
        'old_iter599_form':'Delta G - T G - G T^T = 0 is not the correct left-endpoint realization for this row/column momentum convention'
      },
      'mandatory_anchor':'Iter587 exact one-graviton Ward relation on all three p=-q/2,pprime=+q/2 routes',
      'tolerance':TOL,'rows':rows,
      'observed':{'max_corrected_anchor_abs':max_res,'max_old_residual_minus_missing_left_abs':max_old_prediction},
      'interpretation':'Iter600 blocker is localized to endpoint matrix orientation: the old transpose places the left action on the wrong momentum shift. The corrected dual-row action is derived from the frozen Fourier rule and must pass the Iter587 anchor before any cubic Ward rerun.',
      'source_born_subtraction':'NOT_PERFORMED','source_to_iter582_map':'NOT_PERFORMED','candidate_residual':False,
      'ANSATZ_003':'FORBIDDEN','Fisher_resources':'FORBIDDEN',
      'next_gate_if_pass':'replace only the endpoint realization in the Iter599 covariance evaluator with R/L above; keep Iter596 five classes, Iter588 fixture, 13 source families and all frozen tolerances unchanged; then rerun the full nonlinear Ward gate',
      'next_gate_if_fail':'stop and rederive the row/column Fourier kernel orientation; do not rerun cubic Ward'
    }
    out=ROOT/'results'/'iteration601_endpoint_covariance_matrix'; out.mkdir(parents=True,exist_ok=True)
    rp=out/'result.json'; rp.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    sha=hashlib.sha256(rp.read_bytes()).hexdigest()
    audit={'iteration':ITERATION,'result_sha256':sha,'failures':failures,
           'classification':('PASS_RAW_AUTHORITY_AUDIT_ITER601_ENDPOINT_COVARIANCE' if not failures else 'FAIL_RAW_AUTHORITY_AUDIT_ITER601_ENDPOINT_COVARIANCE')}
    (out/'authority_audit.json').write_text(json.dumps(audit,indent=2,sort_keys=True)+'\n')
    print(json.dumps(result,indent=2,sort_keys=True))
    if failures: raise SystemExit(2)

if __name__=='__main__': main()
