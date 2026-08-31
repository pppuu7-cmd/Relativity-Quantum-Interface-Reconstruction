#!/usr/bin/env python3
"""Iteration 193: freeze v2 of the withheld 12-row cubic protocol after the
v1 preregistered W05 polarization-conditioning failure.

The new seed rule is geometry-only and identical for every row.  It is frozen
before any C5/nonlocal cubic result or Candidate Gravity target is evaluated.
"""
from pathlib import Path
import json, numpy as np

ETA=np.diag([-1.,1.,1.,1.]); k0=np.array([1.,0.,0.,1.])
QS0=np.array([[0.18,0.70,0.20,0.10],[0.14,0.55,-0.25,0.20],[0.22,0.62,0.18,-0.24],[0.16,0.48,0.31,0.12],[0.20,0.58,-0.16,-0.28],[0.12,0.44,0.27,-0.19]],float)
QS=np.vstack([.75*QS0,1.25*QS0]); threshold=.25; grid=np.linspace(-.01,.01,81)

def dot(a,b): return float(a@ETA@b)
def theta(k):
    kc=ETA@k; return ETA-np.outer(kc,kc)/dot(k,k)
def p2(k):
    t=theta(k); return .5*(np.einsum('mr,ns->mnrs',t,t)+np.einsum('ms,nr->mnrs',t,t))-(1/3)*np.einsum('mn,rs->mnrs',t,t)
def raw_norm(k,seed):
    rng=np.random.default_rng(seed); A=rng.normal(size=(4,4)); A=(A+A.T)/2
    P=p2(k); e=np.einsum('mnrs,ra,sb,ab->mn',P,ETA,ETA,A)
    return float(np.einsum('mn,ma,nb,ab',e,ETA,ETA,e))
def choose_hard(q,start):
    for seed in range(start,start+1000):
        n=raw_norm(q,seed)
        if abs(n)>=threshold: return seed,n
    raise RuntimeError('no hard seed')
def choose_partner(q,start):
    for seed in range(start,start+5000):
        ns=np.array([raw_norm(-q-e*k0,seed) for e in grid])
        if np.min(np.abs(ns))>=threshold and np.all(np.sign(ns)==np.sign(ns[0])): return seed,ns
    raise RuntimeError('no partner seed')
rows=[]
for i,q in enumerate(QS):
    s2,n2=choose_hard(q,193000+1000*i); s3,ns=choose_partner(q,193500+1000*i)
    rows.append({"row_id":f"W2-{i:02d}","q":q.tolist(),"q2":dot(q,q),"hard_seed":s2,"partner_seed":s3,
                 "hard_raw_norm":n2,"partner_min_abs_norm_dense_grid":float(np.min(np.abs(ns))),
                 "partner_sign":int(np.sign(ns[0]))})
out={"iteration":193,"model_readiness_percent":24,"protocol":"RQIR-WITHHELD-NULLSOFT-12-v2",
 "parent_kinematics":"same 12 q rows as v1; only polarization seed acceptance is repaired prospectively",
 "seed_rule":{"hard_start":"193000+1000*row","partner_start":"193500+1000*row","scan_increment":1,
              "hard_accept":"abs(raw TT norm)>=0.25","partner_accept":"min abs raw TT norm >=0.25 and constant sign on 81-point epsilon grid [-0.01,0.01]"},
 "rows":rows,"minimum_partner_margin":min(r['partner_min_abs_norm_dense_grid'] for r in rows),
 "status":"PREREGISTERED_V2_ALL_12_ROWS_PASS_GEOMETRIC_CONDITIONING_BEFORE_CUBIC_COMPARATOR_EVALUATION",
 "classification":{"target_optimized":False,"candidate_evaluated":False,"comparator_cubic_evaluated_before_freeze":False,
                   "ANSATZ_003":"NOT_CREATED","Fisher_resources":"FORBIDDEN"},
 "retained_results":["PROTO-NG-003 — GEOMETRY_ONLY_DENSE_GRID_POLARIZATION_ACCEPTANCE_FROZEN_FOR_WITHHELD_V2",
                     "NUM-NG-007 — ALL_12_V2_ROWS_PASS_WITH_MIN_PARTNER_TT_NORM_MARGIN_ABOVE_0P66",
                     "NG-FUNNEL-048 — NUMERICAL_PROTOCOL_REPAIR_MUST_BE_PROSPECTIVE_AND_TARGET_INDEPENDENT"],
 "readiness_change":"unchanged: v2 repairs a numerical protocol validity issue but has not yet produced comparator or residual closure"}
Path('results/preregistered_withheld_row_extension_v2_iteration193.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print(json.dumps(out,indent=2,sort_keys=True))
