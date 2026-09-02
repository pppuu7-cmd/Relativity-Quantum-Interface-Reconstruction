#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 288.

Complete degree<=6 / 210-monomial raised-triangle reduction on the frozen
translation-closed Euclidean kinematics.  The actual same-parent numerator
coefficients are fitted from the Iteration-285 oracle.  The loop integral

  N(l) / [(l^2)^2 (l+q1)^2 (l+q2)^2]

is reduced with Feynman parameters and D=4-2 eps isotropic tensor moments.
For the one-null-leg two-mass triangle the Symanzik polynomial factorizes,
allowing one Feynman parameter to be integrated analytically as beta functions.
The remaining one-dimensional integral uses Gauss-Legendre quadrature.

We extract the normalized discontinuity under the common retarded continuation
of the two nonzero hard invariants.  This is a coefficient-level hard-channel
cut certificate, not yet a decomposition into the three scalar master basis
columns and not yet source/Ward/contact completed T_cut.
"""
import importlib.util, json, math
from pathlib import Path
import numpy as np
from scipy.special import gamma
from numpy.polynomial.legendre import leggauss

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('i285',HERE/'iteration285_actual_numerator_basis_audit.py')
i285=importlib.util.module_from_spec(spec); spec.loader.exec_module(i285)
ETA=i285.ETA; MON6=i285.MON6
KS=i285.KS; KA=i285.KA; KB=i285.KB
PAIR=i285.PAIR


def mdot(a,b): return float(np.asarray(a)@ETA@np.asarray(b))

def fit_sector(sec,seed):
    rng=np.random.default_rng(seed)
    tr=rng.uniform(-.95,.95,(226,4)); ho=rng.uniform(-1.05,1.05,(30,4))
    X=np.array([i285.mon(MON6,l) for l in tr]); H=np.array([i285.mon(MON6,l) for l in ho])
    y=np.array([i285.tri_trace(sec,l) for l in tr]); z=np.array([i285.tri_trace(sec,l) for l in ho])
    c=np.linalg.lstsq(X,y,rcond=None)[0]; r=H@c-z
    return c,{
      'rank':int(np.linalg.matrix_rank(X)),'basis_size':len(MON6),
      'condition_number':float(np.linalg.cond(X)),
      'heldout_max_abs':float(np.max(np.abs(r))),
      'heldout_rms':float(np.sqrt(np.mean(r*r))),
      'heldout_relative_max':float(np.max(np.abs(r))/max(np.max(np.abs(z)),1e-30)),
    }


def laplacian(poly):
    out={}
    for e,c in poly.items():
      for mu in range(4):
        if e[mu]>=2:
          ee=list(e); fac=e[mu]*(e[mu]-1); ee[mu]-=2; ee=tuple(ee)
          out[ee]=out.get(ee,0.0)+c*ETA[mu,mu]*fac
    return out

def coeff_poly(c): return {e:float(x) for e,x in zip(MON6,c) if abs(x)>1e-14}

def linpow(a,b,p):
    out=np.array([1+0j])
    for _ in range(p): out=np.convolve(out,np.array([a,b],complex))
    return out

def poly_u(poly,A,B):
    out=np.zeros(7,dtype=complex)
    for e,c in poly.items():
      arr=np.array([1+0j])
      for i,p in enumerate(e):
        if p: arr=np.convolve(arr,linpow(-A[i],-B[i],p))
      out[:len(arr)] += c*arr
    return out

def beta_an(a,b): return gamma(a)*gamma(b)/gamma(a+b)

NODES,WEIGHTS=leggauss(72); VS=(NODES+1)/2; WS=WEIGHTS/2

def branch_integral(c,q1r,q2r,eps,sgn):
    # q -> exp(+/- i pi/2) q so all nonzero invariants acquire the same
    # upper/lower timelike phase while the null invariant stays null.
    z=np.exp(1j*sgn*np.pi/2)
    q1=z*np.asarray(q1r,float); q2=z*np.asarray(q2r,float)
    a0=mdot(q1r,q1r); b0=mdot(q2r,q2r); c0=mdot(np.asarray(q1r)-np.asarray(q2r),np.asarray(q1r)-np.asarray(q2r))
    null=int(np.argmin([abs(a0),abs(b0),abs(c0)]))
    a=q1@ETA@q1; b=q2@ETA@q2; cc=(q1-q2)@ETA@(q1-q2)
    polys=[coeff_poly(c)]
    for _ in range(3): polys.append(laplacian(polys[-1]))
    total=0j
    for j,poly in enumerate(polys):
      if not poly: continue
      alpha=j-2-eps
      # Taylor + isotropic contraction gives Gamma(2-j+eps)/(4^j j!).
      pref=gamma(2-j+eps)/(4**j*math.factorial(j))
      integ=0j
      for v,w in zip(VS,WS):
        if null==2: # (q1-q2)^2=0
          L=v*a+(1-v)*b; A=np.zeros(4,complex); B=v*q1+(1-v)*q2
          bu=1+alpha; bw=1+alpha; extra=1.0
        elif null==0: # q1^2=0
          L=v*b+(1-v)*cc; A=q2; B=(1-v)*q1-q2
          bu=2+alpha; bw=alpha; extra=v
        else: # q2^2=0
          L=v*a+(1-v)*cc; A=q1; B=(1-v)*q2-q1
          bu=2+alpha; bw=alpha; extra=v
        pc=poly_u(poly,A,B); su=0j
        for n,coef in enumerate(pc):
          if abs(coef)>1e-18: su += coef*beta_an(bu+n+1,bw+1)
        integ += w*extra*(L**alpha)*su
      total += pref*integ
    return total

def disc_eps(c,q1,q2,eps):
    up=branch_integral(c,q1,q2,eps,+1); dn=branch_integral(c,q1,q2,eps,-1)
    return float(np.real((up-dn)/(2j*np.pi)))

EP=np.array([.02,.01,.005,.0025])
def cut_limit(c,q1,q2):
    vals=np.array([disc_eps(c,q1,q2,e) for e in EP])
    p=np.polyfit(EP,vals,2)
    return float(p[-1]),vals.tolist()

def reflect(c): return np.array([x*((-1)**sum(e)) for x,e in zip(c,MON6)])

# Exact calibration: numerator l^2 cancels the repeated propagator and must
# reduce to the same ordinary one-null two-mass triangle for all routings.
lookup={e:i for i,e in enumerate(MON6)}; CL2=np.zeros(len(MON6))
for mu in range(4):
    e=[0]*4; e[mu]=2; CL2[lookup[tuple(e)]]=ETA[mu,mu]

def scalar_target(q1,q2):
    inv=[mdot(q1,q1),mdot(q2,q2),mdot(np.asarray(q1)-np.asarray(q2),np.asarray(q1)-np.asarray(q2))]
    non=[x for x in inv if abs(x)>1e-10]
    return float(-np.log(non[0]/non[1])/(non[0]-non[1]))

cal={}; sectors={}
for sec,seed in [('tri_(0.0, 0.21)',288021),('tri_(0.0, 0.41)',288041),('tri_(0.21, 0.41)',2882141)]:
    q1,q2=PAIR[sec]
    ct,scan=cut_limit(CL2,q1,q2); target=scalar_target(q1,q2)
    cal[sec]={'extrapolated_l2_triangle_cut':ct,'exact_ordinary_triangle_cut':target,'abs_residual':abs(ct-target),'eps_scan':scan}
    c,fit=fit_sector(sec,seed)
    cut,escan=cut_limit(c,q1,q2)
    cr=reflect(c); cutr,_=cut_limit(cr,-np.asarray(q1),-np.asarray(q2))
    sectors[sec]={
      'fit':fit,'q1':np.asarray(q1,float).tolist(),'q2':np.asarray(q2,float).tolist(),
      'invariants':[mdot(q1,q1),mdot(q2,q2),mdot(np.asarray(q1)-np.asarray(q2),np.asarray(q1)-np.asarray(q2))],
      'common_hard_channel_normalized_cut':cut,'eps_scan':escan,
      'reflected_cut':cutr,'reflection_abs_residual':abs(cut-cutr),
      'coefficient_l2_norm':float(np.linalg.norm(c)),
    }

max_cal=max(v['abs_residual'] for v in cal.values())
max_ref=max(v['reflection_abs_residual'] for v in sectors.values())
all_nonzero=all(abs(v['common_hard_channel_normalized_cut'])>1e-6 for v in sectors.values())
all_fit=all(v['fit']['rank']==210 and v['fit']['heldout_relative_max']<1e-6 for v in sectors.values())
cls='PASS_COMPLETE_210_MONOMIAL_TRIANGLE_COMMON_HARD_CHANNEL_CUT_NONZERO' if (max_cal<5e-5 and max_ref<2e-5 and all_nonzero and all_fit) else 'BLOCKED_TRIANGLE_COMMON_CUT_REDUCTION_AUDIT'

result={
 'iteration':288,'model_readiness_percent':24,
 'normalization':'common upper-minus-lower timelike continuation divided by 2*pi*i after loop normalization i*pi^(D/2)',
 'calibration':cal,'triangle_sectors':sectors,
 'max_scalar_triangle_calibration_abs_residual':max_cal,
 'max_loop_reflection_abs_residual':max_ref,
 'classification':cls,'candidate_residual':False,
 'guardrail':'COMMON_CUT_IS_A COEFFICIENT-LEVEL TRIANGLE CERTIFICATE; MASTER-BASIS DECOMPOSITION AND SOURCE/WARD/CONTACT COMPLETION REMAIN DOWNSTREAM',
 'next_gate':289,
}
assert max_cal<5e-5
assert all_fit
print(json.dumps(result,indent=2,sort_keys=True))
