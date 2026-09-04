#!/usr/bin/env python3
"""RQIR post-447 collision-safe class-3 phi/sample-generation MP stage.

Purpose: extend the raw-valid actual-cut parent MP pilot into the first direct
continuous-precision azimuth-sample layer used by the active index-2 fixed-mass
F(u,v) architecture, without claiming physical D_s authority.

Prospectively frozen before execution:
- double-double index 2 / class 3 / q^2=-1;
- one already-valid physical mass corner u=v=+5e-6;
- representative polynomial-support z = {-0.86, 0.0, +0.86};
- all 16 frozen Iteration-407 azimuth nodes;
- full inherited radial Richardson nodes {2e-3,1e-3,5e-4}, both signs;
- direct 80/120-digit recomputation of the traced stripped numerator at every
  radial momentum (no binary parent recast);
- cross-precision limit 1e-30 and inherited radial error limit from the active
  fixed-mass path.

This is a staged coverage gate: PASS certifies the selected full-phi/radial
sample slab only. It does not certify all z values or all 32 mass nodes.
"""
from __future__ import annotations
import contextlib, io, json, math, time
from pathlib import Path
import mpmath as mp

ROOT=Path(__file__).resolve().parent
R=ROOT.parent/'results'
MP_LEVELS=(80,120)
MP_LIMIT=mp.mpf('1e-30')
MASS_U=5.0e-6
MASS_V=5.0e-6
Z_SAMPLES=(-0.86,0.0,0.86)
NPHI=16
RADIAL_HS=(2.0e-3,1.0e-3,5.0e-4)

# Bind both independently raw-consumed prerequisites fail-closed.
for fn in ['post447_class3_actual_cut_parent_mp_pilot.json','post447_iteration407_spectral_algebra_precision_stage.json']:
    o=json.loads((R/fn).read_text())
    if o.get('scientific_gate_pass') is not True:
        raise SystemExit(('prerequisite_not_passed',fn,o.get('classification')))

# Reuse the actual-cut direct-multiprecision implementation, but stop before its
# pilot sampling loop. This preserves the exact class-3 routing and parent MP
# implementation already raw-validated on physical near-cut momenta.
p=ROOT/'post447_class3_actual_cut_parent_mp_pilot.py'
s=p.read_text(); marker='samples=[]\nfor su in (-1.0,1.0):'
if s.count(marker)!=1: raise SystemExit(('pilot_boundary_drift',s.count(marker)))
C={'__name__':'post447_phi_sample_parent','__file__':str(p)}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(s.split(marker,1)[0],str(p),'exec'),C,C)
kin=C['kin']; unit_from=C['unit_from']; stripped_mp=C['stripped_mp']; a=C['a']; q=C['q']

# Inherit the active fixed-mass radial acceptance rather than inventing one.
p431=ROOT/'iteration431_channel2_cut_kinematic_h1_sensitivity.py'
s431=p431.read_text(); key="RADIAL_HS=(2.0e-3,1.0e-3,5.0e-4)"
if s431.count(key)!=1: raise SystemExit(('radial_binding_drift',s431.count(key)))
# The physical path uses the existing global radial tolerance; fetch it from 379.
p379=ROOT/'iteration379_tru1sq_double_double_one_channel_pilot.py'
s379=p379.read_text(); boundary='start=time.perf_counter()'
if s379.count(boundary)!=1: raise SystemExit(('iter379_boundary_drift',s379.count(boundary)))
N={'__name__':'post447_phi_radial_binding','__file__':str(p379)}
with contextlib.redirect_stdout(io.StringIO()): exec(compile(s379.split(boundary,1)[0],str(p379),'exec'),N,N)
RADIAL_LIMIT=float(N['RADIAL_EXTRAP_TOL'])


def mpc_from_pair(pair):
    return mp.mpc(mp.mpf(pair[0]),mp.mpf(pair[1]))


def scaled(a,b):
    return abs(a-b)/max(mp.mpf(1),abs(a),abs(b))


def radial_limit_at(dps,z,phi):
    alpha,rho,_,_=kin(MASS_U,MASS_V); vec=rho*unit_from(z,phi); mids=[]
    for h in RADIAL_HS:
        vals=[]
        for sign in (+1.0,-1.0):
            pvec=-a+alpha*q+(1.0+sign*h)*vec
            vals.append(mpc_from_pair(stripped_mp(pvec,dps)))
        mids.append((vals[0]+vals[1])/2)
    coarse=(4*mids[1]-mids[0])/3
    fine=(4*mids[2]-mids[1])/3
    err=abs(fine-coarse)/max(mp.mpf(1),abs(fine),abs(coarse),*(abs(x) for x in mids))
    return fine,err

start=time.perf_counter(); rows=[]; mx=mp.mpf('0'); maxrad=mp.mpf('0'); finite=True
for z in Z_SAMPLES:
    for m in range(NPHI):
        phi=2.0*math.pi*m/NPHI
        vals={}; rads={}
        for dps in MP_LEVELS:
            with mp.workdps(dps):
                val,er=radial_limit_at(dps,z,phi)
                vals[dps]=(mp.nstr(mp.re(val),dps),mp.nstr(mp.im(val),dps)); rads[dps]=mp.nstr(er,40)
        with mp.workdps(150):
            z80=mpc_from_pair(vals[80]); z120=mpc_from_pair(vals[120]); cr=scaled(z80,z120)
            er80=mp.mpf(rads[80]); er120=mp.mpf(rads[120]); mx=max(mx,cr); maxrad=max(maxrad,er80,er120)
            ok=bool(mp.isfinite(z120.real) and mp.isfinite(z120.imag) and mp.isfinite(er120)); finite=finite and ok
            rows.append({'z':z,'phi_index':m,'phi_fraction':m/NPHI,
                         'mp80_re':vals[80][0],'mp80_im':vals[80][1],
                         'mp120_re':vals[120][0],'mp120_im':vals[120][1],
                         'scaled_mp80_vs_mp120':mp.nstr(cr,30),
                         'radial_error_mp80':rads[80],'radial_error_mp120':rads[120],'finite':ok})

expected=len(Z_SAMPLES)*NPHI
passed=bool(len(rows)==expected and finite and mx<=MP_LIMIT and maxrad<=mp.mpf(repr(RADIAL_LIMIT)))
result={
 'stage':'POST447_CLASS3_PHI_SAMPLE_MP_STAGE__UNNUMBERED_COLLISION_SAFE',
 'classification':('PASS_CLASS3_PHI_SAMPLE_MP80_MP120_SELECTED_SLAB__NON_PROMOTING' if passed else 'BLOCKED_CLASS3_PHI_SAMPLE_MP_SELECTED_SLAB__NON_PROMOTING'),
 'scientific_gate_pass':passed,'promotes_physical_coordinate':False,'MODEL_READINESS':'24%','readiness_change_pp':0,
 'target':{'double_double_index':2,'class_id':3,'q_squared':-1.0},
 'scope':'ONE_MASS_CORNER__THREE_POLYNOMIAL_SUPPORT_Z__ALL_16_PHI__FULL_RADIAL_RICHARDSON__DIRECT_PARENT_MP',
 'frozen':{'u':MASS_U,'v':MASS_V,'z_samples':list(Z_SAMPLES),'phi_nodes':NPHI,'radial_hs':list(RADIAL_HS),'precision_digits':[80,120]},
 'thresholds':{'scaled_mp80_vs_mp120_max':'1e-30','radial_richardson_scaled_max':RADIAL_LIMIT,'required_sample_count':expected,'all_finite':True},
 'observed':{'scaled_mp80_vs_mp120_max':mp.nstr(mx,30),'max_radial_richardson_scaled_error':mp.nstr(maxrad,30),'sample_count':len(rows),'all_finite':finite,'runtime_seconds':time.perf_counter()-start},
 'rows':rows,
 'next_gate_if_pass':'extend continuous 80/120 direct-parent sample generation to the remaining frozen z support and mass-node coverage required by full index-2 F(u,v), preserving the same 16 phi and radial Richardson nodes',
 'next_gate_if_blocked':'localize failing z/phi/radial sample at the same mass node and unchanged parent/radial conventions',
 'guardrails':['STAGED_COVERAGE_ONLY','NO_BINARY_PARENT_RECAST','NO_PHYSICAL_DS_PROMOTION','NO_MASS_NODE_CHANGE','NO_RADIAL_NODE_CHANGE','NO_PHI_ESCALATION','NO_THRESHOLD_WEAKENING','NO_ZERO_FILL','NO_ANSATZ003','NO_FISHER_RESOURCES']
}
print(json.dumps(result,indent=2,sort_keys=True))
if not passed: raise SystemExit(2)
