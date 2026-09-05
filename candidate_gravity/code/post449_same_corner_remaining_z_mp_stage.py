#!/usr/bin/env python3
"""Post-Iteration-449 same-corner remaining-z MP stage.

This stage is deliberately unnumbered until raw consumption. It extends the
raw-valid selected slab only to the two missing frozen Iteration-407 training-z
points at the already-tested mass corner. No physical promotion is allowed.
"""
from __future__ import annotations
import contextlib, io, json, time
from pathlib import Path
import mpmath as mp

ROOT=Path(__file__).resolve().parent
R=ROOT.parent/'results'

# Bind Iteration 449 fail-closed.
i449=json.loads((R/'iteration449_selected_slab_raw_consumption_and_coverage.json').read_text())
if i449.get('scientific_gate_pass') is not True:
    raise SystemExit(('iteration449_not_passed',i449.get('classification')))

# Reuse the exact already-raw-validated selected-slab implementation up to the
# sampling loop; this preserves parent dynamics, routing, radial nodes, phi
# nodes and precision conventions without copying/reinterpreting them.
p=ROOT/'post447_class3_phi_sample_mp_stage.py'
s=p.read_text(); boundary='start=time.perf_counter(); rows=[];'
if s.count(boundary)!=1:
    raise SystemExit(('source_boundary_drift',s.count(boundary)))
C={'__name__':'post449_same_corner_remaining_z','__file__':str(p)}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(s.split(boundary,1)[0],str(p),'exec'),C,C)

MP_LEVELS=C['MP_LEVELS']; MP_LIMIT=C['MP_LIMIT']; NPHI=C['NPHI']; RADIAL_HS=C['RADIAL_HS']
RADIAL_LIMIT=C['RADIAL_LIMIT']; radial_limit_at=C['radial_limit_at']; mpc_from_pair=C['mpc_from_pair']; scaled=C['scaled']
MASS_U=C['MASS_U']; MASS_V=C['MASS_V']
Z_SAMPLES=(-0.43,0.43)

start=time.perf_counter(); rows=[]; mx=mp.mpf('0'); maxrad=mp.mpf('0'); finite=True
for z in Z_SAMPLES:
    for m in range(NPHI):
        phi=2.0*mp.pi*m/NPHI
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
 'stage':'POST449_SAME_CORNER_REMAINING_Z_MP_STAGE__UNNUMBERED_COLLISION_SAFE',
 'classification':('PASS_SAME_CORNER_FULL_Z_SUPPORT_MP80_MP120__NON_PROMOTING' if passed else 'BLOCKED_SAME_CORNER_REMAINING_Z_MP__NON_PROMOTING'),
 'scientific_gate_pass':passed,'promotes_physical_coordinate':False,'MODEL_READINESS':'24%','readiness_change_pp':0,
 'target':{'double_double_index':2,'class_id':3,'q_squared':-1.0},
 'scope':'ONE_MASS_CORNER__REMAINING_TWO_Z__ALL_16_PHI__FULL_RADIAL_RICHARDSON__DIRECT_PARENT_MP',
 'frozen':{'u':MASS_U,'v':MASS_V,'z_samples':list(Z_SAMPLES),'phi_nodes':NPHI,'radial_hs':list(RADIAL_HS),'precision_digits':list(MP_LEVELS)},
 'thresholds':{'scaled_mp80_vs_mp120_max':'1e-30','radial_richardson_scaled_max':RADIAL_LIMIT,'required_sample_count':expected,'all_finite':True},
 'observed':{'scaled_mp80_vs_mp120_max':mp.nstr(mx,30),'max_radial_richardson_scaled_error':mp.nstr(maxrad,30),'sample_count':len(rows),'all_finite':finite,'runtime_seconds':time.perf_counter()-start},
 'rows':rows,
 'next_gate_if_pass':'combine with raw-consumed selected slab to certify all five frozen z values at u=v=+5e-6 only, then extend mass-node coverage without changing conventions',
 'next_gate_if_blocked':'localize first failing z/phi/radial sample at same mass point and unchanged conventions',
 'guardrails':['SAME_MASS_CORNER_ONLY','NO_PHYSICAL_DS_PROMOTION','NO_MASS_NODE_CHANGE','NO_RADIAL_NODE_CHANGE','NO_PHI_ESCALATION','NO_THRESHOLD_WEAKENING','NO_ZERO_FILL','NO_ANSATZ003','NO_FISHER_RESOURCES']
}
print(json.dumps(result,indent=2,sort_keys=True))
if not passed: raise SystemExit(2)
