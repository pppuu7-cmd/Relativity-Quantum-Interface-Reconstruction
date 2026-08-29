"""RQIR Iteration 025: D2 force-calibration null audit.

Tests whether replacing the Toy009 potential-mean calibration rows by directly
measured Newtonian force/gradient rows preserves the exact NP3 hidden source
direction.  It does not for the current source/calibration geometry.

This matters because a D2 force sensor is not automatically a physical
implementation of the existing potential-row calibration Fisher.  Adding
force-gradient rows changes the calibration operator and can destroy the exact
null on which RQIR-NG-005 and the detector comparison are conditioned.
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
    vals,v=np.linalg.eigh(bpos); scale=float(vals.max())
    return vals,v,scale


def probe(vals,v,scale,y):
    w=1/np.abs((scale/vals)-y)
    return (v@np.diag(w)@v.T).astype(complex)


def grad_probe(vals,v,scale,y):
    # At the current y=0 and y=Y1<0 all denominators are positive, so
    # d/dy [1/(scale/vals-y)] = +1/(scale/vals-y)^2.
    a=(scale/vals)-y
    return (v@np.diag(1/a**2)@v.T).astype(complex)


def toy009_matrix():
    vals,v,scale=source_geometry()
    p=[probe(vals,v,scale,0.0),probe(vals,v,scale,Y1)]
    rows=[herm_vec(np.eye(D)),herm_vec(H)]
    for k in (0,1):
        for t in TIMES:
            rows.append(herm_vec(evolve(p[k],float(t))))
    rows.append(herm_vec(sym(evolve(p[0],TR),p[0])))
    extra=[(0,1,TIMES[1]),(1,1,TIMES[5]),(1,0,TR),(0,1,TR),
           (1,0,TIMES[3]),(0,0,TIMES[6]),(0,1,TIMES[6])]
    for k,l,t in extra:
        rows.append(herm_vec(sym(evolve(p[k],float(t)),p[l])))
    A=np.vstack(rows)
    A=A/np.linalg.norm(A,axis=1,keepdims=True)
    return A,vals,v,scale


def force_mean_rows(vals,v,scale):
    g=[grad_probe(vals,v,scale,0.0),grad_probe(vals,v,scale,Y1)]
    rows=[]
    for k in (0,1):
        for t in TIMES:
            rows.append(herm_vec(evolve(g[k],float(t))))
    G=np.vstack(rows)
    return G/np.linalg.norm(G,axis=1,keepdims=True)


def main():
    A,vals,v,scale=toy009_matrix()
    _,sv,vh=np.linalg.svd(A,full_matrices=True)
    n=vh[-1]
    assert A.shape==(24,25)
    assert np.linalg.matrix_rank(A,tol=1e-12)==24
    assert np.linalg.norm(A@n)<1e-12
    assert abs(sv[-1]-0.001999540405542146)<2e-12

    G=force_mean_rows(vals,v,scale)
    p=G@n
    print('abs force-row projections on Toy009 hidden direction=',np.abs(p))
    print('max projection=',np.max(np.abs(p)))
    print('rms projection=',np.sqrt(np.mean(p*p)))

    Aaug=np.vstack([A,G])
    saug=np.linalg.svd(Aaug,compute_uv=False)
    rank=np.linalg.matrix_rank(Aaug,tol=1e-12)
    print('augmented rank=',rank)
    print('augmented smallest singular value=',saug[-1])

    assert np.max(np.abs(p))>1e-2
    assert 5e-3<np.sqrt(np.mean(p*p))<7e-3
    assert rank==25
    assert 0.0029<saug[-1]<0.0031

if __name__=='__main__':
    main()
