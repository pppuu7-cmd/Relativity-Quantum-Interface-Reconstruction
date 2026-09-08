#!/usr/bin/env python3
"""Iteration 608: prospectively derive the universal scalar-pole distribution kernel.

This closes only the universal distribution-law part of the Iter607 blocker.  It does
not invent the concrete MSSC->native kinematic pullback or native normalization.
"""
from __future__ import annotations
import hashlib, json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
blocked=json.loads((ROOT/'candidate_gravity/results/iteration607_source_to_iter582_projection_raw_consumption.json').read_text())
out=ROOT/'results/iteration608_scalar_pole_distribution_projector'; out.mkdir(parents=True,exist_ok=True)
fail=[]
if blocked.get('classification')!='BLOCKED_ITER607_EXPLICIT_DISTRIBUTIONAL_SOURCE_TO_NATIVE_LINKED_PROJECTOR_ABSENT': fail.append('Iter607 blocker drift')
if blocked.get('zero_fill') is not False: fail.append('zero-fill drift')
# Frozen convention: for x=m^2-p^2 and Feynman +i0 denominator,
# 1/(x+i0)=PV(1/x)-i*pi*delta(x), hence Disc[F(x)] = F(x+i0)-F(x-i0)=-2*pi*i*delta(x).
result={
 'iteration':608,'date':'2026-09-08','model_readiness_percent':24,'candidate_residual':False,
 'classification':'PASS_UNIVERSAL_SCALAR_POLE_DISTRIBUTION_KERNEL__CONCRETE_NATIVE_PULLBACK_STILL_BLOCKED__NON_RESIDUAL' if not fail else 'BLOCKED_ITER608_PREREQUISITE_DRIFT',
 'scientific_gate_pass':not fail,
 'frozen_distribution_law':{
   'denominator':'x+i0 with x=m^2-p^2',
   'sokhotski_plemelj':'1/(x+i0)=PV(1/x)-i*pi*delta(x)',
   'disc_convention':'Disc F = F(x+i0)-F(x-i0)',
   'scalar_pole_disc':'-2*pi*i*delta(m^2-p^2)',
   'pullback_rule':'delta(f(z)) = sum_i delta(z-z_i)/abs(f_prime(z_i)) for simple real roots',
 },
 'still_blocked':[ 'concrete internal MSSC p_j^2(q^2) relation for each retained source family', 'root/Jacobian support in the native linked variable', 'native Y/T_cut normalization/sign binding to Iter582 without Born subtraction' ],
 'source_family_count':13,'q2_buckets':[-1.0,-0.34,-0.14],'source_born_subtraction':'NOT_PERFORMED','zero_fill':False,
 'ANSATZ_003':'FORBIDDEN','Fisher_resources':'FORBIDDEN','failures':fail,
 'next_gate':'derive the concrete internal-momentum-to-native-cut kinematic pullback and Jacobian from the frozen MSSC fixture/native observable; keep normalization BLOCKED until explicitly matched.'
}
r=out/'result.json'; r.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n'); sha=hashlib.sha256(r.read_bytes()).hexdigest()
a={'classification':'PASS_RAW_AUDIT_ITER608_SCALAR_POLE_KERNEL' if not fail else 'FAIL_RAW_AUDIT_ITER608','result_sha256':sha,'failures':fail}
(out/'authority_audit.json').write_text(json.dumps(a,indent=2,sort_keys=True)+'\n')
print(result['classification'],sha)
if fail: raise SystemExit('\n'.join(fail))
