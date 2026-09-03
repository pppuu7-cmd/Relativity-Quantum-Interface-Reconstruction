#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 305.

Actual visible direct-timelike triangle normalized-cut reduction for the
weight-completed [Tr U1]_{sab} e=1,c=2 sector at frozen s=0.016.

Iteration 304 proves that all 274 HV-like hidden mu^(2r) polynomial layers are
cut-null in the explicit barred-external-state scope, assuming regular
same-parent D-dimensional coefficients near D=4. Therefore this iteration may
use the four-dimensional visible numerator coefficients reconstructed directly
at the timelike point in Iteration 295 for D_s, but NOT for a scheme-independent
full finite amplitude.

For each ordinary/raised triangle family, combine denominators with Feynman
parameters, shift l -> k-Q, and use repeated four-dimensional Minkowski
Laplacians for barred isotropic tensor moments. The one-null geometry permits
analytic continuation of every polynomial tensor term through Beta and 2F1
functions; no endpoint-divergent numerical quadrature is used.
"""
import contextlib, importlib.util, io, json, math
from pathlib import Path
import numpy as np
from scipy.special import gamma, beta, hyp2f1

HERE=Path(__file__).resolve().parent
buf=io.StringIO()
with contextlib.redirect_stdout(buf):
    spec=importlib.util.spec_from_file_location('i295',HERE/'iteration295_timelike_tru1_family_reconstruction_s0016.py')
    i295=importlib.util.module_from_spec(spec); spec.loader.exec_module(i295)
R295=i295.result
ETA=i295.ETA
EPS=np.array([.04,.02,.01,.005,.0025,.00125],float)


def mdot(a,b): return float(np.asarray(a,float)@ETA@np.asarray(b,float))

def peval(exps,c,x):
    x=np.asarray(x,float)
    return float(sum(ci*np.prod([x[k]**e[k] for k in range(4)]) for ci,e in zip(c,exps)))

def poly_dict(exps,c,tol=2e-12):
    return {tuple(e):float(x) for e,x in zip(exps,c) if abs(x)>tol}

def laplacian(poly):
    out={}
    for e,c in poly.items():
        for mu in range(4):
            if e[mu]>=2:
                ee=list(e); fac=e[mu]*(e[mu]-1); ee[mu]-=2; ee=tuple(ee)
                out[ee]=out.get(ee,0.0)+c*ETA[mu,mu]*fac
    return out

def eval_poly(poly,x):
    x=np.asarray(x,float)
    return float(sum(c*np.prod([x[k]**e[k] for k in range(4)]) for e,c in poly.items()))

def unique_points(shifts):
    pts=[]; counts=[]
    for x in shifts:
        x=np.asarray(x,float); found=False
        for i,p in enumerate(pts):
            if np.max(np.abs(x-p))<1e-10:
                counts[i]+=1; found=True; break
        if not found: pts.append(x); counts.append(1)
    return pts,counts

def tv_fit(poly,qs,seed):
    """Fit P(-Q(t,v)); Q=(1-t)[v q0+(1-v)q1]+t q2."""
    if not poly: return {(0,0):0.0},0.0
    d=max(sum(e) for e in poly)
    basis=[(m,n) for m in range(d+1) for n in range(d+1)]
    g=np.linspace(.04,.96,d+4)
    pts=np.array([(t,v) for t in g for v in g],float)
    def qtv(t,v): return (1-t)*(v*qs[0]+(1-v)*qs[1])+t*qs[2]
    X=np.array([[t**m*v**n for m,n in basis] for t,v in pts])
    y=np.array([eval_poly(poly,-qtv(t,v)) for t,v in pts])
    c=np.linalg.lstsq(X,y,rcond=None)[0]
    rng=np.random.default_rng(seed); ho=rng.uniform(.02,.98,(50,2))
    H=np.array([[t**m*v**n for m,n in basis] for t,v in ho])
    z=np.array([eval_poly(poly,-qtv(t,v)) for t,v in ho])
    rel=float(np.max(np.abs(H@c-z))/max(np.max(np.abs(z)),1.0))
    return {(m,n):float(x) for (m,n),x in zip(basis,c) if abs(x)>2e-12},rel

def order_one_null(pts,cnts):
    if len(pts)!=3: raise RuntimeError(('triangle unique points',len(pts)))
    null=None
    for i in range(3):
        for j in range(i+1,3):
            if abs(mdot(pts[j]-pts[i],pts[j]-pts[i]))<2e-10:
                null=(i,j); break
        if null is not None: break
    if null is None: raise RuntimeError('no null edge')
    i,j=null; k=next(x for x in range(3) if x not in null)
    qs=[pts[i],pts[j],pts[k]]; powers=(int(cnts[i]),int(cnts[j]),int(cnts[k]))
    s02=-mdot(qs[0]-qs[2],qs[0]-qs[2]); s12=-mdot(qs[1]-qs[2],qs[1]-qs[2])
    if min(s02,s12)<=0: raise RuntimeError(('hard edges not timelike',s02,s12))
    return qs,powers,float(s02),float(s12)

def triangle_branch(poly,qs,powers,eps,phase,seed):
    """Analytically continued one-null triangle branch in i*pi^(D/2) normalization."""
    D2=2.0-eps; A=float(sum(powers)); p0,p1,p2=map(float,powers)
    s02=-mdot(qs[0]-qs[2],qs[0]-qs[2]); s12=-mdot(qs[1]-qs[2],qs[1]-qs[2])
    total=0j; pj=poly; maxfit=0.0
    for r in range(4):
        if not pj: break
        alpha=D2+r-A
        pref=-gamma(A-D2-r)/(gamma(p0)*gamma(p1)*gamma(p2)*(4.0**r)*math.factorial(r))
        tv,rel=tv_fit(pj,qs,seed+17*r); maxfit=max(maxfit,rel)
        integ=0.0
        for (m,n),coef in tv.items():
            if abs(coef)<1e-13: continue
            tint=beta(p2+alpha+m,p0+p1+alpha)
            vint=(s12**alpha)*beta(p0+n,p1)*hyp2f1(-alpha,p0+n,p0+p1+n,1.0-s02/s12)
            integ += coef*tint*vint
        total += pref*integ*np.exp(1j*phase*np.pi*alpha)
        pj=laplacian(pj)
    return total,maxfit

def disc(poly,qs,powers,eps,seed):
    ret,fr=triangle_branch(poly,qs,powers,eps,-1,seed)
    adv,fa=triangle_branch(poly,qs,powers,eps,+1,seed)
    return (adv-ret)/(2j*np.pi),ret,adv,max(fr,fa)

def laurent(vals):
    y=np.asarray(vals,complex); z=EPS*y
    X=np.column_stack([np.ones_like(EPS),EPS,EPS**2,EPS**3,EPS**4])
    cr=np.linalg.lstsq(X,z.real,rcond=None)[0]; ci=np.linalg.lstsq(X,z.imag,rcond=None)[0]
    fit=X@cr+1j*(X@ci)
    A=cr[0]+1j*ci[0]; B=cr[1]+1j*ci[1]
    return {'pole_residue_A':[float(A.real),float(A.imag)],
            'finite_B_if_A_zero':[float(B.real),float(B.imag)],
            'eps_times_cut_fit_max_abs_residual':float(np.max(np.abs(fit-z)))}

def zero_limit(vals):
    y=np.asarray(vals,complex)
    X=np.column_stack([np.ones_like(EPS),EPS,EPS**2,EPS**3,EPS**4])
    cr=np.linalg.lstsq(X,y.real,rcond=None)[0]; ci=np.linalg.lstsq(X,y.imag,rcond=None)[0]
    fit=X@cr+1j*(X@ci)
    return cr[0]+1j*ci[0],float(np.max(np.abs(fit-y)))

# Scalar ordinary-triangle calibration against the exact Iteration-288 target.
tri_rows=[(name,row) for name,row in R295['families'].items() if row['family'] in ('ordinary_triangle','raised_triangle')]
assert len(tri_rows)==4
ordinary=next(row for _,row in tri_rows if row['family']=='ordinary_triangle')
opts,ocnts=unique_points(ordinary['canonical_denominator_shifts'])
oqs,opow,os02,os12=order_one_null(opts,ocnts)
one={(0,0,0,0):1.0}
cal=[]; cal_conj=0.0; cal_fit=0.0
for e in EPS:
    d,ret,adv,fit=disc(one,oqs,opow,float(e),30500)
    cal.append(d); cal_conj=max(cal_conj,abs(adv-np.conj(ret))); cal_fit=max(cal_fit,fit)
cal_lim,cal_lfit=zero_limit(cal)
cal_target=-np.log(min(os02,os12)/max(os02,os12))/abs(os12-os02)
cal_abs=abs(cal_lim.real-cal_target)

rows={}; max_polyfit=0.0; max_conj=0.0; max_imag=0.0
for idx,(name,row) in enumerate(sorted(tri_rows)):
    pts,cnts=unique_points(row['canonical_denominator_shifts'])
    qs,powers,s02,s12=order_one_null(pts,cnts)
    exps=[tuple(x) for x in row['monomial_exponents']]
    poly=poly_dict(exps,np.array(row['coefficients'],float))
    scans=[]; cuts=[]; fam_fit=0.0; fam_conj=0.0
    for e in EPS:
        d,ret,adv,pfit=disc(poly,qs,powers,float(e),30510+idx*100)
        cuts.append(d); fam_fit=max(fam_fit,pfit); fam_conj=max(fam_conj,abs(adv-np.conj(ret)))
        max_imag=max(max_imag,abs(d.imag))
        scans.append({'eps':float(e),'cut':[float(d.real),float(d.imag)],
                      'retarded':[float(ret.real),float(ret.imag)],
                      'advanced':[float(adv.real),float(adv.imag)]})
    max_polyfit=max(max_polyfit,fam_fit); max_conj=max(max_conj,fam_conj)
    rows[name]={'family':row['family'],'powers':list(powers),'hard_invariant_magnitudes':[s02,s12],
                'raw_scans':scans,'laurent_cut':laurent(cuts),
                'max_polynomial_parameter_fit_relative_error':fam_fit,
                'max_advanced_minus_conj_retarded_abs':fam_conj}

sum_pole=sum(r['laurent_cut']['pole_residue_A'][0] for r in rows.values())
sum_fin=sum(r['laurent_cut']['finite_B_if_A_zero'][0] for r in rows.values())
passed=(len(rows)==4 and cal_abs<3e-6 and cal_conj<2e-9 and cal_fit<2e-8 and
        max_polyfit<2e-7 and max_conj<2e-8 and max_imag<2e-8)
result={
 'iteration':305,'model_readiness_percent':24,
 'scope':'actual Iteration295 visible direct-timelike ordinary+three raised TrU1 triangle families; normalized common cut only under Iteration304 HV-like evanescent protection',
 'normalization':'loop i*pi^(D/2); D_s=(advanced-retarded)/(2*pi*i); common timelike branch; analytic-continuation-safe Beta/2F1 one-null triangle tensor reduction',
 'epsilon_points':EPS.tolist(),
 'scalar_ordinary_triangle_calibration':{'hard_invariant_magnitudes':[os02,os12],
   'raw_cut':[[float(v.real),float(v.imag)] for v in cal],
   'epsilon_to_zero_limit':[float(cal_lim.real),float(cal_lim.imag)],
   'exact_iteration288_target':float(cal_target),'abs_residual':float(cal_abs),
   'fit_max_abs_residual':float(cal_lfit),'max_branch_conjugacy_abs':float(cal_conj)},
 'triangle_families':rows,
 'max_polynomial_parameter_fit_relative_error':float(max_polyfit),
 'max_advanced_minus_conj_retarded_abs':float(max_conj),
 'max_cut_imag_abs':float(max_imag),
 'sum_four_triangle_cut_pole_residues':float(sum_pole),
 'sum_four_triangle_cut_finite_coefficients_if_pole_zero':float(sum_fin),
 'classification':('PASS_DIRECT_TIMELIKE_TRU1_VISIBLE_TRIANGLE_COMMON_CUT_LAURENT_REDUCTION'
   if passed else 'BLOCKED_DIRECT_TIMELIKE_TRU1_VISIBLE_TRIANGLE_CUT_REDUCTION'),
 'candidate_residual':False,
 'guardrails':[
   'ITERATION304_PROTECTS_THE_CUT_ONLY_NOT_FULL_FINITE_AMPLITUDE',
   'HIDDEN_274_COEFFICIENTS_ARE_NOT_ZERO_FILLED',
   'ITERATION289_WEIGHTED_B3_PROXY_TRIANGLE_COEFFICIENTS_NOT_IMPORTED',
   'NO_SOURCE_BORN_SUBTRACTION_NO_WARD_K2_COMPLETION_NO_COMPARATOR_RESIDUAL_NO_ANSATZ003'
 ],
 'next_gate':'combine validated Iteration302 bubble cut authority with these four triangle cut Laurent coefficients to freeze the complete eight-family e=1,c=2 weight-completed TrU1 normalized-cut subsector; then proceed to the next active C5 sector/source-Ward-contact prerequisites without promoting a full finite amplitude'
}
assert passed,result
print(json.dumps(result,indent=2,sort_keys=True))
