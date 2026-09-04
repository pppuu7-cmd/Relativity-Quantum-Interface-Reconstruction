#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 430.

Diagnostic-only sensitivity audit of the deepest finite-difference stencils that
feed the traced numerator used by the unresolved double-double index 2.

The purpose is to separate arithmetic precision from inherited finite-difference
truncation before implementing the authorized Iteration-424 80/120-digit
fallback.  We reconstruct the routed class-3 numerator layer from Iteration 368
and evaluate the exact same physical row at fixed generic loop probes while
varying the already-existing derivative steps by prospective scale factors
{0.75, 1.0, 1.25}.  No physical mass node, cut integral, routing, numerator,
sign, normalization, or acceptance threshold is changed.

This is NOT a physical D_s gate.  It quantifies whether the parent numerator
stencils are likely to be material at the 2e-5 scale and therefore whether the
high-precision port must also carry an explicit truncation-stability certificate.
"""
from __future__ import annotations
import contextlib, io, json, math
from pathlib import Path
import numpy as np

ITERATION=430
TARGET_CLASS=3
TARGET_INDEX=2
Q2=-1.0
PHYSICAL_REFERENCE_TOL=2.0e-5
SCALES=(0.75,1.0,1.25)
BASE_H1=1.0e-4
BASE_H2=5.0e-4
BASE_HY=4.0e-5
PROBES=[np.array([.43,-.27,.39,.21]),np.array([.61,.19,-.31,.47]),np.array([.37,.52,.28,-.41])]

ROOT=Path(__file__).resolve().parent
P368=ROOT/'iteration368_tru1sq_timelike_full_prepruning_routing.py'
src=P368.read_text().split('# Cache expensive same-parent blocks by routed loop momentum.',1)[0]
ns={'__name__':'iteration430_parent368','__file__':str(P368)}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(src,str(P368),'exec'),ns,ns)

ETA=ns['ETA']; Q0=ns['Q0']; Q1=ns['Q1']; Asub=ns['Asub']; y_down=ns['y_down']
M=ns['M']; LEGS=ns['LEGS']; second_specs=ns['second_specs']; ksum=ns['ksum']; Y0=ns['Y0']

# Reconstruct the same row ordering used by Iterations 368/370/374.
rows=[]
for singleton in LEGS:
    pair=tuple(x for x in LEGS if x!=singleton)
    for i,spec in enumerate(second_specs(pair)):
        rows.append({'class_id':len(rows)+1,'singleton_leg':singleton,'pair_legs':pair,'spec_index':i,'spec':spec})
row=rows[TARGET_CLASS-1]
if row['class_id']!=TARGET_CLASS:
    raise RuntimeError('class_order_drift')


def mdot(v):
    z=np.asarray(v,complex)
    return complex(z@ETA@z)


def y1_scaled(x,hy):
    mode=[M[x]]
    return (y_down([hy],mode)-y_down([-hy],mode))/(2*hy)


def first_u1_scaled(x,p,h1):
    q=M[x][0]
    A1=Asub(M,(x,),p,h1=h1)
    return Q0(p+q)@A1@Q0(p)@Y0


def second_scaled(pair,spec,p,h1,h2,hy):
    pair=tuple(pair); site=spec['extra_site']
    if site=='V2':
        q=ksum(pair); A2=Asub(M,pair,p,h2=h2)
        return Q0(p+q)@A2@Q0(p)@Y0
    vleg=spec['V2_legs'][0]; dleg=spec['extra_local_legs'][0]
    qv=M[vleg][0]; qd=M[dleg][0]
    if site=='N_L':
        A1=Asub(M,(vleg,),p,h1=h1)
        return Q1(M,dleg,p+qv)@A1@Q0(p)@Y0
    if site=='N_R':
        A1=Asub(M,(vleg,),p+qd,h1=h1)
        return Q0(p+qd+qv)@A1@Q1(M,dleg,p)@Y0
    if site=='Y':
        A1=Asub(M,(vleg,),p+qd,h1=h1)
        return Q0(p+qd+qv)@A1@Q0(p+qd)@y1_scaled(dleg,hy)
    raise ValueError(site)


def denominator_shifts(r):
    s=r['singleton_leg']; pair=r['pair_legs']; spec=r['spec']; qp=ksum(pair)
    sh=[np.zeros(4),qp.copy()]; site=spec['extra_site']
    if site=='V2': sh += [qp.copy(),np.zeros(4)]
    else:
        v=spec['V2_legs'][0]; d=spec['extra_local_legs'][0]
        qv=M[v][0]; qd=M[d][0]
        if site=='N_L': sh += [qv+qd,qv,np.zeros(4)]
        elif site=='N_R': sh += [qp.copy(),qd,np.zeros(4)]
        elif site=='Y': sh += [qp.copy(),qd]
        else: raise ValueError(site)
    return sh


def stripped_scaled(r,p,h1,h2,hy):
    s=r['singleton_leg']; pair=r['pair_legs']; qp=ksum(pair)
    F=first_u1_scaled(s,p+qp,h1)
    S=second_scaled(pair,r['spec'],p,h1,h2,hy)
    amp=np.trace(F@S)
    den=1+0j
    for sh in denominator_shifts(r): den*=mdot(p+sh)
    return complex(amp*den)

baseline=[]
variants=[]
for p in PROBES:
    z0=stripped_scaled(row,p,BASE_H1,BASE_H2,BASE_HY); baseline.append(z0)
    rec={'p':p.tolist(),'baseline':[float(z0.real),float(z0.imag)],'variants':[]}
    for sc in SCALES:
        z=stripped_scaled(row,p,BASE_H1*sc,BASE_H2*sc,BASE_HY*sc)
        er=float(abs(z-z0)/max(1.0,abs(z),abs(z0)))
        rec['variants'].append({'scale':sc,'value':[float(z.real),float(z.imag)],'scaled_delta_from_baseline':er})
    variants.append(rec)

max_all=max(v['scaled_delta_from_baseline'] for r in variants for v in r['variants'])
max_nontrivial=max(v['scaled_delta_from_baseline'] for r in variants for v in r['variants'] if abs(v['scale']-1.0)>1e-15)

# One-at-a-time attribution at the central probe.
p=PROBES[0]; z0=stripped_scaled(row,p,BASE_H1,BASE_H2,BASE_HY)
attribution=[]
for name in ('h1','h2','hy'):
    for sc in (0.75,1.25):
        h1,h2,hy=BASE_H1,BASE_H2,BASE_HY
        if name=='h1': h1*=sc
        elif name=='h2': h2*=sc
        else: hy*=sc
        z=stripped_scaled(row,p,h1,h2,hy)
        attribution.append({'parameter':name,'scale':sc,'scaled_delta':float(abs(z-z0)/max(1.0,abs(z),abs(z0)))})
max_attr=max(x['scaled_delta'] for x in attribution)
material=bool(max_nontrivial>PHYSICAL_REFERENCE_TOL)
execution_valid=bool(all(np.isfinite([max_all,max_nontrivial,max_attr])) and len(variants)==len(PROBES))
classification=(
    'PASS_CHANNEL2_DEEP_NUMERATOR_STENCIL_SENSITIVITY__MATERIAL_DIAGNOSTIC_ONLY' if execution_valid and material else
    'PASS_CHANNEL2_DEEP_NUMERATOR_STENCIL_SENSITIVITY__SUBTHRESHOLD_DIAGNOSTIC_ONLY' if execution_valid else
    'FAIL_CHANNEL2_DEEP_NUMERATOR_STENCIL_SENSITIVITY_EXECUTION'
)
result={
 'iteration':ITERATION,'model_readiness_percent':24,'candidate_residual':False,'scientific_gate_pass':execution_valid,
 'classification':classification,'authority_scope':'DIAGNOSTIC_ONLY__NO_PHYSICAL_COORDINATE_PROMOTION',
 'target':{'double_double_global_index':TARGET_INDEX,'class_id':TARGET_CLASS,'q_squared':Q2},
 'row_identity':{'singleton_leg':row['singleton_leg'],'pair_legs':list(row['pair_legs']),'spec_index':row['spec_index'],'spec':row['spec']},
 'base_steps':{'h1':BASE_H1,'h2':BASE_H2,'hy':BASE_HY},'simultaneous_scale_factors':list(SCALES),
 'physical_reference_tolerance_only_not_acceptance':PHYSICAL_REFERENCE_TOL,
 'probe_results':variants,'one_at_a_time_attribution':attribution,
 'max_simultaneous_nontrivial_scaled_delta':max_nontrivial,'max_one_at_a_time_scaled_delta':max_attr,
 'material_relative_to_2e-5_reference':material,
 'interpretation':(
   'If MATERIAL, inherited numerator finite-difference truncation is large enough at generic routed probes that the Iteration-424 high-precision implementation must include an explicit stencil/truncation stability certificate; more decimal digits alone are insufficient. '
   'If SUBTHRESHOLD, arithmetic precision remains the stronger immediate suspect, though finite-difference truncation is still a distinct error source.'
 ),
 'guardrails':['DIAGNOSTIC_ONLY','GENERIC_ROUTED_PROBES_NOT_CUT_AUTHORITY','NO_PHYSICAL_DS_VALUE','NO_THRESHOLD_WEAKENING','NO_MASS_STEP_CHANGE','NO_NUMERATOR_CHANGE','NO_ROUTING_CHANGE','NO_ZERO_FILL','NO_ANSATZ003','NO_FISHER_RESOURCES']
}
print(json.dumps(result,indent=2,sort_keys=True))
if not execution_valid: raise SystemExit(2)
