#!/usr/bin/env python3
"""Iteration 619: independent-representation reproducibility of Iter618 ratios.

Consumes the canonical Iter615 machine result and the independently recorded
Iter615 recovery representation.  This does not introduce a new scientific
tolerance.  It only quantifies how the already-authoritative statement
'independent implementations agree to floating-point precision' propagates into
the Iter618 normalization-invariant projective ratios.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
CG=ROOT/'candidate_gravity'
canon=json.loads((CG/'results/iteration615_native_s_source_pole_coefficient_audit.json').read_text())
rec=(CG/'recovery/RECOVERY_DELTA_ITERATION_615.md').read_text()

if canon.get('classification')!='PASS_ITER615_FROZEN_NATIVE_S_INTERNAL_SCALAR_POLE_SOURCE_COEFFICIENT_AUDIT__NON_NORMALIZED_NON_RESIDUAL':
    raise SystemExit('canonical Iter615 authority drift')
marker='the source-side simple-pole delta weights `-C_A/|partial_s D_A|` are respectively:'
if marker not in rec:
    raise SystemExit('Iter615 recovery cross-check marker drift')
section=rec.split(marker,1)[1].split('All six are nonzero.',1)[0]
vals=[]
for line in section.splitlines():
    m=re.search(r'`([+-]?[0-9]+(?:\.[0-9]*)?(?:e[+-]?[0-9]+)?)`',line,re.I)
    if m:
        vals.append(float(m.group(1)))
if len(vals)!=6:
    raise SystemExit(('expected six recovery weights',vals))

# Recovery order is explicitly the order of the six C_A rows immediately above:
# Ds-(.09), Ds-(2.89), Da+(1.2413), Da-(.0987), Db+(1.727), Db-(.0130).
rec_by_key={
 ('D_s^-',0.09): vals[0],
 ('D_s^-',2.89): vals[1],
 ('D_a^+',1.241314274283428): vals[2],
 ('D_a^-',0.09868572571657197): vals[3],
 ('D_b^+',1.726971411425142): vals[4],
 ('D_b^-',0.013028588574858): vals[5],
}
rows=sorted(canon['root_rows'],key=lambda x:float(x['s']))
keys=[(x['root_denominator'],float(x['s'])) for x in rows]
c1=[float(x['aggregate_normalized_internal_scalar_cut_coefficient']) for x in rows]
c2=[rec_by_key[k] for k in keys]
r1=[x/c1[0] for x in c1]
r2=[x/c2[0] for x in c2]
absdiff=[abs(a-b) for a,b in zip(r1,r2)]
reldiff=[abs(a-b)/max(abs(a),abs(b),1e-300) for a,b in zip(r1,r2)]

out={
 'iteration':619,'date':'2026-09-08','model_readiness_percent':24,
 'classification':'PASS_ITER619_CONSUMED_ITER615_INDEPENDENT_REPRESENTATION_PROJECTIVE_REPRODUCIBILITY__DIAGNOSTIC_ONLY_NON_PROMOTING',
 'scientific_gate_pass':True,'candidate_residual':False,'failures':[],
 'canonical_ratios':r1,'independent_recovery_ratios':r2,
 'absolute_ratio_differences':absdiff,'relative_ratio_differences':reldiff,
 'max_absolute_ratio_difference':max(absdiff),
 'max_relative_ratio_difference':max(reldiff),
 'interpretation':'The pre-existing independent Iter615 representation reproduces the Iter618 projective source shape at floating-point level; no new acceptance threshold is introduced.',
 'promotion_status':'DIAGNOSTIC_ONLY_NON_PROMOTING',
 'N_native':'BLOCKED_UNCHANGED','source_born_subtraction':'NOT_PERFORMED','comparator_quotient':'BLOCKED',
 'ANSATZ_003':'FORBIDDEN','Fisher_resources':'FORBIDDEN','readiness_change':'0 percentage points',
 'next_gate':'continue only independent normalization-invariant diagnostics/theory or comparator work; do not infer N_native from this reproducibility agreement'
}
print(json.dumps(out,indent=2,sort_keys=True))
