#!/usr/bin/env python3
"""Post-parent continuous precision certificate frozen by Iteration 444.

This stage consumes the already-authorized parent matrix values from the exact
Iteration-368 fixture, then performs *all seven* post-parent matrix products and
final trace continuously at 80 and 120 decimal digits.  It covers all 126
representative A/B/cyclic-shift probe contractions (21 classes x 2 probes x 3
orientations).  It is deliberately unnumbered until raw consumption.
"""
from __future__ import annotations
import contextlib, hashlib, io, json
from pathlib import Path
import mpmath as mp
import numpy as np

ROOT=Path(__file__).resolve().parents[2]
P368=ROOT/'candidate_gravity/code/iteration368_tru1sq_timelike_full_prepruning_routing.py'
ns={'__name__':'rqir_iter368_stage','__file__':str(P368)}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(P368.read_text(),str(P368),'exec'),ns,ns)

LEGS=ns['LEGS']; M=ns['M']; PROBES=ns['PROBES']; Q0=ns['Q0']; Q1=ns['Q1']; Asub=ns['Asub']
Y0=ns['Y0']; y1=ns['y1']; ksum=ns['ksum']; second_specs=ns['second_specs']
TH=mp.mpf('1e-30')


def mp_matrix_from_parent(a):
    a=np.asarray(a)
    return mp.matrix([[mp.mpc(repr(float(np.real(a[i,j]))),repr(float(np.imag(a[i,j])))) for j in range(a.shape[1])] for i in range(a.shape[0])])


def first_factors(x,p):
    q=M[x][0]; A1=Asub(M,(x,),p,h1=1e-4)
    return [Q0(p+q),A1,Q0(p),Y0]


def second_factors(pair,spec,p):
    pair=tuple(pair); site=spec['extra_site']
    if site=='V2':
        q=ksum(pair); A2=Asub(M,pair,p,h2=5e-4)
        return [Q0(p+q),A2,Q0(p),Y0]
    vleg=spec['V2_legs'][0]; dleg=spec['extra_local_legs'][0]
    qv=M[vleg][0]; qd=M[dleg][0]
    if site=='N_L':
        A1=Asub(M,(vleg,),p,h1=1e-4)
        return [Q1(M,dleg,p+qv),A1,Q0(p),Y0]
    if site=='N_R':
        A1=Asub(M,(vleg,),p+qd,h1=1e-4)
        return [Q0(p+qd+qv),A1,Q1(M,dleg,p),Y0]
    if site=='Y':
        A1=Asub(M,(vleg,),p+qd,h1=1e-4)
        return [Q0(p+qd+qv),A1,Q0(p+qd),y1(dleg)]
    raise ValueError(site)


def contract(f1,f2,dps):
    with mp.workdps(dps):
        mats=[mp_matrix_from_parent(x) for x in (list(f1)+list(f2))]
        acc=mats[0]
        for m in mats[1:]: acc=acc*m
        z=sum(acc[i,i] for i in range(acc.rows))
        # serialization while requested precision is active
        return (mp.nstr(mp.re(z),dps),mp.nstr(mp.im(z),dps))


def binary_contract(f1,f2):
    mats=[np.asarray(x,dtype=complex) for x in (list(f1)+list(f2))]
    acc=mats[0]
    for m in mats[1:]: acc=acc@m
    return np.trace(acc)


def eval_one(f1,f2,label,meta):
    z80s=contract(f1,f2,80); z120s=contract(f1,f2,120)
    with mp.workdps(140):
        z80=mp.mpc(mp.mpf(z80s[0]),mp.mpf(z80s[1])); z120=mp.mpc(mp.mpf(z120s[0]),mp.mpf(z120s[1]))
        scale=max(abs(z120),mp.mpf('1e-30'))
        cross=abs(z80-z120)/scale
        zb=binary_contract(f1,f2)
        zbd=mp.mpc(repr(float(np.real(zb))),repr(float(np.imag(zb))))
        bdiag=abs(zbd-z120)/scale
        finite=bool(mp.isfinite(z120.real) and mp.isfinite(z120.imag) and np.isfinite(zb.real) and np.isfinite(zb.imag))
        return {**meta,'orientation':label,'mp80_re':z80s[0],'mp80_im':z80s[1],'mp120_re':z120s[0],'mp120_im':z120s[1],
                'scaled_mp80_vs_mp120':mp.nstr(cross,30),'scaled_binary64_vs_mp120_diagnostic':mp.nstr(bdiag,30),'finite':finite}


def main():
    rows=[]
    for singleton in LEGS:
        pair=tuple(x for x in LEGS if x!=singleton); qs=M[singleton][0]; qp=ksum(pair)
        for spec_index,spec in enumerate(second_specs(pair)):
            for probe_index,p0 in enumerate(PROBES):
                p=np.asarray(p0,float)
                meta={'singleton_leg':singleton,'pair_legs':list(pair),'spec_index':spec_index,'extra_site':spec['extra_site'],'probe_index':probe_index}
                # Exact Iteration-368 orientations, retaining parent values before any post-parent product.
                rows.append(eval_one(first_factors(singleton,p+qp),second_factors(pair,spec,p),'A',meta))
                rows.append(eval_one(second_factors(pair,spec,p+qs),first_factors(singleton,p),'B',meta))
                rows.append(eval_one(first_factors(singleton,p),second_factors(pair,spec,p+qs),'A_SHIFT',meta))
    with mp.workdps(140):
        mx=max(mp.mpf(r['scaled_mp80_vs_mp120']) for r in rows)
        bmx=max(mp.mpf(r['scaled_binary64_vs_mp120_diagnostic']) for r in rows)
    finite=all(r['finite'] for r in rows)
    passed=bool(len(rows)==126 and finite and mx<=TH)
    result={
      'stage':'POSTPARENT_CONTRACTION_PRECISION_STAGE__POST_ITER445__UNNUMBERED_UNTIL_RAW_CONSUME',
      'authority_scope':'ITER444_FROZEN_LAYER368_370_POSTPARENT_7_MATMUL_PLUS_TRACE_PRECISION__NON_PROMOTING',
      'classification':'PASS_POSTPARENT_CONTINUOUS_MP80_MP120_CONTRACTION_CERTIFICATE__NON_PROMOTING' if passed else 'BLOCKED_POSTPARENT_CONTINUOUS_PRECISION_CONTRACTION_CERTIFICATE__NON_PROMOTING',
      'scientific_gate_pass':passed,'promotes_physical_coordinate':False,
      'frozen':{'precision_digits':[80,120],'post_parent_matmuls_per_contraction':7,'trace_operations_per_contraction':1,'representative_contraction_count':126,
                'orientations':['A','B','A_SHIFT'],'classes':21,'probes_per_class':2,'same_parent_values':True,'same_routing_and_orientation':True},
      'thresholds':{'scaled_mp80_vs_mp120_max':'1e-30','required_contraction_count':126,'all_finite':True},
      'observed':{'scaled_mp80_vs_mp120_max':mp.nstr(mx,30),'scaled_binary64_vs_mp120_max_diagnostic':mp.nstr(bmx,30),'contraction_count':len(rows),'all_finite':finite},
      'rows':rows,
      'source_sha256':hashlib.sha256(P368.read_bytes()).hexdigest(),
      'guardrails':['NO_OUTER_MP_AROUND_BINARY64_MATMUL_OR_TRACE','PARENT_VALUES_FROZEN_BEFORE_POSTPARENT_PRODUCTS','NO_THRESHOLD_WEAKENING','NO_ROUTING_CHANGE','NO_NUMERATOR_CHANGE','NO_ZERO_FILL','NO_PHYSICAL_DS_PROMOTION'],
      'next_gate_if_pass':'advance continuous precision provenance to the next frozen 379/374 layer before 407 and Iteration 424 physical reevaluation',
      'next_gate_if_blocked':'localize failing contraction without changing parent values, routing, precision threshold, or physics',
      'MODEL_READINESS':'24%','readiness_change_pp':0}
    print(json.dumps(result,indent=2,sort_keys=True))
    if not passed: raise SystemExit(2)

if __name__=='__main__': main()
