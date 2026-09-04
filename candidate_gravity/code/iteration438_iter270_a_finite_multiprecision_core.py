#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 438.

80/120-digit arithmetic-core closure of exact Iteration-270 A_finite on all
26 signed finite-amplitude nodes used by Acoef for the seven nonempty leg
subsets. Non-promoting; thresholds were frozen prospectively.
"""
from __future__ import annotations
import contextlib, hashlib, io, itertools, json
from pathlib import Path
import numpy as np
import mpmath as mp

ITERATION=438
MP_LEVELS=(80,120)
MP_CROSS_LIMIT=mp.mpf('1e-40')
BINARY64_REPRO_LIMIT=1e-9
MODEL_READINESS=24

root=Path(__file__).resolve().parent
src270=root/'iteration270_vd_physical_b3_nonzero.py'
raw270=src270.read_bytes(); text270=raw270.decode()
source_checks={
 'A_finite':'def A_finite(amps,modes,p,total_shift):' in text270,
 'gamma_tensor':'def gamma_tensor(g):' in text270,
 'action_covector':'def action_covector(g,gi,ric):' in text270,
 'R_and_dR':'def R_and_dR(c,rvec,g,dg,ddg):' in text270,
 'lie_on_tensor':'def lie_on_tensor(c,rvec,T,dT):' in text270,
 'Acoef':'def Acoef(M,legs,p,h):' in text270,
 'Asub_steps':'def Asub(M,legs,p,h1=1e-4,h2=5e-4,h3=1e-3):' in text270,
}
if not all(source_checks.values()): raise SystemExit(('iteration270_source_drift',source_checks))

# Reuse the raw-valid Iteration-436 parent arbitrary-precision geometry/norb core.
src436=root/'iteration436_iter270_n1_multiprecision_closure.py'; t436=src436.read_text(); marker='rows=[]'
if t436.count(marker)!=1: raise SystemExit(('iteration436_boundary_drift',t436.count(marker)))
P={'__name__':'iteration438_parent436_prefix','__file__':str(src436)}
with contextlib.redirect_stdout(io.StringIO()): exec(compile(t436.split(marker,1)[0],str(src436),'exec'),P,P)
base=P['ns']; geometry_mp=P['geometry_mp']; mp_mat_from_np=P['mp_mat_from_np']; mp_vec_from_np=P['mp_vec_from_np']; ETA_mp=P['ETA_mp']
mp_max_scaled_matrix_diff=P['mp_max_scaled_matrix_diff']; np_mp_max_scaled_matrix_diff=P['np_mp_max_scaled_matrix_diff']; mp_fro_norm=P['mp_fro_norm']

# Bind prerequisites fail-closed.
resdir=root.parent/'results'
s436=json.loads((resdir/'iteration436_n1_multiprecision_closure_summary.json').read_text())
s437=json.loads((resdir/'iteration437_q1_multiprecision_closure_summary.json').read_text())
if not (s436.get('scientific_gate_pass') is True and s437.get('scientific_gate_pass') is True):
    raise SystemExit('precision_prerequisite_not_passed')


def symdelta(mu,nu,r,s):
    return mp.mpf('0.5')*((1 if (mu==r and nu==s) else 0)+(1 if (mu==s and nu==r) else 0))


def gamma_tensor_mp(g):
    gi=g**-1; T={}; c1=mp.mpf('-1'); c2=mp.mpf('0.25'); c3=mp.mpf('0.25'); c4=mp.mpf('-0.125')
    def Pfun(mu,nu,al,be): return mp.mpf('0.5')*(gi[mu,al]*gi[nu,be]+gi[mu,be]*gi[nu,al])
    for r,s,mu,nu,al,be in itertools.product(range(4),repeat=6):
        S=mp.mpf('0.25')*(symdelta(mu,al,r,s)*gi[nu,be]+symdelta(nu,al,r,s)*gi[mu,be]+symdelta(mu,be,r,s)*gi[nu,al]+symdelta(nu,be,r,s)*gi[mu,al])
        T[(r,s,mu,nu,al,be)]=c1*S+c2*(symdelta(mu,nu,r,s)*gi[al,be]+symdelta(al,be,r,s)*gi[mu,nu])+c3*Pfun(mu,nu,al,be)*g[r,s]+c4*gi[mu,nu]*gi[al,be]*g[r,s]
    return T


def action_covector_mp(g,gi,ric):
    Rsc=sum(gi[i,j]*ric[i,j] for i in range(4) for j in range(4))
    Ein=ric-mp.mpf('0.5')*g*Rsc
    return mp.sqrt(abs(mp.det(g)))*(gi*Ein*gi)


def R_and_dR_mp(c,rvec,g,dg,ddg):
    rc=ETA_mp*rvec; R=mp.matrix(4,4); dR=[mp.matrix(4,4) for _ in range(4)]
    for mu,nu in itertools.product(range(4),repeat=2):
        R[mu,nu]=sum(c[rho]*dg[rho][mu,nu] for rho in range(4))+mp.j*rc[mu]*sum(g[rho,nu]*c[rho] for rho in range(4))+mp.j*rc[nu]*sum(g[mu,rho]*c[rho] for rho in range(4))
    for lam,mu,nu in itertools.product(range(4),repeat=3):
        dR[lam][mu,nu]=mp.j*rc[lam]*R[mu,nu]+sum(c[rho]*ddg[lam][rho][mu,nu] for rho in range(4))+mp.j*rc[mu]*sum(dg[lam][rho,nu]*c[rho] for rho in range(4))+mp.j*rc[nu]*sum(dg[lam][mu,rho]*c[rho] for rho in range(4))
    return R,dR


def lie_on_tensor_mp(c,rvec,T,dT):
    rc=ETA_mp*rvec; out=mp.matrix(4,4)
    for mu,nu in itertools.product(range(4),repeat=2):
        out[mu,nu]=sum(c[rho]*dT[rho][mu,nu] for rho in range(4))+mp.j*rc[mu]*sum(T[rho,nu]*c[rho] for rho in range(4))+mp.j*rc[nu]*sum(T[mu,rho]*c[rho] for rho in range(4))
    return out


def A_finite_mp(amps,modes,p_np,total_shift_np):
    g,gi,dg,ddg,gam,dgam,ric=geometry_mp(amps,modes)
    E=action_covector_mp(g,gi,ric); GT=gamma_tensor_mp(g)
    rR=mp_vec_from_np(p_np); rL=-(mp_vec_from_np(p_np)+mp_vec_from_np(total_shift_np))
    eye=[]
    for a in range(4):
        c=mp.matrix(4,1); c[a]=1; eye.append(c)
    RL=[]; dRL=[]; RR=[]
    for a in range(4):
        rl,drl=R_and_dR_mp(eye[a],rL,g,dg,ddg); rr,_=R_and_dR_mp(eye[a],rR,g,dg,ddg)
        RL.append(rl); dRL.append(drl); RR.append(rr)
    A=mp.matrix(4,4)
    for al,be in itertools.product(range(4),repeat=2):
        directional=lie_on_tensor_mp(eye[be],rR,RL[al],dRL[al])
        total=mp.mpc(0)
        for r,s in itertools.product(range(4),repeat=2):
            conn=mp.mpc(0)
            for mu,nu,aa,bb in itertools.product(range(4),repeat=4):
                conn += GT[(r,s,mu,nu,aa,bb)]*RL[al][mu,nu]*RR[be][aa,bb]
            total += (directional[r,s]+conn)*E[r,s]
        A[al,be]=total
    return A

subsets=[('s',),('a',),('b',),('s','a'),('s','b'),('a','b'),('s','a','b')]
hstr={1:'1e-4',2:'5e-4',3:'1e-3'}
rows=[]; max_cross=mp.mpf('0'); max_legacy=0.0; all_finite=True
for legs in subsets:
    modes=[base['POS'][x] for x in legs]
    total_shift=sum((np.asarray(base['POS'][x][0],float) for x in legs),np.zeros(4))
    hs=hstr[len(legs)]
    for sig in itertools.product((-1,1),repeat=len(legs)):
        refs={}
        for dps in MP_LEVELS:
            with mp.workdps(dps):
                h=mp.mpf(hs); refs[dps]=A_finite_mp([mp.mpf(s)*h for s in sig],modes,base['P0'],total_shift)
        with mp.workdps(160): cross=mp_max_scaled_matrix_diff(refs[80],refs[120])
        h64=float(hs); a64=base['A_finite']([float(s)*h64 for s in sig],modes,base['P0'],total_shift)
        legacy=np_mp_max_scaled_matrix_diff(a64,refs[120])
        finite=bool(np.all(np.isfinite(a64))) and all(mp.isfinite(refs[d][i,j]) for d in MP_LEVELS for i in range(4) for j in range(4))
        max_cross=max(max_cross,cross); max_legacy=max(max_legacy,legacy); all_finite=all_finite and finite
        rows.append({'legs':list(legs),'signs':list(sig),'h':h64,'mp80_vs_mp120_A_finite_scaled':mp.nstr(cross,30),'binary64_vs_mp120_A_finite_scaled':legacy,'mp120_fro_norm':mp.nstr(mp_fro_norm(refs[120]),30),'finite':bool(finite)})

node_count=len(rows); subset_count=len(subsets)
gate=bool(max_cross<=MP_CROSS_LIMIT and max_legacy<=BINARY64_REPRO_LIMIT and all_finite and node_count==26 and subset_count==7)
classification='PASS_ITER270_A_FINITE_80_120_DIGIT_ARITHMETIC_CORE__NON_PROMOTING' if gate else 'BLOCKED_ITER270_A_FINITE_MULTIPRECISION_CORE'
result={
 'iteration':ITERATION,'model_readiness_percent':MODEL_READINESS,'candidate_residual':False,
 'authority_scope':'PARENT_PRECISION_CLOSURE__ITERATION270_A_FINITE_CORE_ONLY__NON_PROMOTING',
 'classification':classification,'scientific_gate_pass':gate,
 'source_path':str(src270),'source_sha256':hashlib.sha256(raw270).hexdigest(),'source_checks':source_checks,
 'prerequisites':{'iteration436':s436.get('classification'),'iteration437':s437.get('classification')},
 'frozen_inputs':{'M':'POS','P0':[float(x) for x in base['P0']],'subsets':[list(x) for x in subsets],'h_by_subset_size':{'1':1e-4,'2':5e-4,'3':1e-3},'node_count':node_count,'subset_count':subset_count},
 'precision_levels_decimal_digits':list(MP_LEVELS),
 'thresholds':{'mp80_vs_mp120_A_finite_scaled_max':'1e-40','binary64_vs_mp120_A_finite_scaled_max':BINARY64_REPRO_LIMIT},
 'observed':{'max_mp80_vs_mp120_A_finite_scaled':mp.nstr(max_cross,30),'max_binary64_vs_mp120_A_finite_scaled':max_legacy,'all_values_finite':all_finite,'node_count':node_count,'subset_count':subset_count},
 'rows':rows,
 'interpretation':'PASS certifies the exact A_finite arithmetic core at every signed finite-amplitude node used by the frozen Iteration-270 Acoef/Asub stencils. It deliberately does not certify the finite-difference Acoef/Asub derivative or truncation error.',
 'next_gate':'if raw-valid PASS, compute Acoef/Asub from the same 80/120-digit A_finite node values at unchanged h1/h2/h3 and separately classify arithmetic closure versus finite-difference truncation/step stability',
 'guardrails':['NO_PHYSICAL_DS_VALUE','A_FINITE_CORE_ONLY','NO_THRESHOLD_WEAKENING','NO_AMPLITUDE_STEP_CHANGE','NO_PARENT_DYNAMICS_CHANGE','NO_ZERO_FILL','NO_ANSATZ003','NO_FISHER_RESOURCES']
}
print(json.dumps(result,indent=2,sort_keys=True))
if not gate: raise SystemExit(2)
