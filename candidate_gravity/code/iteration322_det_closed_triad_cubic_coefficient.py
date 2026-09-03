#!/usr/bin/env python3
"""RQIR Iteration 322: momentum-closed shared-background cubic determinant gate.

Reuses the already validated Iteration-319/320 implementations, but replaces the
third Fourier mode by q3=-(q1+q2) before either H or N is constructed. This is a
non-collinear closed triad. The generated common-fixture calculation is then
run through the same independent graviton/ghost exact-geometry validations and
frozen cubic logdet topology. No Source/Born subtraction is performed.
"""
from __future__ import annotations
import json, pathlib, subprocess, sys, tempfile
root=pathlib.Path(__file__).resolve().parents[2]
p319=root/'candidate_gravity/code/iteration319_det_graviton_three_mode_routing.py'
p320=root/'candidate_gravity/code/iteration320_det_shared_background_cubic_coefficient.py'
s319=p319.read_text()
old="qs=[np.array([.27,-.19,.31,.11]),np.array([-.13,.37,.17,-.29]),np.array([.22,.08,-.34,.41])]"
new="qs=[np.array([.27,-.19,.31,.11]),np.array([-.13,.37,.17,-.29]),np.array([-.14,-.18,-.48,.18])]"
if old not in s319: raise SystemExit('BLOCKED: frozen Iteration-319 q fixture literal changed')
s319=s319.replace(old,new)
with tempfile.TemporaryDirectory() as td:
    td=pathlib.Path(td); g319=td/'iteration319_closed.py'; g319.write_text(s319)
    s320=p320.read_text()
    oldpath="runpy.run_path('candidate_gravity/code/iteration319_det_graviton_three_mode_routing.py')"
    newpath=f"runpy.run_path({str(g319)!r})"
    if oldpath not in s320: raise SystemExit('BLOCKED: Iteration-320 parent-load contract changed')
    g320=td/'iteration320_closed.py'; g320.write_text(s320.replace(oldpath,newpath))
    cp=subprocess.run([sys.executable,str(g320)],cwd=root,text=True,capture_output=True)
    if cp.returncode not in (0,2):
        print(cp.stderr,file=sys.stderr); raise SystemExit(cp.returncode)
    try: base=json.loads(cp.stdout)
    except Exception:
        print(cp.stdout,file=sys.stderr); print(cp.stderr,file=sys.stderr); raise
q1=[.27,-.19,.31,.11]; q2=[-.13,.37,.17,-.29]; q3=[-.14,-.18,-.48,.18]
qtot=[q1[i]+q2[i]+q3[i] for i in range(4)]
closure=max(abs(x) for x in qtot)
base_pass=bool(base.get('scientific_gate_pass'))
ok=base_pass and closure < 1e-14
result={
 'iteration':322,'model_readiness_percent':24,'scientific_gate_pass':ok,
 'classification':('PASS_MOMENTUM_CLOSED_PHYSICAL_DETERMINANT_E0C3_INTEGRAND_COEFFICIENT' if ok else 'FAIL_MOMENTUM_CLOSED_PHYSICAL_DETERMINANT_E0C3_INTEGRAND_COEFFICIENT'),
 'candidate_residual':False,
 'trace_closure':{'q1':q1,'q2':q2,'q3':q3,'q_total':qtot,'max_abs':closure,'closed':closure<1e-14},
 'shared_background_parent_result':base,
 'scientific_status':'delta-supported trace-closure prerequisite satisfied; coefficient remains loop-integrand level until denominator-family reduction/pole-cut classification',
 'guardrails':['NO_SOURCE_BORN_SUBTRACTION','NOT_A_COMPARATOR_RESIDUAL','NO_ANSATZ003','NO_FISHER_RESOURCES','NO_BLIND_HEAVY_FULL_C5','UNSUPPORTED_IS_BLOCKED_NOT_ZERO_FILLED'],
 'next_gate':('enumerate/reduce the momentum-closed determinant coefficient into loop-denominator families and classify pole/cut origin before any matched Source/Born subtraction' if ok else 'preserve FAIL and repair closed-triad H/N routing without weakening frozen thresholds')
}
print(json.dumps(result,indent=2,sort_keys=True))
if not ok: raise SystemExit(2)
