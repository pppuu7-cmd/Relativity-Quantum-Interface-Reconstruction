#!/usr/bin/env python3
"""Iteration 218: minimal covariant scalar source-completion contract.

Freeze a concrete dynamical source model
  S_phi = -1/2 int sqrt(-g) [g^{mu nu} d_mu phi d_nu phi + m^2 phi^2].

The linear graviton-scalar-scalar tensor vertex (stripped of overall constants)
for k=p'-p is
  V^{mu nu}=p^mu p'^nu+p^nu p'^mu-eta^{mu nu}(p.p'-m^2).
It obeys the exact off-shell Ward identity
  k_mu V^{mu nu}=(p'^2-m^2)p^nu-(p^2-m^2)p'^nu.
Thus on-shell scalar legs give a transverse physical source automatically, while
off-shell departures are tied to the same scalar inverse propagator. Higher
h^n phi^2 contact vertices are fixed by the same covariant action and may not be
independently tuned.
"""
from pathlib import Path
import json
import numpy as np

eta=np.diag([1.,-1.,-1.,-1.])
def dot(p,q): return float(p@eta@q)
def lower(p): return eta@p

m=0.7
samples=[
    (np.array([1.3,0.2,-0.1,0.4]),np.array([1.7,-0.15,0.22,0.31])),
    (np.array([1.1,-0.3,0.25,-0.2]),np.array([1.5,0.12,-0.18,0.27])),
    (np.array([2.0,0.4,0.1,-0.3]),np.array([1.8,-0.2,0.33,0.15])),
]
errs=[]
for p,pp in samples:
    k=pp-p
    # contravariant tensor V^{mu nu}
    V=np.outer(p,pp)+np.outer(pp,p)-eta*(dot(p,pp)-m*m)
    lhs=lower(k)@V
    rhs=(dot(pp,pp)-m*m)*p-(dot(p,p)-m*m)*pp
    errs.append(float(np.max(np.abs(lhs-rhs))))

# Explicit on-shell sample with arbitrary spatial momenta.
pv=np.array([0.22,-0.17,0.31]); ppv=np.array([-0.11,0.29,0.08])
p=np.r_[np.sqrt(m*m+pv@pv),pv]
pp=np.r_[np.sqrt(m*m+ppv@ppv),ppv]
k=pp-p
V=np.outer(p,pp)+np.outer(pp,p)-eta*(dot(p,pp)-m*m)
on_shell_transversality=float(np.max(np.abs(lower(k)@V)))

out={
  "iteration":218,
  "date":"2026-09-01",
  "model_readiness_percent":23,
  "source_model_id":"MSSC-001",
  "source_action":"S_phi=-1/2 int sqrt(-g)[g^{mu nu} partial_mu phi partial_nu phi + m^2 phi^2]",
  "vertex_ward_identity":"k_mu V^{mu nu}=(p'^2-m^2)p^nu-(p^2-m^2)p'^nu",
  "max_offshell_ward_identity_error":max(errs),
  "on_shell_vertex_transversality_error":on_shell_transversality,
  "same_dynamics_contact_rule":"all h^n phi^2 source/contact vertices are fixed by expansion of the same covariant scalar action; independent contact tuning forbidden",
  "classification":{
    "linear_source_Ward_identity":"PASS_MACHINE_PRECISION",
    "on_shell_scalar_source_transversality":"PASS_MACHINE_PRECISION",
    "nonlinear_source_completion":"DEFINED_BY_PARENT_ACTION_NOT_YET_FULLY_EXPANDED",
    "gauge_safe_connected_cut_route":"AUTHORIZED_IN_PRINCIPLE_REQUIRES_EXPLICIT_TREE_CONTACT_SET_AND_UNITARITY_CONSTRUCTION",
    "off_shell_1PI_T_cut_inference_from_graviton_S_matrix":"FORBIDDEN_BY_ITERATION217",
    "candidate_residual":"NONE",
    "ANSATZ_003":"NOT_CREATED",
    "Fisher_resources":"FORBIDDEN"
  },
  "retained_results":[
    "SRC-NG-001 — MINIMALLY_COUPLED_SCALAR_ACTION_FIXES_SOURCE_WARD_IDENTITY_AND_ALL_NONLINEAR_SOURCE_CONTACTS_FROM_ONE_DYNAMICS",
    "SRC-NG-002 — DYNAMICAL_SOURCE_COMPLETION_IS_REQUIRED_BEFORE_AN_OFFSHELL_CONNECTED_CUT_CAN_BE_CALLED_GAUGE_SAFE",
    "NG-FUNNEL-075 — USE_CONNECTED_DYNAMICAL_SOURCE_OBSERVABLES_TO_AVOID_GAUGE_DEPENDENT_OFFSHELL_VERTEX_PROMOTION"
  ],
  "readiness_change":"unchanged at 23%; a concrete source-completion route is frozen but the nonlinear connected cut has not yet been computed",
  "next_gate":"Derive and validate the h^2 phi^2 contact together with h phi phi, then construct the lowest nontrivial conserved-source tree amplitude needed on each side of a physical unitarity cut."
}
Path("results/minimal_scalar_source_completion_iteration218.json").write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
print(json.dumps(out,indent=2,sort_keys=True))
