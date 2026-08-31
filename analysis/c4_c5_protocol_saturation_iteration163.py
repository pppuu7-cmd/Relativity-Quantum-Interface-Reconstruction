"""RQIR Candidate Gravity — Iteration 163.

Recompute the frozen dRGT C4 nonlinear tangent quotient after the Iteration 162
expansion of the explicit local C5 ordered-response basis.

This script is deliberately finite-protocol scoped: six frozen TT probes only.
A full-rank six-row comparator span is a protocol-saturation certificate, not a
theory-level identity between dRGT and local EFT.
"""
import json
import numpy as np

EH=np.array([0.30003001285313774,-1.461790494216445,-12.034873790942026,-14.434681522564402,4.867521776975717,-2.7789127642722273])
RICCI3=np.array([0.24070751018780706,0.04049169004306333,-0.2949689689538115,-1.188940394962533,0.3595319351794924,-0.14821657998670623])
RIEMANN3=np.array([0.0162688093782525,-1.0814570326812767,-4.162730203760564,-1.1546645331333212,1.7220685314070152,-0.32479593455554057])
RICCI2=np.array([2.0304860047420306,0.41172109362668774,-3.2456600083419325,-13.33479437694205,4.019028239246117,-2.003363928391969])
RICCIBOX=np.array([-2.205477099600005,-0.9302576050305512,-1.1238094089110584,5.558096521344366,-1.8978074447048878,0.5425052369944467])
RREF=np.array([0.41598902695785883,-1.0421653262124124,-9.30686701147015,-12.449001654539147,4.0683399477607995,-2.3313492002174723])
A3=np.array([0.08410827495950812,0.3388004414024848,2.2537493574606224,1.7936161583555166,-0.690425234550442,0.39855343699621354])
A4=np.array([0.06014797241478866,0.017411147214802865,-0.1670416960113702,-0.6470043472565035,0.17218037853655313,-0.14310845340580042])

M=np.column_stack([EH,RICCI3,RIEMANN3,RICCI2,RICCIBOX,RREF])
T=np.column_stack([A3,A4])

def audit(scale):
    Ms=M*scale[:,None]; Ts=T*scale[:,None]
    s=np.linalg.svd(Ms,compute_uv=False)
    coef=np.linalg.lstsq(Ms,Ts,rcond=None)[0]
    res=Ts-Ms@coef
    return {
        "rank":int(np.linalg.matrix_rank(Ms)),
        "singular_values":s.tolist(),
        "smin_over_smax":float(s[-1]/s[0]),
        "residual_norms":np.linalg.norm(res,axis=0).tolist(),
        "relative_residual_norms":(np.linalg.norm(res,axis=0)/np.linalg.norm(Ts,axis=0)).tolist(),
        "max_abs_residual":float(np.max(np.abs(res)))
    }

scales={
 "raw":np.ones(6),
 "base_row_l2":1/np.maximum(np.linalg.norm(M,axis=1),1e-12),
 "EH_abs_floor":1/np.maximum(np.abs(EH),1e-2),
 "dRGT_reference_abs_floor":1/np.maximum(np.abs(RREF),1e-2),
}
out={"iteration":163,"scope":"six frozen TT chi2R probes","comparator_columns":["EH","Ricci3","Riemann3","Ricci2_full","RicciBoxRicci_full","dRGT_shared_reference"],"targets":["dRGT_alpha3","dRGT_alpha4"],"audits":{k:audit(v) for k,v in scales.items()}}
out["classification"]="FINITE_PROTOCOL_SATURATION_REGIME_SPECIFIC_NON_IDENTIFIABILITY"
out["theory_identity_claimed"]=False
out["novelty_certificate"]=False
assert all(x["rank"]==6 for x in out["audits"].values())
assert max(x["max_abs_residual"] for x in out["audits"].values()) < 1e-10
with open("results/c4_c5_protocol_saturation_iteration163.json","w") as f: json.dump(out,f,indent=2)
print(json.dumps(out,indent=2))
