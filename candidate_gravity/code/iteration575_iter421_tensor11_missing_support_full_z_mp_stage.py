#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 575 tensor11 missing-support MP stage.

Computes exactly one rank from the prospectively frozen 36-node support deficit
needed to reproduce the original Iter421 tensor degree-(1,1) residual at
MP80/MP120.  The complete missing set was frozen before any rank result, so a
matrix execution over all ranks is non-result-dependent.

Scientific arithmetic is inherited from the already validated class-3 direct
multiprecision full-z sample path.  No tensor11 node/radius, parent dynamics,
routing, numerator, sign, normalization, z/phi/radial support, precision or
acceptance threshold is changed.  A per-rank PASS certifies support only and
never promotes physical index2.
"""
from __future__ import annotations
import argparse, contextlib, io, json, math, time
from pathlib import Path
import mpmath as mp

ROOT=Path(__file__).resolve().parent
R=ROOT.parent/'results'
CONTRACT=ROOT.parent/'contracts'/'iteration575_iter421_tensor11_exact_mp_support_manifest.json'

ap=argparse.ArgumentParser()
ap.add_argument('--rank',type=int,required=True)
args=ap.parse_args()
rank=int(args.rank)
if not 1 <= rank <= 36:
    raise SystemExit(('rank_out_of_range',rank))

# Bind the immediately preceding raw-consumed physical state fail-closed.
a574=json.loads((R/'iteration574_iter424_full_spectrum_raw_consumption.json').read_text())
if (a574.get('iteration')!=574 or
    a574.get('classification')!='PASS_RAW_CONSUMED_ITER424_FULL_SPECTRUM_NUMERICAL_CLAUSES__TENSOR11_OPERATIONAL_BLOCKED__NON_PROMOTING' or
    a574.get('status')!='PASS_SCOPED_RAW_CONSUMPTION' or
    a574.get('scientific_gate_pass') is not True or
    a574.get('promotes_physical_coordinate') is not False):
    raise SystemExit(('iteration574_prerequisite_not_passed',a574.get('classification'),a574.get('status')))

# Bind the independent mapping decision: same old observable, MP80/120 still required.
bind=json.loads((R/'post574_tensor11_binding_decision.json').read_text())
if (bind.get('classification')!='MAPPING_FOUND__HIGH_PRECISION_TENSOR11_VALUE_UNCOMPUTED__NEXT_GATE_MP80_MP120' or
    bind.get('scientific_gate_pass') is not True or
    bind.get('iteration424_precision_requirement_digits')!=[80,120] or
    bind.get('pre_result_mapping',{}).get('json_path')!='fit_residuals_scaled.tensor11'):
    raise SystemExit(('post574_tensor11_binding_not_passed',bind.get('classification')))

c=json.loads(CONTRACT.read_text())
if (c.get('iteration')!=575 or
    c.get('classification')!='PASS_PROSPECTIVE_ITER421_TENSOR11_EXACT_MP_SUPPORT_MANIFEST__NON_PROMOTING' or
    c.get('scientific_gate_pass') is not True or
    c.get('promotes_physical_coordinate') is not False):
    raise SystemExit(('iteration575_contract_not_passed',c.get('classification')))
fd=c['frozen_tensor11_definition']; ep=c['execution_policy']
if (fd.get('radius')!=1e-5 or fd.get('radius_multipliers_in_parent_order')!=[1.0,0.75,0.5,0.25] or
    fd.get('fit_basis')!='tensor degree (1,1): [1,x,y,x*y]' or float(fd.get('acceptance_threshold'))!=2e-5 or
    ep.get('precision_digits')!=[80,120] or ep.get('z_samples')!=[-0.86,-0.43,0.0,0.43,0.86] or
    int(ep.get('phi_nodes'))!=16 or float(ep.get('scaled_mp80_vs_mp120_max'))!=1e-30 or
    float(ep.get('radial_richardson_scaled_max'))!=5e-4):
    raise SystemExit(('iteration575_frozen_contract_drift',fd,ep))
missing=c['missing_high_precision_support']['nodes_in_first_occurrence_order_of_original_Iter421_F_cache']
if len(missing)!=36:
    raise SystemExit(('missing_support_count_drift',len(missing)))
node=missing[rank-1]
if int(node.get('rank'))!=rank:
    raise SystemExit(('rank_order_drift',rank,node))
MASS_U=float(node['u']); MASS_V=float(node['v'])

# Reuse the already validated direct-parent MP implementation, stopping before
# its own sampling loop exactly as the quarter support stages did.
p=ROOT/'post447_class3_phi_sample_mp_stage.py'
s=p.read_text()
marker="start=time.perf_counter(); rows=[]; mx=mp.mpf('0'); maxrad=mp.mpf('0'); finite=True"
if s.count(marker)!=1:
    raise SystemExit(('post447_sampling_boundary_drift',s.count(marker)))
C={'__name__':'iteration575_tensor11_support_parent','__file__':str(p)}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(s.split(marker,1)[0],str(p),'exec'),C,C)

MP_LEVELS=C['MP_LEVELS']; MP_LIMIT=C['MP_LIMIT']; NPHI=C['NPHI']
RADIAL_HS=C['RADIAL_HS']; RADIAL_LIMIT=C['RADIAL_LIMIT']
mpc_from_pair=C['mpc_from_pair']; scaled=C['scaled']
if list(MP_LEVELS)!=[80,120] or NPHI!=16 or list(RADIAL_HS)!=[0.002,0.001,0.0005]:
    raise SystemExit(('parent_sampling_contract_drift',MP_LEVELS,NPHI,RADIAL_HS))
if MP_LIMIT!=mp.mpf('1e-30') or abs(float(RADIAL_LIMIT)-5e-4)>1e-18:
    raise SystemExit(('parent_threshold_drift',MP_LIMIT,RADIAL_LIMIT))

# radial_limit_at closes over globals in the executed parent namespace; replace
# only the mass coordinate selected by the frozen manifest.
C['MASS_U']=MASS_U; C['MASS_V']=MASS_V
radial_limit_at=C['radial_limit_at']
Z_SAMPLES=(-0.86,-0.43,0.0,0.43,0.86)

start=time.perf_counter(); rows=[]; mx=mp.mpf('0'); maxrad=mp.mpf('0'); finite=True
for z in Z_SAMPLES:
    for m in range(NPHI):
        phi=2.0*math.pi*m/NPHI; vals={}; rads={}
        for dps in MP_LEVELS:
            with mp.workdps(dps):
                val,er=radial_limit_at(dps,z,phi)
                vals[dps]=(mp.nstr(mp.re(val),dps),mp.nstr(mp.im(val),dps))
                rads[dps]=mp.nstr(er,40)
        with mp.workdps(150):
            z80=mpc_from_pair(vals[80]); z120=mpc_from_pair(vals[120])
            cr=scaled(z80,z120); er80=mp.mpf(rads[80]); er120=mp.mpf(rads[120])
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
classification=(f'PASS_ITER421_TENSOR11_MP_SUPPORT_RANK_{rank}__NON_PROMOTING' if passed
                else f'BLOCKED_ITER421_TENSOR11_MP_SUPPORT_RANK_{rank}__NON_PROMOTING')
result={
 'iteration':575,
 'stage':f'ITER575_ITER421_TENSOR11_MISSING_SUPPORT_FULL_Z_MP__RANK_{rank}',
 'classification':classification,
 'scientific_gate_pass':passed,
 'promotes_physical_coordinate':False,
 'MODEL_READINESS':'24%',
 'readiness_change_pp':0,
 'target':{'double_double_index':2,'class_id':3,'q_squared':-1.0},
 'scope':'ONE_OF_36_PROSPECTIVELY_FROZEN_MISSING_ORIGINAL_ITER421_TENSOR11_F_NODES',
 'frozen':{
   'original_iter421_tensor11_rank':rank,
   'u':MASS_U,'v':MASS_V,
   'tensor11_radius':1e-5,
   'tensor11_radius_multipliers':[1.0,0.75,0.5,0.25],
   'tensor11_fit_basis':'[1,x,y,x*y]',
   'tensor11_final_residual_threshold':2e-5,
   'z_samples':list(Z_SAMPLES),'phi_nodes':NPHI,
   'radial_hs':list(RADIAL_HS),'precision_digits':[80,120]
 },
 'thresholds':{
   'scaled_mp80_vs_mp120_max':'1e-30',
   'radial_richardson_scaled_max':RADIAL_LIMIT,
   'required_sample_count':expected,
   'all_finite':True
 },
 'observed':{
   'scaled_mp80_vs_mp120_max':mp.nstr(mx,30),
   'max_radial_richardson_scaled_error':mp.nstr(maxrad,30),
   'sample_count':len(rows),'all_finite':finite,
   'runtime_seconds':time.perf_counter()-start
 },
 'rows':rows,
 'next_gate_if_pass':'raw-consume only as support; tensor11 remains BLOCKED until all 36 frozen missing ranks are raw-valid and the unchanged original Iter421 tensor11 fit is evaluated with the 28 existing nodes',
 'next_gate_if_blocked':'preserve tensor11 OPERATIONAL_BLOCKED and localize this exact frozen rank without node/radius/threshold changes',
 'guardrails':[
   'ITER574_RAW_SPECTRAL_PASS_REQUIRED','ITER575_COMPLETE_MISSING_SET_FROZEN_BEFORE_RESULTS',
   'ORIGINAL_ITER421_NODE_ONLY','DIRECT_PARENT_MP80_MP120','NO_PER_RANK_PHYSICAL_PROMOTION',
   'NO_RESULT_DEPENDENT_REORDERING','NO_UV_SUBSTITUTION','NO_THRESHOLD_WEAKENING',
   'NO_ZERO_FILL','NO_ANSATZ003','NO_FISHER_RESOURCES'
 ]
}
print(json.dumps(result,indent=2,sort_keys=True))
if not passed:
    raise SystemExit(2)
