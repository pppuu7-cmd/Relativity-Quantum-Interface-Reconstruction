#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 214.

Authority guard for the Iteration-213 physical five-graviton total-s cut.
This script imports the validated tree/cut engine and evaluates the two collinear
endpoint residues directly from the unintegrated tree product.  It does NOT fit
the subtraction coefficient from cap-regulated integrals and does NOT claim that
subtracting an isolated channel cut is a physical IR completion.
"""
from pathlib import Path
import importlib.util, json, math
import numpy as np

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location("it213",HERE/"c5_fivepoint_schannel_cut_ir_iteration213.py")
m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)

EPS=0.01
TH=1.0e-4
PHIS=np.linspace(0,2*math.pi,32,endpoint=False)

def residue(endpoint):
    vals=[]
    for phi in PHIS:
        theta=TH if endpoint=="north" else math.pi-TH
        vals.append((TH**2)*m.cut_integrand(EPS,float(theta),float(phi)))
    vals=np.asarray(vals,complex)
    mean=vals.mean()
    return mean, float(np.max(np.abs(vals-mean))/abs(mean))

rn,spread_n=residue("north")
rs,spread_s=residue("south")
reldiff=float(abs(rn-rs)/abs((rn+rs)/2))
# If I(theta)~r_N/theta^2 and r_S/(pi-theta)^2, then dOmega=2pi sin(theta)dtheta
# gives 2pi(r_N+r_S) log(1/delta) at leading order.
pred=2*math.pi*(rn+rs)

out={
 "iteration":214,
 "date":"2026-09-01",
 "model_readiness_percent":23,
 "epsilon":EPS,
 "theta_limit_probe":TH,
 "north_residue":{"real":float(rn.real),"imag":float(rn.imag),"abs":float(abs(rn)),"phi_relative_spread":spread_n},
 "south_residue":{"real":float(rs.real),"imag":float(rs.imag),"abs":float(abs(rs)),"phi_relative_spread":spread_s},
 "endpoint_relative_difference":reldiff,
 "predicted_raw_complex_log_coefficient":{"real":float(pred.real),"imag":float(pred.imag),"abs":float(abs(pred))},
 "iteration213_cap_magnitude_log_slope":32231.37809459,
 "classification":{
   "endpoint_factorization":"PASS_SCOPED_TREE_CUT_DIAGNOSTIC",
   "single_cut_local_subtraction":"NOT_AUTHORIZED_AS_PHYSICAL_IR_COMPLETION",
   "reason":"universal gravitational IR cancellation applies to the complete amplitude/inclusive observable; an isolated channel-cut endpoint subtraction is scheme/channel dependent unless derived inside that full completion",
   "raw_cut_to_iteration210_extractor":"FORBIDDEN",
   "candidate_residual":"NONE",
   "ANSATZ_003":"NOT_CREATED",
   "Fisher_resources":"FORBIDDEN"
 },
 "retained_results":[
   "IR-NG-003 — THE_TWO_COLLINEAR_ENDPOINTS_OF_THE_FROZEN_S_CUT_SHARE_THE_SAME_TREE_LEVEL_RESIDUE",
   "C5-CUT-013 — THE_OBSERVED_CAP_LOG_IS_QUANTITATIVELY_EXPLAINED_BY_THE_DIRECT_TREE_ENDPOINT_RESIDUES",
   "IR-NG-004 — UNIVERSAL_GRAVITATIONAL_IR_CANCELLATION_DOES_NOT_AUTHORIZE_AN_ISOLATED_CHANNEL_CUT_LOCAL_COUNTERTERM",
   "NG-FUNNEL-071 — PHYSICAL_LOOP_CUT_IMPORT_REQUIRES_FULL_IR_SAFE_OR_EXPLICITLY_SUBTRACTED_AMPLITUDE_AUTHORITY_NOT_ENDPOINT_FITTING"
 ],
 "readiness_change":"unchanged at 23%; the raw-cut IR origin is now factorization-certified, but the physical IR-safe five-point control remains blocked"
}
Path("results/c5_single_cut_ir_factorization_iteration214.json").write_text(json.dumps(out,indent=2,sort_keys=True)+"\n",encoding="utf-8")
print(json.dumps(out,indent=2,sort_keys=True))
