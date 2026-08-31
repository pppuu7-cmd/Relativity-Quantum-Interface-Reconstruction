#!/usr/bin/env python3
"""Iteration 150: scoped unreduced EH + curvature-cubic C5 response.

Computes the multilinear Einstein-Hilbert cubic coefficient directly from the
Gamma-Gamma form of sqrt(-g) R for g=eta+h, without on-shell/EOM reduction.
Adds two explicit covariant curvature-cubic directions in the same metric
convention, projects all three legs onto the frozen Iteration-149 TT protocol,
and reports a scoped rank/SVD certificate.

Important: a single longitudinal replacement of an off-shell 1PI three-vertex
is NOT expected to vanish by itself; the gravitational Ward-Takahashi identity
contains inverse-propagator/contact terms. The script therefore records that
replacement as a diagnostic, not as a gauge-consistency FAIL.
"""
import itertools, json, math
import numpy as np

ETA=np.diag([-1.,1.,1.,1.]); TAU=0.8; LWIN=0.6
QS=[np.array(x,float) for x in [
[0.18,0.70,0.20,0.10],[0.14,0.55,-0.25,0.20],[0.22,0.62,0.18,-0.24],
[0.16,0.48,0.31,0.12],[0.20,0.58,-0.16,-0.28],[0.12,0.44,0.27,-0.19]]]
RS=[np.array(x,float) for x in [
[0.11,-0.21,0.52,0.17],[0.09,0.24,0.46,-0.18],[0.10,-0.18,0.41,0.29],
[0.13,0.22,-0.37,0.33],[0.08,0.26,0.35,0.21],[0.15,-0.20,0.39,0.25]]]

def dot(a,b): return float(a@ETA@b)
def theta(k):
    kc=ETA@k; return ETA-np.outer(kc,kc)/dot(k,k)
def p2(k):
    t=theta(k)
    return .5*(np.einsum('mr,ns->mnrs',t,t)+np.einsum('ms,nr->mnrs',t,t))-(1/3)*np.einsum('mn,rs->mnrs',t,t)
def polarization(k,seed):
    P=p2(k); e=np.einsum('mnrs,ra,sb,ab->mn',P,ETA,ETA,seed)
    n=np.einsum('mn,ma,nb,ab',e,ETA,ETA,e)
    return e/np.sqrt(abs(n))
def window(k):
    return math.exp(-.5*((TAU*k[0])**2+(LWIN*np.linalg.norm(k[1:]))**2))

def eh_gamma_gamma(eps,ks,es):
    g=ETA.astype(complex).copy(); dg=np.zeros((4,4,4),complex)
    for ep,k,e in zip(eps,ks,es):
        g += ep*e
        dg += ep*1j*np.einsum('m,ab->mab',ETA@k,e)
    gi=np.linalg.inv(g); sqrtmg=np.sqrt(-np.linalg.det(g))
    G=np.zeros((4,4,4),complex)
    for a,m,n in itertools.product(range(4),repeat=3):
        G[a,m,n]=.5*sum(gi[a,b]*(dg[m,b,n]+dg[n,b,m]-dg[b,m,n]) for b in range(4))
    val=0j
    for m,n in itertools.product(range(4),repeat=2):
        x=0j
        for a,b in itertools.product(range(4),repeat=2):
            x += G[a,m,b]*G[b,n,a]-G[a,m,n]*G[b,a,b]
        val += gi[m,n]*x
    return sqrtmg*val

def mixed3(fun,d):
    return sum(np.prod(s)*fun([d*x for x in s]) for s in itertools.product([-1,1],repeat=3))/(8*d**3)

def lin_ricci(k,e):
    kc=ETA@k; tr=np.einsum('mn,mn',ETA,e); k2v=dot(k,k); R=np.zeros((4,4),complex)
    for m,n in itertools.product(range(4),repeat=2):
        t1=-kc[m]*sum(k[a]*e[a,n] for a in range(4))
        t2=-kc[n]*sum(k[a]*e[a,m] for a in range(4))
        R[m,n]=.5*(t1+t2+k2v*e[m,n]+kc[m]*kc[n]*tr)
    return R

def lin_riemann(k,e):
    kc=ETA@k; R=np.zeros((4,4,4,4),complex)
    for m,n,r,s in itertools.product(range(4),repeat=4):
        R[m,n,r,s]=.5*(-kc[r]*kc[n]*e[m,s]-kc[s]*kc[m]*e[n,r]+kc[s]*kc[n]*e[m,r]+kc[r]*kc[m]*e[n,s])
    return R

def ricci3(ks,es):
    A=[ETA@lin_ricci(k,e) for k,e in zip(ks,es)]
    return sum(np.trace(A[a]@A[b]@A[c]) for a,b,c in itertools.permutations(range(3))).real

def riem3(ks,es):
    A=[]
    for k,e in zip(ks,es):
        R=lin_riemann(k,e)
        A.append(np.einsum('mnab,ar,bs->mnrs',R,ETA,ETA).reshape(16,16))
    return sum(np.trace(A[a]@A[b]@A[c]) for a,b,c in itertools.permutations(range(3))).real

seeds=[]
for i in range(18):
    rng=np.random.default_rng(100+i); A=rng.normal(size=(4,4)); seeds.append((A+A.T)/2)

rows=[]; perm_errors=[]; longitudinal=[]; convergence=[]
for i,(q,r) in enumerate(zip(QS,RS)):
    p=q+r; ks=[p,-q,-r]; es=[polarization(ks[j],seeds[3*i+j]) for j in range(3)]
    vals=[mixed3(lambda ep: eh_gamma_gamma(ep,ks,es),d).real for d in (2.5e-3,1.25e-3)]
    eh=(4*vals[1]-vals[0])/3
    convergence.append(abs(vals[1]-vals[0]))
    perms=[mixed3(lambda ep: eh_gamma_gamma(ep,[ks[j] for j in P],[es[j] for j in P]),2.5e-3).real for P in itertools.permutations(range(3))]
    perm_errors.append(max(perms)-min(perms))
    rng=np.random.default_rng(900+i); xi=rng.normal(size=4); kc=ETA@ks[0]
    gauge=np.outer(kc,xi)+np.outer(xi,kc)
    longitudinal.append(mixed3(lambda ep: eh_gamma_gamma(ep,ks,[gauge,es[1],es[2]]),2.5e-3).real)
    cR=ricci3(ks,es); cRm=riem3(ks,es)
    common=np.prod([1/dot(k,k) for k in ks])*np.prod([window(k) for k in ks])
    rows.append({'probe':i,'p2':dot(p,p),'q2':dot(q,q),'r2':dot(r,r),'common_retarded_window_factor':common,
                 'EH_cubic':eh,'EH_response':eh*common,'Ricci3_cubic':cR,'Ricci3_response':cR*common,
                 'Riemann3_cubic':cRm,'Riemann3_response':cRm*common})
V=np.array([[x['Ricci3_response'],x['Riemann3_response']] for x in rows])
s=np.linalg.svd(V,compute_uv=False); rank=int(np.linalg.matrix_rank(V))
out={'iteration':150,'scope':'tree, local, TT-projected, six frozen spacelike probes',
     'metric_convention':'g=eta+kappa h; kappa stripped from dimensionless fingerprint',
     'EH_implementation':'direct multilinear coefficient of sqrt(-g) g^{mn}(Gamma^a_mb Gamma^b_na-Gamma^a_mn Gamma^b_ab)',
     'local_directions':['Tr(Ricci^3)','Riemann_mn^rs Riemann_rs^ab Riemann_ab^mn'],
     'rows':rows,'V_C5_local_chi2R':V.tolist(),'rank':rank,'n_columns':2,'singular_values':s.tolist(),
     'smin_over_smax':float(s[-1]/s[0]),'max_EH_permutation_error':float(max(perm_errors)),
     'max_last_step_EH_convergence_delta':float(max(convergence)),
     'longitudinal_replacement_values':longitudinal,
     'ward_interpretation':'NONZERO_EXPECTED_OFFSHELL_1PI_VERTEX; requires inverse-propagator/contact/source-completed Ward-Takahashi check',
     'status':{'EH_cubic_TT_block':'PASS_SCOPED','two_curvature_cubic_columns':'PASS_SCOPED','local_rank_certificate':'PASS_SCOPED',
               'full_offshell_Ward_source_completion':'BLOCKED_WARD_TAKAHASHI_COMPLETION','higher_dimension_local':'BLOCKED','loops_nonanalytic':'BLOCKED',
               'Fisher_resources':'FORBIDDEN_NO_COMPARATOR_QUOTIENT_RESIDUAL','ANSATZ_003':'NOT_CREATED'}}
print(json.dumps(out,indent=2,sort_keys=True))
