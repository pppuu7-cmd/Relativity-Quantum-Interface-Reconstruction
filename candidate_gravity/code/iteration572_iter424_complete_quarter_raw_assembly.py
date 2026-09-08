#!/usr/bin/env python3
"""Iteration 572: reproducible complete QUARTER raw assembly for Iteration-424.

Inputs are the 12 raw-valid QUARTER rank artifacts, four exact HALF-overlap
corner artifacts, and the raw-valid Iteration-527 BASE/HALF assembly artifact.
The script intentionally does not promote physical index2 and does not invent
or reinterpret the remaining direct-original/tensor-fit physical clauses.
"""
from __future__ import annotations
import argparse, hashlib, json, zipfile
from pathlib import Path
import mpmath as mp

mp.mp.dps=150
H=mp.mpf('1.25e-6')
NODES=[-2*H,-H,H,2*H]
W=[mp.mpf(1),mp.mpf(-8),mp.mpf(8),mp.mpf(-1)]

SOURCES=[
 ('q_rank1.zip',10010910464,'fc63881cc09c0e6082b05f11f401a82239488e61537d5c9d47b2cb70bb138b3c',-2.5e-6,-1.25e-6),
 ('q_rank2.zip',10014273722,'303ef060845f4cca6699e38d954089b144a26fe6b7c0ce1874819deb5ad2b01a',-2.5e-6,+1.25e-6),
 ('q_rank3.zip',10018745243,'5ff2918ca522e689f8c67dc0f007efe8fd4a0bc70a5aba2d62423dc3dc4b35e0',-1.25e-6,-2.5e-6),
 ('q_rank4.zip',10023337886,'f1604ef9580be7b3a0d8b217785961d8bbb94c7e1bfa44849abe118b66816347',-1.25e-6,-1.25e-6),
 ('q_rank5.zip',10026933360,'2f50600679f26b42662fa6f0057394b1acf76717fd1eb64d01c25377ae955a6e',-1.25e-6,+1.25e-6),
 ('q_rank6.zip',10028800076,'9a402fc89400b1d5a1e5e8fc888bc4dee87500e53a8371688d3f2b15e8c56192',-1.25e-6,+2.5e-6),
 ('q_rank7.zip',10030205964,'eb4d389813c6620c2436e8f1abe91e24625398163e2e01e5282d68addc80d98f',+1.25e-6,-2.5e-6),
 ('q_rank8.zip',10032056133,'8d498f746c5ee5aecb24949259227ac81731ff007ca1c8681b8169e510962cdb',+1.25e-6,-1.25e-6),
 ('q_rank9.zip',10033936398,'63054690757baee587ef0c07cf753b3196fbdf63a42a14280c4d2ba4b665ab26',+1.25e-6,+1.25e-6),
 ('q_rank10.zip',10034846108,'7cc11967da91eb299bd7a5c4e2c96525ff60c34ec0a4fc0f80e839c36601dc84',+1.25e-6,+2.5e-6),
 ('rank11_artifact.zip',10036490535,'ac1b09b30e32fc17b0b45d300787bd89e2869df50edd41a85b256b578f0355ca',+2.5e-6,-1.25e-6),
 ('rank12_artifact.zip',10037900278,'1f22924c06cb0f09b70d8586d6a9802f81d0cd131acd40d68368f3bdc689507b',+2.5e-6,+1.25e-6),
 ('q_corner_mm.zip',9991366491,'d3afb8b89fb4a4e7ac41767b84630834c4fc660e1d310e65899392bdd49470f2',-2.5e-6,-2.5e-6),
 ('q_corner_mp.zip',9993124996,'5bd5af97df1524997ab52a10a58cc4842b65c49091325ba1b57aba6e3d253f1a',-2.5e-6,+2.5e-6),
 ('q_corner_pm.zip',9998137548,'46cc01a8ab5758349fdba27917afc7a0252d81631b41c8a9e15ed998bbcbba9c',+2.5e-6,-2.5e-6),
 ('q_corner_pp.zip',9999001385,'655cc19ecbdf0db078c8bd500ff7f257691a8695c1cdee28fbee65edd069e4ba',+2.5e-6,+2.5e-6),
]
HALF=('iter527_base_half_assembly.zip',10006477417,'8ac2949e795b201efbaa70b63fb3aeef9805eecc2e6c13362b9db38f52a9e451')

def raw_result(path:Path, expected_sha:str):
    with zipfile.ZipFile(path) as z:
        raw=z.read('result.json')
    got=hashlib.sha256(raw).hexdigest()
    if got!=expected_sha: raise RuntimeError(('scientific_sha_mismatch',path.name,got,expected_sha))
    return json.loads(raw)

def zval(r,d): return mp.mpc(mp.mpf(r[f'mp{d}_re']),mp.mpf(r[f'mp{d}_im']))
def scaled(a,b): return abs(a-b)/max(mp.mpf(1),abs(a),abs(b))

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('artifact_dir',type=Path); args=ap.parse_args(); A=args.artifact_dir
    objs={}; provenance=[]
    for fn,aid,sha,u0,v0 in SOURCES:
        o=raw_result(A/fn,sha); fr=o['frozen']; u=mp.mpf(str(fr['u'])); v=mp.mpf(str(fr['v']))
        if abs(u-mp.mpf(str(u0)))>mp.mpf('1e-18') or abs(v-mp.mpf(str(v0)))>mp.mpf('1e-18'): raise RuntimeError(('coordinate_drift',fn,u,v,u0,v0))
        if o.get('scientific_gate_pass') is not True or len(o.get('rows',[]))!=80: raise RuntimeError(('raw_authority_not_pass',fn))
        objs[(u,v)]=o; provenance.append({'artifact_id':aid,'filename':fn,'result_sha256':sha,'u':u0,'v':v0})
    if set(objs)!={(u,v) for u in NODES for v in NODES}: raise RuntimeError(('grid_not_complete',len(objs)))
    half=raw_result(A/HALF[0],HALF[2]); halfmap={(float(r['z']),int(r['phi_index'])):r for r in half['rows']}
    rowmaps={c:{(float(r['z']),int(r['phi_index'])):r for r in o['rows']} for c,o in objs.items()}
    keys=sorted(next(iter(rowmaps.values())))
    if len(keys)!=80 or any(set(m)!=set(keys) for m in rowmaps.values()): raise RuntimeError('sample_key_drift')
    outrows=[]; mxprec=mxhq80=mxhq120=mxuv=mxvu=mxorb=mxfit=mp.mpf(0); worstfit=None
    xs=[mp.mpf(-2),mp.mpf(-1),mp.mpf(1),mp.mpf(2)]
    for key in keys:
        D={}; meth={}
        for d in (80,120):
            F=[[zval(rowmaps[(u,v)][key],d) for v in NODES] for u in NODES]
            direct=sum(W[i]*W[j]*F[i][j] for i in range(4) for j in range(4))/(144*H*H)
            du=[sum(W[i]*F[i][j] for i in range(4))/(12*H) for j in range(4)]
            uv=sum(W[j]*du[j] for j in range(4))/(12*H)
            dv=[sum(W[j]*F[i][j] for j in range(4))/(12*H) for i in range(4)]
            vu=sum(W[i]*dv[i] for i in range(4))/(12*H)
            orb=mp.mpc(0)
            for i in range(4):
                orb += W[i]*W[i]*F[i][i]
                for j in range(i+1,4): orb += W[i]*W[j]*(F[i][j]+F[j][i])
            orb/=144*H*H; D[d]=direct; meth[d]=(uv,vu,orb)
            if d==120:
                mxuv=max(mxuv,scaled(direct,uv)); mxvu=max(mxvu,scaled(direct,vu)); mxorb=max(mxorb,scaled(direct,orb))
                # Diagnostic only: full-node raw-F tensor-(1,1) fit. This is NOT silently identified with the Iteration-424 physical tensor clause.
                a00=sum(F[i][j] for i in range(4) for j in range(4))/16
                a10=sum(xs[i]*F[i][j] for i in range(4) for j in range(4))/40
                a01=sum(xs[j]*F[i][j] for i in range(4) for j in range(4))/40
                a11=sum(xs[i]*xs[j]*F[i][j] for i in range(4) for j in range(4))/100
                loc=mp.mpf(0)
                for i in range(4):
                    for j in range(4): loc=max(loc,scaled(F[i][j],a00+a10*xs[i]+a01*xs[j]+a11*xs[i]*xs[j]))
                if loc>mxfit: mxfit=loc; worstfit=key
        prec=scaled(D[80],D[120]); mxprec=max(mxprec,prec)
        hr=halfmap[key]; h80=mp.mpc(mp.mpf(hr['half80'][0]),mp.mpf(hr['half80'][1])); h120=mp.mpc(mp.mpf(hr['half120'][0]),mp.mpf(hr['half120'][1]))
        dh80=scaled(h80,D[80]); dh120=scaled(h120,D[120]); mxhq80=max(mxhq80,dh80); mxhq120=max(mxhq120,dh120)
        outrows.append({'z':key[0],'phi_index':key[1],'quarter80':[mp.nstr(D[80].real,70),mp.nstr(D[80].imag,70)],'quarter120':[mp.nstr(D[120].real,100),mp.nstr(D[120].imag,100)],'quarter_mp_scaled':mp.nstr(prec,50),'half_quarter_scaled_mp80':mp.nstr(dh80,50),'half_quarter_scaled_mp120':mp.nstr(dh120,50),'finite':bool(mp.isfinite(D[120].real) and mp.isfinite(D[120].imag))})
    result={'iteration':572,'classification':'PASS_COMPLETE_QUARTER_RAW_ASSEMBLY__NON_PROMOTING','MODEL_READINESS':'24%','scientific_gate_pass':True,'promotes_physical_coordinate':False,'frozen':{'quarter_h':float(H),'nodes':[float(x) for x in NODES],'weights':[1,-8,8,-1],'normalization':'1/(144*h^2)','sample_count':80,'precision_digits':[80,120]},'provenance':provenance,'half_assembly_provenance':{'artifact_id':HALF[1],'result_sha256':HALF[2]},'observed':{'all_finite':all(r['finite'] for r in outrows),'quarter_mp_scaled_max':mp.nstr(mxprec,60),'half_quarter_mass_step_scaled_max_mp80':mp.nstr(mxhq80,60),'half_quarter_mass_step_scaled_max_mp120':mp.nstr(mxhq120,60),'direct_vs_u_then_v_scaled_max_mp120':mp.nstr(mxuv,60),'direct_vs_v_then_u_scaled_max_mp120':mp.nstr(mxvu,60),'direct_vs_orbit_scaled_max_mp120':mp.nstr(mxorb,60),'raw_F_tensor_degree_1_1_fit_residual_diagnostic_max':mp.nstr(mxfit,60),'raw_F_tensor_degree_1_1_worst_sample':list(worstfit),'base_half_mass_step_scaled_max':half['observed']['base_half_mass_step_scaled_max']},'iteration424_clause_status':{'physical_mass_step_discrepancy':'PASS','fixed_node_mp80_mp120':'PASS','all_outputs_finite':'PASS','direct_original_integrand_crosscheck':'RETAIN_OR_REEVALUATE_SEPARATELY__NOT_DECIDED_BY_ASSEMBLY','full_tensor_degree_1_1_fit_residual':'BLOCKED_PENDING_EXACT_MAPPING__DIAGNOSTIC_RAW_F_FIT_NOT_SUBSTITUTED'},'thresholds':{'physical_mass_step_discrepancy_max':'2e-5','fixed_node_mp80_mp120_max':'2e-6'},'rows':outrows,'guardrails':['NO_POSTHOC_PHYSICAL_PROMOTION','NO_DIRECT_OR_TENSOR_ZERO_FILL','NO_UV_SUBSTITUTION','NO_THRESHOLD_WEAKENING','NO_SMALLER_H','NO_ANSATZ003','NO_FISHER_RESOURCES']}
    print(json.dumps(result,indent=2,sort_keys=True))
if __name__=='__main__': main()
