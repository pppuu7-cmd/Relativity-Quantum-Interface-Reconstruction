#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 431.

Diagnostic-only sensitivity audit of the inherited h1 numerator stencil on
actual fixed-mass cut kinematics of unresolved double-double index 2 / class 3 /
q^2=-1.

Iteration 430 found only ~1.94e-13 sensitivity at generic routed probes.  This
iteration moves the same test onto the physical fixed-mass geometry used by the
Iteration-407 analytic/spectral F(u,v) representation.  The target class-3 row
is N_L with singleton s, V2 leg b and local derivative leg a, so h2 and hY do
not enter this primitive; only h1 is varied prospectively by {0.75,1,1.25}.

The frozen radial stripped-limit Richardson nodes {2e-3,1e-3,5e-4} are retained.
No cut integral, physical mass derivative, threshold, routing, numerator, sign,
normalization, or mass node is changed.  This is not a D_s authority gate.
"""
from __future__ import annotations
import contextlib, io, json, math
from pathlib import Path
import numpy as np

ITERATION=431
TARGET_INDEX=2
TARGET_CLASS=3
EXPECTED_Q2=-1.0
H1_BASE=1.0e-4
H1_SCALES=(0.75,1.0,1.25)
RADIAL_HS=(2.0e-3,1.0e-3,5.0e-4)
PHYSICAL_REFERENCE_TOL=2.0e-5
MASS_R=5.0e-6
Z_SAMPLES=(-0.43,0.43)
PHI_FRACS=(0.0,0.25)

ROOT=Path(__file__).resolve().parent
# Build target-2 fixed-mass geometry from Iteration 407 without executing its run.
p407=ROOT/'iteration407_tru1sq_channel4_analytic_spectral_reduction.py'
s407=p407.read_text()
for old,new in [
    ('ITERATION=407','ITERATION=431'),('TARGET_INDEX=4','TARGET_INDEX=2'),
    ("if int(ch['class_id'])!=5 or abs(q2+1.0)>1e-12: raise RuntimeError(('target_identity_drift',ch['class_id'],q2))",
     "if int(ch['class_id'])!=3 or abs(q2+1.0)>1e-12: raise RuntimeError(('target_identity_drift',ch['class_id'],q2))")]:
    if s407.count(old)!=1: raise RuntimeError(('iteration407_specialization_drift',old,s407.count(old)))
    s407=s407.replace(old,new,1)
marker='\nstart=time.perf_counter()\nd_base,diag_base=derivative_from_analytic(BASE_H)'
if s407.count(marker)!=1: raise RuntimeError(('iteration407_execution_boundary_drift',s407.count(marker)))
ns407={'__name__':'iteration431_parent407','__file__':str(p407)}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(s407.split(marker,1)[0]+'\n',str(p407),'exec'),ns407,ns407)

a=np.asarray(ns407['a'],float); q=np.asarray(ns407['q'],float); e1=np.asarray(ns407['e1'],float); e2=np.asarray(ns407['e2'],float); e3=np.asarray(ns407['e3'],float)
kin=ns407['kin']; ch=ns407['ch']; q2=float(ns407['q2'])
if int(ch['class_id'])!=TARGET_CLASS or abs(q2-EXPECTED_Q2)>1e-12: raise RuntimeError(('target_identity_drift',ch['class_id'],q2))

# Reconstruct the underlying physical numerator primitive from Iteration 368.
p368=ROOT/'iteration368_tru1sq_timelike_full_prepruning_routing.py'
s368=p368.read_text().split('# Cache expensive same-parent blocks by routed loop momentum.',1)[0]
ns={'__name__':'iteration431_parent368','__file__':str(p368)}
with contextlib.redirect_stdout(io.StringIO()): exec(compile(s368,str(p368),'exec'),ns,ns)
ETA=ns['ETA']; Q0=ns['Q0']; Q1=ns['Q1']; Asub=ns['Asub']; Y0=ns['Y0']; M=ns['M']; LEGS=ns['LEGS']; second_specs=ns['second_specs']; ksum=ns['ksum']

rows=[]
for singleton in LEGS:
    pair=tuple(x for x in LEGS if x!=singleton)
    for i,spec in enumerate(second_specs(pair)):
        rows.append({'class_id':len(rows)+1,'singleton_leg':singleton,'pair_legs':pair,'spec_index':i,'spec':spec})
row=rows[TARGET_CLASS-1]
if not (row['singleton_leg']=='s' and tuple(row['pair_legs'])==('a','b') and row['spec']['extra_site']=='N_L' and tuple(row['spec']['V2_legs'])==('b',) and tuple(row['spec']['extra_local_legs'])==('a',)):
    raise RuntimeError(('class3_row_identity_drift',row))

def mdot(v):
    z=np.asarray(v,complex); return complex(z@ETA@z)

def denominator_shifts(r):
    s=r['singleton_leg']; pair=r['pair_legs']; spec=r['spec']; qp=ksum(pair)
    sh=[np.zeros(4),qp.copy()]; site=spec['extra_site']
    if site=='V2': sh += [qp.copy(),np.zeros(4)]
    else:
        v=spec['V2_legs'][0]; d=spec['extra_local_legs'][0]; qv=M[v][0]; qd=M[d][0]
        if site=='N_L': sh += [qv+qd,qv,np.zeros(4)]
        elif site=='N_R': sh += [qp.copy(),qd,np.zeros(4)]
        elif site=='Y': sh += [qp.copy(),qd]
        else: raise ValueError(site)
    return sh

def stripped_h1(p,h1):
    s=row['singleton_leg']; pair=row['pair_legs']; qp=ksum(pair)
    # class 3 is N_L: both first-order A insertions depend on h1.
    qs=M[s][0]; A_single=Asub(M,(s,),p+qp,h1=h1)
    F=Q0(p+qp+qs)@A_single@Q0(p+qp)@Y0
    vleg=row['spec']['V2_legs'][0]; dleg=row['spec']['extra_local_legs'][0]
    qv=M[vleg][0]
    A1=Asub(M,(vleg,),p,h1=h1)
    S=Q1(M,dleg,p+qv)@A1@Q0(p)@Y0
    amp=np.trace(F@S); den=1+0j
    for sh in denominator_shifts(row): den*=mdot(p+sh)
    return complex(amp*den)

def unit_from(z,phi):
    rr=math.sqrt(max(0.0,1.0-z*z))
    return rr*math.cos(phi)*e1+rr*math.sin(phi)*e2+z*e3

def radial_limit(u,v,z,phi,h1):
    alpha,rho,_,_=kin(u,v); vec=rho*unit_from(z,phi); mids=[]
    for h in RADIAL_HS:
        vals=[]
        for sign in (+1,-1):
            p=-a+alpha*q+(1.0+sign*h)*vec
            vals.append(stripped_h1(p,h1))
        mids.append(0.5*(vals[0]+vals[1]))
    coarse=(4.0*mids[1]-mids[0])/3.0; fine=(4.0*mids[2]-mids[1])/3.0
    raderr=float(abs(fine-coarse)/max(1.0,abs(fine),abs(coarse),*(abs(x) for x in mids)))
    return fine,raderr

records=[]; max_delta=0.0; max_raderr=0.0
for su in (-1.0,1.0):
  for sv in (-1.0,1.0):
    u=su*MASS_R; v=sv*MASS_R
    for z in Z_SAMPLES:
      for frac in PHI_FRACS:
        phi=2.0*math.pi*frac
        base,rb=radial_limit(u,v,z,phi,H1_BASE); max_raderr=max(max_raderr,rb)
        variants=[]
        for sc in H1_SCALES:
            val,rr=radial_limit(u,v,z,phi,H1_BASE*sc); max_raderr=max(max_raderr,rr)
            er=float(abs(val-base)/max(1.0,abs(val),abs(base))); max_delta=max(max_delta,er)
            variants.append({'h1_scale':sc,'value':[float(val.real),float(val.imag)],'scaled_delta_from_baseline':er,'radial_richardson_scaled_error':rr})
        records.append({'u':u,'v':v,'z':z,'phi_fraction':frac,'baseline':[float(base.real),float(base.imag)],'baseline_radial_error':rb,'variants':variants})

material=bool(max_delta>PHYSICAL_REFERENCE_TOL)
execution_valid=bool(np.isfinite(max_delta) and np.isfinite(max_raderr) and len(records)==16)
classification=(
 'PASS_CHANNEL2_CUT_KINEMATIC_H1_SENSITIVITY__MATERIAL_DIAGNOSTIC_ONLY' if execution_valid and material else
 'PASS_CHANNEL2_CUT_KINEMATIC_H1_SENSITIVITY__SUBTHRESHOLD_DIAGNOSTIC_ONLY' if execution_valid else
 'FAIL_CHANNEL2_CUT_KINEMATIC_H1_SENSITIVITY_EXECUTION')
result={
 'iteration':ITERATION,'model_readiness_percent':24,'candidate_residual':False,'scientific_gate_pass':execution_valid,
 'classification':classification,'authority_scope':'DIAGNOSTIC_ONLY__NO_PHYSICAL_COORDINATE_PROMOTION',
 'target':{'double_double_global_index':TARGET_INDEX,'class_id':TARGET_CLASS,'q_squared':q2},
 'row_identity':{'singleton_leg':'s','pair_legs':['a','b'],'spec_index':row['spec_index'],'extra_site':'N_L','V2_leg':'b','extra_local_leg':'a'},
 'mass_radius':MASS_R,'mass_corners':'all four signed corners','z_samples':list(Z_SAMPLES),'phi_fractions':list(PHI_FRACS),
 'h1_base':H1_BASE,'h1_scales':list(H1_SCALES),'radial_hs':list(RADIAL_HS),
 'max_cut_kinematic_h1_scaled_delta':max_delta,'max_radial_richardson_scaled_error':max_raderr,
 'physical_reference_tolerance_only_not_acceptance':PHYSICAL_REFERENCE_TOL,'material_relative_to_2e-5_reference':material,
 'records':records,
 'interpretation':('If SUBTHRESHOLD, the inherited h1 stencil is directly shown to be subdominant even on representative physical fixed-mass cut kinematics, strengthening the case that complete arithmetic precision/cancellation rather than gross parent truncation is the immediate fallback target. If MATERIAL, the Iteration-424 port needs an explicit h1 truncation certificate in addition to more digits.'),
 'guardrails':['DIAGNOSTIC_ONLY','REPRESENTATIVE_FIXED_MASS_CUT_SAMPLES_NOT_FULL_D_S_AUTHORITY','NO_PHYSICAL_DS_VALUE','NO_THRESHOLD_WEAKENING','NO_MASS_STEP_CHANGE','NO_RADIAL_NODE_CHANGE','NO_NUMERATOR_CHANGE','NO_ROUTING_CHANGE','NO_ZERO_FILL','NO_ANSATZ003','NO_FISHER_RESOURCES']
}
print(json.dumps(result,indent=2,sort_keys=True))
if not execution_valid: raise SystemExit(2)
