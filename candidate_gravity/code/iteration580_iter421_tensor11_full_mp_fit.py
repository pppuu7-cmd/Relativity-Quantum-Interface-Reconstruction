#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 580.

Reproduce the unchanged original Iter421/420 tensor11 observable on the complete
prospectively frozen 64-node MP support after Iter579 raw-valid 36/36 closure.

Inputs:
  --basehalf-manifest  Iter574 canonical 28-node multipart manifest
  --basehalf-bundle    directory containing basehalf/<rank>/<part>/result.json
  --iter575-root       directory containing the 36 Iter575 result.json files;
                       layout is irrelevant because rank is read from payload

The spectral map is exactly the Iter407 index-2 specialization already used by
Iter574.  The final fit deliberately uses the original Iter420 numpy least-
squares definition and normalization; no post-hoc high-precision fit statistic
is introduced.
"""
from __future__ import annotations
import argparse, contextlib, io, json
from pathlib import Path
import mpmath as mp
import numpy as np

ROOT=Path(__file__).resolve().parent
TRAIN=(-0.86,-0.43,0.0,0.43,0.86); NPHI=16; DEG=4; DPS=(80,120)
RADIUS=1e-5; MULTS=(1.0,0.75,0.5,0.25); TOL=2e-5

def key(u,v): return (round(float(u),14),round(float(v),14))

def specialized_geometry():
    p=ROOT/'iteration407_tru1sq_channel4_analytic_spectral_reduction.py'; s=p.read_text()
    repl=[('TARGET_INDEX=4','TARGET_INDEX=2'),
          ("if int(ch['class_id'])!=5 or abs(q2+1.0)>1e-12: raise RuntimeError(('target_identity_drift',ch['class_id'],q2))",
           "if int(ch['class_id'])!=3 or abs(q2+1.0)>1e-12: raise RuntimeError(('target_identity_drift',ch['class_id'],q2))")]
    for old,new in repl:
        if s.count(old)!=1: raise RuntimeError(('iteration407_specialization_drift',old,s.count(old)))
        s=s.replace(old,new,1)
    marker='\nstart=time.perf_counter()\nd_base,diag_base=derivative_from_analytic(BASE_H)'
    if s.count(marker)!=1: raise RuntimeError(('iteration407_boundary_drift',s.count(marker)))
    ns={'__name__':'iteration580_iter407_index2_geometry','__file__':str(p)}
    with contextlib.redirect_stdout(io.StringIO()):
        exec(compile(s.split(marker,1)[0]+'\n',str(p),'exec'),ns,ns)
    if int(ns['ch']['class_id'])!=3 or abs(float(ns['q2'])+1.0)>1e-12: raise RuntimeError('target_identity_drift')
    return ns['affine_coeffs'],ns['kin']

def sample_means(o,dps):
    groups={z:[] for z in TRAIN}
    for r in o['rows']:
        z=min(TRAIN,key=lambda x:abs(float(r['z'])-x))
        if abs(float(r['z'])-z)>1e-12 or int(r['phi_index']) not in range(NPHI): raise RuntimeError('sample_support_drift')
        groups[z].append(mp.mpc(mp.mpf(r[f'mp{dps}_re']),mp.mpf(r[f'mp{dps}_im'])))
    if any(len(groups[z])!=NPHI for z in TRAIN): raise RuntimeError(('phi_count_drift',{z:len(groups[z]) for z in TRAIN}))
    return [sum(groups[z],mp.mpc(0))/NPHI for z in TRAIN]

def spectral_F(o,u,v,dps,affine,kin):
    with mp.workdps(dps):
        yy=sample_means(o,dps); zz=[mp.mpf(repr(z)) for z in TRAIN]
        V=mp.matrix([[z**k for k in range(DEG+1)] for z in zz]); coeff=mp.lu_solve(V,mp.matrix(yy))
        cc0,aa0=affine(float(u),float(v)); beta0=kin(float(u),float(v))[2]
        cc=mp.mpc(repr(float(cc0.real)),repr(float(cc0.imag))); aa=mp.mpc(repr(float(aa0.real)),repr(float(aa0.imag))); beta=mp.mpf(repr(float(beta0)))
        if min(abs(cc-aa),abs(cc+aa))<=mp.mpf('1e-12'): raise RuntimeError(('analytic_endpoint_uncut_too_small',u,v))
        if abs(aa)<mp.mpf('1e-50'):
            js=[(mp.mpf(0) if k%2 else mp.mpf(2)/(k+1))/cc for k in range(DEG+1)]
        else:
            js=[(mp.log(cc+aa)-mp.log(cc-aa))/aa]
            for k in range(1,DEG+1):
                im1=mp.mpf(0) if (k-1)%2 else mp.mpf(2)/k
                js.append((im1-cc*js[-1])/aa)
        return mp.mpf('0.5')*beta*sum(coeff[k]*js[k] for k in range(DEG+1))

def load_basehalf(manifest_path,bundle):
    raw={}
    for x in json.loads(manifest_path.read_text()):
        merged={}
        for pi,part in enumerate(x['artifact_parts']):
            p=bundle/'basehalf'/str(x['rank'])/str(pi)/'result.json'; o=json.loads(p.read_text())
            if o.get('scientific_gate_pass') is not True: raise RuntimeError(('basehalf_not_pass',x['rank'],pi))
            for row in o['rows']:
                rk=(round(float(row['z']),12),int(row['phi_index']))
                if rk in merged: raise RuntimeError(('duplicate_basehalf_sample',x['rank'],rk))
                merged[rk]=row
        if len(merged)!=80: raise RuntimeError(('basehalf_row_count',x['rank'],len(merged)))
        raw[key(x['u'],x['v'])]={'scientific_gate_pass':True,'rows':[merged[k] for k in sorted(merged)]}
    return raw

def load_iter575(root):
    byrank={}
    for p in root.rglob('result.json'):
        o=json.loads(p.read_text()); rank=o.get('frozen',{}).get('original_iter421_tensor11_rank')
        if not isinstance(rank,int): continue
        if rank in byrank: raise RuntimeError(('duplicate_iter575_rank',rank))
        if o.get('scientific_gate_pass') is not True or len(o.get('rows',[]))!=80: raise RuntimeError(('iter575_rank_not_raw_pass',rank))
        byrank[rank]=o
    if set(byrank)!=set(range(1,37)): raise RuntimeError(('iter575_rank_set_drift',sorted(byrank)))
    return {key(o['frozen']['u'],o['frozen']['v']):o for o in byrank.values()}

def fit_original(F,dps):
    points=[]; crosses=[]
    with mp.workdps(dps):
        for mr in MULTS:
            for ms in MULTS:
                r=mp.mpf(repr(RADIUS*mr)); s=mp.mpf(repr(RADIUS*ms))
                C=(F[key(+float(r),+float(s))]-F[key(+float(r),-float(s))]-F[key(-float(r),+float(s))]+F[key(-float(r),-float(s))])/(4*r*s)
                points.append((float(mr*mr),float(ms*ms),complex(C))); crosses.append(C)
    X=np.asarray([[1.0,x,y,x*y] for x,y,_ in points],float); y=np.asarray([z for _,_,z in points],complex)
    cr=np.linalg.lstsq(X,y.real,rcond=None)[0]; ci=np.linalg.lstsq(X,y.imag,rcond=None)[0]
    pred=X@cr+1j*(X@ci)
    residual=float(np.max(np.abs(pred-y))/max(1.0,float(np.max(np.abs(y))),float(np.max(np.abs(pred)))))
    return {'fit_residuals_scaled_tensor11':residual,
            'coefficients':[[float(a),float(b)] for a,b in zip(cr,ci)],
            'max_abs_cross':float(np.max(np.abs(y))),
            'max_abs_prediction':float(np.max(np.abs(pred))),
            'max_abs_raw_residual':float(np.max(np.abs(pred-y)))}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--basehalf-manifest',type=Path,required=True); ap.add_argument('--basehalf-bundle',type=Path,required=True); ap.add_argument('--iter575-root',type=Path,required=True); args=ap.parse_args()
    raw=load_basehalf(args.basehalf_manifest,args.basehalf_bundle); raw.update(load_iter575(args.iter575_root))
    required={key(su*RADIUS*mr,sv*RADIUS*ms) for mr in MULTS for ms in MULTS for su in (-1,1) for sv in (-1,1)}
    if set(raw)!=required: raise RuntimeError(('full64_support_drift',len(raw),len(required),sorted(required-set(raw))))
    affine,kin=specialized_geometry(); fits={}; spectra={d:{} for d in DPS}
    for d in DPS:
        for k,o in raw.items(): spectra[d][k]=spectral_F(o,k[0],k[1],d,affine,kin)
        fits[d]=fit_original(spectra[d],d)
    passed=all(fits[d]['fit_residuals_scaled_tensor11']<=TOL for d in DPS)
    out={'iteration':580,'classification':('PASS_ITER424_TENSOR11_ORIGINAL_OBSERVABLE_MP80_MP120__ITER424_5_OF_5_PASS' if passed else 'FAIL_ITER424_TENSOR11_ORIGINAL_OBSERVABLE_MP80_MP120'),
         'scientific_gate_pass':passed,'MODEL_READINESS':'24%','readiness_change_pp':0,
         'target':{'double_double_index':2,'class_id':3,'q_squared':-1.0},
         'frozen':{'formula':'[F(r,s)-F(r,-s)-F(-r,s)+F(-r,-s)]/(4rs)','radius':RADIUS,'radius_multipliers':list(MULTS),'fit_basis':'[1,x,y,xy]','precision_digits':list(DPS),'threshold':TOL},
         'observed':{str(d):fits[d] for d in DPS},
         'guardrails':['ITER579_ALL36_RAW_PASS_REQUIRED','ITER407_SPECTRAL_PIPELINE','ORIGINAL_ITER420_NUMPY_LSTSQ_AND_NORMALIZATION','NO_POSTHOC_REDEFINITION','NO_THRESHOLD_WEAKENING','NO_UV_SUBSTITUTION','NO_ANSATZ003','NO_FISHER_RESOURCES']}
    print(json.dumps(out,indent=2,sort_keys=True)); raise SystemExit(0 if passed else 2)
if __name__=='__main__': main()
