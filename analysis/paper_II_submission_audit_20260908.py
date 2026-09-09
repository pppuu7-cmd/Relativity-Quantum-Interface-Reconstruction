#!/usr/bin/env python3
"""Submission-level independent audit for RQIR Paper II.

Reproduces the seven RQIR-STAT-001 certificate regressions and adds a
10,000-trial property audit plus a correlated-covariance whitening check.
All random seeds are fixed for reproducibility.
"""
from __future__ import annotations
import json, math, csv
from pathlib import Path
import numpy as np

OUT = Path(__file__).resolve().parent / "data"
OUT.mkdir(exist_ok=True)

def profiled_fisher(s, J, prior=None, rcond=1e-14):
    s=np.asarray(s,float).reshape(-1)
    J=np.asarray(J,float)
    if J.ndim==1: J=J[:,None]
    if J.shape[1]==0: return float(s@s)
    fbb=float(s@s); fbt=s@J; ftt=J.T@J
    if prior is not None: ftt=ftt+np.asarray(prior,float)
    return float(fbb - fbt @ np.linalg.pinv(ftt,rcond=rcond) @ fbt.T)

def certificate():
    rng=np.random.default_rng(20260830)
    s=rng.normal(size=8); J=rng.normal(size=(8,3))
    fs=profiled_fisher(s,J)
    proj=J@np.linalg.pinv(J)
    fp=float(np.linalg.norm((np.eye(len(s))-proj)@s)**2)
    M=rng.normal(size=(3,3))
    while abs(np.linalg.det(M))<0.2: M=rng.normal(size=(3,3))
    P=np.diag([0.2,0.7,1.3])
    fo=profiled_fisher(s,J,P)
    fr=profiled_fisher(s,J@M,M.T@P@M)
    Q=rng.normal(size=(3,3)); extra=Q.T@Q
    fw=profiled_fisher(s,J,P); fst=profiled_fisher(s,J,P+extra)
    s0=np.array([1.,0.])
    cas=[0.,1.,4.,9.,19.,99.]
    rescue=[{"C_a":ca,"F_profile":profiled_fisher(s0,s0[:,None],np.array([[ca]])),
             "analytic":0.0 if ca==0 else ca/(1+ca)} for ca in cas]
    exps=[1.,2.,10.,100.,1e6]
    expo=[{"exposure":e,"F_profile":profiled_fisher(math.sqrt(e)*s0,(math.sqrt(e)*s0)[:,None])} for e in exps]
    g2,g4=.3,.7; g=np.array([g2,g4]); tilt=np.array([g2,-g4])
    ft=profiled_fisher(g,tilt[:,None]); seff=4*g2*g2*g4*g4/(g2*g2+g4*g4)
    eps=1e-8; science=np.array([1.,0.]); nuisance=np.array([[eps],[0.]])
    ftrue=profiled_fisher(science,nuisance,rcond=1e-30)
    ftt=float((nuisance.T@nuisance)[0,0]); fbt=float(science@nuisance[:,0]); threshold=1e-12
    fbad=1-(fbt*fbt/ftt if ftt>threshold else 0.0)
    return {
      "seed":20260830,
      "A_projection_schur":{"schur":fs,"projection":fp,"abs_error":abs(fs-fp)},
      "B_coordinate_invariance":{"original":fo,"reparameterized":fr,"abs_error":abs(fo-fr)},
      "C_prior_monotonicity":{"weak":fw,"strong":fst,"margin":fst-fw},
      "D_prior_rescue":rescue,
      "E_exposure_obstruction":expo,
      "F_two_band":{"g2":g2,"g4":g4,"F_profile":ft,"analytic":seff,
                    "raw_F":float(g@g),"retention":ft/float(g@g)},
      "G_threshold_counterexample":{"eps":eps,"Ftt":ftt,"true":ftrue,"bad_threshold":threshold,"bad":fbad}
    }

def property_audit(n_trials=10000, seed=20260908):
    rng=np.random.default_rng(seed)
    max_ps=max_reparam=max_cov=0.0
    min_mono=float('inf'); min_shared=float('inf')
    violations={k:0 for k in ['projection_schur','reparam','monotonicity','alignment','shared_bound','covariance']}
    for i in range(n_trials):
        n=int(rng.integers(4,12)); m=int(rng.integers(1,min(5,n)))
        s=rng.normal(size=n); J=rng.normal(size=(n,m))
        if i%5==0 and m>1:
            J[:,-1]=J[:,:-1]@rng.normal(size=m-1)
        fs=profiled_fisher(s,J,rcond=1e-13)
        Pj=J@np.linalg.pinv(J,rcond=1e-13)
        fp=float(np.linalg.norm((np.eye(n)-Pj)@s)**2)
        e=abs(fs-fp); max_ps=max(max_ps,e)
        if e>1e-9: violations['projection_schur']+=1
        A=rng.normal(size=(m,m)); prior=A.T@A+1e-4*np.eye(m)
        M=rng.normal(size=(m,m))
        while abs(np.linalg.det(M))<0.1: M=rng.normal(size=(m,m))
        fo=profiled_fisher(s,J,prior,rcond=1e-13)
        fr=profiled_fisher(s,J@M,M.T@prior@M,rcond=1e-13)
        e=abs(fo-fr); max_reparam=max(max_reparam,e)
        if e>1e-8: violations['reparam']+=1
        B=rng.normal(size=(m,m)); strong=profiled_fisher(s,J,prior+B.T@B,rcond=1e-13)
        d=strong-fo; min_mono=min(min_mono,d)
        if d < -1e-9: violations['monotonicity']+=1
        salign=J@rng.normal(size=m)
        fa=profiled_fisher(salign,J,rcond=1e-13)
        if abs(fa)>1e-8*(1+float(salign@salign)): violations['alignment']+=1
        n1=int(rng.integers(m+1,m+6)); n2=int(rng.integers(m+1,m+6))
        g1=rng.normal(size=n1); g2=rng.normal(size=n2)
        W1=rng.normal(size=(n1,m)); W2=rng.normal(size=(n2,m))
        fj=profiled_fisher(np.r_[g1,g2],np.vstack([W1,W2]),rcond=1e-13)
        fsep=profiled_fisher(g1,W1,rcond=1e-13)+profiled_fisher(g2,W2,rcond=1e-13)
        d=fj-fsep; min_shared=min(min_shared,d)
        if d < -1e-8: violations['shared_bound']+=1
        nc=int(rng.integers(4,10)); mc=int(rng.integers(1,min(4,nc)))
        X=rng.normal(size=(nc,nc)); C=X@X.T+0.5*np.eye(nc)
        t=rng.normal(size=nc); K=rng.normal(size=(nc,mc)); Ci=np.linalg.inv(C)
        ffull=float(t@Ci@t-(t@Ci@K)@np.linalg.pinv(K.T@Ci@K,rcond=1e-13)@(K.T@Ci@t))
        vals,vecs=np.linalg.eigh(C); Wc=(vecs*(1/np.sqrt(vals)))@vecs.T
        fw=profiled_fisher(Wc@t,Wc@K,rcond=1e-13)
        e=abs(ffull-fw); max_cov=max(max_cov,e)
        if e>1e-8: violations['covariance']+=1
    return {"seed":seed,"trials":n_trials,
      "max_projection_schur_abs_error":max_ps,
      "max_reparameterization_abs_error":max_reparam,
      "minimum_prior_monotonicity_margin":min_mono,
      "minimum_shared_minus_separate_information":min_shared,
      "max_full_covariance_whitening_abs_error":max_cov,
      "violations":violations}

def deterministic_covariance_case():
    rng=np.random.default_rng(20260908); n=6; m=2
    X=rng.normal(size=(n,n)); C=X@X.T+0.5*np.eye(n)
    t=rng.normal(size=n); K=rng.normal(size=(n,m)); Ci=np.linalg.inv(C)
    ffull=float(t@Ci@t-(t@Ci@K)@np.linalg.pinv(K.T@Ci@K,rcond=1e-13)@(K.T@Ci@t))
    vals,vecs=np.linalg.eigh(C); Wc=(vecs*(1/np.sqrt(vals)))@vecs.T
    fw=profiled_fisher(Wc@t,Wc@K,rcond=1e-13)
    return {"seed":20260908,"dimension":n,"nuisance_dimension":m,
            "condition_number_C":float(np.linalg.cond(C)),"full_metric":ffull,
            "whitened":fw,"abs_error":abs(ffull-fw)}

def write_curve_data():
    with open(OUT/'prior_rescue.csv','w',newline='') as f:
        w=csv.writer(f); w.writerow(['C_a','F_profile'])
        for x in np.linspace(0,20,81): w.writerow([f'{x:.8g}',f'{x/(1+x):.12g}'])
    with open(OUT/'two_band_retention.csv','w',newline='') as f:
        w=csv.writer(f); w.writerow(['ratio_g4_over_g2','retention'])
        for r in np.geomspace(0.08,12.5,121): w.writerow([f'{r:.12g}',f'{4*r*r/(1+r*r)**2:.12g}'])
    with open(OUT/'cutoff_scan.csv','w',newline='') as f:
        w=csv.writer(f); w.writerow(['inverse_threshold','inferred_F'])
        ftt=1e-16
        for th in np.logspace(-20,-10,121): w.writerow([f'{th:.12g}','0' if ftt>th else '1'])
    with open(OUT/'detectability_map.csv','w',newline='') as f:
        w=csv.writer(f); w.writerow(['delta','lambda','retention'])
        for lam in np.linspace(0,4,41):
            for d in np.linspace(0,1.5,41):
                rho=(d*d+lam)/(1+d*d+lam)
                w.writerow([f'{d:.8g}',f'{lam:.8g}',f'{rho:.12g}'])

if __name__=='__main__':
    cert=certificate(); prop=property_audit(); cov=deterministic_covariance_case()
    payload={
      "artifact":"RQIR Paper II submission audit",
      "date":"2026-09-08",
      "baseline_repository_commit":"9c69f6acab4658565eb016380b03df8ac7807799",
      "authoritative_certificate":"docs/PAPER_II_REFERENCE_LIKELIHOOD_CERTIFICATE_ITERATION079.md",
      "authoritative_script":"analysis/paper12_reference_regression_iteration079.py",
      "certificate_reproduction":cert,
      "independent_property_audit":prop,
      "deterministic_full_covariance_case":cov
    }
    (OUT/'rqir_stat_001_submission_audit.json').write_text(json.dumps(payload,indent=2),encoding='utf-8')
    write_curve_data()
    print(json.dumps(payload,indent=2))
