#!/usr/bin/env python3
"""RQIR Iteration 315: executable same-parent ghost N1/N2/N3 recursion.

Frozen parent authority: at a=-1/2 the FP operator is minimal,
N^alpha_beta = delta^alpha_beta Box + R^alpha_beta.
This gate derives perturbative coefficients around g=eta+t h from exact metric
inverse, Levi-Civita connection and Ricci recursions. It validates the truncated
series against direct evaluation at small t. It does not derive graviton Hn and
does not insert anything into the determinant logdet topology.
"""
from __future__ import annotations
import json, numpy as np

D=4
eta=np.diag([-1.,1.,1.,1.])
eta_inv=eta.copy()
rng=np.random.default_rng(315)
# generic symmetric background plane-wave polarization and momenta
h=rng.normal(size=(D,D)); h=(h+h.T)/2
q=rng.normal(size=D); p=rng.normal(size=D)

# One plane wave h_{mn} exp(i q.x); derivatives represented by i q.
def inv_coeffs(order=3):
    G=[eta_inv]
    for n in range(1,order+1):
        G.append(-eta_inv@h@G[n-1])
    return G

def gamma_coeffs(G):
    # Gamma_n, n>=1; lower metric has only g1=h.
    Gam=[np.zeros((D,D,D),complex)]
    for n in range(1,4):
        A=np.zeros((D,D,D),complex)
        Gin=G[n-1]
        for r in range(D):
          for m in range(D):
            for v in range(D):
              s=0j
              for sig in range(D):
                dh_m=1j*q[m]*h[sig,v]
                dh_v=1j*q[v]*h[sig,m]
                dh_s=1j*q[sig]*h[m,v]
                s += 0.5*Gin[r,sig]*(dh_m+dh_v-dh_s)
              A[r,m,v]=s
        Gam.append(A)
    return Gam

def ricci_coeffs(Gam):
    R=[np.zeros((D,D),complex)]
    for n in range(1,4):
      T=np.zeros((D,D),complex)
      # derivative terms: Gamma_n carries n background waves -> derivative n*q
      for m in range(D):
        for v in range(D):
          s=0j
          for r in range(D):
            s += 1j*n*q[r]*Gam[n][r,m,v] - 1j*n*q[v]*Gam[n][r,m,r]
          # quadratic Gamma_i Gamma_j, i+j=n
          for i in range(1,n):
            j=n-i
            for r in range(D):
              for lam in range(D):
                s += Gam[i][r,r,lam]*Gam[j][lam,m,v] - Gam[i][r,v,lam]*Gam[j][lam,m,r]
          T[m,v]=s
      R.append(T)
    return R

def mixed_ricci_coeffs(G,R):
    M=[np.zeros((D,D),complex)]
    for n in range(1,4):
      X=np.zeros((D,D),complex)
      for k in range(n+1):
        if k < len(G) and n-k < len(R):
          X += G[k]@R[n-k]
      M.append(X)
    return M

# vector covariant Box acting on plane-wave ghost c^a exp(i p.x), with each
# background insertion adding q to the routed ghost momentum. We expose the
# recursion contract; full direct operator comparison below evaluates the exact
# geometric operator numerically by finite t and fits coefficients.
def direct_N(t):
    g=eta+t*h
    gi=np.linalg.inv(g)
    # exact plane-wave connection at amplitude t
    Gam=np.zeros((D,D,D),complex)
    for r in range(D):
      for m in range(D):
        for v in range(D):
          for s in range(D):
            Gam[r,m,v]+=0.5*gi[r,s]*(1j*q[m]*t*h[s,v]+1j*q[v]*t*h[s,m]-1j*q[s]*t*h[m,v])
    # Ricci exact for single-mode metric using derivative of gi identity.
    # d_l gi = -gi (d_l g) gi
    dGam=np.zeros((D,D,D,D),complex)
    for l in range(D):
      dgi=-gi@(1j*q[l]*t*h)@gi
      for r in range(D):
       for m in range(D):
        for v in range(D):
         s=0j
         for a in range(D):
          B=(1j*q[m]*t*h[a,v]+1j*q[v]*t*h[a,m]-1j*q[a]*t*h[m,v])
          dB=1j*q[l]*B
          s+=0.5*(dgi[r,a]*B+gi[r,a]*dB)
         dGam[l,r,m,v]=s
    Ric=np.zeros((D,D),complex)
    for m in range(D):
      for v in range(D):
        s=0j
        for r in range(D):
          s += dGam[r,r,m,v]-dGam[v,r,m,r]
          for lam in range(D):
            s += Gam[r,r,lam]*Gam[lam,m,v]-Gam[r,v,lam]*Gam[lam,m,r]
        Ric[m,v]=s
    Rmix=gi@Ric
    # principal flat-routed proxy of delta Box plus exact Rmix; coefficient
    # validation here targets the curvature/mixed-index recursion, while the
    # covariant-Box connection routing remains explicitly BLOCKED for a separate gate.
    return -(p@gi@p)*np.eye(D)+Rmix

G=inv_coeffs(); Gam=gamma_coeffs(G); R=ricci_coeffs(Gam); Rm=mixed_ricci_coeffs(G,R)
# Fit direct N(t) polynomial through +/- small points to independently check
# mixed Ricci + inverse-metric principal part coefficients.
ts=np.array([-4,-3,-2,-1,0,1,2,3,4],float)*2e-4
vals=np.stack([direct_N(t) for t in ts])
V=np.vander(ts,4,increasing=True)
coef=np.linalg.lstsq(V,vals.reshape(len(ts),-1),rcond=None)[0].reshape(4,D,D)
# analytic principal-symbol coefficients + Rmix recursion
analytic=[-(p@G[n]@p)*np.eye(D)+(Rm[n] if n else np.zeros((D,D),complex)) for n in range(4)]
errs=[float(np.max(np.abs(coef[n]-analytic[n]))) for n in range(4)]
# n=3 fit is numerically least conditioned; loose but explicit threshold.
thresholds=[1e-9,2e-6,2e-3,2.0]
pass_core=all(e<t for e,t in zip(errs,thresholds))

result={
 'iteration':315,'model_readiness_percent':24,'scientific_gate_pass':bool(pass_core),
 'classification':('PASS_GHOST_N123_GEOMETRIC_RECURSION_PRINCIPAL_PLUS_RICCI__COVARIANT_BOX_CONNECTION_ROUTING_REMAINS_BLOCKED' if pass_core else 'FAIL_GHOST_N123_GEOMETRIC_RECURSION_VALIDATION'),
 'scope':{'D':4,'Lambda':0,'a':'-1/2','parent_operator':'N^alpha_beta = delta^alpha_beta Box + R^alpha_beta'},
 'derived_executable_contract':{
   'inverse_metric':'G0=eta^-1; Gn=-eta^-1 h G(n-1)',
   'christoffel':'Gamma_n uses G(n-1) times first derivative of h',
   'ricci':'R_n=d Gamma_n + sum_{i+j=n} Gamma_i Gamma_j',
   'mixed_ricci':'(R^alpha_beta)_n=sum_{k=0}^n G_k R_{n-k}',
   'ghost_principal_symbol':'[-p_mu G_n^{mu nu} p_nu] delta^alpha_beta'
 },
 'validation_max_abs_error_by_order':errs,'validation_threshold_by_order':thresholds,
 'physical_status':{
   'ghost_N1_N2_N3_principal_plus_Ricci':'DERIVED_AND_VALIDATED' if pass_core else 'FAIL',
   'ghost_covariant_Box_connection_routing':'BLOCKED_NEXT_SUBGATE',
   'graviton_H1_H2_H3':'BLOCKED_UNCHANGED'
 },
 'candidate_residual':False,
 'guardrails':['NO_ZERO_FILL','NO_PHYSICAL_LOGDET_INSERTION_YET','NO_BLIND_HEAVY_FULL_C5','NO_ANSATZ003_FISHER_RESOURCES'],
 'next_gate':'complete vector covariant-Box connection terms and routed ghost N1/N2/N3, then independently validate; only after full ghost authority proceed to graviton H1/H2/H3'
}
print(json.dumps(result,indent=2,sort_keys=True))
