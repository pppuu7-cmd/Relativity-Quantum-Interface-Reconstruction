#!/usr/bin/env python3
"""Shared deterministic KLT/Parke-Taylor helper for RQIR pure-Einstein 5-graviton cut work.

Derived without physics changes from Iterations 212-213.  It contains only
kinematics/tree-amplitude/cut-integrand functions and performs no calculations
on import.
"""
import cmath, math
import numpy as np


def dot4(p,q):
    return float(p[0]*q[0]-np.dot(p[1:],q[1:]))


def spinors_from_p(p):
    E,px,py,pz = map(float,p)
    zp,zm = complex(E+pz),complex(E-pz)
    if abs(zp)>=abs(zm) and abs(zp)>1e-14:
        a=cmath.sqrt(zp)
        lam=np.array([a,(px+1j*py)/a],complex)
        til=np.array([a,(px-1j*py)/a],complex)
    elif abs(zm)>1e-14:
        b=cmath.sqrt(zm)
        lam=np.array([(px-1j*py)/b,b],complex)
        til=np.array([(px+1j*py)/b,b],complex)
    else:
        raise ValueError('degenerate null momentum')
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
    nx,ny=0.35,-0.25
    nz=math.sqrt(1-nx*nx-ny*ny)
    n5=np.array([nx,ny,nz],float)
    P1=np.array([0.5,0,0,0.5],float)
    P2=np.array([0.5,0,0,-0.5],float)
    P5=np.r_[epsilon,epsilon*n5]
    P34=np.array([1.,0,0,0])-P5
    mass=math.sqrt(dot4(P34,P34)); Estar=mass/2
    nstar=np.array([math.sin(theta_star)*math.cos(phi_star),
                    math.sin(theta_star)*math.sin(phi_star),
                    math.cos(theta_star)])
    q3=np.r_[Estar,Estar*nstar]; q4=np.r_[Estar,-Estar*nstar]
    beta=P34[1:]/P34[0]
    b2=float(np.dot(beta,beta)); gamma=1/math.sqrt(1-b2)
    def boost(q):
        E=q[0]; pv=q[1:]; bd=float(np.dot(beta,pv))
        pnew=pv+(((gamma-1)*bd/b2)+gamma*E)*beta if b2>0 else pv
        return np.r_[gamma*(E+bd),pnew]
    P3,P4=boost(q3),boost(q4)
    return [-P1,-P2,P3,P4,P5]


def cut_integrand_vec(epsilon,n,h1=1,h2=1):
    ks=physical_2to3(epsilon)
    n=np.asarray(n,float)
    ell1=np.r_[0.5,0.5*n]; ell2=np.r_[0.5,-0.5*n]
    left=[ks[0],ks[1],ell1,ell2]
    right=[ks[2],ks[3],ks[4],-ell1,-ell2]
    return m4(left,[-1,-1,h1,h2])*m5(right,[1,1,1,-h1,-h2])


def external_m5(epsilon):
    return m5(physical_2to3(epsilon),[-1,-1,1,1,1])


def spherical(theta,phi):
    return np.array([math.sin(theta)*math.cos(phi),
                     math.sin(theta)*math.sin(phi),
                     math.cos(theta)],float)
