#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 198.

Freeze cubic polarization geometry for the already-frozen v3 K2 hard rows.
The acceptance rule is geometry-only and applied identically to all 12 rows
before any v3 cubic C5/nonlocal or candidate observable is evaluated.
"""
from pathlib import Path
import json, numpy as np

ETA=np.diag([-1.,1.,1.,1.]); k0=np.array([1.,0.,0.,1.])
QS0=np.array([[0.18,0.70,0.20,0.10],[0.14,0.55,-0.25,0.20],[0.22,0.62,0.18,-0.24],[0.16,0.48,0.31,0.12],[0.20,0.58,-0.16,-0.28],[0.12,0.44,0.27,-0.19]],float)
QS=np.vstack([.80*QS0,1.40*QS0]); threshold=.25; grid=np.linspace(-.01,.01,81)

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
        if np.min(np.abs(ns))>=threshold and np.all(np.sign(ns)==np.sign(ns[0])):
            return seed,ns
    raise RuntimeError('no partner seed')

rows=[]
for i,q in enumerate(QS):
    s2,n2=choose_hard(q,198000+1000*i)
    s3,ns=choose_partner(q,198500+1000*i)
    rows.append({
      'row_id':f'W3-{i:02d}','q':q.tolist(),'q2':dot(q,q),
      'hard_seed':s2,'partner_seed':s3,'hard_raw_norm':n2,
      'partner_min_abs_norm_dense_grid':float(np.min(np.abs(ns))),
      'partner_sign':int(np.sign(ns[0]))})

out={
 'iteration':198,
 'protocol':'RQIR-WITHHELD-NULLSOFT-12-v3',
 'parent_kinematics':'Iteration-197 v3 K2-frozen rows at scales 0.80 and 1.40',
 'seed_rule':{
   'hard_start':'198000+1000*row','partner_start':'198500+1000*row','scan_increment':1,
   'hard_accept':'abs(raw TT norm)>=0.25',
   'partner_accept':'min abs raw TT norm >=0.25 and constant sign on 81-point epsilon grid [-0.01,0.01]'},
 'rows':rows,
 'minimum_hard_abs_norm':min(abs(r['hard_raw_norm']) for r in rows),
 'minimum_partner_margin':min(r['partner_min_abs_norm_dense_grid'] for r in rows),
 'status':'PREREGISTERED_V3_ALL_12_ROWS_PASS_GEOMETRIC_CONDITIONING_BEFORE_CUBIC_COMPARATOR_EVALUATION',
 'classification':{
   'target_optimized':False,'candidate_evaluated':False,
   'comparator_cubic_evaluated_before_freeze':False,
   'ANSATZ_003':'NOT_CREATED','Fisher_resources':'FORBIDDEN'},
 'retained_results':[
   'PROTO-NG-005 — V3_GEOMETRY_ONLY_DENSE_GRID_POLARIZATION_ACCEPTANCE_FROZEN_BEFORE_CUBIC_EVALUATION',
   'NUM-NG-012 — ALL_12_V3_ROWS_PASS_WITH_MIN_PARTNER_TT_NORM_MARGIN_ABOVE_0P90',
   'NG-FUNNEL-052 — CONDITIONING_DESIGNED_ROWS_REQUIRE_INDEPENDENT_PROSPECTIVE_POLARIZATION_FREEZE_BEFORE_CUBIC_USE'],
 'model_readiness_percent':24,
 'readiness_change':'unchanged: v3 cubic geometry is now validly frozen but no v3 cubic comparator or candidate residual has yet been evaluated.'}
Path('results/preregistered_withheld_v3_polarization_iteration198.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2,sort_keys=True))
