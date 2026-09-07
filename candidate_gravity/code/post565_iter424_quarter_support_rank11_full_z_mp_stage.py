#!/usr/bin/env python3
"""Post-Iteration-565 frozen Iteration-424 quarter-support rank11 stage."""
from __future__ import annotations
import contextlib, io, json, math, time
from pathlib import Path
import mpmath as mp
ROOT=Path(__file__).resolve().parent; R=ROOT.parent/'results'
auth=json.loads((R/'iteration565_iter424_quarter_rank10_raw_consumption.json').read_text())
if (auth.get('iteration')!=565 or auth.get('classification')!='PASS_RAW_CONSUMED_ITER424_QUARTER_SUPPORT_RANK10_MP80_MP120__NON_PROMOTING' or auth.get('conclusions',{}).get('rank10_raw_valid_pass') is not True or auth.get('conclusions',{}).get('rank11_authorized_by_iteration532_order') is not True or auth.get('next_rank',{}).get('quarter_source_rank')!=11 or abs(float(auth.get('next_rank',{}).get('u'))-2.5e-6)>1e-18 or abs(float(auth.get('next_rank',{}).get('v'))+1.25e-6)>1e-18): raise SystemExit(('iteration565_rank10_raw_consumption_prerequisite_not_passed',auth))
contract=(ROOT/'iteration424_channel2_high_precision_fallback_contract.py').read_text()
for tok in ('5.0e-6','2.5e-6','1.25e-6','PRECISION_LEVELS_DIGITS = [80, 120]'):
    if tok not in contract: raise SystemExit(('iteration424_contract_drift',tok))
p=ROOT/'post447_class3_phi_sample_mp_stage.py'; s=p.read_text(); marker="start=time.perf_counter(); rows=[]; mx=mp.mpf('0'); maxrad=mp.mpf('0'); finite=True"
if s.count(marker)!=1: raise SystemExit(('post447_sampling_boundary_drift',s.count(marker)))
C={'__name__':'post565_iter424_quarter_rank11_parent','__file__':str(p)}
with contextlib.redirect_stdout(io.StringIO()): exec(compile(s.split(marker,1)[0],str(p),'exec'),C,C)
H=1.25e-6; NODES=(-2*H,-H,H,2*H); allq=[(u,v) for u in NODES for v in NODES]; covered={(u,v) for u in (-2*H,2*H) for v in (-2*H,2*H)}; untested=[q for q in allq if q not in covered]
expected_order=[(-2.5e-6,-1.25e-6),(-2.5e-6,1.25e-6),(-1.25e-6,-2.5e-6),(-1.25e-6,-1.25e-6),(-1.25e-6,1.25e-6),(-1.25e-6,2.5e-6),(1.25e-6,-2.5e-6),(1.25e-6,-1.25e-6),(1.25e-6,1.25e-6),(1.25e-6,2.5e-6),(2.5e-6,-1.25e-6),(2.5e-6,1.25e-6)]
if len(untested)!=12 or any(abs(a-c)>1e-18 or abs(b-d)>1e-18 for (a,b),(c,d) in zip(untested,expected_order)): raise SystemExit(('quarter_manifest_or_order_drift',untested))
MASS_U,MASS_V=untested[10]
if abs(MASS_U-2.5e-6)>1e-18 or abs(MASS_V+1.25e-6)>1e-18: raise SystemExit(('rank11_coordinate_drift',MASS_U,MASS_V))
Z_SAMPLES=(-0.86,-0.43,0.0,0.43,0.86); MP_LEVELS=C['MP_LEVELS']; MP_LIMIT=C['MP_LIMIT']; NPHI=C['NPHI']; RADIAL_HS=C['RADIAL_HS']; RADIAL_LIMIT=C['RADIAL_LIMIT']; mpc_from_pair=C['mpc_from_pair']; scaled=C['scaled']
if list(MP_LEVELS)!=[80,120]: raise SystemExit(('precision_levels_drift',MP_LEVELS))
C['MASS_U']=MASS_U; C['MASS_V']=MASS_V; radial_limit_at=C['radial_limit_at']
start=time.perf_counter(); rows=[]; mx=mp.mpf('0'); maxrad=mp.mpf('0'); finite=True
for z in Z_SAMPLES:
  for m in range(NPHI):
    phi=2.0*math.pi*m/NPHI; vals={}; rads={}
    for dps in MP_LEVELS:
      with mp.workdps(dps): val,er=radial_limit_at(dps,z,phi); vals[dps]=(mp.nstr(mp.re(val),dps),mp.nstr(mp.im(val),dps)); rads[dps]=mp.nstr(er,40)
    with mp.workdps(150):
      z80=mpc_from_pair(vals[80]); z120=mpc_from_pair(vals[120]); cr=scaled(z80,z120); er80=mp.mpf(rads[80]); er120=mp.mpf(rads[120]); mx=max(mx,cr); maxrad=max(maxrad,er80,er120); ok=bool(mp.isfinite(z120.real) and mp.isfinite(z120.imag) and mp.isfinite(er120)); finite=finite and ok; rows.append({'z':z,'phi_index':m,'phi_fraction':m/NPHI,'mp80_re':vals[80][0],'mp80_im':vals[80][1],'mp120_re':vals[120][0],'mp120_im':vals[120][1],'scaled_mp80_vs_mp120':mp.nstr(cr,30),'radial_error_mp80':rads[80],'radial_error_mp120':rads[120],'finite':ok})
expected=len(Z_SAMPLES)*NPHI; passed=bool(len(rows)==expected and finite and mx<=MP_LIMIT and maxrad<=mp.mpf(repr(RADIAL_LIMIT)))
result={'stage':'POST565_ITER424_QUARTER_SUPPORT_RANK11_FULL_Z_MP__UNNUMBERED_COLLISION_SAFE','classification':('PASS_ITER424_QUARTER_SUPPORT_RANK11_MP80_MP120__NON_PROMOTING' if passed else 'BLOCKED_ITER424_QUARTER_SUPPORT_RANK11_MP__NON_PROMOTING'),'scientific_gate_pass':passed,'promotes_physical_coordinate':False,'MODEL_READINESS':'24%','readiness_change_pp':0,'target':{'double_double_index':2,'class_id':3,'q_squared':-1.0},'frozen':{'iteration424_mass_step':H,'u':MASS_U,'v':MASS_V,'quarter_source_rank':11,'quarter_new_coordinate_count':12,'source_order':'Iteration532 frozen quarter central4 u-major/v-major after exact HALF-overlap removal','z_samples':list(Z_SAMPLES),'phi_nodes':NPHI,'radial_hs':list(RADIAL_HS),'precision_digits':[80,120]},'thresholds':{'scaled_mp80_vs_mp120_max':'1e-30','radial_richardson_scaled_max':RADIAL_LIMIT,'required_sample_count':expected,'all_finite':True},'observed':{'scaled_mp80_vs_mp120_max':mp.nstr(mx,30),'max_radial_richardson_scaled_error':mp.nstr(maxrad,30),'sample_count':len(rows),'all_finite':finite,'runtime_seconds':time.perf_counter()-start},'rows':rows,'next_gate_if_pass':'raw-consume non-promoting, then advance only to Iteration532 quarter source rank12 (+2.5e-6,+1.25e-6)','next_gate_if_blocked':'localize first failing z/phi/radial sample at quarter rank11 without changing conventions','guardrails':['ITERATION565_RANK10_RAW_CONSUMPTION_PASS_REQUIRED','ITERATION532_SUCCESSOR_ORDER','ITERATION424_FROZEN_MASS_STEPS','ONE_NEW_QUARTER_COORDINATE_ONLY','DIRECT_PARENT_MP80_MP120','NO_PHYSICAL_DS_PROMOTION','NO_THRESHOLD_WEAKENING','NO_ZERO_FILL','NO_UV_SYMMETRY_SUBSTITUTION','NO_ANSATZ003','NO_FISHER_RESOURCES']}
print(json.dumps(result,indent=2,sort_keys=True))
if not passed: raise SystemExit(2)
