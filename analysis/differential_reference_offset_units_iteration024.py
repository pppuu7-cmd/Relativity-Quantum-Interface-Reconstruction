"""RQIR Iteration 024: differential reference stability and physical offset map.

Maps the row-normalized additive-offset nuisances introduced in Iteration 016
back to the unnormalized Toy009 calibration observables, then exposes the
remaining branch-specific readout transduction needed for SI units.

Also encodes the correct timing-control acceptance test: the detector prior is
on differential source-to-detector time error (TDEV-like), not on the ADEV of
one free-running clock.

This is a metrology/resource layer. It does not assign hardware performance
where the repository has no measured transfer function.
"""
from __future__ import annotations
import numpy as np

D=5
E=np.array([1.,2.,3.,4.,6.])
H=np.diag(E).astype(complex)
Y1=-3.7766873836695947
TIMES=np.array([0.,3.09855988,3.45849306,2.93830159,4.13016958,4.84480925,4.99085067])
TR=float(TIMES[2])

SIGMA={
    'D1': {'t_us':9.47, 'b_mean':7.62e-5, 'b_cov':1.03e-4},
    'D2': {'t_us':8.01, 'b_mean':6.44e-5, 'b_cov':1.04e-4},
}


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


def source_ops():
    rng=np.random.default_rng(314159)
    for _ in range(812):
        x=rng.normal(size=(D,D)); braw=(x+x.T)/2
    ev=np.linalg.eigvalsh(braw)
    bpos=braw+(-ev.min()+1)*np.eye(D)
    vals,v=np.linalg.eigh(bpos); scale=float(vals.max())
    def probe(y):
        w=1/np.abs((scale/vals)-y)
        return (v@np.diag(w)@v.T).astype(complex)
    return probe(0.0),probe(Y1)


def raw_row_norms():
    p0,p1=source_ops(); p=[p0,p1]
    rows=[]; labels=[]
    for k in (0,1):
        for t in TIMES:
            rows.append(herm_vec(evolve(p[k],float(t)))); labels.append('mean')
    rows.append(herm_vec(sym(evolve(p[0],TR),p[0]))); labels.append('cov')
    extra=[(0,1,TIMES[1]),(1,1,TIMES[5]),(1,0,TR),(0,1,TR),
           (1,0,TIMES[3]),(0,0,TIMES[6]),(0,1,TIMES[6])]
    for k,l,t in extra:
        rows.append(herm_vec(sym(evolve(p[k],float(t)),p[l]))); labels.append('cov')
    return np.asarray(labels),np.linalg.norm(np.vstack(rows),axis=1)


def raw_offset_targets(branch):
    labels,norms=raw_row_norms()
    out={}
    for lab in ('mean','cov'):
        sig=SIGMA[branch]['b_'+lab]
        vals=norms[labels==lab]*sig
        out[lab]=vals
    return out


def physical_offset_targets(branch, gains_mean, gains_cov):
    """Return allowed readout offsets for y_i = g_i * x_i + o_i.

    gains have physical readout units per raw Toy009 observable unit.  No SI
    answer exists until these gains are experimentally/theoretically supplied.
    """
    raw=raw_offset_targets(branch)
    gm=np.asarray(gains_mean,float); gc=np.asarray(gains_cov,float)
    assert gm.shape==(14,) and gc.shape==(8,)
    return {'mean':np.abs(gm)*raw['mean'], 'cov':np.abs(gc)*raw['cov']}


def timing_passes(branch,tdev_us):
    """Acceptance test on differential source-drive <-> detector-reference TDEV."""
    return np.asarray(tdev_us,float) < SIGMA[branch]['t_us']


def main():
    labels,norms=raw_row_norms()
    mn=norms[labels=='mean']; cv=norms[labels=='cov']
    print('mean raw row norms=',mn)
    print('cov raw row norms=',cv)
    assert np.allclose(mn[:7],1.3717451092471202,rtol=0,atol=2e-12)
    assert np.allclose(mn[7:],0.38208853802366155,rtol=0,atol=2e-12)
    assert 0.0673<cv.min()<0.0675 and 0.9826<cv.max()<0.9829

    for branch in ('D1','D2'):
        raw=raw_offset_targets(branch)
        print('\n'+branch)
        print('differential timing target us=',SIGMA[branch]['t_us'])
        print('raw mean offset range=',raw['mean'].min(),raw['mean'].max())
        print('raw cov offset range=',raw['cov'].min(),raw['cov'].max())
        # Transparent unit-gain benchmark only: e.g. rad if gain=1 rad/raw-unit.
        phys=physical_offset_targets(branch,np.ones(14),np.ones(8))
        assert np.allclose(phys['mean'],raw['mean'])
        assert np.allclose(phys['cov'],raw['cov'])

    d1=raw_offset_targets('D1'); d2=raw_offset_targets('D2')
    assert 2.90e-5<d1['mean'].min()<2.93e-5
    assert 1.04e-4<d1['mean'].max()<1.06e-4
    assert 2.45e-5<d2['mean'].min()<2.48e-5
    assert 8.8e-5<d2['mean'].max()<8.9e-5
    assert timing_passes('D1',[1.0,9.0]).all()
    assert not timing_passes('D2',[9.0]).all()

if __name__=='__main__':
    main()
