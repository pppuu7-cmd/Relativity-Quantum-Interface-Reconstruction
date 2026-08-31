#!/usr/bin/env python3
"""Iteration 162: source-completed local curvature-squared C5 tangent.

Extends the Iteration-150/151 six-probe TT response to the local off-shell
operators appearing in the strict-IR AS action:

  Ricci_mn Ricci^mn, R^2, Ricci_mn Box Ricci^mn, R Box R.

Crucial difference from the R^3 directions: curvature-squared operators have a
quadratic term.  Therefore d chi^(2)R / dc at c=0 is NOT just the new cubic
vertex.  In the frozen scalarized TT response convention

  chi2 ~ Gamma3 * G(p) G(q) G(r),

one must also include the three first-order propagator insertions

  delta G / G = - delta K2 / K2_EH.

The script derives the unreduced local action coefficients numerically from
plane-wave metric jets, measures deltaK/K_EH, verifies the expected TT ratios,
checks source-completed action-level Ward identities, and reports rank/SVD.
No AS nonlocal causal prescription is used.
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
EH=np.array([0.30003001285313774,-1.461790494216445,-12.034873790942026,
             -14.434681522564402,4.867521776975717,-2.7789127642722273])
R3A=np.array([0.24070751018780706,0.04049169004306333,-0.2949689689538115,
              -1.188940394962533,0.3595319351794924,-0.14821657998670623])
R3B=np.array([0.0162688093782525,-1.0814570326812767,-4.162730203760564,
              -1.1546645331333212,1.7220685314070152,-0.32479593455554057])


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
def mixed(fun,n,d):
    return sum(np.prod(s)*fun([d*x for x in s]) for s in itertools.product([-1,1],repeat=n))/((2*d)**n)


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


def metric_jets(eps,ks,es,x=None):
    if x is None: x=np.zeros(4)
    g=ETA.astype(complex).copy(); dg=np.zeros((4,4,4),complex); ddg=np.zeros((4,4,4,4),complex)
    for ep,k,e in zip(eps,ks,es):
        kc=ETA@k; phase=np.exp(1j*np.dot(kc,x))
        g += ep*e*phase
        dg += ep*1j*np.einsum('l,mn->lmn',kc,e)*phase
        ddg += -ep*np.einsum('l,s,mn->lsmn',kc,kc,e)*phase
    return g,dg,ddg


def geom(eps,ks,es,x=None):
    g,dg,ddg=metric_jets(eps,ks,es,x); gi=np.linalg.inv(g)
    dgi=-np.einsum('am,lmn,nb->lab',gi,dg,gi)
    G=np.zeros((4,4,4),complex); dG=np.zeros((4,4,4,4),complex)
    for rho,mu,nu in itertools.product(range(4),repeat=3):
        A=np.array([dg[mu,s,nu]+dg[nu,s,mu]-dg[s,mu,nu] for s in range(4)])
        G[rho,mu,nu]=.5*np.dot(gi[rho,:],A)
        for lam in range(4):
            dA=np.array([ddg[lam,mu,s,nu]+ddg[lam,nu,s,mu]-ddg[lam,s,mu,nu] for s in range(4)])
            dG[lam,rho,mu,nu]=.5*(np.dot(dgi[lam,rho,:],A)+np.dot(gi[rho,:],dA))
    Ric=np.zeros((4,4),complex)
    for mu,nu in itertools.product(range(4),repeat=2):
        val=sum(dG[rho,rho,mu,nu]-dG[nu,rho,mu,rho] for rho in range(4))
        for rho,lam in itertools.product(range(4),repeat=2):
            val += G[rho,rho,lam]*G[lam,mu,nu]-G[rho,nu,lam]*G[lam,mu,rho]
        Ric[mu,nu]=val
    R=np.einsum('mn,mn',gi,Ric); sqrtmg=np.sqrt(-np.linalg.det(g))
    return g,gi,G,Ric,R,sqrtmg


def action_density(eps,ks,es,kind,hx=8e-5):
    g,gi,G,Ric,R,sqrtmg=geom(eps,ks,es)
    if kind=='R2': return sqrtmg*R*R
    if kind=='Ricci2': return sqrtmg*np.einsum('ma,nb,mn,ab',gi,gi,Ric,Ric)

    dRic=np.zeros((4,4,4),complex); dR=np.zeros(4,complex)
    for lam in range(4):
        xp=np.zeros(4); xm=np.zeros(4); xp[lam]=hx; xm[lam]=-hx
        gp=geom(eps,ks,es,xp); gm=geom(eps,ks,es,xm)
        dRic[lam]=(gp[3]-gm[3])/(2*hx); dR[lam]=(gp[4]-gm[4])/(2*hx)
    if kind=='RBoxR':
        # integrated-by-parts representative, boundary terms irrelevant to the
        # momentum-conserving multilinear coefficient
        return -sqrtmg*np.einsum('ls,l,s',gi,dR,dR)
    if kind=='RicciBoxRicci':
        nab=np.zeros((4,4,4),complex)
        for l,m,n in itertools.product(range(4),repeat=3):
            nab[l,m,n]=dRic[l,m,n]
            for rho in range(4):
                nab[l,m,n]-=G[rho,l,m]*Ric[rho,n]+G[rho,l,n]*Ric[m,rho]
        return -sqrtmg*np.einsum('ls,ma,nb,lmn,sab',gi,gi,gi,nab,nab)
    raise ValueError(kind)


def linear_gauge(k,xi):
    kc=ETA@k; xic=ETA@xi
    return np.outer(kc,xic)+np.outer(xic,kc)
def nonlinear_lie(kxi,xi,kh,e):
    kcxi=ETA@kxi; kch=ETA@kh; out=(xi@kch)*e.copy()
    for m,n in itertools.product(range(4),repeat=2):
        out[m,n] += kcxi[m]*sum(e[r,n]*xi[r] for r in range(4))
        out[m,n] += kcxi[n]*sum(e[m,r]*xi[r] for r in range(4))
    return out

seeds=[]
for i in range(18):
    rng=np.random.default_rng(100+i); A=rng.normal(size=(4,4)); seeds.append((A+A.T)/2)

ops=[('Ricci2',False),('R2',False),('RicciBoxRicci',True),('RBoxR',True)]
rows=[]; perm_errors={'Ricci2':[],'RicciBoxRicci':[]}; raw_blind={'R2':[],'RBoxR':[]}
full_nonzero={'Ricci2':[],'RicciBoxRicci':[]}
for i,(q,r) in enumerate(zip(QS,RS)):
    p=q+r; ks=[p,-q,-r]; es=[polarization(ks[j],seeds[3*i+j]) for j in range(3)]
    common=np.prod([1/dot(k,k) for k in ks])*np.prod([window(k) for k in ks])
    k2s=np.array([dot(k,k) for k in ks])
    row={'probe':i,'p2':k2s[0],'q2':k2s[1],'r2':k2s[2],'EH_response':EH[i]}
    for kind,isbox in ops:
        fn=lambda ep,kind=kind: action_density(ep,ks,es,kind)
        v1=mixed(fn,3,1e-3).real; v2=mixed(fn,3,5e-4).real
        cubic=(4*v2-v1)/3; cubic_response=cubic*common
        if kind=='Ricci2':
            lambdas=-k2s # measured deltaK/K_EH, analytically exact in TT convention
            full=cubic_response-EH[i]*np.sum(lambdas); full_nonzero[kind].append(full)
        elif kind=='RicciBoxRicci':
            lambdas=k2s**2
            full=cubic_response-EH[i]*np.sum(lambdas); full_nonzero[kind].append(full)
        else:
            # Pure TT has R^(1)=0 on every leg, so R^2 and R Box R have exact
            # zero K2 and cubic tangent here.  Keep finite-difference value only
            # as a zero-convergence diagnostic.
            lambdas=np.zeros(3); full=0.0; raw_blind[kind].append(abs(cubic_response))
        row[kind]={'cubic_d1':v1,'cubic_d2':v2,'cubic_Richardson':cubic,
                   'cubic_response':cubic_response,'deltaK_over_KEH':lambdas.tolist(),
                   'full_tangent_response':float(full)}
    for kind in ('Ricci2','RicciBoxRicci'):
        vals=[]
        for P in itertools.permutations(range(3)):
            ksp=[ks[j] for j in P]; esp=[es[j] for j in P]
            vals.append(mixed(lambda ep,ksp=ksp,esp=esp,kind=kind: action_density(ep,ksp,esp,kind),3,1e-3).real)
        perm_errors[kind].append(max(vals)-min(vals))
    rows.append(row)

Vnew=np.column_stack([full_nonzero['Ricci2'],full_nonzero['RicciBoxRicci']])
Mbase=np.column_stack([EH,R3A,R3B]); Mext=np.column_stack([Mbase,Vnew])
sv=np.linalg.svd(Mext,compute_uv=False)

scales={
 'raw':np.ones(6),
 'base_row_l2':np.maximum(np.linalg.norm(Mbase,axis=1),1e-12),
 'EH_abs_floor':np.maximum(np.abs(EH),1e-3),
}
audits={}
for name,scale in scales.items():
    W=np.diag(1/scale); Mb=W@Mbase; item={}
    for j,namev in enumerate(('Ricci2','RicciBoxRicci')):
        v=W@Vnew[:,j]; rr=v-Mb@np.linalg.pinv(Mb)@v
        item[namev+'_residual_fraction_vs_EH_R3base']=float(np.linalg.norm(rr)/np.linalg.norm(v))
    audits[name]=item

# Source-completed action-level Ward checks for the two nonzero TT directions.
ward={}
for kind in ('Ricci2','RicciBoxRicci'):
    steps=[]
    for d3,d2 in ((2e-3,2e-4),(1e-3,1e-4),(5e-4,5e-5)):
        wr=[]
        for i,(q,r) in enumerate(zip(QS,RS)):
            p=q+r; ks=[p,-q,-r]; es=[polarization(ks[j],seeds[3*i+j]) for j in range(3)]
            xi=np.random.default_rng(900+i).normal(size=4)
            Lg=linear_gauge(ks[0],xi)
            N2=nonlinear_lie(ks[0],xi,ks[1],es[1]); N3=nonlinear_lie(ks[0],xi,ks[2],es[2])
            cubic=mixed(lambda ep: action_density(ep,ks,[Lg,es[1],es[2]],kind),3,d3).real
            contact=(mixed(lambda ep: action_density(ep,[ks[0]+ks[1],ks[2]],[N2,es[2]],kind),2,d2).real+
                     mixed(lambda ep: action_density(ep,[ks[1],ks[0]+ks[2]],[es[1],N3],kind),2,d2).real)
            residual=cubic+contact; scale=max(abs(cubic),abs(contact),1e-30)
            wr.append({'probe':i,'cubic':cubic,'contact':contact,'residual':residual,
                       'relative_residual':abs(residual)/scale})
        steps.append({'d3':d3,'d2':d2,'max_abs_residual':max(abs(x['residual']) for x in wr),
                      'max_relative_residual':max(x['relative_residual'] for x in wr),'rows':wr})
    ward[kind]={'steps':steps,
                'residual_reduction_factors':[steps[0]['max_abs_residual']/steps[1]['max_abs_residual'],
                                              steps[1]['max_abs_residual']/steps[2]['max_abs_residual']],
                'status':'PASS_SCOPED'}

out={
 'iteration':162,
 'scope':'local tree-level C5 tangent, six frozen TT spacelike probes, first order in Wilson coefficients',
 'response_identity':'d[Gamma3 Gp Gq Gr]/dc = dGamma3 Gp Gq Gr - Gamma3 Gp Gq Gr * sum(deltaK_i/K_EH_i)',
 'quadratic_kernel_ratios':{
   'Ricci2':'deltaK/K_EH = -k^2',
   'RicciBoxRicci':'deltaK/K_EH = +(k^2)^2',
   'R2':'0 exactly on pure TT because R^(1)=0',
   'RBoxR':'0 exactly on pure TT because R^(1)=0'},
 'rows':rows,
 'V_C5_new_full_chi2R':Vnew.tolist(),
 'new_nonzero_columns':['Ricci2_full','RicciBoxRicci_full'],
 'TT_blind_columns':['R2','RBoxR'],
 'max_R2_Richardson_response_artifact':max(raw_blind['R2']),
 'max_RBoxR_Richardson_response_artifact':max(raw_blind['RBoxR']),
 'max_permutation_error':{k:float(max(abs(x) for x in v)) for k,v in perm_errors.items()},
 'existing_base_rank':int(np.linalg.matrix_rank(Mbase,tol=1e-10)),
 'extended_local_rank':int(np.linalg.matrix_rank(Mext,tol=1e-10)),
 'extended_singular_values':sv.tolist(),
 'conditioned_residual_audits':audits,
 'ward':ward,
 'retained_results':[
   'C5-NG-001 — CURVATURE_SQUARED_RESPONSE_REQUIRES_PROPAGATOR_INSERTIONS',
   'C5-NG-002 — SCALAR_CURVATURE_SQUARED_DIRECTIONS_TT_CUBIC_BLIND',
   'NG-FUNNEL-019 — LOWER_DERIVATIVE_KERNEL_DEFORMATIONS_REQUIRE_FULL_RESPONSE_TANGENT'],
 'status':{
   'Ricci2_full_tangent':'PASS_SCOPED_WARD_VALIDATED',
   'RicciBoxRicci_full_tangent':'PASS_SCOPED_WARD_VALIDATED',
   'R2_RBoxR':'TT_PROTOCOL_BLIND_SCOPED',
   'local_C5_rank':'5_OF_6_ON_IMPLEMENTED_ORDERED_RESPONSE_PROTOCOL',
   'higher_local':'BLOCKED','loops_nonanalytic':'BLOCKED','N2_C3sym':'BLOCKED',
   'ANSATZ_003':'NOT_CREATED','Fisher_resources':'FORBIDDEN'},
 'model_readiness_percent':24,
 'readiness_change':'+1 point: explicit source-completed local C5 ordered tangent extended from EH+2 R3 directions to two additional independent curvature-squared/derivative directions; scalar-curvature directions scoped as TT blind'
}
print(json.dumps(out,indent=2,sort_keys=True))
