#!/usr/bin/env python3
"""Continuous 80/120-digit certificate for Iteration-407 spectral algebra.

The already-authorized fixed-mass numerator/phi samples are treated as frozen
parent inputs. This stage certifies only the downstream degree-4 interpolation,
affine-denominator monomial recurrence, and terminal spectral contraction.
It does not claim continuous precision for parent sample generation and cannot
promote physical index 2.
"""
from __future__ import annotations
import contextlib,io,json,hashlib
from pathlib import Path
import mpmath as mp
import numpy as np
ROOT=Path(__file__).resolve().parents[2]
P=ROOT/'candidate_gravity/code/iteration407_tru1sq_channel4_analytic_spectral_reduction.py'
s=P.read_text(); marker='start=time.perf_counter()'
ns={'__name__':'rqir407_spectral_stage','__file__':str(P)}
# Operational source-loader repair: Iteration 407 itself contains the marker
# literal while loading its parent, so split at the final run marker only.
with contextlib.redirect_stdout(io.StringIO()): exec(compile(s.rsplit(marker,1)[0],str(P),'exec'),ns,ns)
BASE=float(ns['BASE_H']); HALF=float(ns['HALF_H']); TRAIN=np.asarray(ns['TRAIN_Z'],float); DEG=int(ns['POLY_DEGREE'])
phi_mean=ns['phi_mean_num']; affine=ns['affine_coeffs']; beta_of=lambda u,v: ns['kin'](u,v)[2]
TH=mp.mpf('1e-30')

def mps(x): return mp.mpf(repr(float(x)))
def mpc(z): return mp.mpc(repr(float(np.real(z))),repr(float(np.imag(z))))

def solve_and_integrate(u,v,dps):
  # Parent samples are frozen at their returned complex values before this layer.
  samples=[phi_mean(u,v,float(z))[0] for z in TRAIN]
  cc0,aa0=affine(u,v); beta0=beta_of(u,v)
  with mp.workdps(dps):
    zz=[mps(z) for z in TRAIN]; yy=[mpc(x) for x in samples]
    V=mp.matrix([[z**k for k in range(DEG+1)] for z in zz]); Y=mp.matrix(yy)
    coeff=mp.lu_solve(V,Y)
    cc,aa,beta=mpc(cc0),mpc(aa0),mps(beta0)
    if abs(aa)<mp.mpf('1e-50'):
      js=[(mp.mpf('0') if k%2 else mp.mpf(2)/(k+1))/cc for k in range(DEG+1)]
    else:
      js=[(mp.log(cc+aa)-mp.log(cc-aa))/aa]
      for k in range(1,DEG+1):
        im1=mp.mpf('0') if (k-1)%2 else mp.mpf(2)/k
        js.append((im1-cc*js[-1])/aa)
    sphere=mp.mpf('0.5')*beta*sum(coeff[k]*js[k] for k in range(DEG+1))
    return mp.nstr(mp.re(sphere),dps),mp.nstr(mp.im(sphere),dps)

def main():
  rows=[]; mx=mp.mpf('0'); finite=True
  for hlabel,h in [('base',BASE),('half',HALF)]:
    for u in (-2*h,-h,h,2*h):
      for v in (-2*h,-h,h,2*h):
        a=solve_and_integrate(u,v,80); b=solve_and_integrate(u,v,120)
        with mp.workdps(140):
          z80=mp.mpc(mp.mpf(a[0]),mp.mpf(a[1])); z120=mp.mpc(mp.mpf(b[0]),mp.mpf(b[1])); scale=max(abs(z120),mp.mpf('1e-30')); d=abs(z80-z120)/scale
          mx=max(mx,d); ok=mp.isfinite(z120.real) and mp.isfinite(z120.imag); finite=finite and bool(ok)
          rows.append({'h_family':hlabel,'u':u,'v':v,'scaled_mp80_vs_mp120':mp.nstr(d,30),'finite':bool(ok)})
  passed=bool(len(rows)==32 and finite and mx<=TH)
  out={'stage':'ITER407_SPECTRAL_ALGEBRA_PRECISION__POST_ITER446_SOURCE_AUDIT__UNNUMBERED_UNTIL_RAW_CONSUME','authority_scope':'ITER407_DEG4_INTERPOLATION_AFFINE_LOG_RECURRENCE_TERMINAL_SPECTRAL_ASSEMBLY__FROZEN_PARENT_SAMPLES__NON_PROMOTING','classification':'PASS_ITER407_SPECTRAL_ALGEBRA_MP80_MP120__NON_PROMOTING' if passed else 'BLOCKED_ITER407_SPECTRAL_ALGEBRA_PRECISION__NON_PROMOTING','scientific_gate_pass':passed,'promotes_physical_coordinate':False,'parent_sample_generation_precision_closed_by_this_gate':False,'frozen':{'precision_digits':[80,120],'mass_nodes':32,'mass_steps':[BASE,HALF],'degree':DEG,'training_z':TRAIN.tolist()},'thresholds':{'scaled_mp80_vs_mp120_max':'1e-30','required_nodes':32},'observed':{'scaled_mp80_vs_mp120_max':mp.nstr(mx,30),'node_count':len(rows),'all_finite':finite},'rows':rows,'source_sha256':hashlib.sha256(P.read_bytes()).hexdigest(),'guardrails':['FROZEN_PARENT_SAMPLES_ONLY','SOURCE_AUDIT_NOT_NUMERICAL_CLOSURE','NO_REOPEN_ITER374','NO_PHYSICAL_INDEX2_PROMOTION','NO_THRESHOLD_WEAKENING','NO_ZERO_FILL'],'next_gate_if_pass':'carry continuous precision through phi-mean/sample-generation layer on the active index2 architecture before Iteration424 physical mass-node reevaluation','MODEL_READINESS':'24%','readiness_change_pp':0}
  print(json.dumps(out,indent=2,sort_keys=True))
  if not passed: raise SystemExit(2)
if __name__=='__main__': main()
