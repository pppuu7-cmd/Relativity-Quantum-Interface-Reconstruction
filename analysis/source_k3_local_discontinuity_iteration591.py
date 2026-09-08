#!/usr/bin/env python3
"""Iteration591: local MSSC-001 K3 hard-channel discontinuity origin audit.

Before any rest-frame q0=sqrt(s) parametrization, the exact mixed third
coefficient of the local MSSC scalar inverse kernel has form
  K3=-p'_cov A3(h1,h2,h3) p_cov + m^2 b3(h1,h2,h3).
A3,b3 contain no channel propagator, loop integral, logarithm, threshold square
root or nonlocal form factor.  Thus K3 may be nonzero as a contact while its
ordinary finite hard-channel Disc_s is zero.  This closes K3 origin only; K1^3
remains a separate Iter590 completeness question.
"""
from __future__ import annotations
import contextlib, hashlib, io, itertools, json, math
from pathlib import Path
import numpy as np

ROOT=Path(__file__).resolve().parents[1]
CROOT=ROOT/'candidate_gravity'/'code'
ETA=np.diag([1.,-1.,-1.,-1.])
CAND_ETA=np.diag([-1.,1.,1.,1.])
MASS=0.7
LEGS=('s','a','b')
# Inherited prospectively from the Iter590 fixture K3 mixed-derivative gate.
TOL=2e-7


def prod(A,B,op=lambda a,b:a*b):
    C={}
    for ma,a in A.items():
        for mb,b in B.items():
            if ma&mb: continue
            m=ma|mb; v=op(a,b)
            C[m]=C[m]+v if m in C else v
    return C


def matrix_inv_series(g,n):
    gi={0:ETA.copy()}
    for bits in range(1,n+1):
        for m in range(1,1<<n):
            if m.bit_count()!=bits: continue
            acc=np.zeros((4,4))
            for a in (1,2,4):
                if m&a and a in g: acc += g[a]@gi[m^a]
            gi[m]=-ETA@acc
    return gi


def determinant_series(g):
    D={}
    for perm in itertools.permutations(range(4)):
        inv=sum(perm[i]>perm[j] for i in range(4) for j in range(i+1,4)); sgn=(-1)**inv
        T={0:1.0}
        for i,j in enumerate(perm):
            T=prod(T,{m:float(v[i,j]) for m,v in g.items()})
        for m,v in T.items(): D[m]=D.get(m,0.0)+sgn*v
    return D


def subsets(mask):
    s=mask
    while True:
        yield s
        if s==0: break
        s=(s-1)&mask


def sqrt_series(Y,n):
    S={0:float(np.sqrt(Y[0]))}
    for bits in range(1,n+1):
        for m in range(1,1<<n):
            if m.bit_count()!=bits: continue
            rest=0.0
            for a in subsets(m):
                b=m^a
                if a and b and a in S and b in S: rest += S[a]*S[b]
            S[m]=(Y.get(m,0.0)-rest)/(2*S[0])
    return S


def exact_mixed_coeff(hs):
    g={0:ETA.copy()}
    for i,h in enumerate(hs): g[1<<i]=np.asarray(h,float)
    gi=matrix_inv_series(g,3)
    sqrtg=sqrt_series({m:-v for m,v in determinant_series(g).items()},3)
    dens=prod(sqrtg,gi,op=lambda a,b:a*b)
    return np.asarray(dens[7],float),float(sqrtg[7])


def K3_formal(A3,b3,pp,p):
    return -float((ETA@pp)@A3@(ETA@p))+MASS*MASS*b3


def exact_K(eps,hs,pp,p):
    g=ETA.copy()
    for e,h in zip(eps,hs): g += float(e)*h
    det=float(np.linalg.det(g))
    if det>=0: raise RuntimeError('left Lorentzian determinant branch')
    s=math.sqrt(-det); gi=np.linalg.inv(g)
    return -float((ETA@pp)@(s*gi)@(ETA@p))+MASS*MASS*s


def mixed3_fd(hs,pp,p,h):
    z=0.0
    for signs in itertools.product((-1,1),repeat=3):
        z += float(np.prod(signs))*exact_K([h*x for x in signs],hs,pp,p)
    return z/(8*h**3)


def main():
    failures=[]
    auth=json.loads((ROOT/'candidate_gravity/results/iteration590_source_cubic_completeness_raw_consumption.json').read_text())
    if auth.get('classification')!='PASS_RAW_CONSUMED_CUBIC_SOURCE_RESPONSE_COMPLETENESS__K1K2_ONLY_SCOPED_NOT_FULL' or auth.get('scientific_gate_pass') is not True:
        raise SystemExit('iteration590 authority missing')
    if auth.get('workflow',{}).get('result_sha256')!='5ba0e9fc88b68b13d08d406829ebf4cc30e8ae85d8d92816f282d105a89d4d63':
        raise SystemExit('iteration590 result authority drift')

    p368=CROOT/'iteration368_tru1sq_timelike_full_prepruning_routing.py'
    src=p368.read_text(); marker='# Cache expensive same-parent blocks by routed loop momentum.'
    if src.count(marker)!=1: raise SystemExit('iteration368 setup boundary drift')
    ns={'__name__':'iteration591_parent368_fixture','__file__':str(p368)}
    with contextlib.redirect_stdout(io.StringIO()): exec(compile(src.split(marker,1)[0],str(p368),'exec'),ns,ns)
    if tuple(ns['LEGS'])!=LEGS: raise SystemExit(('leg order drift',ns['LEGS']))
    M=ns['M']; qs=[np.asarray(M[x][0],float) for x in LEGS]; hs=[np.asarray(M[x][1],float) for x in LEGS]
    if np.max(np.abs(sum(qs,np.zeros(4))))>2e-15: raise SystemExit('fixture momentum closure drift')

    A3,b3=exact_mixed_coeff(hs)
    if not np.all(np.isfinite(A3)) or not math.isfinite(b3): failures.append('nonfinite formal K3 coefficient')

    rng=np.random.default_rng(591218); regress=[]; maxerr=0.0
    for i in range(8):
        p=rng.normal(size=4); pp=rng.normal(size=4)
        formal=K3_formal(A3,b3,pp,p)
        vals=[mixed3_fd(hs,pp,p,h) for h in (1e-2,5e-3,2.5e-3)]
        err=abs(vals[-1]-formal); maxerr=max(maxerr,err)
        regress.append({'probe':i,'formal_K3':formal,'fd_steps':[1e-2,5e-3,2.5e-3],'fd_values':vals,'fine_abs_error':err})
    if maxerr>TOL: failures.append(f'formal-vs-fd K3 mismatch {maxerr}')

    channel=[]; c0=MASS*MASS*b3
    for i,name in enumerate(LEGS):
        q=qs[i]
        candidate_q2=float(q@CAND_ETA@q)
        source_s=-candidate_q2
        if source_s<=0: failures.append(f'{name}: expected timelike source s>0, got {source_s}')
        p=-0.5*q; kval=K3_formal(A3,b3,p,p)
        c1=(kval-c0)/source_s
        channel.append({'singleton':name,'candidate_q2':candidate_q2,'source_s':source_s,
                        'K3_contact_value':kval,'affine_c0':c0,'affine_c1_for_fixed_direction':c1,
                        'analytic_origin':'LOCAL_POLYNOMIAL__NO_CHANNEL_DENOMINATOR_OR_NONANALYTIC_KERNEL',
                        'hard_channel_D_s_K3':0.0})

    result={
      'iteration':591,'date':'2026-09-08','model_readiness_percent':24,
      'classification':'PASS_MSSC001_LOCAL_K3_HARD_CHANNEL_DISC_ZERO__NON_RESIDUAL' if not failures else 'FAIL_MSSC001_LOCAL_K3_ORIGIN_AUDIT',
      'scientific_gate_pass':not failures,'failures':failures,
      'parent_authority':'Iter590 cubic completeness + Iter218/583 MSSC-001 local scalar action',
      'formal_K3':{
        'form':'K3=-p_prime_cov A3(h1,h2,h3) p_cov + m^2 b3(h1,h2,h3)',
        'A3':A3.tolist(),'b3':b3,'momentum_degree':2,
        'internal_propagators':0,'loop_integrals':0,'logs':0,'nonlocal_form_factors':0,'channel_denominators':0,
        'branch_cut_origin':'NONE_FOR_ORDINARY_FINITE_HARD_CHANNEL'
      },
      'formal_vs_exact_regression':{'probe_count':len(regress),'max_fine_abs_error':maxerr,'tolerance':TOL,
                                    'tolerance_origin':'INHERITED_FROM_ITER590_K3_MIXED_DERIVATIVE_CONTROL','records':regress},
      'fixture_channel_origin':channel,
      'discontinuity_rule':'D_s F=Disc_s F/(2*pi*i); a local polynomial contact has Disc_s=0 across an ordinary finite hard-channel branch cut',
      'key_result':'K3 is nonzero as a local contact but carries no hard-channel branch-cut discontinuity: D_s K3=0. This closes only K3 origin; K1^3 remains open.',
      'K3_under_hard_channel_D_s':'PASS_LOCAL_ANALYTIC__DISC_ZERO',
      'K1cubed_under_frozen_linked_T_cut':'OPEN__UNCHANGED_FROM_ITER590',
      'K1K2_only_as_complete_discontinuity_source_block':'NOT_AUTHORIZED_UNTIL_K1CUBED_ORIGIN_CLOSES',
      'source_born_subtraction':'NOT_PERFORMED','candidate_residual':False,'ANSATZ_003':'FORBIDDEN','Fisher_resources':'FORBIDDEN',
      'next_gate_if_pass':'classify K1^3 under the frozen split-invariant Y=(K2,S_soft2_full)/linked T_cut protocol; do not discard it solely as reducible/non-1PI and do not import Born subtraction from unrelated on-shell cuts.'
    }
    out=ROOT/'results/iteration591_source_k3_local_discontinuity'; out.mkdir(parents=True,exist_ok=True)
    rp=out/'result.json'; rp.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    sha=hashlib.sha256(rp.read_bytes()).hexdigest()
    audit={'iteration':591,'result_sha256':sha,'failures':failures,
           'classification':'PASS_RAW_AUTHORITY_AUDIT_ITER591_K3_DISC_ZERO' if not failures else 'FAIL_RAW_AUTHORITY_AUDIT_ITER591_K3_DISC_ZERO'}
    (out/'authority_audit.json').write_text(json.dumps(audit,indent=2,sort_keys=True)+'\n')
    print(json.dumps(result,indent=2,sort_keys=True))
    if failures: raise SystemExit(2)

if __name__=='__main__': main()
