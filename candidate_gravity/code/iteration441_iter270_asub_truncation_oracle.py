#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 441.

Prospectively frozen representation/truncation oracle for Iteration-270 Acoef/Asub.
Compares the frozen central two-point-per-axis stencil to an independent tensor-product
fourth-order first-derivative stencil at the same base h spacings (using ±h, ±2h only).
No smaller h is introduced. Non-promoting.
"""
from __future__ import annotations
import contextlib, hashlib, io, itertools, json
from pathlib import Path
import numpy as np
import mpmath as mp

ITERATION=441
MODEL_READINESS=24
MP_LEVELS=(80,120)
MP_CROSS_LIMIT=mp.mpf('1e-30')
REP_LIMIT=mp.mpf('2e-5')
REQUIRED_HIGHORDER_NODES=124
REQUIRED_SUBSETS=7

root=Path(__file__).resolve().parent
src270=root/'iteration270_vd_physical_b3_nonzero.py'
raw270=src270.read_bytes(); text270=raw270.decode()
source_checks={
 'A_finite':'def A_finite(amps,modes,p,total_shift):' in text270,
 'Acoef':'def Acoef(M,legs,p,h):' in text270,
 'Asub':'def Asub(M,legs,p,h1=1e-4,h2=5e-4,h3=1e-3):' in text270,
}
if not all(source_checks.values()): raise SystemExit(('iteration270_source_drift',source_checks))

src438=root/'iteration438_iter270_a_finite_multiprecision_core.py'
t438=src438.read_text(); marker="subsets=[('s',),('a',),('b',),('s','a'),('s','b'),('a','b'),('s','a','b')]"
if t438.count(marker)!=1: raise SystemExit(('iteration438_boundary_drift',t438.count(marker)))
P={'__name__':'iteration441_parent438_prefix','__file__':str(src438)}
with contextlib.redirect_stdout(io.StringIO()): exec(compile(t438.split(marker,1)[0],str(src438),'exec'),P,P)
base=P['base']; A_finite_mp=P['A_finite_mp']; mp_max_scaled_matrix_diff=P['mp_max_scaled_matrix_diff']; mp_fro_norm=P['mp_fro_norm']

resdir=root.parent/'results'
s440=json.loads((resdir/'iteration440_acoef_asub_multiprecision_closure_summary.json').read_text())
if s440.get('scientific_gate_pass') is not True:
    raise SystemExit('iteration440_prerequisite_not_passed')

subsets=[('s',),('a',),('b',),('s','a'),('s','b'),('a','b'),('s','a','b')]
hstr={1:'1e-4',2:'5e-4',3:'1e-3'}
# Fourth-order first derivative: [f(-2h)-8f(-h)+8f(h)-f(2h)]/(12h)
node_mult=(-2,-1,1,2)
weight={-2:mp.mpf(1),-1:mp.mpf(-8),1:mp.mpf(8),2:mp.mpf(-1)}
rows=[]; max_cross=mp.mpf('0'); max_rep=mp.mpf('0'); all_finite=True; node_count=0
for legs in subsets:
    modes=[base['POS'][x] for x in legs]
    total_shift=sum((np.asarray(base['POS'][x][0],float) for x in legs),np.zeros(4))
    refs={}; centrals={}
    for dps in MP_LEVELS:
        with mp.workdps(dps):
            h=mp.mpf(hstr[len(legs)])
            high=mp.matrix(4,4)
            for mults in itertools.product(node_mult,repeat=len(legs)):
                coeff=mp.mpf(1)
                amps=[]
                for m in mults:
                    coeff*=weight[m]; amps.append(mp.mpf(m)*h)
                A=A_finite_mp(amps,modes,base['P0'],total_shift)
                high += coeff*A
                if dps==80: node_count += 1
            high /= (mp.mpf(12)*h)**len(legs)
            refs[dps]=high

            central=mp.matrix(4,4)
            for sig in itertools.product((-1,1),repeat=len(legs)):
                A=A_finite_mp([mp.mpf(s)*h for s in sig],modes,base['P0'],total_shift)
                central += int(np.prod(sig))*A
            central /= (mp.mpf(2)*h)**len(legs)
            centrals[dps]=central
    with mp.workdps(160):
        cross=mp_max_scaled_matrix_diff(refs[80],refs[120])
        rep=mp_max_scaled_matrix_diff(centrals[120],refs[120])
    finite=all(mp.isfinite(refs[d][i,j]) and mp.isfinite(centrals[d][i,j]) for d in MP_LEVELS for i in range(4) for j in range(4))
    max_cross=max(max_cross,cross); max_rep=max(max_rep,rep); all_finite=all_finite and bool(finite)
    rows.append({'legs':list(legs),'h':float(hstr[len(legs)]),'highorder_node_count':4**len(legs),
                 'mp80_vs_mp120_highorder_scaled':mp.nstr(cross,30),
                 'central_vs_highorder_mp120_scaled':mp.nstr(rep,30),
                 'central_mp120_fro_norm':mp.nstr(mp_fro_norm(centrals[120]),30),
                 'highorder_mp120_fro_norm':mp.nstr(mp_fro_norm(refs[120]),30),'finite':bool(finite)})

subset_count=len(rows)
gate=bool(max_cross<=MP_CROSS_LIMIT and max_rep<=REP_LIMIT and all_finite and node_count==REQUIRED_HIGHORDER_NODES and subset_count==REQUIRED_SUBSETS)
classification='PASS_ITER270_ASUB_FIXED_H_FOURTH_ORDER_DERIVATIVE_ORACLE__NON_PROMOTING' if gate else 'BLOCKED_ITER270_ASUB_FIXED_H_TRUNCATION_REPRESENTATION'
result={
 'iteration':ITERATION,'model_readiness_percent':MODEL_READINESS,'candidate_residual':False,
 'authority_scope':'PARENT_REPRESENTATION_CLOSURE__ITERATION270_ASUB_FIXED_H_STENCIL__NON_PROMOTING',
 'classification':classification,'scientific_gate_pass':gate,
 'source_path':str(src270),'source_sha256':hashlib.sha256(raw270).hexdigest(),'source_checks':source_checks,
 'prerequisite':s440.get('classification'),
 'frozen_inputs':{'M':'POS','P0':[float(x) for x in base['P0']],'subsets':[list(x) for x in subsets],
                  'h_by_subset_size':{'1':1e-4,'2':5e-4,'3':1e-3},
                  'highorder_axis_nodes':[-2,-1,1,2],
                  'highorder_axis_weights':[1,-8,8,-1],
                  'highorder_denominator':'12h per differentiated axis'},
 'precision_levels_decimal_digits':list(MP_LEVELS),
 'thresholds':{'mp80_vs_mp120_highorder_scaled_max':'1e-30','central_vs_highorder_mp120_scaled_max':'2e-5',
               'required_highorder_node_count':REQUIRED_HIGHORDER_NODES,'required_subset_count':REQUIRED_SUBSETS},
 'observed':{'max_mp80_vs_mp120_highorder_scaled':mp.nstr(max_cross,30),
             'max_central_vs_highorder_mp120_scaled':mp.nstr(max_rep,30),
             'all_values_finite':all_finite,'highorder_node_count':node_count,'subset_count':subset_count},
 'rows':rows,
 'interpretation':'This gate tests fixed-h representation/truncation without reducing any parent spacing. PASS means the frozen central stencil agrees with an independent fourth-order tensor-product derivative oracle within the prospectively frozen 2e-5 ceiling. FAIL/BLOCKED is preserved and forbids outward precision promotion.',
 'next_gate':'If raw-valid PASS, certify the next outward dependency layer 368/370 under continuous arbitrary-precision provenance or quantitative retained-binary64 bounds. If BLOCKED, localize the failing subset/component and replace the finite-difference representation rather than weakening h or thresholds.',
 'guardrails':['NO_PHYSICAL_DS_VALUE','NO_SMALLER_AMPLITUDE_H','NO_PHYSICAL_MASS_STEP_CHANGE','NO_THRESHOLD_WEAKENING','NO_PARENT_DYNAMICS_CHANGE','NO_ZERO_FILL','NO_ANSATZ003','NO_FISHER_RESOURCES']
}
print(json.dumps(result,indent=2,sort_keys=True))
if not gate: raise SystemExit(2)
