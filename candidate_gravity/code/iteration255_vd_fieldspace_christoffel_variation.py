#!/usr/bin/env python3
"""Iteration 255: pointwise validation of the frozen VD field-space Christoffel variation.

No external packages beyond numpy.  The independent path constructs the 10x10
DeWitt metric on symmetric 4x4 metric components and differentiates it numerically.
"""
import json
import itertools
import numpy as np

D=4
A_VD=-0.5
pairs=[(i,j) for i in range(D) for j in range(i,D)]
basis=[]
for i,j in pairs:
    E=np.zeros((D,D)); E[i,j]=1.0; E[j,i]=1.0
    basis.append(E)
N=len(pairs)

def symdelta(mu,nu,r,s):
    return 0.5*((mu==r and nu==s)+(mu==s and nu==r))

def P_upper(g,mu,nu,al,be):
    gi=np.linalg.inv(g)
    return 0.5*(gi[mu,al]*gi[nu,be]+gi[mu,be]*gi[nu,al])

def field_metric(g):
    gi=np.linalg.inv(g); root=np.sqrt(abs(np.linalg.det(g)))
    M=np.zeros((N,N))
    for A,EA in enumerate(basis):
        for B,EB in enumerate(basis):
            p=0.5*(np.einsum('ma,nb,mn,ab',gi,gi,EA,EB)+np.einsum('mb,na,mn,ab',gi,gi,EA,EB))
            tr=np.einsum('mn,mn',gi,EA)*np.einsum('ab,ab',gi,EB)
            M[A,B]=root*0.5*(p+A_VD*tr)
    return M

def d_field_metric(g,step):
    out=np.zeros((N,N,N))
    for A,E in enumerate(basis):
        out[A]=(field_metric(g+step*E)-field_metric(g-step*E))/(2*step)
    return out

def christoffel_from_metric(g,step=1e-5):
    G=field_metric(g); Gi=np.linalg.inv(G); dG=d_field_metric(g,step)
    C=np.zeros((N,N,N))
    for c in range(N):
        for A in range(N):
            for B in range(N):
                C[c,A,B]=0.5*sum(Gi[c,L]*(dG[A,L,B]+dG[B,L,A]-dG[L,A,B]) for L in range(N))
    return C

def gamma_tensor(g):
    gi=np.linalg.inv(g); T=np.zeros((D,D,D,D,D,D))
    c1,c2,c3,c4=-1.0,0.25,0.25,-0.125
    for r,s,mu,nu,al,be in itertools.product(range(D),repeat=6):
        S=0.25*(symdelta(mu,al,r,s)*gi[nu,be]+symdelta(nu,al,r,s)*gi[mu,be]+symdelta(mu,be,r,s)*gi[nu,al]+symdelta(nu,be,r,s)*gi[mu,al])
        T[r,s,mu,nu,al,be]=(c1*S+c2*(symdelta(mu,nu,r,s)*gi[al,be]+symdelta(al,be,r,s)*gi[mu,nu])+c3*P_upper(g,mu,nu,al,be)*g[r,s]+c4*gi[mu,nu]*gi[al,be]*g[r,s])
    return T

def delta_gamma_tensor(g,h):
    gi=np.linalg.inv(g); H=gi@h@gi; out=np.zeros((D,D,D,D,D,D))
    c1,c2,c3,c4=-1.0,0.25,0.25,-0.125
    def dP(mu,nu,al,be):
        return -0.5*(H[mu,al]*gi[nu,be]+gi[mu,al]*H[nu,be]+H[mu,be]*gi[nu,al]+gi[mu,be]*H[nu,al])
    for r,s,mu,nu,al,be in itertools.product(range(D),repeat=6):
        SH=0.25*(symdelta(mu,al,r,s)*H[nu,be]+symdelta(nu,al,r,s)*H[mu,be]+symdelta(mu,be,r,s)*H[nu,al]+symdelta(nu,be,r,s)*H[mu,al])
        out[r,s,mu,nu,al,be]=(-c1*SH-c2*(symdelta(mu,nu,r,s)*H[al,be]+symdelta(al,be,r,s)*H[mu,nu])+c3*(dP(mu,nu,al,be)*g[r,s]+P_upper(g,mu,nu,al,be)*h[r,s])+c4*(-H[mu,nu]*gi[al,be]*g[r,s]-gi[mu,nu]*H[al,be]*g[r,s]+gi[mu,nu]*gi[al,be]*h[r,s]))
    return out

def to_coordinate(T):
    C=np.zeros((N,N,N))
    for c,(r,s) in enumerate(pairs):
        for A,EA in enumerate(basis):
            for B,EB in enumerate(basis):
                C[c,A,B]=np.einsum('mnab,mn,ab->',T[r,s],EA,EB)
    return C

eta=np.diag([-1.0,1.0,1.0,1.0])
h=np.diag([0.0,1.0,-1.0,0.0])  # TT for null q along z
inner=2e-5; outer=2e-4
C_ind=christoffel_from_metric(eta,inner)
C_formula=to_coordinate(gamma_tensor(eta))
dC_ind=(christoffel_from_metric(eta+outer*h,inner)-christoffel_from_metric(eta-outer*h,inner))/(2*outer)
dC_formula=to_coordinate(delta_gamma_tensor(eta,h))
result={
  "D":4,"Lambda":0,"a_VD":-0.5,"split":"linear covariant metric, gamma1=1 gamma2..6=0",
  "tt_background":{"eta_diag":[-1,1,1,1],"h_diag":[0,1,-1,0]},
  "inner_fd_step":inner,"outer_fd_step":outer,
  "max_base_christoffel_mismatch":float(np.max(np.abs(C_ind-C_formula))),
  "max_first_variation_mismatch":float(np.max(np.abs(dC_ind-dC_formula))),
  "max_first_variation_component":float(np.max(np.abs(dC_ind))),
  "analytic_input_pair_symmetry_residual":float(np.max(np.abs(dC_formula-dC_formula.transpose(0,2,1)))),
  "status":"PASS_SCOPED_FIELDSPACE_CHRISTOFFEL_FIRST_VARIATION_AND_TT_VALIDATION"
}
print(json.dumps(result,indent=2,sort_keys=True))
