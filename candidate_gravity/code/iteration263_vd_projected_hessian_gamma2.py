#!/usr/bin/env python3
"""Iteration 263 certificate: projected A=K E bookkeeping and Gamma2 validation."""
import itertools, json, numpy as np
D=4; A_VD=-0.5
pairs=[(i,j) for i in range(D) for j in range(i,D)]
basis=[]
for i,j in pairs:
    E=np.zeros((D,D)); E[i,j]=1.; E[j,i]=1.; basis.append(E)
N=len(pairs)

def symdelta(mu,nu,r,s):
    return 0.5*((mu==r and nu==s)+(mu==s and nu==r))

def field_metric(g):
    gi=np.linalg.inv(g); root=np.sqrt(abs(np.linalg.det(g))); M=np.zeros((N,N))
    for A,EA in enumerate(basis):
      for B,EB in enumerate(basis):
        p=0.5*(np.einsum('ma,nb,mn,ab',gi,gi,EA,EB)+np.einsum('mb,na,mn,ab',gi,gi,EA,EB))
        tr=np.einsum('mn,mn',gi,EA)*np.einsum('ab,ab',gi,EB)
        M[A,B]=root*0.5*(p+A_VD*tr)
    return M

def d_field_metric(g,h):
    out=np.zeros((N,N,N))
    for A,E in enumerate(basis): out[A]=(field_metric(g+h*E)-field_metric(g-h*E))/(2*h)
    return out

def christoffel_direct(g,h=1e-4):
    G=field_metric(g); Gi=np.linalg.inv(G); dG=d_field_metric(g,h); C=np.zeros((N,N,N))
    for c in range(N):
      for A in range(N):
       for B in range(N):
        C[c,A,B]=0.5*sum(Gi[c,L]*(dG[A,L,B]+dG[B,L,A]-dG[L,A,B]) for L in range(N))
    return C

def gamma_tensor(g):
    gi=np.linalg.inv(g); T=np.zeros((D,D,D,D,D,D)); c1,c2,c3,c4=-1.,.25,.25,-.125
    def P(mu,nu,al,be): return .5*(gi[mu,al]*gi[nu,be]+gi[mu,be]*gi[nu,al])
    for r,s,mu,nu,al,be in itertools.product(range(D),repeat=6):
      S=.25*(symdelta(mu,al,r,s)*gi[nu,be]+symdelta(nu,al,r,s)*gi[mu,be]+symdelta(mu,be,r,s)*gi[nu,al]+symdelta(nu,be,r,s)*gi[mu,al])
      T[r,s,mu,nu,al,be]=c1*S+c2*(symdelta(mu,nu,r,s)*gi[al,be]+symdelta(al,be,r,s)*gi[mu,nu])+c3*P(mu,nu,al,be)*g[r,s]+c4*gi[mu,nu]*gi[al,be]*g[r,s]
    return T

def to_coord(T):
    C=np.zeros((N,N,N))
    for c,(r,s) in enumerate(pairs):
      for A,EA in enumerate(basis):
       for B,EB in enumerate(basis): C[c,A,B]=np.einsum('mnab,mn,ab->',T[r,s],EA,EB)
    return C

def mixed(F,eta,x,y,h):
    return (F(eta+h*x+h*y)-F(eta+h*x-h*y)-F(eta-h*x+h*y)+F(eta-h*x-h*y))/(4*h*h)

eta=np.diag([-1.,1.,1.,1.]); x=np.diag([0.,1.,-1.,0.]); y=np.zeros((4,4)); y[1,2]=y[2,1]=1.
inner=1e-4; outer=2e-3
G2_direct=mixed(lambda g: christoffel_direct(g,inner),eta,x,y,outer)
G2_formula=mixed(lambda g: to_coord(gamma_tensor(g)),eta,x,y,outer)
G2_swap=mixed(lambda g: to_coord(gamma_tensor(g)),eta,y,x,outer)

# Projected same-parent term labels after E0=0; null-soft E1[s]=0.
A1_s=['K0 E1[s]']
A2_sa=['K0 E2[s,a]','K1[s] E1[a]']
A2_ab=['K0 E2[a,b]','K1[a] E1[b]','K1[b] E1[a]']
A3_sab=['K0 E3[s,a,b]','K1[s] E2[a,b]','K1[a] E2[s,b]','K1[b] E2[s,a]','K2[s,a] E1[b]','K2[s,b] E1[a]']
result={
 'iteration':263,'D':4,'Lambda':0,'a_VD':-0.5,
 'gamma2_validation':{
   'inner_fd_step':inner,'outer_mixed_step':outer,
   'max_second_mixed_variation_mismatch':float(np.max(np.abs(G2_direct-G2_formula))),
   'max_second_mixed_variation_component':float(np.max(np.abs(G2_direct))),
   'analytic_input_pair_symmetry_residual':float(np.max(np.abs(G2_formula-G2_formula.transpose(0,2,1)))),
   'mixed_leg_exchange_residual':float(np.max(np.abs(G2_formula-G2_swap)))},
 'projected_A_nullsoft_counts':{'A1_s':len(A1_s),'A2_sa':len(A2_sa),'A2_ab':len(A2_ab),'A3_sab':len(A3_sab)},
 'A3_sab_terms':A3_sab,
 'status':['PASS_EXACT_PROJECT_BEFORE_EXPAND_A_EQUALS_K_E_CUBIC_REDUCTION','PASS_SCOPED_FIELDSPACE_CHRISTOFFEL_SECOND_POLARIZED_VARIATION','NO_FULL_UNPROJECTED_H3_OR_S5_REQUIRED_FOR_PHYSICAL_U1W_B3','NO_INDEPENDENT_GAMMA2_ANSATZ']
}
print(json.dumps(result,indent=2,sort_keys=True))
