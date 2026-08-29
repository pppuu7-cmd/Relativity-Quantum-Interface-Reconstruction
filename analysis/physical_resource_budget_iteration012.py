"""RQIR Iteration 012: map abstract Fisher strengths to physical shot/time budgets.

Uses the current Iteration-011 Toy009 balanced calibration geometry.  It
reconstructs the local D1 nuisance Fisher problem, computes scalar-gamma
retention thresholds, and converts preparation/calibration Fisher requirements
into generic repetition/time budgets through per-shot standardized sensitivity.

This is a resource-accounting layer, not a hardware forecast.  The scalar
`gamma` model is retained only as a diagnostic proxy; physical rows are
heterogeneous and must ultimately receive separate covariance models.
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


def reconstruct_source():
    rng=np.random.default_rng(314159)
    for _ in range(812):
        x=rng.normal(size=(D,D)); braw=(x+x.T)/2
    ev=np.linalg.eigvalsh(braw)
    bpos=braw+(-ev.min()+1)*np.eye(D)
    vals,v=np.linalg.eigh(bpos); scale=float(vals.max())
    return vals,v,scale

VALS,V,SCALE=reconstruct_source()


def probe(y):
    w=1/np.abs((SCALE/VALS)-y)
    return (V@np.diag(w)@V.T).astype(complex)


def harmonic(delta,readout,pump,n):
    rw=np.zeros_like(readout,complex)
    for i in range(D):
        for j in range(D):
            if int(round(E[i]-E[j]))==n: rw[i,j]=readout[i,j]
    return 2*np.trace(delta@((rw@pump-pump@rw)/(2j)))


def build_model():
    p=[probe(0.0),probe(Y1)]
    rows=[herm_vec(np.eye(D)),herm_vec(H)]
    labels=['trace','energy']
    for k in (0,1):
        for t in TIMES:
            rows.append(herm_vec(evolve(p[k],float(t))))
            labels.append('mean')
    rows.append(herm_vec(sym(evolve(p[0],TR),p[0]))); labels.append('cov')
    extra=[(0,1,TIMES[1]),(1,1,TIMES[5]),(1,0,TR),(0,1,TR),
           (1,0,TIMES[3]),(0,0,TIMES[6]),(0,1,TIMES[6])]
    for k,l,t in extra:
        rows.append(herm_vec(sym(evolve(p[k],float(t)),p[l])))
        labels.append('cov')
    A=np.vstack(rows)
    An=A/np.linalg.norm(A,axis=1,keepdims=True)
    _,sv,vh=np.linalg.svd(An,full_matrices=True)
    n=vh[-1]; Q=vh[:-1].T
    d0=mat(n); d0/=np.max(np.abs(np.linalg.eigvalsh(d0)))
    theta0=2*EPS*herm_vec(d0)
    B=np.zeros((4,D*D),float)
    for j in range(D*D):
        e=np.zeros(D*D); e[j]=1
        op=mat(e)
        h2=harmonic(op,p[0],p[0],2); h4=harmonic(op,p[0],p[0],4)
        B[:,j]=[h2.real,h2.imag,h4.real,h4.imag]
    s=B@theta0
    B/=np.sqrt(float(s@s)); s=B@theta0
    return dict(A=An,labels=labels,smin=float(sv[-1]),n=n,Q=Q,
                s=s,Bu=B@Q,Ac=An@Q)


def profiled_fisher(model,gamma,c_a=1e12):
    s=model['s']; bu=model['Bu']; ac=model['Ac']
    J=np.column_stack([s,s,bu])
    F=J.T@J
    F[1,1]+=c_a
    F[2:,2:]+=gamma*(ac.T@ac)
    N=F[1:,1:]; c=F[0,1:]
    return float(F[0,0]-c@np.linalg.pinv(N,rcond=1e-12)@c)


def gamma_for_target(model,target,c_a=1e12):
    grid=np.logspace(2,8,4000)
    vals=np.array([profiled_fisher(model,float(g),c_a) for g in grid])
    idx=np.where(vals>=target)[0]
    return None if len(idx)==0 else float(grid[int(idx[0])])


def prep_fisher_ratio(retained):
    return retained/(1-retained)


def repetitions(required_fisher,xi_single_shot):
    # xi = |d mean / d theta| / sigma for a mean-like Gaussian channel.
    # The same formula applies to any channel after xi^2 is replaced by its
    # actual single-shot Fisher information.
    return required_fisher/(xi_single_shot**2)


def coherence_min_seconds(max_phase,gap_hz):
    # Dimensionless phase tau = Omega t = 2 pi f t.
    return max_phase/(2*np.pi*gap_hz)


def main():
    m=build_model()
    counts={x:m['labels'].count(x) for x in sorted(set(m['labels']))}
    print('row classes:',counts)
    print('current s_min:',m['smin'])
    print('1/s_min^2:',1/m['smin']**2)
    print('scalar-gamma retention thresholds:')
    gs={r:gamma_for_target(m,r) for r in [0.5,0.8,0.9,0.95]}
    for r,g in gs.items(): print(r,g)

    # Illustrative detector target: beta=1 measured at detector SNR rho_D=5.
    rho_D=5.0; S_D=rho_D**2
    print('\nPreparation layer, detector SNR=5:')
    for r in [0.8,0.9,0.95]:
        C_rel=prep_fisher_ratio(r); C_abs=C_rel*S_D
        print('retain',r,'C_a/S_D',C_rel,'C_a physical',C_abs)
        for xi in [0.1,1.0,10.0]:
            print('  xi',xi,'Nprep',repetitions(C_abs,xi))

    # Scalar-gamma shot-equivalent diagnostic.  The abstract model gives the
    # same Fisher weight to every normalized row.  There are 14 mean rows and
    # 8 covariance rows; trace and energy are logically separate constraints.
    g90=gs[0.9]; row_info=g90*S_D
    print('\n90% scalar-gamma diagnostic at detector SNR=5:')
    print('required normalized Fisher per row:',row_info)
    print('physical gravitational rows:',14+8)
    for xi in [1.0,10.0,100.0]:
        nrow=repetitions(row_info,xi)
        ntot=(14+8)*nrow
        print('xi',xi,'shots/row',nrow,'total grav shots',ntot,
              'time@1ms_s',ntot*1e-3,'time@10ms_s',ntot*1e-2)

    print('\nMinimum per-shot coherence to reach largest stored phase:')
    phase=float(np.max(TIMES))
    for f in [1.0,100.0,1000.0]:
        print('gap_Hz',f,'Tcoh_min_s',coherence_min_seconds(phase,f))

    # Gaussian covariance channel: if V(theta) is the variance, the single-
    # shot Fisher is 0.5*(d ln V/d theta)^2.  This must replace a mean-channel
    # xi^2 when allocating shots to the eight covariance rows.
    assert counts=={'cov':8,'energy':1,'mean':14,'trace':1}
    assert abs(m['smin']-0.0019995404055)<2e-10
    assert 1.4e6 < gs[0.9] < 1.8e6

if __name__=='__main__': main()
