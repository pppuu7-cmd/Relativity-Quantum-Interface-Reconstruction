#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 436.

Prospectively frozen 80/120-digit closure of the exact Iteration-270 parent chain

    geometry -> nhat -> y_down -> norb -> N1

for M=POS, legs s/a/b, P0 and h=3e-5.  This is N1-only, non-promoting.
Acceptance was frozen in RESEARCH_LOG_ITERATION_436.md and
recovery/RECOVERY_DELTA_ITERATION_436.md before raw workflow authority.
"""
from __future__ import annotations
import hashlib, itertools, json, math
from pathlib import Path
import numpy as np
import mpmath as mp

ITERATION=436
H_STR='3e-5'
MP_LEVELS=(80,120)
MP_CROSS_LIMIT=mp.mpf('1e-40')
ENDPOINT_BINARY64_REPRO_LIMIT=1e-12
LEGACY_N1_PHYSICAL_REFERENCE=2e-5
MODEL_READINESS=24

root=Path(__file__).resolve().parent
src=root/'iteration270_vd_physical_b3_nonzero.py'
raw=src.read_bytes(); text=raw.decode()
source_checks={
    'geometry_present':'def geometry(amps,modes):' in text,
    'nhat_present':'def nhat(amps,modes,p):' in text,
    'y_down_present':'def y_down(amps,modes):' in text,
    'norb_formula':'def norb(amps,modes,p): return y_down(amps,modes)@nhat(amps,modes,p)' in text,
    'N1_signature':'def N1(M,x,p,h=3e-5):' in text,
    'N1_formula':'return (norb([h],m,p)-norb([-h],m,p))/(2*h)' in text,
}
if not all(source_checks.values()):
    raise SystemExit(('iteration270_source_drift',source_checks))

prefix=text.split('# A-layer certificates.')[0]
ns={'__name__':'iteration436_iteration270_prefix'}
exec(compile(prefix,str(src),'exec'),ns)
if tuple(ns['LEGS']) != ('s','a','b'):
    raise SystemExit(('leg_order_drift',ns['LEGS']))
if max(abs(float(a)-b) for a,b in zip(ns['P0'],[0.7,-0.4,0.5,0.9]))>1e-15:
    raise SystemExit(('P0_drift',ns['P0']))

ETA_mp=mp.matrix([[-1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]])

def mp_vec_from_np(v):
    return mp.matrix([mp.mpf(repr(float(x))) for x in v])

def mp_mat_from_np(a):
    return mp.matrix([[mp.mpc(repr(float(complex(a[i,j]).real)),repr(float(complex(a[i,j]).imag)))
                       for j in range(4)] for i in range(4)])

def mp_max_scaled_matrix_diff(a,b):
    z=mp.mpf('0')
    for i in range(4):
        for j in range(4):
            z=max(z,abs(a[i,j]-b[i,j])/max(mp.mpf(1),abs(a[i,j]),abs(b[i,j])))
    return z

def np_mp_max_scaled_matrix_diff(a,b):
    with mp.workdps(160):
        z=mp.mpf('0')
        for i in range(4):
            for j in range(4):
                av=mp.mpc(repr(float(complex(a[i,j]).real)),repr(float(complex(a[i,j]).imag)))
                z=max(z,abs(av-b[i,j])/max(mp.mpf(1),abs(av),abs(b[i,j])))
        return float(z)

def mp_fro_norm(a):
    return mp.sqrt(sum(abs(a[i,j])**2 for i in range(4) for j in range(4)))

def geometry_mp(amps,modes):
    g=mp.matrix(ETA_mp)
    emodes=[mp_mat_from_np(e) for _,e in modes]
    covk=[ETA_mp*mp_vec_from_np(k) for k,_ in modes]
    for av,em in zip(amps,emodes):
        g += av*em
    gi=g**-1
    dg=[mp.matrix(4,4) for _ in range(4)]
    ddg=[[mp.matrix(4,4) for _ in range(4)] for __ in range(4)]
    for mu in range(4):
        for av,em,kc in zip(amps,emodes,covk):
            dg[mu] += (mp.j*kc[mu]*av)*em
        for nu in range(4):
            for av,em,kc in zip(amps,emodes,covk):
                ddg[mu][nu] += (-kc[mu]*kc[nu]*av)*em
    dgi=[-(gi*dg[l]*gi) for l in range(4)]
    gam=[[[mp.mpc(0) for _ in range(4)] for __ in range(4)] for ___ in range(4)]
    dgam=[[[[mp.mpc(0) for _ in range(4)] for __ in range(4)] for ___ in range(4)] for ____ in range(4)]
    half=mp.mpf('0.5')
    for r,m,n in itertools.product(range(4),repeat=3):
        A=[dg[m][ss,n]+dg[n][ss,m]-dg[ss][m,n] for ss in range(4)]
        gam[r][m][n]=half*sum(gi[r,ss]*A[ss] for ss in range(4))
        for l in range(4):
            dgam[l][r][m][n]=half*sum(
                dgi[l][r,ss]*A[ss] + gi[r,ss]*(ddg[l][m][ss,n]+ddg[l][n][ss,m]-ddg[l][ss][m,n])
                for ss in range(4)
            )
    ric=mp.matrix(4,4)
    for m,n in itertools.product(range(4),repeat=2):
        z=mp.mpc(0)
        for r in range(4):
            z += dgam[r][r][m][n]-dgam[n][r][m][r]
            for l in range(4):
                z += gam[r][r][l]*gam[l][m][n]-gam[r][n][l]*gam[l][m][r]
        ric[m,n]=z
    return g,gi,dg,ddg,gam,dgam,ric

def nhat_mp(amps,modes,p_np):
    g,gi,dg,ddg,gam,dgam,ric=geometry_mp(amps,modes)
    pc=ETA_mp*mp_vec_from_np(p_np)
    out=mp.matrix(4,4); ricm=gi*ric
    for beta in range(4):
        pol=[mp.mpf(1) if a==beta else mp.mpf(0) for a in range(4)]
        lap=[mp.mpc(0) for _ in range(4)]
        for mu,nu,a in itertools.product(range(4),repeat=3):
            term=-(pc[mu]*pc[nu])*pol[a]
            term += sum(dgam[mu][a][nu][r]*pol[r] for r in range(4))
            term += sum(gam[a][nu][r]*(mp.j*pc[mu])*pol[r] for r in range(4))
            term += sum(gam[a][mu][ss]*((mp.j*pc[nu])*pol[ss]+sum(gam[ss][nu][r]*pol[r] for r in range(4))) for ss in range(4))
            term -= sum(gam[ss][mu][nu]*((mp.j*pc[ss])*pol[a]+sum(gam[a][ss][r]*pol[r] for r in range(4))) for ss in range(4))
            lap[a] += gi[mu,nu]*term
        rv=ricm*mp.matrix(pol)
        for a in range(4):
            out[a,beta]=lap[a]+rv[a]
    return out

def y_down_mp(amps,modes):
    g=mp.matrix(ETA_mp)
    for av,(_,e) in zip(amps,modes):
        g += av*mp_mat_from_np(e)
    return mp.sqrt(abs(mp.det(g)))*g

def norb_mp(amps,modes,p_np):
    return y_down_mp(amps,modes)*nhat_mp(amps,modes,p_np)

def evaluate_leg_at_precision(x,dps):
    with mp.workdps(dps):
        h=mp.mpf(H_STR); modes=[ns['POS'][x]]
        fp=norb_mp([h],modes,ns['P0'])
        fm=norb_mp([-h],modes,ns['P0'])
        n1=(fp-fm)/(2*h)
        # Diagnostic conditioning in the same high-precision realization.
        amp=mp.mpf('0')
        tiny=mp.mpf('1e-200')
        for i in range(4):
            for j in range(4):
                amp=max(amp,(abs(fp[i,j])+abs(fm[i,j]))/max(abs(fp[i,j]-fm[i,j]),tiny))
        return fp,fm,n1,amp

rows=[]
max_cross=mp.mpf('0'); max_endpoint_binary64=0.0; max_legacy_n1=0.0
all_finite=True
for x in ns['LEGS']:
    refs={}
    for dps in MP_LEVELS:
        refs[dps]=evaluate_leg_at_precision(x,dps)
    with mp.workdps(160):
        cross=mp_max_scaled_matrix_diff(refs[80][2],refs[120][2])
    max_cross=max(max_cross,cross)

    h=float(H_STR); mode=[ns['POS'][x]]
    fp64=ns['norb']([h],mode,ns['P0']); fm64=ns['norb']([-h],mode,ns['P0'])
    n164=ns['N1'](ns['POS'],x,ns['P0'],h)
    ep_plus=np_mp_max_scaled_matrix_diff(fp64,refs[120][0])
    ep_minus=np_mp_max_scaled_matrix_diff(fm64,refs[120][1])
    legacy=np_mp_max_scaled_matrix_diff(n164,refs[120][2])
    max_endpoint_binary64=max(max_endpoint_binary64,ep_plus,ep_minus)
    max_legacy_n1=max(max_legacy_n1,legacy)

    finite=bool(np.all(np.isfinite(fp64)) and np.all(np.isfinite(fm64)) and np.all(np.isfinite(n164)))
    with mp.workdps(160):
        finite=finite and all(mp.isfinite(refs[d][k][i,j]) for d in MP_LEVELS for k in (0,1,2) for i in range(4) for j in range(4))
    all_finite=all_finite and finite
    rows.append({
        'leg':x,
        'h':h,
        'mp80_vs_mp120_N1_scaled':mp.nstr(cross,30),
        'binary64_vs_mp120_endpoint_plus_scaled':ep_plus,
        'binary64_vs_mp120_endpoint_minus_scaled':ep_minus,
        'binary64_vs_mp120_N1_scaled':legacy,
        'mp120_N1_fro_norm':mp.nstr(mp_fro_norm(refs[120][2]),30),
        'mp120_max_cancellation_amplification':mp.nstr(refs[120][3],30),
        'finite':bool(finite),
    })

precision_closed=bool(max_cross<=MP_CROSS_LIMIT)
endpoint_equivalent=bool(max_endpoint_binary64<=ENDPOINT_BINARY64_REPRO_LIMIT)
legacy_reproduced=bool(max_legacy_n1<=LEGACY_N1_PHYSICAL_REFERENCE)
gate=bool(precision_closed and endpoint_equivalent and all_finite)
if gate and legacy_reproduced:
    classification='PASS_ITER270_N1_80_120_DIGIT_CLOSURE__LEGACY_REPRODUCED__NON_PROMOTING'
elif gate:
    classification='PASS_ITER270_N1_80_120_DIGIT_CLOSURE__LEGACY_DRIFT_MATERIAL__NON_PROMOTING'
else:
    classification='BLOCKED_ITER270_N1_MULTIPRECISION_CLOSURE'

result={
    'iteration':ITERATION,
    'authority_scope':'PARENT_PRECISION_CLOSURE__ITERATION270_N1_ONLY__NON_PROMOTING',
    'classification':classification,
    'scientific_gate_pass':gate,
    'model_readiness_percent':MODEL_READINESS,
    'candidate_residual':False,
    'source_path':str(src),
    'source_sha256':hashlib.sha256(raw).hexdigest(),
    'source_checks':source_checks,
    'frozen_inputs':{'M':'POS','legs':list(ns['LEGS']),'P0':[float(x) for x in ns['P0']],'h':float(H_STR)},
    'precision_levels_decimal_digits':list(MP_LEVELS),
    'thresholds':{
        'mp80_vs_mp120_N1_scaled_max':'1e-40',
        'binary64_vs_mp120_endpoint_norb_scaled_max':ENDPOINT_BINARY64_REPRO_LIMIT,
        'legacy_binary64_vs_mp120_N1_physical_reference':LEGACY_N1_PHYSICAL_REFERENCE,
    },
    'observed':{
        'max_mp80_vs_mp120_N1_scaled':mp.nstr(max_cross,30),
        'max_binary64_vs_mp120_endpoint_norb_scaled':max_endpoint_binary64,
        'max_binary64_vs_mp120_N1_scaled':max_legacy_n1,
        'legacy_N1_reproduced_within_2e-5':legacy_reproduced,
        'all_values_finite':all_finite,
    },
    'rows':rows,
    'interpretation':(
        'PASS certifies only the complete Iteration-270 N1 numerical realization at the frozen representative inputs. '
        'Endpoint binary64 reproduction validates formula/port equivalence before the ill-conditioned subtraction. '
        'The legacy-N1 comparison is classified against the unchanged 2e-5 physical reference but does not weaken any downstream gate. '
        'Q1, Asub/Acoef/A_finite, 368/370, fixed-mass F, Iteration 424 and physical D_s remain uncertified.'
    ),
    'next_gate':('if raw-valid PASS, freeze a separate Q1=-Q0(p+k)@N1@Q0(p) 80/120-digit closure using certified Q0 and N1; otherwise preserve N1 as blocked and diagnose the failed subcriterion without changing h or thresholds'),
    'guardrails':['NO_PHYSICAL_DS_VALUE','N1_ONLY','NO_THRESHOLD_WEAKENING','NO_H_CHANGE','NO_MOMENTUM_OR_POLARIZATION_CHANGE','NO_PARENT_DYNAMICS_CHANGE','NO_ZERO_FILL','NO_ANSATZ003','NO_FISHER_RESOURCES']
}
print(json.dumps(result,indent=2,sort_keys=True))
if not gate:
    raise SystemExit(2)
