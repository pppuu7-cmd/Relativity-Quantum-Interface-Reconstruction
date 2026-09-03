#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 350.

Fail-closed audit before physically substituting the Iteration-346 12-route U2
survivors on the matched timelike fixture. Iteration 346 inherited 18 exact
singleton-soft kills from Iteration 308 by setting the designated soft-leg A1
component to zero. Iteration 348, however, re-specialized physical A1/A2 on an
exact timelike triad. This gate asks whether that designated singleton remains
zero on the timelike fixture. If not, the 12-route survivor set may NOT be
silently reused; the physical timelike route census must be rebuilt from all 30
placements without null-soft pruning.
"""
from __future__ import annotations
import contextlib, io, json, re
from pathlib import Path
import numpy as np

ROOT=Path(__file__).resolve().parent
PARENT=ROOT/'iteration341_u2_v1_a12_same_parent_geometry.py'
src=PARENT.read_text().split('def geom_x',1)[0]
old=r"D=4; M=2; ZERO=\(0,0\)\neta=np\.diag\(\[-1\.,1\.,1\.,1\.\]\)\.astype\(complex\)\nrng=np\.random\.default_rng\(341\)\nhs=\[\]\nfor _ in range\(M\):\n    x=rng\.normal\(size=\(D,D\)\); hs\.append\(0\.08\*\(x\+x\.T\)/2\)\nqs=\[np\.array\(\[\.31,-\.17,\.23,\.11\]\), np\.array\(\[-\.19,\.29,\.13,-\.37\]\)\]\np=np\.array\(\[\.43,-\.27,\.39,\.21\]\)"
new="""D=4; M=3; ZERO=(0,0,0)
eta=np.diag([-1.,1.,1.,1.]).astype(complex)
rng=np.random.default_rng(319)
hs=[]
for _ in range(M):
    x=rng.normal(size=(D,D)); hs.append(0.12*(x+x.T)/2)
qs=[np.array([1.0,0.0,0.0,0.0]),np.array([-0.4,0.1,0.1,0.0]),np.array([-0.6,-0.1,-0.1,0.0])]
p=np.array([.43,-.27,.39,.21])"""
src,n=re.subn(old,new,src,count=1)
if n!=1: raise RuntimeError(f'Iteration-341 fixture signature drift: {n}')
ns={'__name__':'iteration350_a_provider','__file__':str(PARENT)}
with contextlib.redirect_stdout(io.StringIO()): exec(compile(src,'iteration350_a_provider','exec'),ns,ns)
A=ns['Acoef']; qs=ns['qs']; eta=ns['eta']
first=[(1,0,0),(0,1,0),(0,0,1)]
norms={str(a):float(np.max(np.abs(A[a]))) for a in first}
q2=[float(np.real(np.asarray(q)@eta@np.asarray(q))) for q in qs]
soft_mode=(1,0,0)
soft_norm=norms[str(soft_mode)]
zero_threshold=1e-12
soft_is_exact_zero=soft_norm<=zero_threshold
# Audit itself passes if it cleanly establishes either compatibility or a
# fail-closed incompatibility; compatibility is a separate scientific field.
audit_pass=bool(np.isfinite(soft_norm) and all(np.isfinite(x) for x in norms.values()))
classification=(
 'PASS_AUDIT_TIMELIKE_REBASE_PRESERVES_SINGLETON_SOFT_A1_ZERO__ITERATION346_12_SURVIVORS_REUSABLE'
 if soft_is_exact_zero else
 'PASS_AUDIT_TIMELIKE_REBASE_BREAKS_SINGLETON_SOFT_A1_ZERO__ITERATION346_12_SURVIVORS_NOT_PHYSICAL_AUTHORITY__REBUILD_30_ROUTE_CENSUS_NEXT'
)
result={
 'iteration':350,'model_readiness_percent':24,'scientific_gate_pass':audit_pass,
 'classification':classification,'candidate_residual':False,
 'fixture':{'q_squared':q2,'designated_iteration346_soft_leg':'mode (1,0,0)','matched_timelike_source':'Iteration348'},
 'physical_A1':{'per_mode_max_abs':norms,'designated_soft_mode_max_abs':soft_norm,'exact_zero_threshold':zero_threshold,'singleton_soft_zero_preserved':soft_is_exact_zero},
 'route_authority':{'iteration346_12_survivors_reusable_on_timelike_fixture':soft_is_exact_zero,'if_false':'BLOCKED_REBUILD_FROM_ALL_30_RAW_PLACEMENTS_WITH_PHYSICAL_A_COMPONENTS'},
 'guardrails':['DO_NOT_ZERO_FILL_TIMELIKE_A1','DO_NOT_REUSE_NULL_SOFT_KILLS_OUTSIDE_THEIR_LIMIT','NEGATIVE_AUDIT_RESULT_IS_SCIENTIFIC_RESULT','NO_CUT_INTEGRATION_BEFORE_PHYSICAL_ROUTE_CENSUS','NO_SOURCE_BORN_SUBTRACTION','NO_ANSATZ003','NO_FISHER_RESOURCES','NO_BLIND_FULL_C5'],
 'next_gate':('physical substitution into 12 Iteration346 survivors' if soft_is_exact_zero else 'rebuild matched-timelike physical cubic U2 route census from all 30 Iteration308 raw placements; evaluate which routes are actually zero/nonzero with Iteration348/349 providers before family reduction')
}
print(json.dumps(result,indent=2,sort_keys=True))
if not audit_pass: raise SystemExit(2)
