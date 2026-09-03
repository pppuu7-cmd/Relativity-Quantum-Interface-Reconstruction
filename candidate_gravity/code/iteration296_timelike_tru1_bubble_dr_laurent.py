#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 296.

Direct-timelike DR/Laurent reduction of the ordinary and raised bubble families
of the actual weight-completed cubic [Tr U1]_{sab} at frozen s=0.016.

This script imports/reconstructs the Iteration-295 timelike numerator families.
It does NOT use Iteration-287/289 weighted-kernel coefficients or poles.

For a canonical bubble
  N(l) / [(l^2)^a ((l+q)^2)^b]
we Feynman-parameterize, translate the numerator, and use repeated Minkowski
Laplacians for isotropic tensor moments in D=4-2 eps.  The common loop
normalization is i*pi^(D/2).  The retarded branch is (-s-i0), and the
normalized discontinuity is fixed as
  D_s F = (F_advanced-F_retarded)/(2*pi*i),
so D_s log_R(-s)=1 exactly.  The massless scalar bubble has nonlocal term
-log_R(-s), hence its normalized cut tends to -1; that sign is the calibration
used below.

This is a scoped prerequisite for the subsequent triangle reduction.  It is
not the full e=1,c=2 TrU1 comparator coordinate and not a Candidate residual.
"""
import importlib.util, json, math
from pathlib import Path
import numpy as np
from scipy.special import gamma

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('i295',HERE/'iteration295_timelike_tru1_family_reconstruction_s0016.py')
i295=importlib.util.module_from_spec(spec); spec.loader.exec_module(i295)
R295=i295.result
ETA=i295.ETA


def mdot(a,b): return float(np.asarray(a,float)@ETA@np.asarray(b,float))

def peval(exps,c,x):
    x=np.asarray(x,float)
    return float(sum(ci*np.prod([x[k]**e[k] for k in range(4)]) for ci,e in zip(c,exps)))

def full_exponents(deg):
    return [(a,b,c,d) for a in range(deg+1) for b in range(deg+1-a)
            for c in range(deg+1-a-b) for d in range(deg+1-a-b-c)]

def translate_fit(row,q0,seed):
    """Fit N_new(L)=N_old(L-q0) in the exact same full-coordinate basis."""
    exps=[tuple(x) for x in row['monomial_exponents']]; c=np.array(row['coefficients'],float)
    rng=np.random.default_rng(seed); n=len(exps)
    pts=rng.uniform(-.9,.9,(n+24,4)); ho=rng.uniform(-1.1,1.1,(32,4))
    X=np.array([[np.prod([p[k]**e[k] for k in range(4)]) for e in exps] for p in pts])
    y=np.array([peval(exps,c,p-np.asarray(q0,float)) for p in pts])
    cc=np.linalg.lstsq(X,y,rcond=None)[0]
    H=np.array([[np.prod([p[k]**e[k] for k in range(4)]) for e in exps] for p in ho])
    z=np.array([peval(exps,c,p-np.asarray(q0,float)) for p in ho])
    rel=float(np.max(np.abs(H@cc-z))/max(np.max(np.abs(z)),1e-30))
    return exps,cc,rel

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

def xpoly_coeff(poly,q):
    """Polynomial coefficients p_n for P(-(1-x)q)=sum_n p_n x^n."""
    if not poly: return np.zeros(1)
    deg=max(sum(e) for e in poly)
    xs=np.linspace(-.35,1.25,deg+5)
    ys=np.array([eval_poly(poly,-(1-x)*np.asarray(q,float)) for x in xs])
    pc=np.polynomial.polynomial.polyfit(xs,ys,deg)
    chk=np.max(np.abs(np.polynomial.polynomial.polyval(xs,pc)-ys))
    scale=max(np.max(np.abs(ys)),1.0)
    if chk/scale>2e-9: raise RuntimeError(('xpoly-fit',chk/scale,deg))
    return pc

def beta_fn(x,y): return gamma(x)*gamma(y)/gamma(x+y)

def bubble_branch(poly,q,a,b,eps,phase):
    """phase=-1 retarded (-s-i0), +1 advanced (-s+i0)."""
    nu=a+b; D2=2.0-eps; s=-mdot(q,q)
    if not s>0: raise RuntimeError(('not-timelike',s,q))
    Z=s*np.exp(1j*phase*np.pi)  # -s +/- i0
    total=0j; pj=poly
    for j in range(4):
        if not pj: break
        alpha=D2+j-nu
        pref=gamma(nu-D2-j)/(gamma(a)*gamma(b)*(4.0**j)*math.factorial(j))
        pc=xpoly_coeff(pj,q)
        integ=0j
        for n,coef in enumerate(pc):
            if abs(coef)>1e-13:
                integ += coef*beta_fn(a+alpha+n,b+alpha)
        total += pref*(Z**alpha)*integ
        pj=laplacian(pj)
    return total

def disc(poly,q,a,b,eps):
    ret=bubble_branch(poly,q,a,b,eps,-1)
    adv=bubble_branch(poly,q,a,b,eps,+1)
    return (adv-ret)/(2j*np.pi),ret,adv

# Exact scalar ordinary-bubble calibration in the same normalization.  Its
# nonlocal finite term is -log_R(-s), so D_s bubble -> -1.
def scalar_bubble_exact(s,eps,phase):
    Z=s*np.exp(1j*phase*np.pi)
    return gamma(eps)*gamma(1-eps)**2/gamma(2-2*eps)*(Z**(-eps))

def scalar_disc_exact(s,eps):
    return (scalar_bubble_exact(s,eps,+1)-scalar_bubble_exact(s,eps,-1))/(2j*np.pi)

EPS=np.array([.04,.02,.01,.005,.0025],float)

def laurent(vals):
    y=np.asarray(vals,complex); z=EPS*y
    X=np.column_stack([np.ones_like(EPS),EPS,EPS**2,EPS**3])
    cr=np.linalg.lstsq(X,z.real,rcond=None)[0]; ci=np.linalg.lstsq(X,z.imag,rcond=None)[0]
    A=cr[0]+1j*ci[0]; B=cr[1]+1j*ci[1]
    fit=X@cr+1j*(X@ci); err=float(np.max(np.abs(fit-z)))
    return {'pole_residue_A':[float(A.real),float(A.imag)],
            'finite_B_if_A_zero':[float(B.real),float(B.imag)],
            'eps_times_cut_fit_max_abs_residual':err}

def unique_points(shifts):
    pts=[]; counts=[]
    for x in shifts:
        x=np.asarray(x,float)
        found=False
        for i,p in enumerate(pts):
            if np.max(np.abs(x-p))<1e-10: counts[i]+=1; found=True; break
        if not found: pts.append(x); counts.append(1)
    return pts,counts

rows={}
max_translation_rel=0.0
for name,row in R295['families'].items():
    if row['family'] not in ('ordinary_bubble','raised_bubble'): continue
    pts,cnts=unique_points(row['canonical_denominator_shifts'])
    if len(pts)!=2: raise RuntimeError((name,len(pts),cnts))
    if row['family']=='raised_bubble':
        ir=cnts.index(2); io=1-ir
    else:
        ir=0; io=1
    q0=pts[ir]; q=pts[io]-q0; a=cnts[ir]; b=cnts[io]
    exps,cc,trel=translate_fit(row,q0,2960+len(rows)); max_translation_rel=max(max_translation_rel,trel)
    poly=poly_dict(exps,cc)
    scans=[]; cuts=[]; max_branch_conj=0.0
    for e in EPS:
        d,ret,adv=disc(poly,q,a,b,float(e)); cuts.append(d)
        max_branch_conj=max(max_branch_conj,abs(adv-np.conj(ret)))
        scans.append({'eps':float(e),'cut':[float(d.real),float(d.imag)],
                      'retarded':[float(ret.real),float(ret.imag)],
                      'advanced':[float(adv.real),float(adv.imag)]})
    au=laurent(cuts)
    rows[name]={'family':row['family'],'powers':[int(a),int(b)],'timelike_s':float(-mdot(q,q)),
                'translation_fit_relative_error':trel,'raw_scans':scans,'laurent_cut':au,
                'max_advanced_minus_conj_retarded_abs':float(max_branch_conj)}

cal={}
SCALAR_CUT_TARGET=-1.0
for s in (.016,.216):
    vals=[scalar_disc_exact(s,float(e)) for e in EPS]
    cal[str(s)]={'raw_cut':[[float(v.real),float(v.imag)] for v in vals],
                 'laurent':laurent(vals),
                 'limit_target':SCALAR_CUT_TARGET}
max_cal=max(abs(v['laurent']['finite_B_if_A_zero'][0]-SCALAR_CUT_TARGET) for v in cal.values())
max_imag=max(abs(x['cut'][1]) for r in rows.values() for x in r['raw_scans'])
max_pole=max(abs(r['laurent_cut']['pole_residue_A'][0]) for r in rows.values())

passed=(len(rows)==4 and max_translation_rel<2e-7 and max_cal<2e-3 and max_imag<2e-8)
cls=('PASS_DIRECT_TIMELIKE_TRU1_BUBBLE_COMMON_DR_PLUS_MINUS_I0_LAURENT_REDUCTION'
     if passed else 'BLOCKED_TIMELIKE_TRU1_BUBBLE_DR_REDUCTION_AUDIT')
result={'iteration':296,'model_readiness_percent':24,
 'scope':'actual weight-completed TrU1 e=1,c=2 ordinary+raised bubble families at timelike s=0.016 row',
 'normalization':'loop i*pi^(D/2); D_s=(advanced-retarded)/(2*pi*i); retarded argument (-s-i0); D_s log_R(-s)=1; scalar bubble D_s -> -1 because its finite nonlocal term is -log_R(-s)',
 'epsilon_points':EPS.tolist(),'scalar_bubble_calibration':cal,'bubble_families':rows,
 'max_translation_fit_relative_error':max_translation_rel,
 'max_scalar_cut_limit_abs_error':max_cal,'max_cut_imag_abs':max_imag,
 'max_abs_bubble_cut_laurent_pole_residue':max_pole,
 'classification':cls,'candidate_residual':False,
 'guardrails':['ITERATION289_WEIGHTED_KERNEL_PROXY_POLE_NOT_IMPORTED',
   'THIS_PASS_DOES_NOT_COMPLETE_TRIANGLE_SECTORS_OR_FULL_E1C2_TRU1',
   'FOUR_D_NUMERATOR_D_MEASURE_FINITE_REMAINDER_REMAINS_SCHEME_SCOPED_UNDER_ITERATION297_299',
   'NO_SOURCE_BORN_SUBTRACTION_BEFORE_MATCHED_OBSERVABLE_POLE_CLASSIFICATION'],
 'next_gate':'apply Iteration299 evanescent-sensitivity promotion rule to the validated bubble Laurent structure; same-parent finite remainder still requires D-dimensional numerator continuation or explicit scheme conversion before direct-timelike triangle completion'}
assert passed,result
print(json.dumps(result,indent=2,sort_keys=True))
