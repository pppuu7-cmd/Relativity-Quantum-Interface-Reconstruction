#!/usr/bin/env python3
"""Iteration 449: remaining frozen-z support slab A for index-2 class-3 MP sample generation.

Prospectively frozen before execution:
- double-double index 2 / class 3 / q^2=-1;
- same already-valid mass corner u=v=+5e-6;
- remaining frozen z slab A = {-0.71,-0.43,-0.19};
- all 16 frozen phi nodes;
- full inherited radial Richardson nodes {2e-3,1e-3,5e-4}, both signs;
- direct 80/120-digit parent recomputation; no binary-parent recast;
- same 1e-30 cross-precision and inherited radial thresholds.

This is non-promoting coverage only. PASS does not close the mass corner until
slab B {0.27,0.43,0.69} is also raw-valid under the same contract.
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
Z_SAMPLES=(-0.71,-0.43,-0.19)
NPHI=16
RADIAL_HS=(2.0e-3,1.0e-3,5.0e-4)

# Fail-closed binding to the two raw-consumed numerical prerequisites already
# present in repository results. The selected-slab result itself is not used as
# a numerical input, so no result is silently zero-filled or interpolated.
for fn in ['post447_class3_actual_cut_parent_mp_pilot.json','post447_iteration407_spectral_algebra_precision_stage.json']:
    o=json.loads((R/fn).read_text())
    if o.get('scientific_gate_pass') is not True:
        raise SystemExit(('prerequisite_not_passed',fn,o.get('classification')))

# Reuse the same direct multiprecision parent implementation as the raw-valid
# previous stages, stopping before its pilot sampling loop.
p=ROOT/'post447_class3_actual_cut_parent_mp_pilot.py'
s=p.read_text(); marker='samples=[]\nfor su in (-1.0,1.0):'
if s.count(marker)!=1: raise SystemExit(('pilot_boundary_drift',s.count(marker)))
C={'__name__':'iter449_parent','__file__':str(p)}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(s.split(marker,1)[0],str(p),'exec'),C,C)
kin=C['kin']; unit_from=C['unit_from']; stripped_mp=C['stripped_mp']; a=C['a']; q=C['q']

# Bind the same inherited radial tolerance from the retained physical path.
p379=ROOT/'iteration379_tru1sq_double_double_one_channel_pilot.py'
s379=p379.read_text(); boundary='start=time.perf_counter()'
if s379.count(boundary)!=1: raise SystemExit(('iter379_boundary_drift',s379.count(boundary)))
N={'__name__':'iter449_radial_binding','__file__':str(p379)}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(s379.split(boundary,1)[0],str(p379),'exec'),N,N)
RADIAL_LIMIT=float(N['RADIAL_EXTRAP_TOL'])


def mpc_from_pair(pair):
    return mp.mpc(mp.mpf(pair[0]),mp.mpf(pair[1]))


def scaled(x,y):
    return abs(x-y)/max(mp.mpf(1),abs(x),abs(y))


def radial_limit_at(dps,z,phi):
    alpha,rho,_,_=kin(MASS_U,MASS_V)
    vec=rho*unit_from(z,phi)
    mids=[]
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
                vals[dps]=(mp.nstr(mp.re(val),dps),mp.nstr(mp.im(val),dps))
                rads[dps]=mp.nstr(er,40)
        with mp.workdps(150):
            z80=mpc_from_pair(vals[80]); z120=mpc_from_pair(vals[120]); cr=scaled(z80,z120)
            er80=mp.mpf(rads[80]); er120=mp.mpf(rads[120])
            mx=max(mx,cr); maxrad=max(maxrad,er80,er120)
            ok=bool(mp.isfinite(z120.real) and mp.isfinite(z120.imag) and mp.isfinite(er120))
            finite=finite and ok
            rows.append({'z':z,'phi_index':m,'phi_fraction':m/NPHI,
                         'mp80_re':vals[80][0],'mp80_im':vals[80][1],
                         'mp120_re':vals[120][0],'mp120_im':vals[120][1],
                         'scaled_mp80_vs_mp120':mp.nstr(cr,30),
                         'radial_error_mp80':rads[80],'radial_error_mp120':rads[120],
                         'finite':ok})

expected=len(Z_SAMPLES)*NPHI
passed=bool(len(rows)==expected and finite and mx<=MP_LIMIT and maxrad<=mp.mpf(repr(RADIAL_LIMIT)))
result={
 'stage':'ITERATION449_CLASS3_REMAINING_Z_SLAB_A_MP',
 'classification':('PASS_ITER449_REMAINING_Z_SLAB_A_MP80_MP120__NON_PROMOTING' if passed else 'BLOCKED_ITER449_REMAINING_Z_SLAB_A_MP__NON_PROMOTING'),
 'scientific_gate_pass':passed,'promotes_physical_coordinate':False,
 'MODEL_READINESS':'24%','readiness_change_pp':0,
 'target':{'double_double_index':2,'class_id':3,'q_squared':-1.0},
 'scope':'ONE_MASS_CORNER__REMAINING_Z_SLAB_A__ALL_16_PHI__FULL_RADIAL_RICHARDSON__DIRECT_PARENT_MP',
 'frozen':{'u':MASS_U,'v':MASS_V,'z_samples':list(Z_SAMPLES),'phi_nodes':NPHI,
           'radial_hs':list(RADIAL_HS),'precision_digits':[80,120]},
 'thresholds':{'scaled_mp80_vs_mp120_max':'1e-30','radial_richardson_scaled_max':RADIAL_LIMIT,
               'required_sample_count':expected,'all_finite':True},
 'observed':{'scaled_mp80_vs_mp120_max':mp.nstr(mx,30),
             'max_radial_richardson_scaled_error':mp.nstr(maxrad,30),
             'sample_count':len(rows),'all_finite':finite,
             'runtime_seconds':time.perf_counter()-start},
 'rows':rows,
 'next_gate_if_pass':'run remaining frozen-z slab B {0.27,0.43,0.69} at the same mass corner with identical phi/radial/precision contract; only both slabs plus the raw-valid selected slab close z support at this mass corner',
 'next_gate_if_blocked':'localize first failing z/phi/radial sample without changing mass point, radial nodes, phi grid, routing, dynamics or thresholds',
 'guardrails':['STAGED_COVERAGE_ONLY','NO_BINARY_PARENT_RECAST','NO_PHYSICAL_DS_PROMOTION',
               'NO_MASS_NODE_CHANGE','NO_RADIAL_NODE_CHANGE','NO_PHI_ESCALATION',
               'NO_THRESHOLD_WEAKENING','NO_ZERO_FILL','NO_ANSATZ003','NO_FISHER_RESOURCES']
}
print(json.dumps(result,indent=2,sort_keys=True))
if not passed: raise SystemExit(2)
