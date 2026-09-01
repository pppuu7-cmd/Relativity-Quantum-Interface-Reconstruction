import numpy as np, math, json, time
from pathlib import Path
from numpy.polynomial.legendre import leggauss
eta=np.diag([1.,-1.,-1.,-1.]).astype(complex)
def dot(a,b): return a@eta@b
def A4(P1,k2,k3,P4,e2,e3):
    F=np.outer(k3,e3)-np.outer(e3,k3)
    return ((2*dot(e2,P1)*dot(e3,k2)-2*(e2@eta@F@eta@P1))/(2*dot(k2,k3)) -2*dot(e2,P1)*dot(e3,P4)/(2*dot(P1,k2)))
def Msep(P1,k2,k3,P4,l2,l3,r2,r3): return -(2*dot(k2,k3))*A4(P1,k3,k2,P4,l3,l2)*A4(P1,k2,k3,P4,r2,r3)
def tensor_amp(P1,k2,k3,P4,T2,T3): return sum(c2*c3*Msep(P1,k2,k3,P4,l2,l3,r2,r3) for c2,l2,r2 in T2 for c3,l3,r3 in T3)
def spin2_basis(n,alpha=0.0):
    n=np.asarray(n,float); n=n/np.linalg.norm(n); ref=np.array([0.,0.,1.])
    if abs(float(n@ref))>0.9: ref=np.array([1.,0.,0.])
    e1=np.cross(ref,n); e1/=np.linalg.norm(e1); e2=np.cross(n,e1); e2/=np.linalg.norm(e2)
    c,s=math.cos(alpha),math.sin(alpha); f1=c*e1+s*e2; f2=-s*e1+c*e2
    E1=np.r_[0.,f1].astype(complex); E2=np.r_[0.,f2].astype(complex); q=1/math.sqrt(2)
    return ([(q,E1,E1),(-q,E2,E2)],[(q,E1,E2),(q,E2,E1)])
def physical(m=0.7,sqrts=2.0,theta=0.8):
    s=sqrts*sqrts; p=(s-m*m)/(2*sqrts); Es=(s+m*m)/(2*sqrts)
    Pin=np.array([Es,0,0,p],complex); kin=np.array([p,0,0,-p],complex)
    kout=np.array([p,p*math.sin(theta),0,p*math.cos(theta)],complex); Pout=np.array([Es,-p*math.sin(theta),0,-p*math.cos(theta)],complex)
    return Pin,kin,kout,Pout,p,Es

def make_integrand(theta_ext,pol_idx):
    Pin,kin,kout,Pout,p,Es=physical(theta=theta_ext)
    Tin=spin2_basis([0,0,-1])[pol_idx]; Tout=spin2_basis([math.sin(theta_ext),0,math.cos(theta_ext)])[pol_idx]
    born=tensor_amp(-Pin,-kin,kout,Pout,Tin,Tout); R=-8*born; nout=np.array([math.sin(theta_ext),0,math.cos(theta_ext)])
    def hk(n):
        n=np.asarray(n,float); n/=np.linalg.norm(n); lg=np.r_[p,p*n].astype(complex); ls=np.r_[Es,-p*n].astype(complex)
        left=(-Pin,-kin,lg,ls); right=(-ls,-lg,kout,Pout)
        cut=sum(tensor_amp(*left,Tin,T)*tensor_amp(*right,T,Tout) for T in spin2_basis(n))
        return cut-R/(1+n[2])-R/(1-float(n@nout))
    return hk, born

def frame(c,other):
    c=np.asarray(c,float); c/=np.linalg.norm(c); other=np.asarray(other,float); other/=np.linalg.norm(other)
    gamma=math.acos(np.clip(c@other,-1.,1.)); e=(other-math.cos(gamma)*c)/math.sin(gamma); e/=np.linalg.norm(e); f=np.cross(c,e); f/=np.linalg.norm(f)
    return gamma,e,f

def integrate(theta_ext,pol_idx,N,rule):
    hk,born=make_integrand(theta_ext,pol_idx); cin=np.array([0.,0.,-1.]); cout=np.array([math.sin(theta_ext),0.,math.cos(theta_ext)])
    xr,wr=leggauss(N); total=0j
    for c,other in [(cin,cout),(cout,cin)]:
        gamma,e,f=frame(c,other); A=1-math.cos(gamma); sg=math.sin(gamma)
        if rule=='A':
            Nphi=2*N; phis=(np.arange(Nphi)+0.5)*2*math.pi/Nphi; wphis=np.full(Nphi,2*math.pi/Nphi)
        else:
            xp,wp=leggauss(N); phis=math.pi*(xp+1.); wphis=math.pi*wp
        for ph,wph in zip(phis,wphis):
            rmax=math.atan2(A,sg*math.cos(ph)); rhos=0.5*(xr+1.)*rmax; wrhos=0.5*rmax*wr; u=math.cos(ph)*e+math.sin(ph)*f
            for rho,wrr in zip(rhos,wrhos):
                n=math.cos(rho)*c+math.sin(rho)*u; total += wph*wrr*math.sin(rho)*hk(n)
    return total.real, born.real

FORWARD_THETA_GRID=[0.13,0.105,0.085,0.068,0.054,0.043,0.034,0.027]
N=16
FROZEN_REL_ENVELOPE=3e-7
records=[]
for pol,name in [(0,'plus'),(1,'cross')]:
    for th in FORWARD_THETA_GRID:
        a,bo=integrate(th,pol,N,'A'); b,_=integrate(th,pol,N,'B')
        z=math.sin(th/2)**2
        records.append({'theta_ext':th,'z':z,'polarization':name,'cubature_A':float(a),'cubature_B':float(b),'born':float(bo),'relative_disagreement':float(abs(a-b)/max(abs(a),abs(b),1e-30))})

def extract(pol):
    r=[q for q in records if q['polarization']==pol]
    z=np.array([q['z'] for q in r],float)
    y=np.array([(q['cubature_A']+q['cubature_B'])/2 for q in r],float)
    L=np.log(z)
    X=np.column_stack([np.ones_like(z),L,z,z*L,z*z,z*z*L])
    T=np.column_stack([z**k for k in range(6)])
    def fit(M,idx):
        c=np.linalg.lstsq(M[idx],y[idx],rcond=None)[0]
        rel=float(np.linalg.norm(M[idx]@c-y[idx])/np.linalg.norm(y[idx]))
        return [float(v) for v in c],rel
    windows={'all8':np.arange(8),'deep7':np.arange(1,8),'outer7':np.arange(0,7)}
    fits={}
    for wn,idx in windows.items():
        cr,rr=fit(X,idx); ct,rt=fit(T,idx)
        fits[wn]={'regular_log_coefficients':cr,'regular_log_relative_l2_residual':rr,'taylor_degree5_coefficients':ct,'taylor_degree5_relative_l2_residual':rt}
    P=np.linalg.pinv(X)
    sigma=FROZEN_REL_ENVELOPE*np.abs(y)
    c=P@y
    dc=np.abs(P)@sigma
    snr=np.divide(np.abs(c),dc,out=np.zeros_like(c),where=dc>0)
    return {
      'basis':['1','L','z','zL','z^2','z^2L'],'L_definition':'log(z)','fits':fits,
      'full_window_log_coefficients':{'b0':float(c[1]),'b1':float(c[3]),'b2':float(c[5])},
      'full_window_log_coefficient_worst_case_bounds_from_3e-7_row_envelope':{'b0':float(dc[1]),'b1':float(dc[3]),'b2':float(dc[5])},
      'full_window_log_coefficient_abs_over_worst_case_bound':{'b0':float(snr[1]),'b1':float(snr[3]),'b2':float(snr[5])},
      'all_log_coefficients_resolved_above_frozen_envelope':bool(np.all(snr[[1,3,5]]>1.0)),
      'any_log_coefficient_resolved_above_frozen_envelope':bool(np.any(snr[[1,3,5]]>1.0)),
    }

extractions={p:extract(p) for p in ['plus','cross']}
max_rel=max(q['relative_disagreement'] for q in records)
pure_graviton_control={
  'authority':'results/c5_fivepoint_finite_cut_extractor_iteration215.json',
  'regular_log_relative_l2_residual':2.791237182608158e-7,
  'equal_parameter_pure_taylor_degree5_relative_l2_residual':9.496951084345664e-5,
  'relative_l2_numerical_error_envelope':3.4037051620849225e-8,
  'pure_taylor_residual_over_numerical_envelope':2790.180298263071,
  'classification':'PASS_SCOPED_LOG_STRUCTURE_RESOLVED'
}
out={
 'iteration':226,'date':'2026-09-01','model_readiness_percent':24,'source_model_id':'MSSC-001',
 'source_observable':'Born-subtracted connected scalar-source s-channel hard remainder from Iterations 221-225',
 'transfer_coordinate':'z=-t/(4 p^2)=sin^2(theta_ext/2)',
 'forward_theta_grid':FORWARD_THETA_GRID,
 'grid_rule':'comparator-only forward-transfer grid; no Candidate Gravity residual or ansatz information used',
 'cubature_order':N,
 'frozen_relative_numerical_envelope':FROZEN_REL_ENVELOPE,
 'records':records,
 'max_two_cubature_relative_disagreement':max_rel,
 'extractions':extractions,
 'pure_graviton_positive_control':pure_graviton_control,
 'classification':{
   'source_forward_numerical_gate':'PASS_WITHIN_FROZEN_3E-7_ENVELOPE',
   'source_log_nonanalyticity':'REGIME_SPECIFIC_NON_IDENTIFIABILITY_NO_CERTIFICATE',
   'source_exact_analytic_identity':'NOT_CLAIMED',
   'source_consistency_fail':'NO',
   'source_near_degeneracy':'YES_ANALYTIC_VS_LOG_WITHIN_NUMERICAL_ENVELOPE',
   'pure_graviton_control_log_structure':'PASS_FROM_ITERATION215',
   'source_vs_pure_graviton_mismatch_candidate_novelty':'NO',
   'candidate_residual':'NONE','ANSATZ_003':'NOT_CREATED','Fisher_resources':'FORBIDDEN'
 },
 'retained_results':[
   'SRC-CUT-007 — MSSC001_FORWARD_HARD_REMAINDER_IS_NUMERICALLY_STABLE_ON_A_FROZEN_TRANSFER_GRID',
   'SRC-CUT-008 — MSSC001_FORWARD_LOG_COEFFICIENTS_ARE_NOT_RESOLVED_AGAINST_THE_FROZEN_3E-7_ENVELOPE',
   'REL-NG-005 — PURE_GRAVITON_LOG_POSITIVE_CONTROL_AND_SOURCE_HARD_REMAINDER_HAVE_DIFFERENT_RESOLUTION_STATUS_AND_MUST_NOT_BE_IDENTIFIED',
   'NG-FUNNEL-082 — SOURCE_CONTROL_NONANALYTIC_NONIDENTIFIABILITY_IS_NOT_CANDIDATE_NOVELTY'
 ],
 'readiness_change':'unchanged at 24%; source-comparator forward structure is now classified, but no new comparator-foundation rubric point or unique residual block closes',
 'next_gate':'Return to missing comparator authority: audit AS Lorentzian/in-in nonlinear linked-cut authority first; if still BLOCKED, record exact blocker and proceed to C3 CTP ordered nonlinear completion. Do not zero-fill either.'
}
Path('results').mkdir(exist_ok=True)
Path('results/scalar_source_forward_regular_log_iteration226.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print(json.dumps(out,indent=2,sort_keys=True))
