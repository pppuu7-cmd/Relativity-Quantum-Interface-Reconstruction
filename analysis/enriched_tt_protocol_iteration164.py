#!/usr/bin/env python3
"""Iteration 164: target-independent enrichment of the saturated six-row TT protocol.

The six legacy TT rows were saturated in Iteration 163 by
  [EH, Ricci^3, Riemann^3, Ricci^2_full, Ricci Box Ricci_full, dRGT reference].
This script adds six NEW spacelike triplets frozen by a deterministic kinematic
rule that never consults the dRGT target residuals, recomputes the same declared
C5/C4 columns, and only then tests the dRGT tangent quotient.

Provenance correction: Iteration 163 labelled the two arrays "alpha3, alpha4".
They are exactly the Iteration-156 tangent columns d/d log(m^2), d/d alpha3.
alpha4 remains cubic-TT blind because L4 starts quartic.  The old six-row
numerical saturation certificate is unchanged; only the labels are corrected.
"""
from pathlib import Path
import contextlib, io, itertools, json, math, runpy
import numpy as np

# Reuse the already Ward-validated numerical engines, without duplicating them.
with contextlib.redirect_stdout(io.StringIO()):
    c150 = runpy.run_path("analysis/c5_cubic_response_iteration150.py")
    c162 = runpy.run_path("analysis/c5_curvature_squared_retarded_tangent_iteration162.py")

r150 = json.loads(Path("results/c5_cubic_response_iteration150.json").read_text())
r162 = json.loads(Path("results/c5_curvature_squared_retarded_tangent_iteration162.json").read_text())
r156 = json.loads(Path("results/c4_drgt_nonlinear_tangent_iteration156.json").read_text())
assert r156["tangent_parameters"] == ["log_m2", "alpha3"]
assert "BLIND" in r156["alpha4_cubic_TT_status"]

ETA = c150["ETA"]
dot = c150["dot"]
polarization = c150["polarization"]
window = c150["window"]
mixed = c150["mixed3"]
eh_gamma_gamma = c150["eh_gamma_gamma"]
ricci3 = c150["ricci3"]
riem3 = c150["riem3"]
action_density = c162["action_density"]

# Legacy authoritative six rows.
EH0 = np.array([x["EH_response"] for x in r150["rows"]], float)
R3A0 = np.array([x["Ricci3_response"] for x in r150["rows"]], float)
R3B0 = np.array([x["Riemann3_response"] for x in r150["rows"]], float)
V2_0 = np.array(r162["V_C5_new_full_chi2R"], float)
RREF0 = np.array(r156["tree_response"], float)
T0 = np.array(r156["V_C4_chi2R"], float)  # columns: dlogm2, dalpha3
M0 = np.column_stack([EH0, R3A0, R3B0, V2_0, RREF0])

# Freeze six new rows BEFORE target evaluation.  Generator/acceptance depends
# only on spacelike kinematics and anti-collinearity/conditioning guards.
rng = np.random.default_rng(164031)
pairs = []
attempts = 0
while len(pairs) < 6:
    attempts += 1
    q = np.empty(4); r = np.empty(4)
    q[0] = rng.uniform(0.08, 0.24); r[0] = rng.uniform(0.08, 0.24)
    q[1:] = rng.uniform(-0.68, 0.68, 3); r[1:] = rng.uniform(-0.68, 0.68, 3)
    p = q + r
    inv = np.array([dot(p,p), dot(q,q), dot(r,r)])
    if not np.all((inv >= 0.18) & (inv <= 1.05)):
        continue
    c = abs(np.dot(q[1:], r[1:])/(np.linalg.norm(q[1:])*np.linalg.norm(r[1:])))
    if c > 0.82 or inv.max()/inv.min() > 4.0:
        continue
    pairs.append((q.copy(), r.copy()))
assert attempts == 16

new_rows=[]; Mnew=[]; Tnew=[]
for i,(q,r) in enumerate(pairs):
    p=q+r; ks=[p,-q,-r]
    es=[]
    for leg in range(3):
        rr=np.random.default_rng(2000+3*i+leg)
        A=rr.normal(size=(4,4)); seed=(A+A.T)/2
        es.append(polarization(ks[leg],seed))
    k2=np.array([dot(k,k) for k in ks])
    W=float(np.prod([window(k) for k in ks])); common=W/float(np.prod(k2))

    # EH cubic response, same Richardson convention as Iteration 150.
    e1=mixed(lambda ep: eh_gamma_gamma(ep,ks,es),2.5e-3).real
    e2=mixed(lambda ep: eh_gamma_gamma(ep,ks,es),1.25e-3).real
    EH=float(((4*e2-e1)/3)*common)
    R3A=float(ricci3(ks,es)*common); R3B=float(riem3(ks,es)*common)

    vals={}
    for kind in ("Ricci2","RicciBoxRicci"):
        fn=lambda ep,kind=kind: action_density(ep,ks,es,kind)
        a=c162["mixed"](fn,3,1e-3).real; b=c162["mixed"](fn,3,5e-4).real
        cubic_response=float(((4*b-a)/3)*common)
        lambdas=-k2 if kind=="Ricci2" else k2**2
        vals[kind]=float(cubic_response-EH*np.sum(lambdas))

    # Same frozen dRGT TT dynamics and parameter convention as Iteration 156.
    H=[ETA@e for e in es]
    T3=float(sum(np.trace(H[a]@H[b]@H[c]).real for a,b,c in itertools.permutations(range(3))))
    E=EH*float(np.prod(k2)); P=T3*W; m2=0.04; cpot=3.0/8.0
    D=float(np.prod(k2+m2)); N=E+m2*cpot*P; Rref=N/D
    dlogm2=m2*((cpot*P-N*sum(1/(x+m2) for x in k2))/D)
    dalpha3=m2*(1.0/8.0)*P/D

    Mnew.append([EH,R3A,R3B,vals["Ricci2"],vals["RicciBoxRicci"],Rref])
    Tnew.append([dlogm2,dalpha3])
    new_rows.append({"probe":6+i,"q":q.tolist(),"r":r.tolist(),
      "p2":float(k2[0]),"q2":float(k2[1]),"r2":float(k2[2]),
      "EH":EH,"Ricci3":R3A,"Riemann3":R3B,
      "Ricci2_full":vals["Ricci2"],"RicciBoxRicci_full":vals["RicciBoxRicci"],
      "dRGT_shared_reference":Rref,"d_dlogm2":dlogm2,"d_dalpha3":dalpha3})

M=np.vstack([M0,np.array(Mnew,float)]); T=np.vstack([T0,np.array(Tnew,float)])

def audit(scale):
    Ms=M*scale[:,None]; Ts=T*scale[:,None]
    s=np.linalg.svd(Ms,compute_uv=False); coef=np.linalg.lstsq(Ms,Ts,rcond=None)[0]
    res=Ts-Ms@coef
    return {"base_rank":int(np.linalg.matrix_rank(Ms,tol=1e-12)),
      "combined_rank":int(np.linalg.matrix_rank(np.column_stack([Ms,Ts]),tol=1e-12)),
      "singular_values":s.tolist(),"smin_over_smax":float(s[-1]/s[0]),
      "residual_norms":np.linalg.norm(res,axis=0).tolist(),
      "relative_residual_norms":(np.linalg.norm(res,axis=0)/np.linalg.norm(Ts,axis=0)).tolist(),
      "max_abs_residual_by_target":np.max(np.abs(res),axis=0).tolist()}

scales={"raw":np.ones(12),
 "base_row_l2":1/np.maximum(np.linalg.norm(M,axis=1),1e-12),
 "EH_abs_floor":1/np.maximum(np.abs(M[:,0]),1e-2),
 "dRGT_reference_abs_floor":1/np.maximum(np.abs(M[:,-1]),1e-2)}
audits={k:audit(v) for k,v in scales.items()}

progress=[]
for n in range(1,7):
    Mn=np.vstack([M0,np.array(Mnew[:n],float)]); Tn=np.vstack([T0,np.array(Tnew[:n],float)])
    for name,scale in (("raw",np.ones(6+n)),("row_l2",1/np.maximum(np.linalg.norm(Mn,axis=1),1e-12))):
        Ms=Mn*scale[:,None]; Ts=Tn*scale[:,None]; res=Ts-Ms@np.linalg.lstsq(Ms,Ts,rcond=None)[0]
        progress.append({"new_rows_added":n,"scaling":name,"base_rank":int(np.linalg.matrix_rank(Ms)),
          "combined_rank":int(np.linalg.matrix_rank(np.column_stack([Ms,Ts]))),
          "relative_residual_dlogm2":float(np.linalg.norm(res[:,0])/np.linalg.norm(Ts[:,0])),
          "relative_residual_dalpha3":float(np.linalg.norm(res[:,1])/np.linalg.norm(Ts[:,1]))})

out={"iteration":164,"scope":"12-row enriched TT chi2R protocol",
 "iteration163_label_correction":{"incorrect_labels":["dRGT_alpha3","dRGT_alpha4"],
   "correct_labels":["dRGT_dlogm2","dRGT_dalpha3"],"alpha4":"CUBIC_TT_BLIND","numerics_changed":False},
 "row_freeze":{"legacy_rows":6,"new_rows":6,"generator_seed":164031,"accepted_after_attempts":attempts,
   "acceptance":"0.18<=p2,q2,r2<=1.05; |cos spatial(q,r)|<=0.82; max/min invariants<=4; targets unused",
   "polarization_seed_rule":"2000+3*i+leg","new_rows":new_rows},
 "comparator_columns":["EH","Ricci3","Riemann3","Ricci2_full","RicciBoxRicci_full","dRGT_shared_reference"],
 "targets":["dRGT_dlogm2","dRGT_dalpha3"],"audits":audits,"progressive_freeze_robustness":progress,
 "classification":{"six_row_saturation":"RETAINED_SCOPED","twelve_row_local_quotient":"NOT_SATURATED",
   "dlogm2":"NONZERO_NEAR_DEGENERATE_NOT_PROMOTABLE",
   "dalpha3":"NONZERO_SCOPED_RESIDUAL_NOT_FULL_COMPARATOR_CERTIFICATE","full_novelty_certificate":False},
 "retained_results":[
   "C4-NG-005 — SIX_ROW_SATURATION_DOES_NOT_PERSIST_UNDER_TARGET_INDEPENDENT_TT_ROW_ENRICHMENT",
   "C4-NG-006 — DRGT_DLOGM2_DIRECTION_IS_NEAR_DEGENERATE_AFTER_ENRICHED_LOCAL_C5_QUOTIENT",
   "NG-FUNNEL-021 — PROTOCOL_SATURATION_MUST_BE_TESTED_FOR_STABILITY_UNDER_PRE_FROZEN_ROW_ENRICHMENT",
   "PROVENANCE-CORR-001 — ITERATION163 TARGET LABELS ARE DLOGM2 AND DALPHA3; ALPHA4 REMAINS CUBIC_TT_BLIND"],
 "blocked":["C3 enriched rows","nonlocal enriched causal rows","AS enriched retarded rows","non-TT/helicity completion","C5 loops/full non-TT"],
 "ANSATZ_003":"NOT_CREATED","Fisher_resources":"FORBIDDEN_NO_FULL_COMPARATOR_QUOTIENT_RESIDUAL",
 "model_readiness_percent":23,
 "readiness_change":"+1 comparator-foundation point; unique residual remains 0/20 until full enriched comparator quotient"}
Path("results/enriched_tt_protocol_iteration164.json").write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
print(json.dumps(out,indent=2,sort_keys=True))
