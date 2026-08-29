"""RQIR Iteration 030: finite-reference D2 potential transduction audit.

A D2 force readout does not directly measure the Toy009/Toy010 absolute
potential row B(y).  A force-integral implementation measures the relational
potential difference B(y)-B(y_ref).  This script quantifies the geometry/rate
tradeoff for the current balanced calibration baseline.

White-force model convention: for a one-sided flat equivalent-force PSD S_F,
a time-T average has variance S_F/(2T).  Uniformly integrating force over a
path of length L then gives Var[int F dy] = L^2 S_F/(2T).  Common factors cancel
in the rate ratios reported below.
"""
from __future__ import annotations
import numpy as np

D=5
E=np.array([1.,2.,3.,4.,6.])
H=np.diag(E).astype(complex)
Y1=-3.7766873836695947
TIMES=np.array([0.,3.09855988,3.45849306,2.93830159,4.13016958,4.84480925,4.99085067])
TR=float(TIMES[2])


def herm_vec(a):
    out=[a[i,i].real for i in range(D)]
    for i in range(D):
        for j in range(i+1,D):
            out += [np.sqrt(2)*a[i,j].real,np.sqrt(2)*a[i,j].imag]
    return np.asarray(out,float)


def evolve(a,t):
    return a*np.exp(1j*(E[:,None]-E[None,:])*t)


def sym(a,b):
    return (a@b+b@a)/2


def source_geometry():
    rng=np.random.default_rng(314159)
    for _ in range(812):
        x=rng.normal(size=(D,D)); braw=(x+x.T)/2
    ev=np.linalg.eigvalsh(braw)
    bpos=braw+(-ev.min()+1)*np.eye(D)
    vals,v=np.linalg.eigh(bpos)
    scale=float(vals.max())
    return vals,v,scale


VALS,V,SCALE=source_geometry()
RADII=SCALE/VALS


def probe(y):
    w=1/np.abs(RADII-y)
    return (V@np.diag(w)@V.T).astype(complex)


def grad_probe(y):
    a=RADII-y
    return (V@np.diag(1/a**2)@V.T).astype(complex)


def calibration_matrix(yref=None):
    ps=[]
    for y in (0.0,Y1):
        p=probe(y) if yref is None else probe(y)-probe(yref)
        ps.append(p)
    rows=[herm_vec(np.eye(D)),herm_vec(H)]
    for k in (0,1):
        for t in TIMES:
            rows.append(herm_vec(evolve(ps[k],float(t))))
    rows.append(herm_vec(sym(evolve(ps[0],TR),ps[0])))
    extra=[(0,1,TIMES[1]),(1,1,TIMES[5]),(1,0,TR),(0,1,TR),
           (1,0,TIMES[3]),(0,0,TIMES[6]),(0,1,TIMES[6])]
    for k,l,t in extra:
        rows.append(herm_vec(sym(evolve(ps[k],float(t)),ps[l])))
    A=np.vstack(rows)
    return A/np.linalg.norm(A,axis=1,keepdims=True)


def null_summary(yref):
    A=calibration_matrix(yref)
    _,sv,vh=np.linalg.svd(A,full_matrices=True)
    return np.linalg.matrix_rank(A,tol=1e-12),sv[-1],vh[-1]


def native_rates(yref):
    # Return q_pot and q_force in units with S_F=1.  q values are for a
    # normalized nuisance coordinate aligned with each raw Hermitian row.
    qp=[]; qf=[]
    for y in (0.0,Y1):
        db=probe(y)-probe(yref)
        g=grad_probe(y)
        L=abs(y-yref)
        nb=np.linalg.norm(herm_vec(db))
        ng=np.linalg.norm(herm_vec(g))
        qp.append(2*nb**2/L**2)
        qf.append(2*ng**2)
    return np.asarray(qp),np.asarray(qf)


def main():
    rank0,s0,n0=null_summary(None)
    print('absolute baseline rank,smin=',rank0,s0)
    assert rank0==24
    assert abs(s0-0.001999540405542146)<2e-12

    refs=[-5.,-10.,-20.,-50.,-100.,-1000.]
    for yr in refs:
        rank,smin,n=null_summary(yr)
        overlap=abs(float(n@n0))
        old_res=float(np.linalg.norm(calibration_matrix(None)@n))
        qp,qf=native_rates(yr)
        # 7 time settings per probe; equal corrected GM cancels.
        Kp=7*np.sum(1/qp)
        Kf=7*np.sum(1/qf)
        x=Kf/Kp
        print(f'yref={yr:8.1f} rank={rank} smin={smin:.12g} overlap={overlap:.12g} '
              f'old_res={old_res:.12g} qp/qf={qp/qf} x={x:.12g}')
        assert rank==24

    # Regression values used in the document.
    _,s10,n10=null_summary(-10.)
    qp10,qf10=native_rates(-10.)
    x10=(7*np.sum(1/qf10))/(7*np.sum(1/qp10))
    assert abs(abs(n10@n0)-0.9992856122196577)<2e-12
    assert abs(s10-0.0025148744378673455)<2e-12
    assert np.allclose(qp10/qf10,[0.011360124596838786,0.21491011744747499],rtol=2e-12)
    assert abs(x10-0.20115783800509573)<2e-12

    _,_,n100=null_summary(-100.)
    qp100,qf100=native_rates(-100.)
    x100=(7*np.sum(1/qf100))/(7*np.sum(1/qp100))
    assert abs(abs(n100@n0)-0.9999995341087619)<2e-12
    assert abs(x100-0.0026838077840484545)<2e-12

if __name__=='__main__':
    main()
