#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 380.

Analytic-azimuth reduction of the sole determinant triangle q^2=-1 channel that
remained convergence-BLOCKED after Iterations 333--335.

No parent, numerator, routing, cut surface, causal prescription or scientific
nonzero/convergence threshold is changed.  For the cubic triangle family all
three insertions are first-background-order insertions of a second-order
operator, so the stripped triangle numerator is expected to be polynomial of
loop momentum degree <=6.  On the exact two-particle cut k is affine in the
unit vector n.  Aligning the third spatial basis vector with A_perp makes the
uncut denominator exactly c+a z.  The azimuthally averaged numerator must then
be a polynomial Nbar(z) of degree <=6.  This claim is tested on held-out z nodes
and independent azimuth phases before using the analytic 1D moments

    J_n = int_{-1}^1 z^n/(c+a z) dz.

A direct sparse product-quadrature evaluation of the original physical
integrand is retained as an independent cross-check at the unchanged 2e-5
scaled convergence threshold.  Unsupported remains BLOCKED.
"""
from __future__ import annotations
import contextlib, io, json, math
from pathlib import Path
import numpy as np
from numpy.polynomial import Chebyshev, Polynomial

ITERATION=380
ROOT=Path(__file__).resolve().parent
src=(ROOT/'iteration333_det_direct_timelike_discontinuity_family_reduction.py').read_text()
prefix=src.split('bubble_results=[]',1)
if len(prefix)!=2: raise RuntimeError('iteration333_boundary_drift')
ns={'__name__':'iteration380_parent333','__file__':str(ROOT/'iteration333_det_direct_timelike_discontinuity_family_reduction.py')}
with contextlib.redirect_stdout(io.StringIO()): exec(compile(prefix[0],str(ROOT/'iteration333_det_direct_timelike_discontinuity_family_reduction.py'),'exec'),ns,ns)
triangle_groups=ns['triangle_groups']; family_num=ns['family_num']; rest_basis=ns['rest_basis']; mdot=ns['mdot']; denom=ns['denom']
if len(triangle_groups)!=1: raise RuntimeError(('triangle_family_count',len(triangle_groups)))
rep,group=next(iter(triangle_groups.items()))
# Triangle authority must be the cubic H1/N1 topology; fail closed if route structure drifts.
if not all(len(r['seq'])==3 and all(sum(a)==1 for a in r['seq']) for r in group):
    raise RuntimeError('triangle_not_three_first_order_insertions')
shifts=[np.asarray(s,float)/100.0 for s in rep]
pair=None
for i,j in ((0,1),(0,2),(1,2)):
    q2=mdot(shifts[j]-shifts[i],shifts[j]-shifts[i])
    if abs(q2+1.0)<1e-12:
        pair=(i,j,({0,1,2}-{i,j}).pop(),q2); break
if pair is None: raise RuntimeError('q2_minus1_channel_not_found')
i,j,kidx,q2=pair
Q=shifts[j]-shifts[i]; M,u,old_basis=rest_basis(Q); sk=shifts[kidx]
R=sk-shifts[i]; A=R-0.5*Q; Aperp=A+mdot(A,u)*u
aperp2=mdot(Aperp,Aperp)
if aperp2<=1e-14: raise RuntimeError('degenerate_Aperp')
e3=Aperp/math.sqrt(aperp2)
# Complete an orthonormal Q-perpendicular basis with e3 fixed.
basis12=[]
for v0 in old_basis:
    v=v0-mdot(v0,e3)*e3
    for e in basis12: v=v-mdot(v,e)*e
    n2=mdot(v,v)
    if n2>1e-12: basis12.append(v/math.sqrt(n2))
    if len(basis12)==2: break
if len(basis12)!=2: raise RuntimeError('aligned_basis_failure')
e1,e2=basis12; basis=[e1,e2,e3]
gram=np.array([[mdot(x,y) for y in basis] for x in basis])
if np.max(np.abs(gram-np.eye(3)))>2e-12: raise RuntimeError(('bad_aligned_gram',gram))

const=mdot(A,A)+M*M/4.0
amp=M*math.sqrt(aperp2)
dmin=const-amp; dmax=const+amp
if not (dmin>2e-9 or dmax<-2e-9): raise RuntimeError(('third_denominator_not_bounded',dmin,dmax))

def cut_k(z,phi):
    rr=math.sqrt(max(0.0,1.0-z*z))
    n=rr*math.cos(phi)*e1+rr*math.sin(phi)*e2+z*e3
    l=-0.5*Q+0.5*M*n
    return l-shifts[i]

def phi_mean_num(z,nphi=16,phase=0.0):
    total=0j; mx=0.0; denerr=0.0
    for m in range(nphi):
        phi=2.0*math.pi*(m+phase)/nphi
        k=cut_k(float(z),phi)
        num=complex(family_num(group,k)); total+=num; mx=max(mx,abs(num))
        d=complex(denom(k+sk)); denerr=max(denerr,abs(d-(const+amp*float(z))))
    return total/nphi,mx,denerr

# Seven fixed interpolation nodes determine a degree-six polynomial.  Held-out
# nodes and phase-shifted azimuth averages test rather than assume that degree.
ztrain=np.array([-0.92,-0.67,-0.36,0.0,0.31,0.63,0.91],float)
zheld=np.array([-0.97,-0.81,-0.53,-0.19,0.14,0.44,0.76,0.96],float)
PHASE=0.37123456789
train=[]; raw_num_max=0.0; den_affine_err=0.0; phi_stability=0.0
for z in ztrain:
    v,mx,de=phi_mean_num(z,16,0.0); vp,_,dep=phi_mean_num(z,16,PHASE)
    train.append(v); raw_num_max=max(raw_num_max,mx); den_affine_err=max(den_affine_err,de,dep); phi_stability=max(phi_stability,abs(v-vp))
train=np.asarray(train,complex)
coef_cheb=np.polynomial.chebyshev.chebfit(ztrain,train,6)
poly=Chebyshev(coef_cheb).convert(kind=Polynomial)
coef=np.asarray(poly.coef,complex)
fit_train=np.array([poly(z) for z in ztrain],complex)
train_err=float(np.max(np.abs(fit_train-train)))
held_err=0.0; held_phase=0.0
held_rows=[]
for z in zheld:
    v,mx,de=phi_mean_num(z,16,0.0); vp,_,dep=phi_mean_num(z,16,PHASE); pred=complex(poly(z))
    raw_num_max=max(raw_num_max,mx); den_affine_err=max(den_affine_err,de,dep); held_err=max(held_err,abs(v-pred)); held_phase=max(held_phase,abs(v-vp))
    held_rows.append({'z':float(z),'physical_phi_mean':[float(v.real),float(v.imag)],'poly_prediction':[float(pred.real),float(pred.imag)],'phase_shifted_phi_mean':[float(vp.real),float(vp.imag)]})
num_scale=max(raw_num_max,float(np.max(np.abs(train))),1e-30)
poly_scaled=max(train_err,held_err)/num_scale
phi_scaled=max(phi_stability,held_phase)/num_scale

# Analytic rational moments J_n = int z^n/(c+a z) dz.
def moments(nmax,c,a):
    out=[]
    if abs(a)<1e-14:
        for n in range(nmax+1): out.append((0.0 if n%2 else 2.0/(n+1))/c)
        return np.asarray(out,complex)
    J0=np.log(complex((c+a)/(c-a)))/a
    out=[J0]
    for n in range(1,nmax+1):
        im1=0.0 if (n-1)%2 else 2.0/n
        out.append(im1/a-(c/a)*out[-1])
    return np.asarray(out,complex)
J=moments(len(coef)-1,const,amp)
analytic_mean=0.5*np.dot(coef,J)

# Independent direct sparse product rule on the ORIGINAL numerator/denominator.
def direct_mean(nz,nphi,phase=0.0):
    zs,ws=np.polynomial.legendre.leggauss(nz); total=0j; mx=0.0; shell=0.0; minthird=float('inf')
    for z,w in zip(zs,ws):
        ring=0j
        for m in range(nphi):
            phi=2.0*math.pi*(m+phase)/nphi; k=cut_k(float(z),phi)
            d0=abs(denom(k+shifts[i])); d1=abs(denom(k+shifts[j])); shell=max(shell,d0,d1)
            third=complex(denom(k+sk)); minthird=min(minthird,abs(third))
            val=complex(family_num(group,k))/third; ring+=val; mx=max(mx,abs(val))
        total+=float(w)*(ring/nphi)
    return 0.5*total,mx,shell,minthird

direct0,mx0,shell0,min3a=direct_mean(12,24,0.0)
directp,mxp,shellp,min3b=direct_mean(12,24,PHASE)
int_scale=max(mx0,mxp,1e-30)
direct_cross=max(abs(direct0-analytic_mean),abs(directp-analytic_mean),abs(directp-direct0))/int_scale
nonzero_ratio=abs(analytic_mean)/int_scale

THRESH=2e-5; NONZERO_RATIO=2e-6
POLY_TOL=2e-8; PHI_TOL=2e-8; DEN_AFFINE_TOL=2e-10
structural=bool(poly_scaled<POLY_TOL and phi_scaled<PHI_TOL and den_affine_err<DEN_AFFINE_TOL and max(shell0,shellp)<1e-10 and min(min3a,min3b)>2e-9)
resolved=bool(structural and direct_cross<THRESH and nonzero_ratio>NONZERO_RATIO)
classification=('PASS_DET_TRIANGLE_Q2_MINUS1_ANALYTIC_AZIMUTH_REDUCTION_NONZERO_DISCONTINUITY' if resolved else 'BLOCKED_DET_TRIANGLE_Q2_MINUS1_ANALYTIC_AZIMUTH_REDUCTION')
result={
 'iteration':ITERATION,'model_readiness_percent':24,'scientific_gate_pass':resolved,'candidate_residual':False,
 'classification':classification,
 'scope':'SOLE_Q2_MINUS1_DETERMINANT_TRIANGLE_CHANNEL__ANALYTIC_AZIMUTH_REDUCTION__NO_OTHER_CHANNEL_RECOMPUTE',
 'q2':float(q2),'cut_pair':[i,j],'uncut_index':kidx,'triangle_route_count':len(group),
 'polynomial_degree_bound':6,'triangle_all_insertions_first_background_order':True,
 'third_denominator':{'form':'c+a*z','c':float(const),'a':float(amp),'exact_range':[float(dmin),float(dmax)],'max_direct_affine_abs_error':float(den_affine_err)},
 'azimuth_numerator':{'chebyshev_fit_degree':6,'power_coefficients':[[float(x.real),float(x.imag)] for x in coef],
                      'train_scaled_max_error':float(train_err/num_scale),'heldout_scaled_max_error':float(held_err/num_scale),
                      'max_phase_shift_scaled_error':float(phi_scaled),'heldout':held_rows},
 'analytic_sphere_mean':[float(analytic_mean.real),float(analytic_mean.imag)],
 'direct_sparse_crosscheck':{'grid':[12,24],'phase':PHASE,'base_mean':[float(direct0.real),float(direct0.imag)],
                             'shifted_mean':[float(directp.real),float(directp.imag)],'max_abs_sample':float(int_scale),
                             'scaled_disagreement':float(direct_cross),'max_cut_shell_error':float(max(shell0,shellp)),
                             'minimum_sampled_third_abs_denominator':float(min(min3a,min3b))},
 'central_to_sample_ratio':float(nonzero_ratio),
 'thresholds':{'unchanged_discontinuity_scaled_convergence_max':THRESH,'unchanged_nonzero_ratio_min':NONZERO_RATIO,
               'polynomial_heldout_scaled_max':POLY_TOL,'azimuth_phase_scaled_max':PHI_TOL,'denominator_affine_abs_max':DEN_AFFINE_TOL},
 'guardrails':['NO_PARENT_OR_NUMERATOR_CHANGE','NO_THRESHOLD_WEAKENING','DEGREE6_CLAIM_HELDOUT_TESTED','DIRECT_ORIGINAL_INTEGRAND_CROSSCHECK_REQUIRED',
               'NO_SOURCE_BORN_SUBTRACTION','NO_ANSATZ003','NO_FISHER_RESOURCES','ITERATION297_FINITE_DR_WARNING_REMAINS'],
 'next_gate':('if PASS, freeze all three determinant triangle two-particle channels as NONZERO and assemble the complete channel-resolved normalized determinant absorptive vector; full finite-DR remainder still remains separately blocked by Iteration297' if resolved else 'preserve the q2=-1 channel BLOCKED and inspect only failed polynomial/phase/direct-crosscheck component without weakening thresholds')
}
print(json.dumps(result,indent=2,sort_keys=True))
if not resolved: raise SystemExit(2)
