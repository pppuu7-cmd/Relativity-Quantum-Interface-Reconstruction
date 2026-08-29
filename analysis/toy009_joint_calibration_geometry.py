"""RQIR Iteration 011: joint calibration geometry for Toy 009.

Reconstructs Toy 009 deterministically (seed 314159, trial 811), evaluates the
inherited Toy 007 calibration, and verifies the accepted joint second-probe /
calibration-time redesign. The scan helper searches the same 24-row NP3
structure while requiring positive rho+/- and no degradation of baseline
response survival eta_R or normalized smallest singular value s_min.

This is finite-dimensional experiment design, not an experimental or new-
physics claim.
"""
from __future__ import annotations
import numpy as np

D=5
E=np.array([1.,2.,3.,4.,6.])
H=np.diag(E).astype(complex)
EPS=0.08
BASE_Y1=-3.5955271928522547
BASE_TIMES=np.array([0.,3.0709312960670494,3.583928899215236,3.73521464966555,4.18983,4.897032874946426,5.657269795944965])
ACCEPT_Y1=-3.7766873836695947
ACCEPT_TIMES=np.array([0.,3.09855988,3.45849306,2.93830159,4.13016958,4.84480925,4.99085067])
BASE_ETA=0.5688230045520637
BASE_SMIN=0.0015122241664651476


def herm_vec(a):
    out=[a[i,i].real for i in range(D)]
    for i in range(D):
        for j in range(i+1,D): out += [np.sqrt(2)*a[i,j].real,np.sqrt(2)*a[i,j].imag]
    return np.asarray(out,float)

def mat(v):
    a=np.zeros((D,D),complex); k=0
    for i in range(D): a[i,i]=v[k]; k+=1
    for i in range(D):
        for j in range(i+1,D):
            a[i,j]=(v[k]+1j*v[k+1])/np.sqrt(2); a[j,i]=a[i,j].conjugate(); k+=2
    return a

def evolve(a,t): return a*np.exp(1j*(E[:,None]-E[None,:])*t)
def sym(a,b): return (a@b+b@a)/2
def comm(a,b): return (a@b-b@a)/(2j)

def reconstruct_source():
    rng=np.random.default_rng(314159)
    for _ in range(812):
        x=rng.normal(size=(D,D)); braw=(x+x.T)/2
    ev=np.linalg.eigvalsh(braw); bpos=braw+(-ev.min()+1)*np.eye(D)
    vals,v=np.linalg.eigh(bpos); scale=float(vals.max())
    b0=(bpos/scale).astype(complex)
    grad=(v@np.diag((vals/scale)**2)@v.T).astype(complex)
    return b0,grad,v,vals,scale

B0,GRAD,V,VALS,SCALE=reconstruct_source()

def probe(y):
    w=1/np.abs((SCALE/VALS)-y)
    return (V@np.diag(w)@V.T).astype(complex)

def harmonic(delta,readout,pump,n):
    rw=np.zeros_like(readout,complex)
    for i in range(D):
        for j in range(D):
            if int(round(E[i]-E[j]))==n: rw[i,j]=readout[i,j]
    return 2*np.trace(delta@((rw@pump-pump@rw)/(2j)))

def seff(z2,z4):
    p2,p4=abs(z2)**2,abs(z4)**2
    return 4*p2*p4/(p2+p4)

def evaluate(y1,times):
    times=np.asarray(times,float); tR=times[2]; p=[probe(0),probe(y1)]
    rows=[herm_vec(np.eye(D)),herm_vec(H)]
    for k in (0,1):
        for t in times: rows.append(herm_vec(evolve(p[k],t)))
    rows.append(herm_vec(sym(evolve(p[0],tR),p[0])))
    extra=[(0,1,times[1]),(1,1,times[5]),(1,0,tR),(0,1,tR),(1,0,times[3]),(0,0,times[6]),(0,1,times[6])]
    for k,l,t in extra: rows.append(herm_vec(sym(evolve(p[k],t),p[l])))
    A=np.vstack(rows); _,s,vh=np.linalg.svd(A,full_matrices=True)
    rank=int(np.sum(s>1e-10))
    if rank!=24: return None
    nv=vh[-1]; d0=mat(nv); d0/=np.max(np.abs(np.linalg.eigvalsh(d0)))
    rp=np.eye(D)/D+EPS*d0; rm=np.eye(D)/D-EPS*d0
    if min(np.linalg.eigvalsh(rp).min(),np.linalg.eigvalsh(rm).min())<=0: return None
    delta=rp-rm
    h2,h4=harmonic(delta,p[0],p[0],2),harmonic(delta,p[0],p[0],4)
    g2,g4=harmonic(delta,GRAD,p[0],2),harmonic(delta,GRAD,p[0],4)
    cr=herm_vec(comm(evolve(p[0],tR),p[0])); eta=abs(cr@nv)/np.linalg.norm(cr)
    An=A/np.linalg.norm(A,axis=1,keepdims=True); sn=np.linalg.svd(An,compute_uv=False); nz=sn[sn>1e-10]
    bt=evolve(p[0],tR); mp=np.trace(rp@bt); mm=np.trace(rm@bt)
    dp,dm=bt-mp*np.eye(D),bt-mm*np.eye(D)
    m0p,m0m=np.trace(rp@p[0]),np.trace(rm@p[0])
    npv=float(np.real(np.trace(rp@sym(dp,p[0]-m0p*np.eye(D)))))
    nmv=float(np.real(np.trace(rm@sym(dm,p[0]-m0m*np.eye(D)))))
    return dict(rank=rank,se1=seff(h2,h4),se2=seff(g2,g4),eta=float(eta),smin=float(nz[-1]),cond=float(nz[0]/nz[-1]),
                eigp=np.linalg.eigvalsh(rp),eigm=np.linalg.eigvalsh(rm),mean_diff=float(abs(mp-mm)),noise_diff=abs(npv-nmv),
                response_plus=float(np.real(np.trace(rp@comm(bt,p[0])))),response_minus=float(np.real(np.trace(rm@comm(bt,p[0])))),
                residual=float(np.max(np.abs(A@herm_vec(d0)))),h2=h2,h4=h4,g2=g2,g4=g4)

def random_scan(n=5000,seed=2026082901):
    base=evaluate(BASE_Y1,BASE_TIMES); rng=np.random.default_rng(seed); best=None
    for _ in range(n):
        y=BASE_Y1+rng.normal(0,0.8)
        if not -8<y<-0.3: continue
        t=BASE_TIMES.copy(); t[1:]=np.mod(t[1:]+rng.normal(0,0.35,6),2*np.pi)
        m=evaluate(y,t)
        if m is None or m['eta']<base['eta'] or m['smin']<base['smin']: continue
        score=min(m['se1']/base['se1'],m['se2']/base['se2'])
        if best is None or score>best[0]: best=(score,y,t,m)
    return best

if __name__=='__main__':
    b=evaluate(BASE_Y1,BASE_TIMES); a=evaluate(ACCEPT_Y1,ACCEPT_TIMES)
    print('baseline',b)
    print('accepted',a)
    print('D1 gain',a['se1']/b['se1'])
    print('D2 gain',a['se2']/b['se2'])
    assert a['rank']==24
    assert a['eta']>=b['eta'] and a['smin']>=b['smin']
    assert min(a['eigp'])>0 and min(a['eigm'])>0
    assert a['mean_diff']<1e-12 and a['noise_diff']<1e-12 and a['residual']<1e-12
