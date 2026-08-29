"""RQIR Iteration 026: D2 calibration-branch Fisher comparison.

Compares three D2 calibration operators on one hard trace+energy constrained
source space:
  NP3-null: original 14 potential means + 8 covariance rows;
  native-replace: 14 force-gradient means replace potential means;
  augmented: original means + force-gradient means + covariance rows.

The hidden-state amplitude is restored as an explicit nuisance.  This avoids
mistaking a rank change for beta identifiability.  All rows are row-normalized.
The numerical gamma values are the corrected Iteration-015 D2 90%-retention
benchmark and therefore are a local Fisher diagnostic, not a hardware forecast.
"""
from __future__ import annotations
import numpy as np

D=5
E=np.array([1.,2.,3.,4.,6.])
H=np.diag(E).astype(complex)
EPS=0.08
Y1=-3.7766873836695947
TIMES=np.array([0.,3.09855988,3.45849306,2.93830159,4.13016958,4.84480925,4.99085067])
TR=float(TIMES[2])
GM=2.414e6
GC=0.929e6


def herm_vec(a):
    out=[a[i,i].real for i in range(D)]
    for i in range(D):
        for j in range(i+1,D):
            out += [np.sqrt(2)*a[i,j].real,np.sqrt(2)*a[i,j].imag]
    return np.asarray(out,float)


def mat(v):
    a=np.zeros((D,D),complex); k=0
    for i in range(D): a[i,i]=v[k]; k+=1
    for i in range(D):
        for j in range(i+1,D):
            a[i,j]=(v[k]+1j*v[k+1])/np.sqrt(2)
            a[j,i]=a[i,j].conjugate(); k+=2
    return a


def evolve(a,t):
    return a*np.exp(1j*(E[:,None]-E[None,:])*t)


def sym(a,b): return (a@b+b@a)/2


def source_geometry():
    rng=np.random.default_rng(314159)
    for _ in range(812):
        x=rng.normal(size=(D,D)); braw=(x+x.T)/2
    ev=np.linalg.eigvalsh(braw)
    bpos=braw+(-ev.min()+1)*np.eye(D)
    vals,v=np.linalg.eigh(bpos)
    return vals,v,float(vals.max())


VALS,V,SCALE=source_geometry()


def probe(y):
    return (V@np.diag(1/np.abs(SCALE/VALS-y))@V.T).astype(complex)


def grad_probe(y):
    a=SCALE/VALS-y
    return (V@np.diag(1/a**2)@V.T).astype(complex)


def harmonic(delta,readout,pump,n):
    rw=np.zeros_like(readout,complex)
    for i in range(D):
        for j in range(D):
            if int(round(E[i]-E[j]))==n: rw[i,j]=readout[i,j]
    return 2*np.trace(delta@((rw@pump-pump@rw)/(2j)))


def build():
    p=[probe(0.),probe(Y1)]
    rows=[herm_vec(np.eye(D)),herm_vec(H)]
    labels=['trace','energy']
    for k in (0,1):
        for t in TIMES:
            rows.append(herm_vec(evolve(p[k],float(t)))); labels.append('mean')
    rows.append(herm_vec(sym(evolve(p[0],TR),p[0]))); labels.append('cov')
    extra=[(0,1,TIMES[1]),(1,1,TIMES[5]),(1,0,TR),(0,1,TR),
           (1,0,TIMES[3]),(0,0,TIMES[6]),(0,1,TIMES[6])]
    for k,l,t in extra:
        rows.append(herm_vec(sym(evolve(p[k],float(t)),p[l]))); labels.append('cov')
    A=np.vstack(rows); A=A/np.linalg.norm(A,axis=1,keepdims=True)
    _,sv,vh=np.linalg.svd(A,full_matrices=True)
    n=vh[-1]
    d0=mat(n); d0/=np.max(np.abs(np.linalg.eigvalsh(d0)))
    theta0=2*EPS*herm_vec(d0)

    grad=(V@np.diag((VALS/SCALE)**2)@V.T).astype(complex)
    B=np.zeros((4,D*D),float)
    for j in range(D*D):
        e=np.zeros(D*D); e[j]=1.; op=mat(e)
        h2=harmonic(op,grad,p[0],2); h4=harmonic(op,grad,p[0],4)
        B[:,j]=[h2.real,h2.imag,h4.real,h4.imag]
    B/=np.linalg.norm(B@theta0)
    s=B@theta0

    G=[]
    for k,y in [(0,0.),(1,Y1)]:
        gp=grad_probe(y)
        for t in TIMES: G.append(herm_vec(evolve(gp,float(t))))
    G=np.vstack(G); G=G/np.linalg.norm(G,axis=1,keepdims=True)

    # Exact trace+energy elimination.
    _,ss,vhh=np.linalg.svd(A[:2],full_matrices=True)
    Z=vhh[int(np.sum(ss>1e-12)):].T
    q=theta0/np.linalg.norm(theta0)
    P=Z-np.outer(q,q@Z)
    U,sp,_=np.linalg.svd(P,full_matrices=False)
    Zu=U[:,sp>1e-10]
    assert Z.shape==(25,23) and Zu.shape==(25,22)
    assert np.linalg.norm(A[:2]@Z)<1e-12
    assert np.max(np.abs(q@Zu))<1e-12
    return A,np.asarray(labels),G,theta0,B,s,Z,Zu,sv


def branch_rows(A,labels,G,kind):
    im=np.where(labels=='mean')[0]; ic=np.where(labels=='cov')[0]
    if kind=='null':
        return np.vstack([A[im],A[ic]]), np.r_[np.full(len(im),GM),np.full(len(ic),GC)]
    if kind=='native_replace':
        return np.vstack([G,A[ic]]), np.r_[np.full(len(G),GM),np.full(len(ic),GC)]
    if kind=='augmented':
        return np.vstack([A[im],G,A[ic]]), np.r_[np.full(len(im)+len(G),GM),np.full(len(ic),GC)]
    raise ValueError(kind)


def profiled(A,labels,G,theta0,B,s,Zu,kind,c_a=0.,scale=1.):
    # params = beta, fractional hidden amplitude alpha, 22 orthogonal source nuisances
    Jd=np.column_stack([s,s,B@Zu])
    F=Jd.T@Jd
    M,W=branch_rows(A,labels,G,kind); W=W*scale
    Jc=np.column_stack([M@theta0,M@Zu])
    F[1:,1:]+=Jc.T@(W[:,None]*Jc)
    F[1,1]+=c_a
    N=F[1:,1:]; c=F[0,1:]
    return float(F[0,0]-c@np.linalg.pinv(N,rcond=1e-13)@c)


def main():
    A,labels,G,theta0,B,s,Z,Zu,sv=build()
    print('original rank=',np.linalg.matrix_rank(A,1e-12),'smin=',sv[-1])
    for kind in ['null','native_replace','augmented']:
        M,_=branch_rows(A,labels,G,kind)
        MR=M@Z
        uu,ss,vh=np.linalg.svd(MR,full_matrices=True)
        rank=int(np.sum(ss>1e-12))
        print('\n',kind,'hard-subspace rank=',rank,'/23')
        if rank<23:
            znull=Z@vh[-1]; znull/=np.linalg.norm(znull)
            q=theta0/np.linalg.norm(theta0)
            bz=B@znull
            print(' overlap with old hidden=',abs(znull@q))
            print(' detector null norm=',np.linalg.norm(bz))
            print(' detector alignment with beta signal=',abs(s@bz)/np.linalg.norm(bz))
        for ca in [0.,1.,10.,100.,225.,1e12]:
            print(' C_a=',ca,'Fbeta=',profiled(A,labels,G,theta0,B,s,Zu,kind,ca))

    # Augmented branch: calibration-only scale needed for 90% with no prep prior.
    lo,hi=1.,100.
    for _ in range(70):
        mid=np.sqrt(lo*hi)
        if profiled(A,labels,G,theta0,B,s,Zu,'augmented',0.,mid)>=0.9: hi=mid
        else: lo=mid
    print('\naugmented scale for Fbeta=0.9 with C_a=0:',hi)

    # Regression guards.
    Mn,_=branch_rows(A,labels,G,'native_replace')
    assert np.linalg.matrix_rank(Mn@Z,1e-12)==22
    _,_,vhn=np.linalg.svd(Mn@Z,full_matrices=True)
    zn=Z@vhn[-1]; zn/=np.linalg.norm(zn)
    assert 0.74<abs(zn@(theta0/np.linalg.norm(theta0)))<0.77
    assert abs(s@(B@zn))/np.linalg.norm(B@zn)>0.97
    f_native_inf=profiled(A,labels,G,theta0,B,s,Zu,'native_replace',0.,1e4)
    assert 0.040<f_native_inf<0.045
    f_aug=profiled(A,labels,G,theta0,B,s,Zu,'augmented',0.)
    assert 0.64<f_aug<0.66
    assert 4.7<hi<5.1

if __name__=='__main__': main()
