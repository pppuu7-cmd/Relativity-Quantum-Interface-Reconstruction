#!/usr/bin/env python3
"""Iteration 597: full source-level nonlinear Ward evaluation on the frozen Iter596 contract.

The implementation is independent of family-by-family discontinuity bookkeeping.  It
constructs the same MSSC-001 scalar inverse kernel as a finite Fourier matrix on the
exact Iter368/588 three-mode fixture, inverts it, and evaluates the covariant Green-
function identity

    Delta G - T G - G T^T = 0,

where Delta g contains the frozen linear gauge leg plus BOTH nonlinear spectator
Lie-derivative terms and T acts on BOTH scalar endpoints.  The mixed spectator
coefficient is therefore the complete cubic Ward target.  A separate cubic
coefficient of G is cross-checked against the authoritative Iter594 13-family
assembly before Ward classification.

No Source/Born subtraction, source-to-Iter582 map, comparator quotient, ANSATZ-003,
Fisher or resource step is permitted here.
"""
from __future__ import annotations
import contextlib, hashlib, io, itertools, json, math
from pathlib import Path
import numpy as np

ITERATION=597
ROOT=Path(__file__).resolve().parents[1]
CROOT=ROOT/'candidate_gravity'/'code'
ETA=np.diag([1.,-1.,-1.,-1.])
MASS=0.7
LEGS=('s','a','b')
MODE={'a':(1,0),'b':(0,1),'s':(-1,-1)}
PROBES=[np.array([.43,-.27,.39,.21]),np.array([.61,.19,-.31,.47])]
XI_BASIS=[np.eye(4)[i] for i in range(4)]
FD_STEPS=(2e-2,1e-2,5e-3)
GRID_N=16
LAT_R=3
ANCHOR_TOL=2e-11
ASSEMBLY_MATCH_TOL=2e-5
WARD_ABS_TOL=2e-6
WARD_STEP_TOL=2e-5


def mdot(v):
    v=np.asarray(v); return v@ETA@v


def mode_add(a,b): return (a[0]+b[0],a[1]+b[1])


def phase(mode,t1,t2): return np.exp(-1j*(mode[0]*t1+mode[1]*t2))


def inherit_fixture():
    p368=CROOT/'iteration368_tru1sq_timelike_full_prepruning_routing.py'
    src=p368.read_text(); marker='# Cache expensive same-parent blocks by routed loop momentum.'
    if src.count(marker)!=1: raise RuntimeError('iteration368 setup boundary drift')
    ns={'__name__':'iteration597_parent368_fixture','__file__':str(p368)}
    with contextlib.redirect_stdout(io.StringIO()):
        exec(compile(src.split(marker,1)[0],str(p368),'exec'),ns,ns)
    if tuple(ns['LEGS'])!=LEGS: raise RuntimeError(('leg order drift',ns['LEGS']))
    M=ns['M']
    qs={x:np.asarray(M[x][0],float) for x in LEGS}
    hs={x:np.asarray(M[x][1],float) for x in LEGS}
    return qs,hs


def coeff_from_grid(vals,mode):
    # vals shape (N,N,...) and convention F(theta)=sum_r F_r exp(-i r.theta)
    N=vals.shape[0]
    out=0
    for i in range(N):
        t1=2*np.pi*i/N
        for j in range(N):
            t2=2*np.pi*j/N
            out += vals[i,j]*np.exp(1j*(mode[0]*t1+mode[1]*t2))
    return out/(N*N)


def metric_and_variation_grids(eu,ev,g,u,v,xi,hs,qs):
    N=GRID_N
    B=np.empty((N,N),complex); A=np.empty((N,N,4,4),complex)
    dB=np.empty((N,N),complex); dA=np.empty((N,N,4,4),complex)
    qg_cov=ETA@qs[g]; xi_cov=ETA@xi
    dg0=np.outer(qg_cov,xi_cov)+np.outer(xi_cov,qg_cov)

    def lie_one(x):
        r=qs[x]; h=hs[x]; r_cov=ETA@r
        xir=float(xi@r_cov)
        xih=xi@h
        hxi=h@xi
        return xir*h + np.outer(qg_cov,xih) + np.outer(hxi,qg_cov)

    dgu=lie_one(u); dgv=lie_one(v)
    mg,mu,mv=MODE[g],MODE[u],MODE[v]
    mgu=mode_add(mg,mu); mgv=mode_add(mg,mv)
    for i in range(N):
        t1=2*np.pi*i/N
        for j in range(N):
            t2=2*np.pi*j/N
            gg=ETA.astype(complex).copy()
            gg += eu*hs[u]*phase(mu,t1,t2) + ev*hs[v]*phase(mv,t1,t2)
            dgg=(dg0*phase(mg,t1,t2)
                 + eu*dgu*phase(mgu,t1,t2)
                 + ev*dgv*phase(mgv,t1,t2))
            det=np.linalg.det(gg)
            root=np.sqrt(-det)
            gi=np.linalg.inv(gg)
            B[i,j]=root; A[i,j]=root*gi
            db=0.5*root*np.trace(gi@dgg)
            dB[i,j]=db
            dA[i,j]=db*gi-root*(gi@dgg@gi)
    return A,B,dA,dB


def plain_metric_grids(eps,hs):
    N=GRID_N
    B=np.empty((N,N),complex); A=np.empty((N,N,4,4),complex)
    for i in range(N):
        t1=2*np.pi*i/N
        for j in range(N):
            t2=2*np.pi*j/N
            gg=ETA.astype(complex).copy()
            for x,e in eps.items(): gg += e*hs[x]*phase(MODE[x],t1,t2)
            root=np.sqrt(-np.linalg.det(gg)); B[i,j]=root; A[i,j]=root*np.linalg.inv(gg)
    return A,B


def lattice(p0,qs):
    inds=[(i,j) for i in range(-LAT_R,LAT_R+1) for j in range(-LAT_R,LAT_R+1)]
    pos={n:k for k,n in enumerate(inds)}
    ps={n:p0+n[0]*qs['a']+n[1]*qs['b'] for n in inds}
    return inds,pos,ps


def needed_modes(inds):
    return sorted({(a[0]-b[0],a[1]-b[1]) for a in inds for b in inds})


def build_K_from_coeffs(Ac,Bc,inds,ps):
    n=len(inds); K=np.zeros((n,n),complex)
    for ir,r in enumerate(inds):
        pp=ps[r]; ppc=ETA@pp
        for ic,c in enumerate(inds):
            p=ps[c]; pc=ETA@p; d=(r[0]-c[0],r[1]-c[1])
            K[ir,ic]=-(ppc@Ac[d]@pc)+MASS*MASS*Bc[d]
    return K


def build_T(g,xi,inds,pos,ps):
    n=len(inds); T=np.zeros((n,n),complex); sh=MODE[g]
    for c in inds:
        r=(c[0]+sh[0],c[1]+sh[1])
        if r in pos:
            T[pos[r],pos[c]]=xi@(ETA@ps[c])
    return T


def covariance_G(eu,ev,g,u,v,xi,p0,hs,qs):
    inds,pos,ps=lattice(p0,qs); modes=needed_modes(inds)
    A,B,dA,dB=metric_and_variation_grids(eu,ev,g,u,v,xi,hs,qs)
    Ac={m:coeff_from_grid(A,m) for m in modes}; Bc={m:coeff_from_grid(B,m) for m in modes}
    dAc={m:coeff_from_grid(dA,m) for m in modes}; dBc={m:coeff_from_grid(dB,m) for m in modes}
    K=build_K_from_coeffs(Ac,Bc,inds,ps); dK=build_K_from_coeffs(dAc,dBc,inds,ps)
    G=np.linalg.inv(K); dG=-G@dK@G; T=build_T(g,xi,inds,pos,ps)
    C=dG-T@G-G@T.T
    return C,inds,pos,G,K,dK


def mixed2(fun,h):
    return (fun(h,h)-fun(h,-h)-fun(-h,h)+fun(-h,-h))/(4*h*h)


def cubic_G_coeff(p0,hs,qs,h):
    inds,pos,ps=lattice(p0,qs); modes=needed_modes(inds); c=pos[(0,0)]
    total=0j
    for signs in itertools.product((-1,1),repeat=3):
        eps={x:h*s for x,s in zip(LEGS,signs)}
        A,B=plain_metric_grids(eps,hs)
        Ac={m:coeff_from_grid(A,m) for m in modes}; Bc={m:coeff_from_grid(B,m) for m in modes}
        K=build_K_from_coeffs(Ac,Bc,inds,ps); G=np.linalg.inv(K)
        total += np.prod(signs)*G[c,c]
    return total/(8*h**3)


def main():
    failures=[]
    contract=json.loads((ROOT/'candidate_gravity'/'results'/'iteration596_nonlinear_ward_contract.json').read_text())
    if contract.get('classification')!='PASS_PROSPECTIVE_FULL_NONLINEAR_WARD_CONTRACT_FREEZE_AND_ONE_LEG_REDUCTION__NON_RESIDUAL' or contract.get('failures')!=[]:
        raise SystemExit('Iter596 committed contract authority not PASS')
    r594=json.loads((ROOT/'candidate_gravity'/'results'/'iteration594_full_cubic_routed_assembly.json').read_text())
    if r594.get('classification')!='PASS_FULL_SAME_ACTION_ROUTED_CUBIC_SOURCE_ASSEMBLY_AND_PERMUTATION_SYMMETRY__NON_WARD_NON_RESIDUAL' or r594.get('failures')!=[]:
        raise SystemExit('Iter594 authority not PASS')
    qs,hs=inherit_fixture()
    closure=float(np.max(np.abs(sum((qs[x] for x in LEGS),np.zeros(4)))))
    if closure>1e-14: failures.append(f'fixture closure {closure}')

    # Mandatory one-leg reduction of the IMPLEMENTED matrix covariance identity.
    anchors=[]
    for p0 in PROBES:
        for g in LEGS:
            for ix,xi in enumerate(XI_BASIS):
                u,v=tuple(x for x in LEGS if x!=g)
                C,inds,pos,*_=covariance_G(0.0,0.0,g,u,v,xi,p0,hs,qs)
                sh=MODE[g]; c=(0,0); r=(sh[0],sh[1])
                if r not in pos: raise RuntimeError('lattice too small for anchor')
                val=C[pos[r],pos[c]]
                err=abs(val)
                anchors.append({'p0':p0.tolist(),'gauge_leg':g,'xi_basis':ix,'abs_covariance_residual':float(err)})
                if err>ANCHOR_TOL: failures.append(f'implemented one-leg covariance anchor {g}/xi{ix}/{p0.tolist()} = {err}')

    # Independent cross-check that this Fourier-matrix G reproduces Iter594 full 13-family cubic derivative.
    assembly=[]
    for ip,p0 in enumerate(PROBES):
        vals=[cubic_G_coeff(p0,hs,qs,h) for h in FD_STEPS]
        target=float(r594['probe_results'][ip]['canonical_assembly']['full_dabcG'])
        match=abs(vals[-1].real-target); imag=abs(vals[-1].imag); step=abs(vals[-1]-vals[-2])
        assembly.append({'p0':p0.tolist(),'fd_steps':list(FD_STEPS),'matrix_cubic_values_real':[float(z.real) for z in vals],
                         'matrix_cubic_values_imag':[float(z.imag) for z in vals],'iter594_target':target,
                         'last_match_abs':float(match),'last_imag_abs':float(imag),'last_step_abs':float(step)})
        if match>ASSEMBLY_MATCH_TOL: failures.append(f'Iter594 cubic assembly cross-check mismatch probe {ip}: {match}')
        if imag>ASSEMBLY_MATCH_TOL: failures.append(f'Iter594 cubic assembly cross-check imaginary probe {ip}: {imag}')
        if step>ASSEMBLY_MATCH_TOL: failures.append(f'Iter594 cubic assembly cross-check convergence probe {ip}: {step}')

    ward=[]; max_abs=0.; max_step=0.
    for p0 in PROBES:
        inds,pos,_=lattice(p0,qs); c=pos[(0,0)]
        for g in LEGS:
            u,v=tuple(x for x in LEGS if x!=g)
            for ix,xi in enumerate(XI_BASIS):
                vals=[]
                for h in FD_STEPS:
                    def f(eu,ev):
                        C,*_=covariance_G(eu,ev,g,u,v,xi,p0,hs,qs)
                        return C[c,c]
                    vals.append(mixed2(f,h))
                last=vals[-1]; step=abs(vals[-1]-vals[-2]); ab=abs(last)
                max_abs=max(max_abs,float(ab)); max_step=max(max_step,float(step))
                ward.append({'p0':p0.tolist(),'gauge_leg':g,'spectators':[u,v],'xi_basis':ix,
                             'fd_steps':list(FD_STEPS),'ward_values_real':[float(z.real) for z in vals],
                             'ward_values_imag':[float(z.imag) for z in vals],
                             'last_abs':float(ab),'last_step_abs':float(step)})
                if ab>WARD_ABS_TOL: failures.append(f'full nonlinear Ward residual {g}/xi{ix}/{p0.tolist()} = {ab}')
                if step>WARD_STEP_TOL: failures.append(f'full nonlinear Ward convergence {g}/xi{ix}/{p0.tolist()} = {step}')

    result={
      'iteration':597,'date':'2026-09-08','model_readiness_percent':24,
      'classification':'PASS_FULL_SOURCE_LEVEL_NONLINEAR_WARD_ON_FROZEN_ITER596_CONTRACT__NON_RESIDUAL' if not failures else 'FAIL_FULL_SOURCE_LEVEL_NONLINEAR_WARD_ON_FROZEN_ITER596_CONTRACT__PRESERVED_NEGATIVE_RESULT',
      'scientific_gate_pass':not failures,'failures':failures,
      'scope':'FULL_SAME_PARENT_CUBIC_GREEN_FUNCTION_WARD__NO_COMPARATOR_SUBTRACTION',
      'identity':'Delta G - T G - G T^T = 0; mixed spectator coefficient with exact Iter588 q_s+q_a+q_b=0',
      'full_family_content':'same parent K inverse; cubic derivative algebraically contains K3 + six K1/K2 + six ordered K1^3',
      'parent_authorities':['Iter594 13-family assembly','Iter596 prospectively frozen nonlinear Ward recursion'],
      'thresholds_frozen_pre_result':{'anchor_abs':ANCHOR_TOL,'assembly_match_abs':ASSEMBLY_MATCH_TOL,'ward_abs':WARD_ABS_TOL,'ward_last_step':WARD_STEP_TOL,'fd_steps':list(FD_STEPS),'grid_n':GRID_N,'lattice_radius':LAT_R},
      'fixture_closure':closure,'implemented_one_leg_anchors':anchors,'iter594_crosscheck':assembly,'ward_rows':ward,
      'observed':{'max_full_ward_abs':max_abs,'max_full_ward_last_step':max_step},
      'source_born_subtraction':'NOT_PERFORMED','source_to_iter582_map':'NOT_PERFORMED','candidate_residual':False,
      'ANSATZ_003':'FORBIDDEN','Fisher_resources':'FORBIDDEN',
      'explicit_nonclaims':['not a comparator identity','not a comparator-subtracted residual','not a novelty certificate'],
      'next_gate_if_pass':'raw-consume this artifact; if PASS, freeze/apply the full-observable source-to-Iter582/native-linked map before any Source/Born subtraction or fixed comparator quotient',
      'next_gate_if_fail':'preserve the negative Ward result; diagnose the exact failed gauge/spectator/endpoint component without weakening Iter596 or deleting source families'
    }
    out=ROOT/'results'/'iteration597_full_nonlinear_ward'; out.mkdir(parents=True,exist_ok=True)
    rp=out/'result.json'; rp.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    sha=hashlib.sha256(rp.read_bytes()).hexdigest()
    audit={'iteration':597,'result_sha256':sha,'failures':failures,
           'classification':'PASS_RAW_AUTHORITY_AUDIT_ITER597_FULL_NONLINEAR_WARD' if not failures else 'FAIL_RAW_AUTHORITY_AUDIT_ITER597_FULL_NONLINEAR_WARD'}
    (out/'authority_audit.json').write_text(json.dumps(audit,indent=2,sort_keys=True)+'\n')
    print(json.dumps(result,indent=2,sort_keys=True))
    # Scientific FAIL is preserved in artifact but workflow must finish nonzero so green is never confused with PASS.
    if failures: raise SystemExit(2)

if __name__=='__main__': main()
