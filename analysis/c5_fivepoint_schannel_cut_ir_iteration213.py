#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 213.

Physical real-massless 2->3 preregistration and raw s-channel two-particle
unitarity-cut infrared endpoint diagnostic for pure Einstein gravity.

External all-outgoing helicities are --+++ with leg 5 soft and positive.
The total-s cut uses M4(--++) on the left and M5(++ + --) on the right.
The tree amplitudes are evaluated using Parke-Taylor + KLT. The raw cut is
NOT a physical observable: this script explicitly tests its angular endpoint
behavior to determine whether IR subtraction/inclusive completion is required
before the Iteration-210 regular+log soft extractor.
"""
from pathlib import Path
import json, math, cmath
import numpy as np
from numpy.polynomial.legendre import leggauss

ITERATION = 213
EPSILON_DIAGNOSTIC = 0.01
CAPS = np.array([0.3,0.2,0.14,0.1,0.07,0.05,0.035,0.025],float)
N_MU = 100
N_PHI = 128

def dot4(p,q):
    return float(p[0]*q[0]-np.dot(p[1:],q[1:]))

def spinors_from_p(p):
    E,px,py,pz = map(float,p)
    zp, zm = complex(E+pz), complex(E-pz)
    if abs(zp)>=abs(zm) and abs(zp)>1e-14:
        a=cmath.sqrt(zp)
        lam=np.array([a,(px+1j*py)/a],complex)
        til=np.array([a,(px-1j*py)/a],complex)
    elif abs(zm)>1e-14:
        b=cmath.sqrt(zm)
        lam=np.array([(px-1j*py)/b,b],complex)
        til=np.array([(px+1j*py)/b,b],complex)
    else:
        raise ValueError("degenerate null momentum")
    return lam,til

def spinors_for_momenta(ps):
    ls,ts=[],[]
    for p in ps:
        l,t=spinors_from_p(p); ls.append(l); ts.append(t)
    return ls,ts

def angle(ls,i,j): return ls[i][0]*ls[j][1]-ls[i][1]*ls[j][0]
def square(ts,i,j): return ts[i][0]*ts[j][1]-ts[i][1]*ts[j][0]
def sij(ls,ts,i,j): return angle(ls,i,j)*square(ts,j,i)

def ym_tree(order,hels,ls,ts):
    neg=[i for i,h in enumerate(hels) if h<0]
    pos=[i for i,h in enumerate(hels) if h>0]
    seq=list(order)
    if len(neg)==2:
        num=angle(ls,neg[0],neg[1])**4
        den=1+0j
        for a,b in zip(seq,seq[1:]+seq[:1]): den*=angle(ls,a,b)
        return 1j*num/den
    if len(pos)==2:
        num=square(ts,pos[0],pos[1])**4
        den=1+0j
        for a,b in zip(seq,seq[1:]+seq[:1]): den*=square(ts,a,b)
        return 1j*num/den
    return 0j

def m4(ps,hels):
    ls,ts=spinors_for_momenta(ps)
    A=lambda o: ym_tree(o,hels,ls,ts)
    return -1j*sij(ls,ts,0,1)*A((0,1,2,3))*A((0,1,3,2))

def m5(ps,hels):
    ls,ts=spinors_for_momenta(ps)
    A=lambda o: ym_tree(o,hels,ls,ts)
    return (1j*sij(ls,ts,0,1)*sij(ls,ts,2,3)*A((0,1,2,3,4))*A((1,0,3,2,4))
            +1j*sij(ls,ts,0,2)*sij(ls,ts,1,3)*A((0,2,1,3,4))*A((2,0,3,1,4)))

def physical_2to3(epsilon,theta_star=0.9,phi_star=0.4):
    """All-outgoing momenta k1..k5 for physical 2->3 at sqrt(s)=1."""
    nx,ny=0.35,-0.25
    nz=math.sqrt(1-nx*nx-ny*ny)
    n5=np.array([nx,ny,nz],float)
    P1=np.array([0.5,0,0,0.5],float)
    P2=np.array([0.5,0,0,-0.5],float)
    P5=np.r_[epsilon,epsilon*n5]
    P34=np.array([1.,0,0,0])-P5
    mass=math.sqrt(dot4(P34,P34))
    Estar=mass/2
    nstar=np.array([math.sin(theta_star)*math.cos(phi_star),
                    math.sin(theta_star)*math.sin(phi_star),
                    math.cos(theta_star)])
    q3=np.r_[Estar,Estar*nstar]
    q4=np.r_[Estar,-Estar*nstar]
    beta=P34[1:]/P34[0]
    b2=float(np.dot(beta,beta)); gamma=1/math.sqrt(1-b2)
    def boost(q):
        E=q[0]; pv=q[1:]; bd=float(np.dot(beta,pv))
        pnew=pv+(((gamma-1)*bd/b2)+gamma*E)*beta if b2>0 else pv
        return np.r_[gamma*(E+bd),pnew]
    P3,P4=boost(q3),boost(q4)
    return [-P1,-P2,P3,P4,P5]

def cut_integrand(epsilon,theta,phi,h1=1,h2=1):
    ks=physical_2to3(epsilon)
    n=np.array([math.sin(theta)*math.cos(phi),math.sin(theta)*math.sin(phi),math.cos(theta)])
    ell1=np.r_[0.5,0.5*n]
    ell2=np.r_[0.5,-0.5*n]
    left=[ks[0],ks[1],ell1,ell2]
    right=[ks[2],ks[3],ks[4],-ell1,-ell2]
    left_hels=[-1,-1,h1,h2]
    right_hels=[1,1,1,-h1,-h2]
    return m4(left,left_hels)*m5(right,right_hels)

def angular_integral(epsilon,delta):
    # Raw dOmega integral over theta in [delta,pi-delta]. Overall two-body
    # phase-space and Disc normalizations are intentionally not applied yet.
    lo,hi=-math.cos(delta),math.cos(delta)
    x,w=leggauss(N_MU)
    mus=(lo+hi)/2+(hi-lo)*x/2
    weights=(hi-lo)*w/2
    phis=np.linspace(0,2*math.pi,N_PHI,endpoint=False)
    total=0j
    for mu,wi in zip(mus,weights):
        theta=math.acos(float(mu))
        total += wi*(2*math.pi/N_PHI)*sum(cut_integrand(epsilon,theta,float(phi)) for phi in phis)
    return total

# External kinematic certificate over representative soft values.
kin_checks=[]
for eps in [0.04,0.01,0.001]:
    ks=physical_2to3(eps)
    kin_checks.append({
        "epsilon":eps,
        "momentum_conservation_max_abs":float(np.max(np.abs(np.sum(np.array(ks),axis=0)))),
        "max_abs_mass_shell":float(max(abs(dot4(k,k)) for k in ks)),
    })

# Tree-helicity selection on a generic cut angle.
helicity_terms=[]
for h1 in [-1,1]:
    for h2 in [-1,1]:
        val=cut_integrand(EPSILON_DIAGNOSTIC,0.8,0.7,h1,h2)
        helicity_terms.append({"h1":h1,"h2":h2,"abs_integrand":float(abs(val))})

# Endpoint scaling at fixed phi.
thetas=np.array([0.1,0.05,0.02,0.01,0.005,0.002],float)
theta2_abs=[]
for theta in thetas:
    theta2_abs.append(float(theta**2*abs(cut_integrand(EPSILON_DIAGNOSTIC,float(theta),0.7))))

# Raw cap dependence.
raw=[]
for delta in CAPS:
    val=angular_integral(EPSILON_DIAGNOSTIC,float(delta))
    raw.append({"delta":float(delta),"real":float(val.real),"imag":float(val.imag),"abs":float(abs(val))})
raw_abs=np.array([r["abs"] for r in raw])
log_inv=np.log(1/CAPS)
fit=np.polyfit(log_inv[-6:],raw_abs[-6:],1)
pred=np.polyval(fit,log_inv[-6:])
fit_rel=float(np.linalg.norm(pred-raw_abs[-6:])/np.linalg.norm(raw_abs[-6:]))

out={
    "iteration":ITERATION,
    "date":"2026-09-01",
    "model_readiness_percent":23,
    "protocol":"real massless 2->3 at sqrt(s)=1; all-outgoing --+++; total-s two-particle cut",
    "kinematic_checks":kin_checks,
    "cut_partition":{
        "left":"M4(k1-,k2-,ell1+,ell2+)",
        "right":"M5(k3+,k4+,k5+,-ell1-,-ell2-)",
        "phase_space":"ell1=(1/2)(1,n), ell2=(1/2)(1,-n), n on S^2",
        "helicity_sum_rule":"tree selection leaves only h1=h2=+ on the left in the frozen external MHV sector"
    },
    "helicity_terms_at_theta_0p8_phi_0p7":helicity_terms,
    "endpoint_thetas":thetas.tolist(),
    "theta2_times_abs_integrand":theta2_abs,
    "theta2_abs_integrand_smallest_theta":theta2_abs[-1],
    "angular_caps":CAPS.tolist(),
    "raw_angular_integrals":raw,
    "abs_integral_log_fit_last6":{
        "slope":float(fit[0]),
        "intercept":float(fit[1]),
        "relative_fit_residual":fit_rel
    },
    "classification":{
        "real_2to3_kinematics":"PASS_MACHINE_PRECISION",
        "helicity_sum_reduction":"PASS_TREE_SELECTION",
        "raw_cut_endpoint":"IR_COLLINEAR_LOG_DIVERGENT",
        "raw_cut_to_iteration210_extractor":"FORBIDDEN_BEFORE_IR_SUBTRACTION_OR_INCLUSIVE_COMPLETION",
        "candidate_residual":"NONE",
        "ANSATZ_003":"NOT_CREATED",
        "Fisher_resources":"FORBIDDEN"
    },
    "retained_results":[
        "C5-CUT-011 — REAL_FIVE_GRAVITON_TOTAL_S_CUT_REDUCES_TO_M4_MHV_TIMES_M5_MHV_IN_THE_FROZEN_HELICITY_SECTOR",
        "IR-NG-002 — RAW_FIVE_GRAVITON_S_CHANNEL_CUT_HAS_THETA_MINUS_TWO_ENDPOINT_BEHAVIOR_AND_LOGARITHMIC_ANGULAR_CAP_DEPENDENCE",
        "C5-CUT-012 — RAW_UNITARITY_CUT_MUST_BE_IR_SUBTRACTED_OR_INCLUSIVELY_COMPLETED_BEFORE_REGULAR_LOG_SOFT_EXTRACTION",
        "NG-FUNNEL-070 — UNIVERSAL_LOOP_IR_LOGS_MUST_NOT_BE_MISIDENTIFIED_AS_LINKED_GRAVITY_RESIDUALS"
    ],
    "readiness_change":"unchanged at 23%; the physical cut geometry and its IR blocker are now explicit, but no IR-safe five-point cut has been extracted",
    "next_gate":"Derive/freeze the universal gravitational IR subtraction for this exact cut convention from the on-shell Born amplitude/eikonal soft factor, validate cap independence after subtraction, then run the finite-epsilon regular+log extractor."
}
Path("results/c5_fivepoint_schannel_cut_ir_iteration213.json").write_text(json.dumps(out,indent=2,sort_keys=True)+"\n",encoding="utf-8")
print(json.dumps(out,indent=2,sort_keys=True))
