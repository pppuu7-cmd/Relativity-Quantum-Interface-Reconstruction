#!/usr/bin/env python3
"""Iteration 173 structural audit of the fixed PQCG MSR/JD cubic completion.

This is deliberately a structural, not phenomenological, certificate.  It shows
that the linear stochastic authority plus the nonlinear Einstein drift does not
fix the two-response-field cubic vertex unless the field dependence of the
conserved diffusion kernel is also fixed.

Toy response functional (one projected mode):
  S = t*(L*h + g*h**2/2 - J) - 1/2*t*(D0 + lam*h)*t
where t is the MSR response field.  At h=0, all lam choices have the same
linear response/noise kernel.  At cubic order, however,
  Gamma_t_h_h = g,
  Gamma_t_t_h = -lam,
  Gamma_t_t_t = 0.
Thus linear two-point data and the fixed nonlinear drift determine g but not
lam.  The toy algebra is used only as an underdetermination certificate; it is
not asserted to be the full tensorial PQCG action.
"""

import json
from pathlib import Path
import sympy as sp

h, t, L, g, J, D0, lam = sp.symbols("h t L g J D0 lam")
S = t * (L*h + g*h**2/sp.Integer(2) - J) - sp.Rational(1,2)*t*(D0 + lam*h)*t

# Hessian at the background h=t=0: independent of lam.
vars_ = (h, t)
H = sp.Matrix([[sp.diff(S, a, b).subs({h:0,t:0,J:0}) for b in vars_] for a in vars_])

# Cubic vertices at the background.
Gamma_thh = sp.diff(S, t, h, h).subs({h:0,t:0,J:0})
Gamma_tth = sp.diff(S, t, t, h).subs({h:0,t:0,J:0})
Gamma_ttt = sp.diff(S, t, t, t).subs({h:0,t:0,J:0})

assert lam not in H.free_symbols
assert sp.simplify(Gamma_thh - g) == 0
assert sp.simplify(Gamma_tth + lam) == 0
assert sp.simplify(Gamma_ttt) == 0

result = {
    "iteration": 173,
    "status": "BLOCKED_C3_CTP_ORDERED_COMPLETION",
    "structural_model": "S=t*(L*h+g*h^2/2-J)-1/2*t*(D0+lam*h)*t",
    "linear_hessian": [[str(x) for x in row] for row in H.tolist()],
    "linear_hessian_depends_on_lambda": False,
    "cubic_vertices": {
        "Gamma_t_h_h": str(Gamma_thh),
        "Gamma_t_t_h": str(Gamma_tth),
        "Gamma_t_t_t": str(Gamma_ttt),
    },
    "interpretation": {
        "fixed_nonlinear_drift_fixes_one_response_vertex": True,
        "linear_noise_fails_to_fix_two_response_cubic_vertex": True,
        "additional_nonlinear_conserved_diffusion_completion_required": True,
        "ctp_ra_mapping_fixed_by_existing_authority": False,
    },
    "classification": "operational BLOCKED / underdetermined comparator completion; not a consistency FAIL and not a zero column",
}

out = Path("results/c3_pqcg_msr_completion_audit_iteration173.json")
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
