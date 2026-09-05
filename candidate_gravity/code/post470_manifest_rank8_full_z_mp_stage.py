#!/usr/bin/env python3
from __future__ import annotations
import contextlib, io, json, math, time
from pathlib import Path
import mpmath as mp
ROOT=Path(__file__).resolve().parent; R=ROOT.parent/'results'
auth=json.loads((R/'iteration470_mass_node_raw_consumed.json').read_text())
if auth.get('authoritative_iteration')!=470 or auth.get('scientific_gate_pass') is not True: raise SystemExit('iteration470 prerequisite not passed')
coord=auth.get('next_gate',{})
if coord.get('distinct_rank')!=8 or abs(float(coord.get('u'))-5e-6)>1e-18 or abs(float(coord.get('v'))+1e-5)>1e-18: raise SystemExit(('rank8_manifest_prerequisite_drift',coord))
p=ROOT/'post447_class3_phi_sample_mp_stage.py'; s=p.read_text(); marker="start=time.perf_counter(); rows=[]; mx=mp.mpf('0'); maxrad=mp.mpf('0'); finite=True"
if s.count(marker)!=1: raise SystemExit(('post447_sampling_boundary_drift',s.count(marker)))
C={'__name__':'post470_rank8_parent','__file__':str(p)}
with contextlib.redirect_stdout(io.StringIO()): exec(compile(s.split(marker,1)[0],str(p),'exec'),C,C)
p379=ROOT/'iteration379_tru1sq_double_double_one_channel_pilot.py'; s379=p379.read_text(); boundary='start=time.perf_counter()'
if s379.count(boundary)!=1: raise SystemExit(('iter379_boundary_drift',s379.count(boundary)))
N={'__name__':'post470_mass_binding','__file__':str(p379)}
with contextlib.redirect_stdout(io.StringIO()): exec(compile(s379.split(boundary,1)[0],str(p379),'exec'),N,N)
BASE_H=float(N['BASE_H'])
if abs(BASE_H-5e-6)>1e-18: raise SystemExit(('base_h_drift',BASE_H))
MASS_U=+1.0*BASE_H; MASS_V=-2.0*BASE_H; Z_SAMPLES=(-0.86,-0.43,0.0,0.43,0.86)
MP_LEVELS=C['MP_LEVELS']; MP_LIMIT=C['MP_LIMIT']; NPHI=C['NPHI']; RADIAL_HS=C['RADIAL_HS']; RADIAL_LIMIT=C['RADIAL_LIMIT']; mpc_from_pair=C['mpc_from_pair']; scaled=C['scaled']; C['MASS_U']=MASS_U; C['MASS_V']=MASS_V; radial_limit_at=C['radial_limit_at']
start=time.perf_counter(); rows=[]; mx=mp.mpf('0'); maxrad=mp.mpf('0'); finite=True
for z in Z_SAMPLES:
  for m in range(NPHI):
    phi=2.0*math.pi*m/NPHI; vals={}; rads={}
    for dps in MP_LEVELS:
      with mp.workdps(dps): val,er=radial_limit_at(dps,z,phi); vals[dps]=(mp.nstr(mp.re(val),dps),mp.nstr(mp.im(val),dps)); rads[dps]=mp.nstr(er,40)
    with mp.workdps(150):
      z80=mpc_from_pair(vals[80]); z120=mpc_from_pair(vals[120]); cr=scaled(z80,z120); er80=mp.mpf(rads[80]); er120=mp.mpf(rads[120]); mx=max(mx,cr); maxrad=max(maxrad,er80,er120); ok=bool(mp.isfinite(z120.real) and mp.isfinite(z120.imag) and mp.isfinite(er120)); finite=finite and ok
      rows.append({'z':z,'phi_index':m,'phi_fraction':m/NPHI,'mp80_re':vals[80][0],'mp80_im':vals[80][1],'mp120_re':vals[120][0],'mp120_im':vals[120][1],'scaled_mp80_vs_mp120':mp.nstr(cr,30),'radial_error_mp80':rads[80],'radial_error_mp120':rads[120],'finite':ok})
expected=len(Z_SAMPLES)*NPHI; passed=bool(len(rows)==expected and finite and mx<=MP_LIMIT and maxrad<=mp.mpf(repr(RADIAL_LIMIT)))
result={'stage':'POST470_MANIFEST_RANK8_FULL_Z_MP_STAGE__UNNUMBERED_COLLISION_SAFE','classification':('PASS_NEXT_MASS_NODE_FULL_Z_MP80_MP120__NON_PROMOTING' if passed else 'BLOCKED_NEXT_MASS_NODE_FULL_Z_MP__NON_PROMOTING'),'scientific_gate_pass':passed,'promotes_physical_coordinate':False,'MODEL_READINESS':'24%','readiness_change_pp':0,'target':{'double_double_index':2,'class_id':3,'q_squared':-1.0},'frozen':{'u':MASS_U,'v':MASS_V,'source_order_rule':'Iteration455 distinct rank 8','source_occurrence_multiplicity':1,'base_h':BASE_H,'z_samples':list(Z_SAMPLES),'phi_nodes':NPHI,'radial_hs':list(RADIAL_HS),'precision_digits':[80,120]},'thresholds':{'scaled_mp80_vs_mp120_max':'1e-30','radial_richardson_scaled_max':RADIAL_LIMIT,'required_sample_count':expected,'all_finite':True},'observed':{'scaled_mp80_vs_mp120_max':mp.nstr(mx,30),'max_radial_richardson_scaled_error':mp.nstr(maxrad,30),'sample_count':len(rows),'all_finite':finite,'runtime_seconds':time.perf_counter()-start},'rows':rows,'next_gate_if_pass':'raw-consume non-promoting, then advance to manifest distinct rank 9 only','next_gate_if_blocked':'localize first failing z/phi/radial sample at u=+5e-6,v=-1e-5','guardrails':['ITERATION470_RAW_PASS_REQUIRED','ONE_MASS_COORDINATE_ONLY','ITERATION455_MANIFEST_ORDER','NO_BLIND_REMAINING_GRID_SWEEP','NO_PHYSICAL_DS_PROMOTION','NO_THRESHOLD_WEAKENING','NO_ZERO_FILL','NO_ANSATZ003','NO_FISHER_RESOURCES']}
print(json.dumps(result,indent=2,sort_keys=True))
if not passed: raise SystemExit(2)
