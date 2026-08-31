#!/usr/bin/env python3
"""Iteration 175: tensor/soft Ward decomposition certificate.

The current scalar WardLock=0 is too coarse.  General-coordinate invariance fixes
part of a soft-graviton 1PI cubic vertex from the quadratic inverse kernel, while
a separately gauge-invariant nonminimal piece can be written with the linearized
soft Riemann tensor and an independent three-point form factor B.

This script validates the tensor geometry used to define the next finite RQIR
relation space:
  * pure-gauge soft polarization has vanishing linearized Riemann;
  * physical TT polarization has nonzero Riemann;
  * the Riemann contribution scales as k^2, i.e. enters the sub-subleading soft
    sector rather than leading/subleading locks.

It does not invent comparator B columns.  Those remain to be instantiated from
fixed C4/C5/nonlocal/AS parent dynamics.
"""
from pathlib import Path
import json
import math
import numpy as np


def linearized_riemann(k, eps):
    """Fourier-space R^(1)_{mu nu rho sigma}, overall sign convention irrelevant."""
    R=np.zeros((4,4,4,4),dtype=float)
    for mu in range(4):
        for nu in range(4):
            for rho in range(4):
                for sig in range(4):
                    R[mu,nu,rho,sig] = -0.5*(
                        k[rho]*k[nu]*eps[mu,sig]
                        + k[sig]*k[mu]*eps[nu,rho]
                        - k[sig]*k[nu]*eps[mu,rho]
                        - k[rho]*k[mu]*eps[nu,sig]
                    )
    return R

# Null soft momentum along +z.
k=np.array([1.0,0.0,0.0,1.0])
xi=np.array([0.3,0.7,-0.2,0.4])
eps_gauge=np.outer(k,xi)+np.outer(xi,k)

eps_tt=np.zeros((4,4),dtype=float)
eps_tt[1,1]=1.0/math.sqrt(2.0)
eps_tt[2,2]=-1.0/math.sqrt(2.0)

R_gauge=linearized_riemann(k,eps_gauge)
R_tt=linearized_riemann(k,eps_tt)

gauge_max=float(np.max(np.abs(R_gauge)))
gauge_norm=float(np.linalg.norm(R_gauge))
tt_max=float(np.max(np.abs(R_tt)))
tt_norm=float(np.linalg.norm(R_tt))

scale_checks=[]
for a in (0.5,2.0,3.0):
    n=float(np.linalg.norm(linearized_riemann(a*k,eps_tt)))
    ratio=n/tt_norm
    scale_checks.append({"scale":a,"norm_ratio":ratio,"expected_k2_ratio":a*a,"abs_error":abs(ratio-a*a)})

out={
  "iteration":175,
  "scope":"soft tensor decomposition for source-completed amputated cubic RQIR protocol",
  "pure_gauge_riemann_max_abs":gauge_max,
  "pure_gauge_riemann_norm":gauge_norm,
  "tt_riemann_max_abs":tt_max,
  "tt_riemann_norm":tt_norm,
  "soft_scaling_checks":scale_checks,
  "max_soft_scaling_error":max(x["abs_error"] for x in scale_checks),
  "decomposition":"Gamma3_soft = W[K2] + Rlin_soft : B3 + higher-soft-order",
  "interpretation":{
    "W[K2]":"WARD_DETERMINED_LONGITUDINAL_SHARED_STRUCTURE",
    "Rlin:B3":"GAUGE_INVARIANT_TRANSVERSE_OR_NONMINIMAL_THREE_POINT_STRUCTURE",
    "leading_soft":"LOCK_NOT_NOVELTY",
    "subleading_soft":"LOCK_NOT_NOVELTY_IN_FROZEN_LOCAL_EFT_SETTING",
    "subsubleading_soft":"MODEL_DEPENDENT_COMPARATOR_SPACE_NOT_AUTOMATIC_NOVELTY"
  },
  "finite_protocol_next_coordinates":{
    "per_row":"B_T = projector_transverse[Gamma_arr - W[K2]]",
    "number_of_frozen_rows":6,
    "transverse_row_dimension_before_comparator_subtraction":6,
    "status":"PROTOCOL_FROZEN_COMPARATOR_COLUMNS_NOT_YET_ALL_INSTANTIATED"
  },
  "classification":{
    "scalar_WardLock_only":"INSUFFICIENT_FOR_MODEL_DISCRIMINATION",
    "ward_determined_longitudinal_vertex":"PROJECT_AS_HARD_CONSISTENCY_SHARED_STRUCTURE",
    "transverse_B_form_factor":"NEXT_COMPARATOR_RESIDUAL_SPACE",
    "C3_ordered_B":"BLOCKED",
    "C4_B":"REQUIRES_FIXED_PARENT_PROJECTION",
    "C5_B":"REQUIRES_FIXED_EFT_OPERATOR_PROJECTION",
    "nonlocal_B":"FIXED_IN_PRINCIPLE_FOR_QG_NL_EXP_001_BUT_NOT_PROJECTED",
    "AS_B":"BLOCKED_REAL_TIME_THREE_POINT_COMPLETION",
    "ANSATZ_003":"NOT_CREATED",
    "Fisher_resources":"FORBIDDEN"
  },
  "retained_results":[
    "SOFT-NG-001 — WARD_DETERMINED_SOFT_CUBIC_PART_IS_SHARED_STRUCTURE_FIXED_BY_THE_TWO_POINT_KERNEL",
    "SOFT-NG-002 — LINEARIZED_RIEMANN_THREE_POINT_FORM_FACTOR_IS_GAUGE_INVARIANT_AND_ENTERS_AT_SUBSUBLEADING_K2_ORDER",
    "NG-FUNNEL-035 — REPLACE_SCALAR_WARDLOCK_WITH_WARD_SUBTRACTED_TRANSVERSE_CUBIC_COORDINATES"
  ],
  "model_readiness_percent":24,
  "readiness_change":"unchanged: a physically sharper residual space is frozen, but fixed comparator transverse columns are not yet complete"
}

Path("results/soft_ward_transverse_decomposition_iteration175.json").write_text(json.dumps(out,indent=2,sort_keys=True)+"\n",encoding="utf-8")
print(json.dumps(out,indent=2,sort_keys=True))
