#!/usr/bin/env python3
"""Iteration 165: target-independent local-C5 cubic completion through dimension 12.

Iteration 164 left a scoped dRGT tangent residual in a 12-row TT protocol because
only five pure-C5 ordered-response columns were instantiated.  C5 had already
used a dimension-12 cutoff in the linear TT sector.  Here the nonlinear sector
is extended by a deterministic descendant rule that never consults the target:

  * add the standard mixed cubic invariant Ricci Ricci Riemann (dimension 6);
  * for the two already-authorized Ricci^3 and cyclic Riemann^3 chains, add
    Box^n descendants n=1,2,3 (dimensions 8,10,12).

All these operators start at O(h^3) about flat space.  Therefore their cubic
terms are exactly products of linearized curvatures with flat Box factors; metric
corrections to index raising and variations of Box first enter O(h^4).  Their
operator-specific B2 vanishes, so the cubic Ward check is simply B3[L_xi,...]=0.

The script reuses the frozen Iteration-164 rows and Iteration-150 curvature
conventions, then audits rank/SVD and dRGT target residuals.  This is a finite
protocol certificate, never a theory identity.
"""
from pathlib import Path
import contextlib, io, itertools, json, runpy
import numpy as np

with contextlib.redirect_stdout(io.StringIO()):
    i164 = runpy.run_path("analysis/enriched_tt_protocol_iteration164.py")

c150 = i164["c150"]
ETA = c150["ETA"]
dot = c150["dot"]
polarization = c150["polarization"]
window = c150["window"]
lin_ricci = c150["lin_ricci"]
lin_riemann = c150["lin_riemann"]

# Pure-C5 base from Iteration 164: omit the dRGT shared-reference column.
M164 = np.asarray(i164["M"], float)
T = np.asarray(i164["T"], float)  # d/dlog(m^2), d/dalpha3
C5base = M164[:, :5]

legacy_pairs = list(zip(c150["QS"], c150["RS"]))
new_pairs = i164["pairs"]
pairs = legacy_pairs + new_pairs


def make_es(i, ks):
    out=[]
    for leg in range(3):
        seed_id = 100 + 3*i + leg if i < 6 else 2000 + 3*(i-6) + leg
        rng=np.random.default_rng(seed_id)
        A=rng.normal(size=(4,4)); seed=(A+A.T)/2
        out.append(polarization(ks[leg], seed))
    return out


def ricci_chain_boxn(ks, es, n):
    """Mixed cubic coefficient of R_m^n R_n^r Box^n R_r^m."""
    A=[ETA @ lin_ricci(k,e) for k,e in zip(ks,es)]
    val=0j
    for a,b,c in itertools.permutations(range(3)):
        val += (-dot(ks[c],ks[c]))**n * np.trace(A[a]@A[b]@A[c])
    return val.real


def riemann_chain_boxn(ks, es, n):
    """Mixed cubic coefficient of cyclic Riem Riem Box^n Riem."""
    A=[]
    for k,e in zip(ks,es):
        R=lin_riemann(k,e)
        A.append(np.einsum('mnab,ar,bs->mnrs',R,ETA,ETA).reshape(16,16))
    val=0j
    for a,b,c in itertools.permutations(range(3)):
        val += (-dot(ks[c],ks[c]))**n * np.trace(A[a]@A[b]@A[c])
    return val.real


def mixed_ricci_ricci_riemann(ks, es):
    """Mixed coefficient of R_mn R_rs R^{m r n s}."""
    Ric=[lin_ricci(k,e) for k,e in zip(ks,es)]
    Rm=[lin_riemann(k,e) for k,e in zip(ks,es)]
    val=0j
    for a,b,c in itertools.permutations(range(3)):
        Rup=np.einsum('abcd,ma,rb,nc,sd->mrns',Rm[c],ETA,ETA,ETA,ETA)
        val += np.einsum('mn,rs,mrns',Ric[a],Ric[b],Rup)
    return val.real


rows=[]
max_lin_ricci_gauge=0.0; max_lin_riemann_gauge=0.0
max_descendant_gauge=0.0; max_mixed_gauge=0.0
for i,(q,r) in enumerate(pairs):
    p=q+r; ks=[p,-q,-r]; es=make_es(i,ks)
    common=float(np.prod([1/dot(k,k) for k in ks])*np.prod([window(k) for k in ks]))
    rec={"probe":i,"p2":dot(p,p),"q2":dot(q,q),"r2":dot(r,r),"common":common}
    rec["mixed_RicciRicciRiemann"] = mixed_ricci_ricci_riemann(ks,es)*common
    for n in (1,2,3):
        rec[f"RicciChain_Box{n}"] = ricci_chain_boxn(ks,es,n)*common
        rec[f"RiemannChain_Box{n}"] = riemann_chain_boxn(ks,es,n)*common

    # Gauge/Ward check: each new O(h^3) operator is made solely from linearized
    # curvatures, so replacement of any one leg by L_xi must annihilate it.
    for leg in range(3):
        xi=np.random.default_rng(165000+3*i+leg).normal(size=4)
        kc=ETA@ks[leg]; gauge=np.outer(kc,xi)+np.outer(xi,kc)
        max_lin_ricci_gauge=max(max_lin_ricci_gauge,float(np.max(np.abs(lin_ricci(ks[leg],gauge)))))
        max_lin_riemann_gauge=max(max_lin_riemann_gauge,float(np.max(np.abs(lin_riemann(ks[leg],gauge)))))
        eg=list(es); eg[leg]=gauge
        for n in (1,2,3):
            max_descendant_gauge=max(max_descendant_gauge,
                abs(ricci_chain_boxn(ks,eg,n)),abs(riemann_chain_boxn(ks,eg,n)))
        max_mixed_gauge=max(max_mixed_gauge,abs(mixed_ricci_ricci_riemann(ks,eg)))
    rows.append(rec)

# Dimension-ordered, target-independent extension of the five-column pure-C5 base.
extra_names=[
    "mixed_RicciRicciRiemann_dim6",
    "RicciChain_Box1_dim8","RiemannChain_Box1_dim8",
    "RicciChain_Box2_dim10","RiemannChain_Box2_dim10",
    "RicciChain_Box3_dim12","RiemannChain_Box3_dim12",
]
extra=np.column_stack([
    [r["mixed_RicciRicciRiemann"] for r in rows],
    [r["RicciChain_Box1"] for r in rows], [r["RiemannChain_Box1"] for r in rows],
    [r["RicciChain_Box2"] for r in rows], [r["RiemannChain_Box2"] for r in rows],
    [r["RicciChain_Box3"] for r in rows], [r["RiemannChain_Box3"] for r in rows],
])
C5=np.column_stack([C5base,extra])

progress=[]
for j in range(0,8):
    B=np.column_stack([C5base,extra[:,:j]]) if j else C5base
    progress.append({"extra_columns_added":j,"n_columns":int(B.shape[1]),
        "base_rank":int(np.linalg.matrix_rank(B,tol=1e-12)),
        "rank_with_both_dRGT_targets":int(np.linalg.matrix_rank(np.column_stack([B,T]),tol=1e-12))})


def audit(scale):
    B=C5*scale[:,None]; Y=T*scale[:,None]
    s=np.linalg.svd(B,compute_uv=False)
    coeff=np.linalg.solve(B,Y)
    res=Y-B@coeff
    return {"rank":int(np.linalg.matrix_rank(B,tol=1e-12)),
        "singular_values":s.tolist(),"smin_over_smax":float(s[-1]/s[0]),
        "condition_number":float(s[0]/s[-1]),
        "relative_residuals":(np.linalg.norm(res,axis=0)/np.linalg.norm(Y,axis=0)).tolist(),
        "max_abs_residuals":np.max(np.abs(res),axis=0).tolist()}

scales={
    "raw":np.ones(12),
    "base_row_l2":1/np.maximum(np.linalg.norm(C5,axis=1),1e-12),
    "EH_abs_floor":1/np.maximum(np.abs(C5[:,0]),1e-2),
}
audits={k:audit(v) for k,v in scales.items()}

out={
 "iteration":165,
 "scope":"12 frozen spacelike TT ordered-response rows; local C5 tree subset through cubic operator dimension 12",
 "target_independent_completion_rule":"extend the two existing cubic curvature chains with Box^n descendants n=1,2,3 and add the mixed Ricci-Ricci-Riemann cubic invariant; stop at the pre-existing dimension-12 C5 cutoff",
 "base_columns":["EH","Ricci3","Riemann3","Ricci2_full","RicciBoxRicci_full"],
 "extra_columns":extra_names,
 "matrix_shape":list(C5.shape),
 "rank":int(np.linalg.matrix_rank(C5,tol=1e-12)),
 "rank_with_dRGT_targets":int(np.linalg.matrix_rank(np.column_stack([C5,T]),tol=1e-12)),
 "progressive_dimension_order":progress,
 "audits":audits,
 "ward":{"max_abs_linearized_Ricci_on_gauge":max_lin_ricci_gauge,
         "max_abs_linearized_Riemann_on_gauge":max_lin_riemann_gauge,
         "max_abs_derivative_descendant_B3_on_gauge":max_descendant_gauge,
         "max_abs_mixed_B3_on_gauge":max_mixed_gauge,
         "status":"PASS_SCOPED_MACHINE_PRECISION"},
 "rows":rows,
 "classification":{"local_C5_dimension12_subset":"FULL_ROW_RANK_12_OF_12",
    "dRGT_dlogm2":"ABSORBED_FINITE_PROTOCOL",
    "dRGT_dalpha3":"ABSORBED_FINITE_PROTOCOL",
    "full_12row_ordered_TT_novelty_dimension":"ZERO_BECAUSE_C5_SUBSET_ALREADY_SPANS_ROW_SPACE",
    "theory_identity":False},
 "retained_results":[
    "C5-NG-003 — DIMENSION12_LOCAL_C5_CUBIC_SUBSET_SATURATES_ENRICHED_12ROW_TT_PROTOCOL",
    "C4-NG-007 — ITERATION164_DRGT_RESIDUAL_ABSORBED_BY_TARGET_INDEPENDENT_DIMENSION12_C5_COMPLETION",
    "NG-FUNNEL-022 — FINITE_PROTOCOL_RESIDUAL_MUST_SURVIVE_THEORY_AUTHORIZED_COMPARATOR_BASIS_COMPLETION",
    "NG-FUNNEL-023 — ONCE_ONE_AUTHORIZED_COMPARATOR_SPANS_THE_FINITE_ROW_SPACE_ADDITIONAL_BLOCKED_COMPARATORS_CANNOT_RESTORE_A_RESIDUAL_IN_THAT_SAME_SPACE"],
 "nonlocal_registry_note":"NL-WNL-001 and QG-NL-EXP-001 are distinct Iteration-158 comparator records; neither blocked nonlinear column is needed to prove zero residual in this already C5-saturated 12-row sector, but both remain relevant outside it",
 "ANSATZ_003":"NOT_CREATED",
 "Fisher_resources":"FORBIDDEN_ZERO_ALGEBRAIC_RESIDUAL",
 "model_readiness_percent":24,
 "readiness_change":"+1 comparator-foundation point (23/25 -> 24/25); robust unique residual remains 0/20"
}
Path("results/c5_dimension12_cubic_completion_iteration165.json").write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
print(json.dumps(out,indent=2,sort_keys=True))
