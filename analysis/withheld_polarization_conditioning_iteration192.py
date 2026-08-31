#!/usr/bin/env python3
"""Iteration 192: audit the prospectively frozen polarization seeds of
RQIR-WITHHELD-NULLSOFT-12-v1 before any cubic comparator result is accepted.

The normalized hard TT projector is invalid for a soft extrapolation if its raw
projected norm crosses zero between epsilon=0 and a frozen soft step.  This is a
geometry/numerics validity check, not a target selection.
"""
from pathlib import Path
import json, numpy as np

ETA=np.diag([-1.,1.,1.,1.])
QS0=np.array([[0.18,0.70,0.20,0.10],[0.14,0.55,-0.25,0.20],[0.22,0.62,0.18,-0.24],[0.16,0.48,0.31,0.12],[0.20,0.58,-0.16,-0.28],[0.12,0.44,0.27,-0.19]],float)
scales=[0.75,1.25]; HS=[0.01,0.005,0.0025,0.00125,0.000625]; k0=np.array([1.,0.,0.,1.])

def dot(a,b): return float(a@ETA@b)
def theta(k):
    kc=ETA@k; return ETA-np.outer(kc,kc)/dot(k,k)
def p2(k):
    t=theta(k); return .5*(np.einsum('mr,ns->mnrs',t,t)+np.einsum('ms,nr->mnrs',t,t))-(1/3)*np.einsum('mn,rs->mnrs',t,t)
def raw_norm(k,seed):
    rng=np.random.default_rng(seed); A=rng.normal(size=(4,4)); A=(A+A.T)/2
    P=p2(k); e=np.einsum('mnrs,ra,sb,ab->mn',P,ETA,ETA,A)
    return float(np.einsum('mn,ma,nb,ab',e,ETA,ETA,e))

rows=[]
for scale in scales:
    for src,q0 in enumerate(QS0):
        rid=len(rows); q=scale*q0; s2=19000+2*rid; s3=19001+2*rid
        n2=raw_norm(q,s2); n30=raw_norm(-q,s3)
        n3=[raw_norm(-q-h*k0,s3) for h in HS]
        signs=[np.sign(n30)]+[np.sign(z) for z in n3]
        sign_flip=any(s!=signs[0] for s in signs[1:])
        rows.append({"row_id":f"W{rid:02d}","source_row":src,"scale":scale,
                     "seed_pair":[s2,s3],"hard2_raw_norm":n2,
                     "partner_raw_norm_at_soft_zero":n30,
                     "partner_raw_norm_positive_steps":n3,
                     "min_abs_partner_norm":min(abs(z) for z in [n30]+n3),
                     "sign_flip_before_soft_limit":bool(sign_flip),
                     "cubic_soft_status":"BLOCKED_POLARIZATION_ZERO_CROSSING" if sign_flip else "PASS_GEOMETRIC_CONDITIONING"})
blocked=[r['row_id'] for r in rows if r['sign_flip_before_soft_limit']]
out={
 "iteration":192,"model_readiness_percent":24,
 "protocol":"RQIR-WITHHELD-NULLSOFT-12-v1",
 "scope":"pre-comparator cubic polarization-conditioning audit; K2-only rows unaffected",
 "rows":rows,"blocked_rows":blocked,"n_blocked":len(blocked),
 "classification":{
   "K2_iteration191":"UNAFFECTED_SEED_INDEPENDENT",
   "cubic_v1_protocol":"PARTIALLY_BLOCKED_DO_NOT_DROP_OR_RESEED_POSTHOC",
   "candidate_evaluated":False,"ANSATZ_003":"NOT_CREATED","Fisher_resources":"FORBIDDEN"},
 "retained_results":[
   "NUM-NG-006 — PREREGISTERED_W05_POLARIZATION_CROSSES_A_TT_PROJECTOR_ZERO_BEFORE_THE_SOFT_LIMIT",
   "PROTO-NG-002 — FAILED_PREREGISTERED_CUBIC_ROW_MUST_NOT_BE_SILENTLY_RESEEDED_OR_DROPPED",
   "NG-FUNNEL-047 — POLARIZATION_CONDITIONING_CRITERION_MUST_BE_FROZEN_BEFORE_THE_NEXT_WITHHELD_CUBIC_PROTOCOL"
 ],
 "readiness_change":"unchanged: a preregistered numerical validity failure is identified before comparator/candidate evaluation"
}
Path('results/withheld_polarization_conditioning_iteration192.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print(json.dumps(out,indent=2,sort_keys=True))
