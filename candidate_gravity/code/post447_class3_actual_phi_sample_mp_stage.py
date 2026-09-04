#!/usr/bin/env python3
"""RQIR collision-safe post-447 actual-cut phi/sample-generation MP stage.

Purpose: extend the raw-valid actual-cut parent MP pilot across the unchanged
Iteration-407-style z/phi sample geometry for unresolved double-double index 2,
without claiming physical D_s closure.

Prospectively frozen scope:
- target index 2 / class 3 / q^2=-1;
- real Iteration-368 timelike M, seed 319;
- one frozen mass corner u=v=+5e-6;
- TRAIN_Z = [-0.86,-0.43,0,0.43,0.86];
- HELDOUT_Z = [-0.71,-0.19,0.27,0.69];
- unchanged NPHI=16, phi=2*pi*m/16;
- finest already-frozen radial pair h_r=5e-4, both signs;
- unchanged parent A1 h1=1e-4 and N1/Q1 h=3e-5;
- direct parent recomputation at 80 and 120 decimal digits;
- cross-precision threshold 1e-30.

This gate certifies only this frozen finest-radial-pair phi/sample-generation
slice if it passes. It does NOT close the full radial Richardson representation,
all mass nodes, Iteration424, or physical D_s.
"""
from __future__ import annotations
import contextlib, io, json, math, time
from pathlib import Path
import numpy as np
import mpmath as mp

ROOT=Path(__file__).resolve().parent
MP_LEVELS=(80,120)
MP_LIMIT=mp.mpf('1e-30')
PHYSICAL_REFERENCE=mp.mpf('2e-5')
TRAIN_Z=(-0.86,-0.43,0.0,0.43,0.86)
HELDOUT_Z=(-0.71,-0.19,0.27,0.69)
NPHI=16
MASS_U=5.0e-6
MASS_V=5.0e-6
RADIAL_H=5.0e-4

# Reuse only the proven generalized direct-MP machinery from the collision-safe
# pilot. Stop before its 8-point execution loop.
pilot=ROOT/'post447_class3_actual_cut_parent_mp_pilot.py'
t=pilot.read_text(); marker='samples=[]'
if t.count(marker)!=1: raise SystemExit(('pilot_boundary_drift',t.count(marker)))
P={'__name__':'post447_phi_parent_prefix','__file__':str(pilot)}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(t.split(marker,1)[0],str(pilot),'exec'),P,P)

C=P['C']; kin=P['kin']; unit_from=P['unit_from']; stripped_mp=P['stripped_mp']; stripped_h1=P['stripped_h1']
a=np.asarray(P['a'],float); q=np.asarray(P['q'],float)
if int(C['ch']['class_id'])!=3 or abs(float(C['q2'])+1.0)>1e-12:
    raise SystemExit('target_identity_drift')

# Fail-closed binding to the two newly raw-consumed PASSes.
R=ROOT.parent/'results'
for fn in ['post447_class3_actual_cut_parent_mp_pilot.json','post447_iteration407_spectral_algebra_precision_stage.json']:
    o=json.loads((R/fn).read_text())
    if o.get('scientific_gate_pass') is not True:
        raise SystemExit(('prerequisite_not_passed',fn))


def scaled(a,b):
    return abs(a-b)/max(mp.mpf(1),abs(a),abs(b))


def as_mpc(pair):
    return mp.mpc(mp.mpf(pair[0]),mp.mpf(pair[1]))

alpha,rho,_,_=kin(MASS_U,MASS_V)
zs=list(TRAIN_Z)+list(HELDOUT_Z)
samples=[]
for z in zs:
    for m in range(NPHI):
        phi=2.0*math.pi*m/NPHI
        vec=rho*unit_from(z,phi)
        for radial_sign in (-1.0,1.0):
            p=-a+alpha*q+(1.0+radial_sign*RADIAL_H)*vec
            samples.append({'z':float(z),'m':m,'phi':phi,'radial_sign':radial_sign,'p':np.asarray(p,float)})

start=time.perf_counter(); rows=[]
max_raw_cross=mp.mpf('0'); max_raw_binary=mp.mpf('0'); all_finite=True
# Store values by (z,m,sign,dps) for midpoint and phi-mean assembly.
vals={}; bvals={}
for i,s in enumerate(samples):
    refs={}
    for dps in MP_LEVELS:
        refs[dps]=stripped_mp(s['p'],dps)
    with mp.workdps(150):
        z80=as_mpc(refs[80]); z120=as_mpc(refs[120])
        cross=scaled(z80,z120); max_raw_cross=max(max_raw_cross,cross)
        zb=complex(stripped_h1(s['p'],1e-4)); zbm=mp.mpc(repr(float(zb.real)),repr(float(zb.imag)))
        bdiag=scaled(zbm,z120); max_raw_binary=max(max_raw_binary,bdiag)
        finite=bool(mp.isfinite(z120.real) and mp.isfinite(z120.imag) and np.isfinite(zb.real) and np.isfinite(zb.imag))
        all_finite=all_finite and finite
        key=(s['z'],s['m'],int(s['radial_sign']))
        vals[(key,80)]=z80; vals[(key,120)]=z120; bvals[key]=zbm
        rows.append({'sample_index':i,'z':s['z'],'phi_index':s['m'],'phi':s['phi'],'radial_sign':s['radial_sign'],
                     'mp80_re':refs[80][0],'mp80_im':refs[80][1],'mp120_re':refs[120][0],'mp120_im':refs[120][1],
                     'scaled_mp80_vs_mp120':mp.nstr(cross,30),'scaled_binary64_vs_mp120_diagnostic':mp.nstr(bdiag,30),'finite':finite})

mid_rows=[]; mean_rows=[]
max_mid_cross=mp.mpf('0'); max_mean_cross=mp.mpf('0')
max_mid_binary=mp.mpf('0'); max_mean_binary=mp.mpf('0')
for z in zs:
    mpmeans={80:[],120:[]}; bmeans=[]
    for m in range(NPHI):
        with mp.workdps(150):
            mids={}
            for dps in MP_LEVELS:
                minus=vals[((float(z),m,-1),dps)]; plus=vals[((float(z),m,1),dps)]
                mids[dps]=(minus+plus)/2
                mpmeans[dps].append(mids[dps])
            bmid=(bvals[(float(z),m,-1)]+bvals[(float(z),m,1)])/2; bmeans.append(bmid)
            cr=scaled(mids[80],mids[120]); bd=scaled(bmid,mids[120])
            max_mid_cross=max(max_mid_cross,cr); max_mid_binary=max(max_mid_binary,bd)
            mid_rows.append({'z':float(z),'phi_index':m,'scaled_midpoint_mp80_vs_mp120':mp.nstr(cr,30),
                             'scaled_midpoint_binary64_vs_mp120_diagnostic':mp.nstr(bd,30)})
    with mp.workdps(150):
        mean80=sum(mpmeans[80],mp.mpc(0))/NPHI; mean120=sum(mpmeans[120],mp.mpc(0))/NPHI; bmean=sum(bmeans,mp.mpc(0))/NPHI
        cr=scaled(mean80,mean120); bd=scaled(bmean,mean120)
        max_mean_cross=max(max_mean_cross,cr); max_mean_binary=max(max_mean_binary,bd)
        mean_rows.append({'z':float(z),'set':('train' if z in TRAIN_Z else 'heldout'),
                          'mp80_re':mp.nstr(mp.re(mean80),80),'mp80_im':mp.nstr(mp.im(mean80),80),
                          'mp120_re':mp.nstr(mp.re(mean120),120),'mp120_im':mp.nstr(mp.im(mean120),120),
                          'scaled_phi_mean_mp80_vs_mp120':mp.nstr(cr,30),
                          'scaled_phi_mean_binary64_vs_mp120_diagnostic':mp.nstr(bd,30)})

passed=bool(len(rows)==len(zs)*NPHI*2 and all_finite and max_raw_cross<=MP_LIMIT and max_mid_cross<=MP_LIMIT and max_mean_cross<=MP_LIMIT)
result={
 'stage':'POST447_CLASS3_ACTUAL_PHI_SAMPLE_MP_STAGE__UNNUMBERED_COLLISION_SAFE',
 'classification':('PASS_CLASS3_ACTUAL_PHI_SAMPLE_MP80_MP120_FINEST_RADIAL_PAIR__NON_PROMOTING' if passed else 'BLOCKED_CLASS3_ACTUAL_PHI_SAMPLE_MP_FINEST_RADIAL_PAIR__NON_PROMOTING'),
 'scientific_gate_pass':passed,'promotes_physical_coordinate':False,'MODEL_READINESS':'24%','work_completion_percent_if_pass':62,
 'target':{'double_double_index':2,'class_id':3,'q_squared':-1.0},
 'scope':'ONE_FROZEN_MASS_CORNER__ALL_ITER407_STYLE_TRAIN_HELDOUT_Z__NPHI16__FINEST_FROZEN_RADIAL_PAIR_ONLY',
 'frozen':{'u':MASS_U,'v':MASS_V,'training_z':list(TRAIN_Z),'heldout_z':list(HELDOUT_Z),'nphi':NPHI,
           'radial_h':RADIAL_H,'radial_signs':[-1,1],'precision_digits':[80,120],'A1_h1':1e-4,'N1_h':3e-5,
           'M_fixture':'Iteration368 TIMELIKE M seed319'},
 'thresholds':{'scaled_mp80_vs_mp120_max':'1e-30','required_raw_sample_count':len(zs)*NPHI*2,'all_finite':True,
               'binary64_vs_mp120_physical_reference_diagnostic_only':'2e-5'},
 'observed':{'raw_sample_count':len(rows),'all_finite':all_finite,
             'max_raw_sample_scaled_mp80_vs_mp120':mp.nstr(max_raw_cross,30),
             'max_radial_midpoint_scaled_mp80_vs_mp120':mp.nstr(max_mid_cross,30),
             'max_phi_mean_scaled_mp80_vs_mp120':mp.nstr(max_mean_cross,30),
             'max_raw_sample_scaled_binary64_vs_mp120_diagnostic':mp.nstr(max_raw_binary,30),
             'max_radial_midpoint_scaled_binary64_vs_mp120_diagnostic':mp.nstr(max_mid_binary,30),
             'max_phi_mean_scaled_binary64_vs_mp120_diagnostic':mp.nstr(max_mean_binary,30),
             'binary64_phi_mean_material_relative_to_2e-5_reference':bool(max_mean_binary>PHYSICAL_REFERENCE),
             'runtime_seconds':time.perf_counter()-start},
 'phi_mean_rows':mean_rows,'midpoint_diagnostics':mid_rows,'raw_rows':rows,
 'interpretation':'PASS certifies direct MP80/MP120 stability of the actual index-2 phi/sample-generation slice over all frozen Iteration-407-style training and heldout z nodes and unchanged NPHI16 at one frozen mass corner, using the finest already-frozen radial pair. It does not certify the full three-scale radial Richardson representation, all mass nodes, Iteration424, or D_s.',
 'next_gate_if_pass':'extend the same direct MP path through the complete frozen radial Richardson representation and then across the physical mass-node set before Iteration424 reevaluation',
 'next_gate_if_blocked':'localize the failing z/phi/radial sample and Q0/Q1/A1 contribution without changing nodes, h, routing, or thresholds',
 'guardrails':['NO_AUTHORITATIVE_ITERATION_NUMBER_REUSE','NO_BINARY_PARENT_RECAST_AS_MP','NO_PHYSICAL_DS_PROMOTION','NPHI16_UNCHANGED','NO_H_CHANGE','NO_MASS_NODE_CHANGE','NO_THRESHOLD_WEAKENING','NO_ANGULAR_GRID_ESCALATION','NO_ZERO_FILL','NO_ROUTING_NUMERATOR_SIGN_NORMALIZATION_CHANGE','NO_ANSATZ003','NO_FISHER_RESOURCES']
}
print(json.dumps(result,indent=2,sort_keys=True))
if not passed: raise SystemExit(2)
