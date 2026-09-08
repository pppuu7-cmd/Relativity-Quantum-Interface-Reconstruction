#!/usr/bin/env python3
"""Deterministic post-Iteration575 consumer for the original Iter421 tensor11 gate.

Inputs:
- the already raw-consumed Iter574 full-spectrum source artifact, which carries
  the exact 28-node BASE/HALF MP raw bundle;
- all 36 prospectively frozen Iter575 missing-support rank artifacts.

If and only if all 36 new ranks are raw-valid PASS, reconstruct F(u,v) at all
64 original Iter421 signed nodes with the unchanged Iter407 spectral pipeline
and evaluate the unchanged tensor degree-(1,1) residual independently at MP80
and MP120.  No node/radius/basis/threshold is selected from results.

This consumer is deliberately unnumbered and non-promoting.  A later raw
consumption authority may promote index2 only if the produced tensor11 clause
is PASS and the other four Iter424 clauses remain PASS.
"""
from __future__ import annotations
import argparse, contextlib, hashlib, io, json
from pathlib import Path
import mpmath as mp

ROOT=Path(__file__).resolve().parent
R=ROOT.parent/'results'
CONTRACT=ROOT.parent/'contracts'/'iteration575_iter421_tensor11_exact_mp_support_manifest.json'
TRAIN=(-0.86,-0.43,0.0,0.43,0.86)
NPHI=16
DEG=4
DPS=(80,120)
TENSOR_TOL=mp.mpf('2e-5')

def key(u,v): return (round(float(u),14),round(float(v),14))

def sha256_bytes(b): return hashlib.sha256(b).hexdigest()

def verify_json(path:Path,want:str|None=None):
    raw=path.read_bytes(); got=sha256_bytes(raw)
    if want is not None and got!=want.lower():
        raise RuntimeError(('sha256_mismatch',str(path),got,want))
    return json.loads(raw),got

def sample_means(o,dps):
    groups={z:[] for z in TRAIN}
    for r in o['rows']:
        z=min(TRAIN,key=lambda x:abs(float(r['z'])-x))
        if abs(float(r['z'])-z)>1e-12: raise RuntimeError(('training_z_drift',r['z']))
        ph=int(r['phi_index'])
        if ph not in range(NPHI): raise RuntimeError(('phi_index_drift',ph))
        groups[z].append(mp.mpc(mp.mpf(r[f'mp{dps}_re']),mp.mpf(r[f'mp{dps}_im'])))
    if any(len(groups[z])!=NPHI for z in TRAIN):
        raise RuntimeError(('phi_count_drift',{z:len(groups[z]) for z in TRAIN}))
    return [sum(groups[z],mp.mpc(0))/NPHI for z in TRAIN]

def specialized_geometry():
    p=ROOT/'iteration407_tru1sq_channel4_analytic_spectral_reduction.py'; s=p.read_text()
    repl=[
      ('TARGET_INDEX=4','TARGET_INDEX=2'),
      ("if int(ch['class_id'])!=5 or abs(q2+1.0)>1e-12: raise RuntimeError(('target_identity_drift',ch['class_id'],q2))",
       "if int(ch['class_id'])!=3 or abs(q2+1.0)>1e-12: raise RuntimeError(('target_identity_drift',ch['class_id'],q2))")
    ]
    for old,new in repl:
        if s.count(old)!=1: raise RuntimeError(('iteration407_specialization_drift',old,s.count(old)))
        s=s.replace(old,new,1)
    marker='\nstart=time.perf_counter()\nd_base,diag_base=derivative_from_analytic(BASE_H)'
    if s.count(marker)!=1: raise RuntimeError(('iteration407_boundary_drift',s.count(marker)))
    ns={'__name__':'post575_iter407_index2_geometry','__file__':str(p)}
    with contextlib.redirect_stdout(io.StringIO()):
        exec(compile(s.split(marker,1)[0]+'\n',str(p),'exec'),ns,ns)
    if int(ns['ch']['class_id'])!=3 or abs(float(ns['q2'])+1.0)>1e-12:
        raise RuntimeError('target_identity_drift')
    return ns['affine_coeffs'],ns['kin']

def spectral_F(o,u,v,dps,affine,kin):
    with mp.workdps(dps):
        yy=sample_means(o,dps); zz=[mp.mpf(repr(z)) for z in TRAIN]
        V=mp.matrix([[z**k for k in range(DEG+1)] for z in zz])
        coeff=mp.lu_solve(V,mp.matrix(yy))
        cc0,aa0=affine(float(u),float(v)); beta0=kin(float(u),float(v))[2]
        cc=mp.mpc(repr(float(cc0.real)),repr(float(cc0.imag)))
        aa=mp.mpc(repr(float(aa0.real)),repr(float(aa0.imag)))
        beta=mp.mpf(repr(float(beta0)))
        if min(abs(cc-aa),abs(cc+aa))<=mp.mpf('1e-12'):
            raise RuntimeError(('analytic_endpoint_uncut_too_small',u,v,cc,aa))
        if abs(aa)<mp.mpf('1e-50'):
            js=[(mp.mpf(0) if k%2 else mp.mpf(2)/(k+1))/cc for k in range(DEG+1)]
        else:
            js=[(mp.log(cc+aa)-mp.log(cc-aa))/aa]
            for k in range(1,DEG+1):
                im1=mp.mpf(0) if (k-1)%2 else mp.mpf(2)/k
                js.append((im1-cc*js[-1])/aa)
        return mp.mpf('0.5')*beta*sum(coeff[k]*js[k] for k in range(DEG+1))

def fit_tensor11(points,dps):
    # Same mathematical least-squares problem as Iter421's np.linalg.lstsq on
    # basis [1,x,y,xy], now solved at the required multiprecision.
    with mp.workdps(dps):
        A=mp.matrix([[mp.mpf(1),x,y,x*y] for x,y,_ in points])
        b=mp.matrix([z for _,_,z in points])
        coeff=mp.lu_solve(A.T*A,A.T*b)
        pred=A*coeff
        den=max([mp.mpf(1)]+[abs(z) for _,_,z in points]+[abs(pred[i]) for i in range(len(points))])
        resid=max(abs(pred[i]-b[i]) for i in range(len(points)))/den
        return coeff,resid,[pred[i] for i in range(len(points))]

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--existing-root',type=Path,required=True)
    ap.add_argument('--new-root',type=Path,required=True)
    args=ap.parse_args()

    a574=json.loads((R/'iteration574_iter424_full_spectrum_raw_consumption.json').read_text())
    if (a574.get('iteration')!=574 or
        a574.get('classification')!='PASS_RAW_CONSUMED_ITER424_FULL_SPECTRUM_NUMERICAL_CLAUSES__TENSOR11_OPERATIONAL_BLOCKED__NON_PROMOTING' or
        a574.get('scientific_gate_pass') is not True):
        raise RuntimeError(('iteration574_prerequisite_not_passed',a574.get('classification')))
    c=json.loads(CONTRACT.read_text())
    if (c.get('iteration')!=575 or c.get('classification')!='PASS_PROSPECTIVE_ITER421_TENSOR11_EXACT_MP_SUPPORT_MANIFEST__NON_PROMOTING' or
        c.get('scientific_gate_pass') is not True):
        raise RuntimeError(('iteration575_contract_not_passed',c.get('classification')))
    fd=c['frozen_tensor11_definition']
    if (fd.get('radius')!=1e-5 or fd.get('radius_multipliers_in_parent_order')!=[1.0,0.75,0.5,0.25] or
        fd.get('fit_basis')!='tensor degree (1,1): [1,x,y,x*y]' or float(fd.get('acceptance_threshold'))!=2e-5):
        raise RuntimeError(('tensor11_definition_drift',fd))

    # Reconstruct the 28 existing raw-valid BASE/HALF nodes from the exact
    # Iter574 source artifact bundle and independently verify every part SHA.
    bh=json.loads((args.existing_root/'basehalf_manifest.json').read_text())
    if len(bh)!=28: raise RuntimeError(('basehalf_manifest_count_drift',len(bh)))
    raw_nodes={}; existing_prov=[]
    for x in bh:
        parts=x.get('artifact_parts')
        if not isinstance(parts,list) or not parts: raise RuntimeError(('artifact_parts_missing',x.get('rank')))
        merged={}; pp=[]
        for pi,part in enumerate(parts):
            p=args.existing_root/'bundle'/'basehalf'/str(x['rank'])/str(pi)/'result.json'
            o,got=verify_json(p,part['scientific_json_sha256'])
            if o.get('scientific_gate_pass') is not True: raise RuntimeError(('existing_part_not_pass',x['rank'],pi,o.get('classification')))
            for row in o.get('rows',[]):
                rk=(round(float(row['z']),12),int(row['phi_index']))
                if rk in merged: raise RuntimeError(('existing_duplicate_row',x['rank'],rk))
                merged[rk]=row
            pp.append({'part_index':pi,'artifact_id':part['artifact_id'],'sha256':got})
        if len(merged)!=80: raise RuntimeError(('existing_merged_row_count',x['rank'],len(merged)))
        zset={rk[0] for rk in merged}; phset={rk[1] for rk in merged}
        if zset!={-0.86,-0.43,0.0,0.43,0.86} or phset!=set(range(16)):
            raise RuntimeError(('existing_support_drift',x['rank'],sorted(zset),sorted(phset)))
        k=key(x['u'],x['v'])
        if k in raw_nodes: raise RuntimeError(('existing_coordinate_duplicate',k))
        raw_nodes[k]={'scientific_gate_pass':True,'rows':[merged[rk] for rk in sorted(merged)]}
        existing_prov.append({'rank':x['rank'],'u':x['u'],'v':x['v'],'parts':pp})
    if len(raw_nodes)!=28: raise RuntimeError(('existing_distinct_count_drift',len(raw_nodes)))

    # Consume exactly 36 same-run Iter575 rank artifacts. Each embedded audit
    # must bind result SHA, rank and coordinate. Valid scientific BLOCKED is
    # retained as BLOCKED rather than treated as infrastructure failure.
    missing=c['missing_high_precision_support']['nodes_in_first_occurrence_order_of_original_Iter421_F_cache']
    if len(missing)!=36: raise RuntimeError(('missing_manifest_count_drift',len(missing)))
    blocked=[]; new_prov=[]
    for node in missing:
        rank=int(node['rank']); d=args.new_root/f'rank_{rank}'
        ro,got=verify_json(d/'result.json')
        ao,agot=verify_json(d/'authority_audit.json')
        if (ao.get('schema')!='rqir_iteration575_tensor11_support_authority_audit_v1' or ao.get('iteration')!=575 or
            int(ao.get('rank'))!=rank or ao.get('result_json_sha256')!=got or ao.get('raw_result_integrity_valid') is not True):
            raise RuntimeError(('new_authority_audit_invalid',rank,ao))
        if (ro.get('iteration')!=575 or int(ro.get('frozen',{}).get('original_iter421_tensor11_rank'))!=rank or
            abs(float(ro.get('frozen',{}).get('u'))-float(node['u']))>1e-18 or
            abs(float(ro.get('frozen',{}).get('v'))-float(node['v']))>1e-18 or len(ro.get('rows',[]))!=80):
            raise RuntimeError(('new_rank_schema_invalid',rank,ro.get('classification')))
        if ro.get('classification')==f'BLOCKED_ITER421_TENSOR11_MP_SUPPORT_RANK_{rank}__NON_PROMOTING':
            if ro.get('scientific_gate_pass') is not False: raise RuntimeError(('blocked_gate_flag_drift',rank))
            blocked.append(rank)
        elif ro.get('classification')==f'PASS_ITER421_TENSOR11_MP_SUPPORT_RANK_{rank}__NON_PROMOTING':
            if ro.get('scientific_gate_pass') is not True: raise RuntimeError(('pass_gate_flag_drift',rank))
            k=key(node['u'],node['v'])
            if k in raw_nodes: raise RuntimeError(('new_coordinate_already_existing',rank,k))
            raw_nodes[k]=ro
        else:
            raise RuntimeError(('new_classification_invalid',rank,ro.get('classification')))
        new_prov.append({'rank':rank,'u':node['u'],'v':node['v'],'result_sha256':got,'audit_sha256':agot,'classification':ro.get('classification')})

    base={
      'stage':'POST575_ITER421_TENSOR11_EXACT_MP_CONSUMER__UNNUMBERED_COLLISION_SAFE',
      'MODEL_READINESS':'24%','readiness_change_pp':0,'promotes_physical_coordinate':False,
      'target':{'double_double_index':2,'class_id':3,'q_squared':-1.0},
      'frozen':{'R':1e-5,'radius_multipliers':[1.0,0.75,0.5,0.25],
                'fit_coordinates':'x=(r/R)^2,y=(s/R)^2','fit_basis':'[1,x,y,x*y]',
                'tensor11_residual_threshold':'2e-5','precision_digits':[80,120],
                'required_signed_F_nodes':64,'existing_nodes':28,'new_nodes':36},
      'support_provenance':{'existing':existing_prov,'new':new_prov},
      'guardrails':['UNCHANGED_ORIGINAL_ITER421_TENSOR11_OBSERVABLE','NO_NODE_RADIUS_BASIS_THRESHOLD_CHANGE',
                    'ALL_36_NEW_RANKS_RAW_CONSUMED_BEFORE_FIT','NO_UV_SUBSTITUTION','NO_ZERO_FILL',
                    'NO_PHYSICAL_PROMOTION_IN_THIS_UNNUMBERED_CONSUMER','NO_ANSATZ003','NO_FISHER_RESOURCES']
    }
    if blocked:
        base.update({
          'classification':'BLOCKED_ITER421_TENSOR11_EXACT_MP_SUPPORT__ONE_OR_MORE_RANKS_BLOCKED__NON_PROMOTING',
          'scientific_gate_pass':False,
          'support_state':{'raw_valid_pass_ranks':36-len(blocked),'blocked_ranks':blocked,'complete_for_fit':False},
          'tensor11':None,
          'interpretation':'At least one prospectively frozen original-Iter421 support node failed its unchanged MP/radial support gate; tensor11 remains BLOCKED and no fit is evaluated.'
        })
        print(json.dumps(base,indent=2,sort_keys=True)); return

    if len(raw_nodes)!=64:
        raise RuntimeError(('complete_support_count_drift',len(raw_nodes)))
    expected={key(u,v) for a in (1e-5,7.5e-6,5e-6,2.5e-6) for u in (a,-a) for b in (1e-5,7.5e-6,5e-6,2.5e-6) for v in (b,-b)}
    if set(raw_nodes)!=expected:
        raise RuntimeError(('complete_support_set_drift',sorted(expected-set(raw_nodes)),sorted(set(raw_nodes)-expected)))

    affine,kin=specialized_geometry()
    spectra={d:{} for d in DPS}; max_fprec=mp.mpf(0)
    for k,o in raw_nodes.items():
        vals={d:spectral_F(o,k[0],k[1],d,affine,kin) for d in DPS}
        for d in DPS: spectra[d][k]=vals[d]
        with mp.workdps(150): max_fprec=max(max_fprec,abs(vals[80]-vals[120]))

    R0=mp.mpf('1e-5'); mult=[mp.mpf('1'),mp.mpf('0.75'),mp.mpf('0.5'),mp.mpf('0.25')]
    fits={}; cross_precision_points=mp.mpf(0)
    point_dump={d:[] for d in DPS}
    for dps in DPS:
        with mp.workdps(dps):
            pts=[]
            for mr in mult:
                for ms in mult:
                    r=R0*mr; s=R0*ms
                    F=lambda u,v: spectra[dps][key(u,v)]
                    z=(F(r,s)-F(r,-s)-F(-r,s)+F(-r,-s))/(4*r*s)
                    x=mr*mr; y=ms*ms; pts.append((x,y,z))
                    point_dump[dps].append({'mr':mp.nstr(mr,20),'ms':mp.nstr(ms,20),'x':mp.nstr(x,30),'y':mp.nstr(y,30),
                                            'C_re':mp.nstr(mp.re(z),dps),'C_im':mp.nstr(mp.im(z),dps)})
            coeff,resid,pred=fit_tensor11(pts,dps)
            fits[dps]={'residual_scaled':mp.nstr(resid,50),
                       'intercept_re':mp.nstr(mp.re(coeff[0]),dps),'intercept_im':mp.nstr(mp.im(coeff[0]),dps),
                       'coefficients':[[mp.nstr(mp.re(z),dps),mp.nstr(mp.im(z),dps)] for z in coeff]}
    with mp.workdps(150):
        for i in range(16):
            z80=mp.mpc(mp.mpf(point_dump[80][i]['C_re']),mp.mpf(point_dump[80][i]['C_im']))
            z120=mp.mpc(mp.mpf(point_dump[120][i]['C_re']),mp.mpf(point_dump[120][i]['C_im']))
            cross_precision_points=max(cross_precision_points,abs(z80-z120))
        r80=mp.mpf(fits[80]['residual_scaled']); r120=mp.mpf(fits[120]['residual_scaled'])
        tensor_pass=bool(r80<=TENSOR_TOL and r120<=TENSOR_TOL)
    base.update({
      'classification':('PASS_ITER424_TENSOR11_EXACT_MP80_MP120__READY_FOR_FAIL_CLOSED_RAW_CONSUMPTION__NON_PROMOTING'
                        if tensor_pass else 'FAIL_ITER424_TENSOR11_EXACT_MP80_MP120_RESIDUAL__NON_PROMOTING'),
      'scientific_gate_pass':tensor_pass,
      'support_state':{'raw_valid_pass_ranks':36,'blocked_ranks':[],'complete_for_fit':True,'total_signed_F_nodes':64},
      'tensor11':{'MP80':fits[80],'MP120':fits[120],
                  'both_residuals_le_2e-5':tensor_pass,
                  'max_abs_C_point_MP80_minus_MP120_diagnostic':mp.nstr(cross_precision_points,50),
                  'max_abs_spectral_F_MP80_minus_MP120_diagnostic':mp.nstr(max_fprec,50),
                  'points':{'MP80':point_dump[80],'MP120':point_dump[120]}},
      'iteration424_clause_state_if_raw_consumed':{
        'mass_step':'PASS_ITER574','direct_original':'PASS_ITER573','tensor11':('PASS' if tensor_pass else 'FAIL'),
        'Ds_MP80_MP120':'PASS_ITER574','finite':'PASS_ITER574',
        'full_five_clause_pass_possible':tensor_pass
      },
      'interpretation':('All 36 missing support ranks passed and the unchanged original Iter421 tensor11 residual passes independently at MP80 and MP120; physical promotion still requires separate raw consumption authority.'
                        if tensor_pass else 'All support exists, but the unchanged original Iter421 tensor11 residual fails at MP80 and/or MP120; preserve this scoped negative result and do not promote index2.')
    })
    print(json.dumps(base,indent=2,sort_keys=True))

if __name__=='__main__': main()
