#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 185.

Exact multilinear plane-wave expansion through cubic order for
  sqrt(-g) R_mn Box^n R^mn, n=0..4,
on the six frozen null-soft TT rows.  The recursive covariant Box acting on a
rank-2 tensor includes connection and inverse-metric variations, so n>=2 is not
inferred by multiplying lower-order columns by powers of q^2.

The script reports the n=2,3,4 soft2 columns and source-completed Ward checks.
"""
import itertools, json, math
from pathlib import Path
import numpy as np

ETA=np.diag([-1.,1.,1.,1.])
QS=[np.array(x,float) for x in [[0.18,0.70,0.20,0.10],[0.14,0.55,-0.25,0.20],[0.22,0.62,0.18,-0.24],[0.16,0.48,0.31,0.12],[0.20,0.58,-0.16,-0.28],[0.12,0.44,0.27,-0.19]]]
k0=np.array([1.,0.,0.,1.])
e_soft=np.zeros((4,4)); e_soft[1,1]=1/math.sqrt(2); e_soft[2,2]=-1/math.sqrt(2)
seeds=[]
for i in range(12):
    rng=np.random.default_rng(17700+i); A=rng.normal(size=(4,4)); seeds.append((A+A.T)/2)
HS=np.array([0.01,0.005,0.0025,0.00125,0.000625])

def dot(a,b): return float(a@ETA@b)
def theta(k):
    kc=ETA@k; return ETA-np.outer(kc,kc)/dot(k,k)
def p2(k):
    t=theta(k); return .5*(np.einsum('mr,ns->mnrs',t,t)+np.einsum('ms,nr->mnrs',t,t))-(1/3)*np.einsum('mn,rs->mnrs',t,t)
def polarization(k,seed):
    P=p2(k); e=np.einsum('mnrs,ra,sb,ab->mn',P,ETA,ETA,seed)
    n=np.einsum('mn,ma,nb,ab',e,ETA,ETA,e); return e/np.sqrt(abs(n))

def subsets(mask):
    s=mask
    while True:
        yield s
        if s==0: break
        s=(s-1)&mask

def prod(A,B,op=lambda a,b:a*b):
    C={}
    for ma,a in A.items():
        for mb,b in B.items():
            if ma&mb: continue
            m=ma|mb; v=op(a,b); C[m]=C.get(m,0)+v
    return C

def deriv(A,ks,axis):
    C={}
    for m,a in A.items():
        if m==0: C[m]=np.zeros_like(a,dtype=complex)
        else:
            K=sum((ks[i] for i in range(len(ks)) if m>>i&1),np.zeros(4))
            C[m]=1j*(ETA@K)[axis]*a
    return C

def matrix_inv_series(g):
    gi={0:ETA.astype(complex)}; nbits=max(g).bit_length()
    for bits in range(1,nbits+1):
        for m in range(1,1<<nbits):
            if m.bit_count()!=bits: continue
            acc=np.zeros((4,4),complex)
            for a in [1<<i for i in range(nbits)]:
                if m&a and a in g: acc += g[a]@gi[m^a]
            gi[m]=-ETA@acc
    return gi

def series_entry(A,i,j): return {m:v[i,j] for m,v in A.items()}
def determinant_series(g):
    D={}
    for perm in itertools.permutations(range(4)):
        inv=sum(perm[i]>perm[j] for i in range(4) for j in range(i+1,4)); sgn=(-1)**inv
        T={0:1+0j}
        for i,j in enumerate(perm): T=prod(T,series_entry(g,i,j))
        for m,v in T.items(): D[m]=D.get(m,0)+sgn*v
    return D

def sqrt_series(Y):
    S={0:complex(np.sqrt(Y[0]))}; nbits=max(Y).bit_length()
    for bits in range(1,nbits+1):
        for m in range(1,1<<nbits):
            if m.bit_count()!=bits: continue
            rest=0j
            for a in subsets(m):
                b=m^a
                if a and b and a in S and b in S: rest += S[a]*S[b]
            S[m]=(Y.get(m,0)-rest)/(2*S[0])
    return S

def build_geom(ks,es):
    g={0:ETA.astype(complex)}
    for i,e in enumerate(es): g[1<<i]=e.astype(complex)
    gi=matrix_inv_series(g); dg=[deriv(g,ks,l) for l in range(4)]
    nm=1<<len(ks); G={m:np.zeros((4,4,4),complex) for m in range(nm)}
    for mg,gv in gi.items():
        for md in range(nm):
            if mg&md or md not in dg[0]: continue
            M=mg|md
            for rho,mu,nu in itertools.product(range(4),repeat=3):
                G[M][rho,mu,nu]+=.5*sum(gv[rho,s]*(dg[mu][md][s,nu]+dg[nu][md][s,mu]-dg[s][md][mu,nu]) for s in range(4))
    dG=[deriv(G,ks,l) for l in range(4)]
    Ric={m:np.zeros((4,4),complex) for m in range(nm)}
    for m in range(nm):
        for mu,nu in itertools.product(range(4),repeat=2):
            Ric[m][mu,nu]+=sum(dG[rho][m][rho,mu,nu]-dG[nu][m][rho,mu,rho] for rho in range(4))
    GG=prod(G,G,op=lambda A,B:np.einsum('rrl,lmn->mn',A,B)-np.einsum('rnl,lmr->mn',A,B))
    for m,v in GG.items(): Ric[m]+=v
    sqrtg=sqrt_series({m:-v for m,v in determinant_series(g).items()})
    return gi,G,Ric,sqrtg

def covder_rank2(T,ks,G):
    nm=1<<len(ks); N={m:np.zeros((4,4,4),complex) for m in range(nm)}
    for l in range(4):
        dT=deriv(T,ks,l)
        for m,v in dT.items(): N[m][l]+=v
    GT=prod(G,T,op=lambda A,B:np.einsum('rlm,rn->lmn',A,B)+np.einsum('rln,mr->lmn',A,B))
    for m,v in GT.items(): N[m]-=v
    return N

def box_rank2(T,ks,gi,G):
    N=covder_rank2(T,ks,G); nm=1<<len(ks)
    P={m:np.zeros((4,4,4,4),complex) for m in range(nm)}
    for a in range(4):
        dN=deriv(N,ks,a)
        for m,v in dN.items(): P[m][a]+=v
    GN=prod(G,N,op=lambda A,B:(np.einsum('rab,rmn->abmn',A,B)+np.einsum('ram,brn->abmn',A,B)+np.einsum('ran,bmr->abmn',A,B)))
    for m,v in GN.items(): P[m]-=v
    return prod(gi,P,op=lambda A,B:np.einsum('ab,abmn->mn',A,B))

def action_coeff(ks,es,n):
    gi,G,Ric,sqrtg=build_geom(ks,es); T=Ric
    for _ in range(n): T=box_rank2(T,ks,gi,G)
    RT=prod(Ric,T,op=lambda A,B:np.einsum('mn,ab->mnab',A,B))
    gi2=prod(gi,gi,op=lambda A,B:np.einsum('ma,nb->mnab',A,B))
    contr=prod(gi2,RT,op=lambda A,B:np.einsum('mnab,mnab',A,B))
    return prod(sqrtg,contr).get((1<<len(ks))-1,0).real

def row_kin(i,e):
    q=QS[i]; ks=[e*k0,q,-q-e*k0]
    return ks,[e_soft,polarization(ks[1],seeds[2*i]),polarization(ks[2],seeds[2*i+1])]

def soft2(i,n):
    f0=action_coeff(*row_kin(i,0),n); c=[]
    for h in HS:
        c.append((action_coeff(*row_kin(i,h),n)+action_coeff(*row_kin(i,-h),n)-2*f0)/(2*h*h))
    r1=[(4*c[j+1]-c[j])/3 for j in range(len(c)-1)]
    r2=[(16*r1[j+1]-r1[j])/15 for j in range(len(r1)-1)]
    return r2[-1],abs(r2[-1]-r2[-2])

def linear_gauge(k,xi):
    kc=ETA@k; xic=ETA@xi; return np.outer(kc,xic)+np.outer(xic,kc)
def nonlinear_lie(kxi,xi,kh,e):
    kcxi=ETA@kxi; kch=ETA@kh; out=(xi@kch)*e.copy()
    for m,n in itertools.product(range(4),repeat=2):
        out[m,n]+=kcxi[m]*sum(e[r,n]*xi[r] for r in range(4))+kcxi[n]*sum(e[m,r]*xi[r] for r in range(4))
    return out

def ward_row(i,n,esoft=.01):
    q=QS[i]; k1=esoft*k0; k2=q; k3=-q-k1
    e2=polarization(k2,seeds[2*i]); e3=polarization(k3,seeds[2*i+1]); xi=np.array([.31,-.27,.19,.41])
    L=linear_gauge(k1,xi); N2=nonlinear_lie(k1,xi,k2,e2); N3=nonlinear_lie(k1,xi,k3,e3)
    cubic=action_coeff([k1,k2,k3],[L,e2,e3],n)
    contact=action_coeff([k1+k2,k3],[N2,e3],n)+action_coeff([k2,k1+k3],[e2,N3],n)
    return cubic+contact,abs(cubic+contact)/max(abs(cubic),abs(contact),1e-30)

if __name__=='__main__':
    columns={}; errors={}; ward={}
    for n in range(5):
        rr=[soft2(i,n) for i in range(6)]
        columns[str(n)]=[float(z[0]) for z in rr]; errors[str(n)]=float(max(z[1] for z in rr))
        if n>=2:
            ww=[ward_row(i,n) for i in range(6)]
            ward[str(n)]={'max_abs':float(max(abs(z[0]) for z in ww)),'max_relative':float(max(z[1] for z in ww))}
    out={'iteration':185,'columns':columns,'max_soft2_error':errors,'ward':ward,'model_readiness_percent':24}
    Path('results/c5_local_quadratic_soft2_completion_iteration185_reproduced.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
