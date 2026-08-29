"""RQIR Iteration 059: Toy012 branch-A control/systematics revalidation.

Revalidates geometry, reference-position, phase/timing and additive-offset
nuisances on the balanced Toy012 complementary D2 architecture.  The preferred
local branch uses 14 relational means + 14 direct-force means and a selected
subset of the 8 centered relational covariance rows, with independent source
metrology supplying C_alpha.

This is a normalized Fisher/control-budget calculation, not a hardware
forecast.  Exact trace+energy elimination and the fractional alpha coordinate
are retained.
"""
from __future__ import annotations
import numpy as np
import toy011_local_nearest_neighbor_source as t11
import toy011_centered_profiled_resource_audit_iteration054 as i54
import toy012_complementary_d2_branch_iteration057 as i57

TARGET=0.90
F_GAP=100.0
FRAC=0.10

# Resource-relevant relational covariance subsets found in Iteration 060-style
# prescan.  They are included here only to test robustness of control targets.
BRANCHES={
    'k4': ((2,4,5,6), 15.061939558628682),
    'k5': ((2,3,4,5,6), 13.819478635553859),
    'k8': (tuple(range(8)), 13.669414719050629),
}


def base_objects(y1=i57.Y1,yref=i57.YREF,dt=0.0):
    Q=t11.lanczos_q(i57.Q0)
    p0=i57.probe_at(Q,0.0); p1=i57.probe_at(Q,y1); pref=i57.probe_at(Q,yref)
    g0=i57.grad_at(Q,0.0); g1=i57.grad_at(Q,y1)
    times=i57.TIMES+dt
    rm,rc=i54.operator_rows([p0-pref,p1-pref],times)
    fm,_fc=i54.operator_rows([g0,g1],times)
    return np.vstack([rm,fm]),rc


def build_pack():
    Q=t11.lanczos_q(i57.Q0)
    return i54.make_pack(Q,i57.Y1,i57.TIMES)


def selected_rows(indices,y1=i57.Y1,yref=i57.YREF,dt=0.0):
    means,rc=base_objects(y1,yref,dt)
    return np.vstack([means,rc[list(indices)]])


def systematics_matrix(pack,indices,step=1e-5):
    theta0=pack['theta0']
    cols=[]
    for name in ('y1','yref','dt'):
        if name=='y1':
            plus=selected_rows(indices,i57.Y1+step,i57.YREF,0.0)
            minus=selected_rows(indices,i57.Y1-step,i57.YREF,0.0)
        elif name=='yref':
            plus=selected_rows(indices,i57.Y1,i57.YREF+step,0.0)
            minus=selected_rows(indices,i57.Y1,i57.YREF-step,0.0)
        else:
            plus=selected_rows(indices,i57.Y1,i57.YREF,+step)
            minus=selected_rows(indices,i57.Y1,i57.YREF,-step)
        cols.append(((plus-minus)/(2.0*step))@theta0)

    nc=len(indices)
    # Separate additive references for relational mean, force mean and covariance.
    cols.extend([
        np.r_[np.ones(14),np.zeros(14),np.zeros(nc)],
        np.r_[np.zeros(14),np.ones(14),np.zeros(nc)],
        np.r_[np.zeros(28),np.ones(nc)],
    ])
    return np.column_stack(cols)


def row_weights(indices):
    return np.r_[np.full(28,i57.GM),np.full(len(indices),i57.GC)]


def conservative_sigmas(V,W,fraction=FRAC):
    root=np.sqrt(W)
    out=[]
    for j in range(V.shape[1]):
        mx=float(np.max(np.abs(V[:,j])*root))
        out.append(np.inf if mx==0 else fraction/mx)
    return np.asarray(out)


def profiled(pack,indices,c_alpha,scale=1.0,with_control_priors=True,
             fraction=FRAC):
    M=selected_rows(indices)
    W=row_weights(indices)*scale
    s=pack['s2']; B=pack['B2']; Zu=pack['Zu']; theta0=pack['theta0']
    Jd=np.column_stack([s,s,B@Zu])
    F=Jd.T@Jd
    Jc=np.column_stack([M@theta0,M@Zu])
    F[1:,1:]+=Jc.T@(W[:,None]*Jc)
    F[1,1]+=c_alpha*scale

    V=systematics_matrix(pack,indices)
    nb=F.shape[0]; ns=V.shape[1]
    Fa=np.zeros((nb+ns,nb+ns)); Fa[:nb,:nb]=F
    cross=Jc.T@(W[:,None]*V)
    Fa[1:nb,nb:]=cross; Fa[nb:,1:nb]=cross.T
    Fa[nb:,nb:]=V.T@(W[:,None]*V)
    if with_control_priors:
        sig=conservative_sigmas(V,row_weights(indices),fraction)
        # Scale reference campaigns together with the main auxiliary budget.
        Fa[nb:,nb:]+=np.diag(scale/sig**2)
    N=Fa[1:,1:]; c=Fa[0,1:]
    return float(Fa[0,0]-c@np.linalg.pinv(N,rcond=1e-13)@c)


def scale_for_target(pack,indices,c_alpha):
    lo,hi=1.0,2.0
    for _ in range(70):
        mid=0.5*(lo+hi)
        if profiled(pack,indices,c_alpha,mid,True)>=TARGET: hi=mid
        else: lo=mid
    return hi


def main():
    pack=build_pack()
    for name,(inds,ca) in BRANCHES.items():
        V=systematics_matrix(pack,inds)
        sig=conservative_sigmas(V,row_weights(inds))
        timing_us=sig[2]/(2*np.pi*F_GAP)*1e6
        f1=profiled(pack,inds,ca,1.0,True)
        lam=scale_for_target(pack,inds,ca)
        print(name,'sigmas [y1,yref,dtau,brel,bforce,bcov]',sig)
        print(name,'timing us',timing_us,'F at scale1',f1,'scale90',lam)

    # Demonstrate that exposure alone cannot replace independent controls.
    inds,ca=BRANCHES['k4']
    no_prior=[profiled(pack,inds,ca,x,False) for x in (1.0,2.0,10.0,100.0)]
    print('k4 no-control-prior exposure scan',no_prior)

    sig=conservative_sigmas(systematics_matrix(pack,BRANCHES['k4'][0]),
                            row_weights(BRANCHES['k4'][0]))
    assert abs(sig[0]-0.5854846361102)<3e-10
    assert abs(sig[1]-1.184281513701)<3e-10
    assert abs(sig[2]-0.002604968934671)<3e-12
    assert abs(sig[3]-9.095847262484e-5)<3e-13
    assert abs(sig[4]-9.095847262484e-5)<3e-13
    assert abs(sig[5]-7.255721022780e-5)<3e-13
    assert abs(sig[2]/(2*np.pi*100.0)*1e6-4.145936825537)<3e-10
    assert abs(scale_for_target(pack,*BRANCHES['k4'])-1.002369784197)<3e-10
    assert abs(scale_for_target(pack,*BRANCHES['k5'])-1.002589685907)<3e-10
    assert 0.79<no_prior[-1]<0.82

if __name__=='__main__':
    main()
