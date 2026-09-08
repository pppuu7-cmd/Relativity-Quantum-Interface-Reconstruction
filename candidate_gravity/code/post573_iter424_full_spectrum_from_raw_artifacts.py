#!/usr/bin/env python3
"""Post-Iteration-573 frozen Iteration-424 full-spectrum reconstruction.

Consumes only already raw-valid BASE/HALF and QUARTER result.json artifacts.
Reconstructs spectrum-integrated F(u,v) at MP80/MP120 with the frozen
Iteration-407 pipeline (16-phi mean at five TRAIN_Z nodes, degree-4
interpolation, affine denominator, analytic affine-log recurrence), then
central4-assembles physical D_s for h={5e-6,2.5e-6,1.25e-6}.

This gate computes only the Iteration-424 physical mass-step, cross-precision
and finiteness clauses. Direct-original is inherited only through Iteration573.
Tensor11 remains BLOCKED unless an independently frozen exact mapping exists.
"""
from __future__ import annotations
import argparse, contextlib, hashlib, io, json
from pathlib import Path
import mpmath as mp

ROOT=Path(__file__).resolve().parent
R=ROOT.parent/'results'
TRAIN=(-0.86,-0.43,0.0,0.43,0.86)
NPHI=16
DEG=4
DPS=(80,120)
C=[mp.mpf(1),mp.mpf(-8),mp.mpf(8),mp.mpf(-1)]
MASS_TOL=mp.mpf('2e-5')
CROSS_TOL=mp.mpf('2e-6')

QUARTER=[
 {'rank':1,'u':-2.5e-6,'v':-1.25e-6,'artifact_id':10010910464,'sha256':'fc63881cc09c0e6082b05f11f401a82239488e61537d5c9d47b2cb70bb138b3c'},
 {'rank':2,'u':-2.5e-6,'v':+1.25e-6,'artifact_id':10014273722,'sha256':'303ef060845f4cca6699e38d954089b144a26fe6b7c0ce1874819deb5ad2b01a'},
 {'rank':3,'u':-1.25e-6,'v':-2.5e-6,'artifact_id':10018745243,'sha256':'5ff2918ca522e689f8c67dc0f007efe8fd4a0bc70a5aba2d62423dc3dc4b35e0'},
 {'rank':4,'u':-1.25e-6,'v':-1.25e-6,'artifact_id':10023337886,'sha256':'f1604ef9580be7b3a0d8b217785961d8bbb94c7e1bfa44849abe118b66816347'},
 {'rank':5,'u':-1.25e-6,'v':+1.25e-6,'artifact_id':10026933360,'sha256':'2f50600679f26b42662fa6f0057394b1acf76717fd1eb64d01c25377ae955a6e'},
 {'rank':6,'u':-1.25e-6,'v':+2.5e-6,'artifact_id':10028800076,'sha256':'9a402fc89400b1d5a1e5e8fc888bc4dee87500e53a8371688d3f2b15e8c56192'},
 {'rank':7,'u':+1.25e-6,'v':-2.5e-6,'artifact_id':10030205964,'sha256':'eb4d389813c6620c2436e8f1abe91e24625398163e2e01e5282d68addc80d98f'},
 {'rank':8,'u':+1.25e-6,'v':-1.25e-6,'artifact_id':10032056133,'sha256':'8d498f746c5ee5aecb24949259227ac81731ff007ca1c8681b8169e510962cdb'},
 {'rank':9,'u':+1.25e-6,'v':+1.25e-6,'artifact_id':10033936398,'sha256':'63054690757baee587ef0c07cf753b3196fbdf63a42a14280c4d2ba4b665ab26'},
 {'rank':10,'u':+1.25e-6,'v':+2.5e-6,'artifact_id':10034846108,'sha256':'7cc11967da91eb299bd7a5c4e2c96525ff60c34ec0a4fc0f80e839c36601dc84'},
 {'rank':11,'u':+2.5e-6,'v':-1.25e-6,'artifact_id':10036490535,'sha256':'ac1b09b30e32fc17b0b45d300787bd89e2869df50edd41a85b256b578f0355ca'},
 {'rank':12,'u':+2.5e-6,'v':+1.25e-6,'artifact_id':10037900278,'sha256':'1f22924c06cb0f09b70d8586d6a9802f81d0cd131acd40d68368f3bdc689507b'},
 {'rank':'corner_mm','u':-2.5e-6,'v':-2.5e-6,'artifact_id':9991366491,'sha256':'d3afb8b89fb4a4e7ac41767b84630834c4fc660e1d310e65899392bdd49470f2'},
 {'rank':'corner_mp','u':-2.5e-6,'v':+2.5e-6,'artifact_id':9993124996,'sha256':'5bd5af97df1524997ab52a10a58cc4842b65c49091325ba1b57aba6e3d253f1a'},
 {'rank':'corner_pm','u':+2.5e-6,'v':-2.5e-6,'artifact_id':9998137548,'sha256':'46cc01a8ab5758349fdba27917afc7a0252d81631b41c8a9e15ed998bbcbba9c'},
 {'rank':'corner_pp','u':+2.5e-6,'v':+2.5e-6,'artifact_id':9999001385,'sha256':'655cc19ecbdf0db078c8bd500ff7f257691a8695c1cdee28fbee65edd069e4ba'},
]

def key(u,v): return (round(float(u),14),round(float(v),14))
def scaled(a,b): return abs(a-b)/max(mp.mpf(1),abs(a),abs(b))
def load_json_verified(path:Path,want:str):
    raw=path.read_bytes(); got=hashlib.sha256(raw).hexdigest()
    if got!=want: raise RuntimeError(('scientific_sha_mismatch',str(path),got,want))
    o=json.loads(raw)
    if o.get('scientific_gate_pass') is not True or len(o.get('rows',[]))!=80:
        raise RuntimeError(('raw_authority_not_pass',str(path),o.get('classification'),len(o.get('rows',[]))))
    return o

def sample_means(o,dps):
    groups={z:[] for z in TRAIN}
    for r in o['rows']:
        z=min(TRAIN,key=lambda x:abs(float(r['z'])-x))
        if abs(float(r['z'])-z)>1e-12: raise RuntimeError(('training_z_drift',r['z']))
        if int(r['phi_index']) not in range(NPHI): raise RuntimeError(('phi_index_drift',r['phi_index']))
        groups[z].append(mp.mpc(mp.mpf(r[f'mp{dps}_re']),mp.mpf(r[f'mp{dps}_im'])))
    if any(len(groups[z])!=NPHI for z in TRAIN): raise RuntimeError(('phi_count_drift',{z:len(groups[z]) for z in TRAIN}))
    return [sum(groups[z],mp.mpc(0))/NPHI for z in TRAIN]

def specialized_geometry():
    p=ROOT/'iteration407_tru1sq_channel4_analytic_spectral_reduction.py'; s=p.read_text()
    repl=[('TARGET_INDEX=4','TARGET_INDEX=2'),("if int(ch['class_id'])!=5 or abs(q2+1.0)>1e-12: raise RuntimeError(('target_identity_drift',ch['class_id'],q2))", "if int(ch['class_id'])!=3 or abs(q2+1.0)>1e-12: raise RuntimeError(('target_identity_drift',ch['class_id'],q2))")]
    for old,new in repl:
        if s.count(old)!=1: raise RuntimeError(('iteration407_specialization_drift',old,s.count(old)))
        s=s.replace(old,new,1)
    marker='\nstart=time.perf_counter()\nd_base,diag_base=derivative_from_analytic(BASE_H)'
    if s.count(marker)!=1: raise RuntimeError(('iteration407_boundary_drift',s.count(marker)))
    ns={'__name__':'post573_iter407_index2_geometry','__file__':str(p)}
    with contextlib.redirect_stdout(io.StringIO()): exec(compile(s.split(marker,1)[0]+'\n',str(p),'exec'),ns,ns)
    if int(ns['ch']['class_id'])!=3 or abs(float(ns['q2'])+1.0)>1e-12: raise RuntimeError('target_identity_drift')
    return ns['affine_coeffs'],ns['kin']

def spectral_F(o,u,v,dps,affine,kin):
    with mp.workdps(dps):
        yy=sample_means(o,dps); zz=[mp.mpf(repr(z)) for z in TRAIN]
        V=mp.matrix([[z**k for k in range(DEG+1)] for z in zz]); coeff=mp.lu_solve(V,mp.matrix(yy))
        cc0,aa0=affine(float(u),float(v)); beta0=kin(float(u),float(v))[2]
        cc=mp.mpc(repr(float(cc0.real)),repr(float(cc0.imag))); aa=mp.mpc(repr(float(aa0.real)),repr(float(aa0.imag))); beta=mp.mpf(repr(float(beta0)))
        if min(abs(cc-aa),abs(cc+aa))<=mp.mpf('1e-12'): raise RuntimeError(('analytic_endpoint_uncut_too_small',u,v,cc,aa))
        if abs(aa)<mp.mpf('1e-50'):
            js=[(mp.mpf(0) if k%2 else mp.mpf(2)/(k+1))/cc for k in range(DEG+1)]
        else:
            js=[(mp.log(cc+aa)-mp.log(cc-aa))/aa]
            for k in range(1,DEG+1):
                im1=mp.mpf(0) if (k-1)%2 else mp.mpf(2)/k
                js.append((im1-cc*js[-1])/aa)
        return mp.mpf('0.5')*beta*sum(coeff[k]*js[k] for k in range(DEG+1))

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--emit-quarter-manifest',action='store_true'); ap.add_argument('--basehalf-manifest',type=Path); ap.add_argument('--bundle',type=Path); args=ap.parse_args()
    if args.emit_quarter_manifest:
        print(json.dumps(QUARTER,indent=2,sort_keys=True)); return
    if args.basehalf_manifest is None or args.bundle is None: raise SystemExit('basehalf manifest and bundle required')
    # Fail closed on the latest prerequisite authority files.
    q572=json.loads((R/'iteration572_iter424_complete_quarter_assembly.json').read_text())
    q573=json.loads((R/'iteration573_iter424_frozen_clause_authority_mapping.json').read_text())
    if q572.get('classification')!='PASS_COMPLETE_QUARTER_RAW_ASSEMBLY__NON_PROMOTING' or q572.get('scientific_gate_pass') is not True: raise RuntimeError('iteration572_prerequisite_not_passed')
    if q573.get('scientific_gate_pass') is not True: raise RuntimeError(('iteration573_prerequisite_not_passed',q573.get('classification')))
    affine,kin=specialized_geometry()
    bh=json.loads(args.basehalf_manifest.read_text()); raw_bh={}; prov=[]
    for x in bh:
        p=args.bundle/'basehalf'/str(x['rank'])/'result.json'; o=load_json_verified(p,x['scientific_json_sha256']); k=key(x['u'],x['v']); raw_bh[k]=o
        prov.append({'family':'BASE_HALF','rank':x['rank'],'artifact_id':x['artifact_id'],'sha256':x['scientific_json_sha256'],'u':x['u'],'v':x['v']})
    raw_q={}
    for x in QUARTER:
        p=args.bundle/'quarter'/str(x['rank'])/'result.json'; o=load_json_verified(p,x['sha256']); k=key(x['u'],x['v']); raw_q[k]=o
        prov.append({'family':'QUARTER','rank':x['rank'],'artifact_id':x['artifact_id'],'sha256':x['sha256'],'u':x['u'],'v':x['v']})
    expected_bh={key(u,v) for h in (5e-6,2.5e-6) for u in (-2*h,-h,h,2*h) for v in (-2*h,-h,h,2*h)}
    expected_q={key(u,v) for h in (1.25e-6,) for u in (-2*h,-h,h,2*h) for v in (-2*h,-h,h,2*h)}
    if not expected_bh.issubset(raw_bh): raise RuntimeError(('basehalf_support_missing',sorted(expected_bh-set(raw_bh))))
    if set(raw_q)!=expected_q: raise RuntimeError(('quarter_support_drift',len(raw_q),len(expected_q)))
    spectra={}; fprec=mp.mpf(0); finite=True
    for family,raw,hs in [('BASE_HALF',raw_bh,(5e-6,2.5e-6)),('QUARTER',raw_q,(1.25e-6,))]:
        coords=set()
        for h in hs:
            coords|={key(u,v) for u in (-2*h,-h,h,2*h) for v in (-2*h,-h,h,2*h)}
        for k in sorted(coords):
            vals={d:spectral_F(raw[k],k[0],k[1],d,affine,kin) for d in DPS}
            with mp.workdps(150):
                finite=finite and all(mp.isfinite(vals[d].real) and mp.isfinite(vals[d].imag) for d in DPS); fprec=max(fprec,abs(vals[80]-vals[120]))
                spectra[(family,k)]={d:mp.mpc(vals[d]) for d in DPS}
    def ds_at(h,family,dps):
        ns=(-2*h,-h,h,2*h); total=mp.mpc(0)
        for i,u in enumerate(ns):
            for j,v in enumerate(ns): total+=C[i]*C[j]*spectra[(family,key(u,v))][dps]
        return -total/(mp.mpf(144)*mp.mpf(repr(h))**2)
    ds={}
    for label,h,fam in [('BASE',5e-6,'BASE_HALF'),('HALF',2.5e-6,'BASE_HALF'),('QUARTER',1.25e-6,'QUARTER')]:
        ds[label]={d:ds_at(h,fam,d) for d in DPS}
    with mp.workdps(150):
        bh=max(scaled(ds['BASE'][d],ds['HALF'][d]) for d in DPS); hq=max(scaled(ds['HALF'][d],ds['QUARTER'][d]) for d in DPS); mstep=max(bh,hq)
        cross=max(abs(ds[label][80]-ds[label][120]) for label in ds)
        dsfinite=all(mp.isfinite(ds[label][d].real) and mp.isfinite(ds[label][d].imag) for label in ds for d in DPS)
        mass_pass=bool(mstep<=MASS_TOL); cross_pass=bool(cross<=CROSS_TOL); finite_pass=bool(finite and dsfinite)
        numerical_pass=bool(mass_pass and cross_pass and finite_pass)
    out={
      'stage':'POST573_ITER424_FULL_SPECTRUM_FROM_RAW_ARTIFACTS__UNNUMBERED_COLLISION_SAFE',
      'classification':('PASS_ITER424_FULL_SPECTRUM_NUMERICAL_CLAUSES__TENSOR11_STILL_BLOCKED__NON_PROMOTING' if numerical_pass else 'FAIL_ITER424_FULL_SPECTRUM_NUMERICAL_CLAUSE__NON_PROMOTING'),
      'scientific_gate_pass':numerical_pass,'promotes_physical_coordinate':False,'MODEL_READINESS':'24%','readiness_change_pp':0,
      'target':{'double_double_index':2,'class_id':3,'q_squared':-1.0},
      'frozen':{'pipeline':'Iteration407 phi-average -> degree4 -> affine coefficients -> analytic affine-log recurrence -> central4','training_z':list(TRAIN),'phi_nodes':NPHI,'degree':DEG,'mass_steps':[5e-6,2.5e-6,1.25e-6],'precision_digits':[80,120],'central4_coefficients':[1,-8,8,-1]},
      'thresholds':{'physical_mass_step_discrepancy_max':'2e-5','abs_Ds_80_minus_Ds_120_max':'2e-6','all_values_finite':True},
      'observed':{'base_half_scaled_discrepancy_max':mp.nstr(bh,50),'half_quarter_scaled_discrepancy_max':mp.nstr(hq,50),'physical_mass_step_discrepancy_max':mp.nstr(mstep,50),'abs_Ds_80_minus_Ds_120_max':mp.nstr(cross,50),'max_spectral_F_abs_mp80_minus_mp120_diagnostic':mp.nstr(fprec,50),'all_spectrum_and_Ds_values_finite':finite_pass},
      'physical_Ds':{label:{str(d):[mp.nstr(ds[label][d].real,80),mp.nstr(ds[label][d].imag,80)] for d in DPS} for label in ds},
      'iteration424_clause_status':{'physical_mass_step_discrepancy':('PASS' if mass_pass else 'FAIL'),'direct_original_integrand_crosscheck':'PASS_INHERITED_ITERATION573_FROM_RAW_VALID_ITERATION421__MAX_2.0658997659274425e-9','tensor_degree_1_1_fit_residual':'OPERATIONAL_BLOCKED_NO_FROZEN_MAPPING__DO_NOT_SUBSTITUTE_RAW_F_BILINEAR_DIAGNOSTIC','abs_Ds_80digit_minus_Ds_120digit':('PASS' if cross_pass else 'FAIL'),'all_values_finite':('PASS' if finite_pass else 'FAIL')},
      'artifact_provenance':prov,
      'next_gate_if_numerical_pass':'preserve tensor11 BLOCKED unless an already-pre-result frozen high-precision tensor11 contract is found; no physical promotion until all five clauses PASS',
      'next_gate_if_numerical_fail':'preserve scoped scientific FAIL of the computed frozen clause(s); do not weaken thresholds or change nodes/precision',
      'guardrails':['RAW_VALID_ARTIFACTS_ONLY','ITERATION407_SPECTRAL_PIPELINE','ITERATION424_THRESHOLDS_UNCHANGED','NO_TENSOR11_POSTHOC_MAPPING','NO_RAW_F_BILINEAR_SUBSTITUTION','NO_UV_SUBSTITUTION','NO_ZERO_FILL','NO_SMALLER_H','NO_ANSATZ003','NO_FISHER_RESOURCES']}
    print(json.dumps(out,indent=2,sort_keys=True))
    if not numerical_pass: raise SystemExit(2)
if __name__=='__main__': main()
