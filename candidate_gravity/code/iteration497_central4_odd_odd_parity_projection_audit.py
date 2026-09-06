#!/usr/bin/env python3
from fractions import Fraction as Q
import json

nodes = (-2, -1, 1, 2)
c = {-2: Q(1,12), -1: Q(-2,3), 1: Q(2,3), 2: Q(-1,12)}

assert all(c[-x] == -c[x] for x in nodes)
W = {(x,y): c[x]*c[y] for x in nodes for y in nodes}
assert all(W[(-x,y)] == -W[(x,y)] for x in nodes for y in nodes)
assert all(W[(x,-y)] == -W[(x,y)] for x in nodes for y in nodes)
assert all(W[(-x,-y)] == W[(x,y)] for x in nodes for y in nodes)

# Exact projector identity: sum W F = sum W F_oo, where
# F_oo(x,y)=[F(x,y)-F(-x,y)-F(x,-y)+F(-x,-y)]/4.
# Verify coefficient equality symbolically for all 16 independent samples.
coeff_projected = {(x,y): Q(0) for x in nodes for y in nodes}
for x in nodes:
    for y in nodes:
        w = W[(x,y)] / 4
        coeff_projected[(x,y)] += w
        coeff_projected[(-x,y)] -= w
        coeff_projected[(x,-y)] -= w
        coeff_projected[(-x,-y)] += w
assert coeff_projected == W

# Even-in-x or even-in-y sectors are annihilated exactly.
# The four-point orbit form is also exact:
# S = sum_{a,b>0} c_a c_b [F(a,b)-F(-a,b)-F(a,-b)+F(-a,-b)].
positive = (1,2)
coeff_orbit = {(x,y): Q(0) for x in nodes for y in nodes}
for a in positive:
    for b in positive:
        wab = c[a]*c[b]
        coeff_orbit[(a,b)] += wab
        coeff_orbit[(-a,b)] -= wab
        coeff_orbit[(a,-b)] -= wab
        coeff_orbit[(-a,-b)] += wab
assert coeff_orbit == W

result = {
  "iteration": 497,
  "classification": "PASS_CENTRAL4_ODD_ODD_PARITY_PROJECTION_EXACT__NON_PROMOTING",
  "nodes": list(nodes),
  "coefficients": {str(k): str(v) for k,v in c.items()},
  "identities": {
    "c_minus_x": "-c_x",
    "w_minus_x_y": "-w_x_y",
    "w_x_minus_y": "-w_x_y",
    "w_minus_x_minus_y": "w_x_y",
    "assembly_projection": "D_h[F] = D_h[F_oo]",
    "F_oo": "(F(x,y)-F(-x,y)-F(x,-y)+F(-x,-y))/4",
    "annihilated_exactly": ["even-in-x sector", "even-in-y sector"],
    "orbit_reduction": "16-sample signed assembly equals four positive-quadrant odd-odd orbit differences"
  },
  "scope": "estimator/assembly provenance only",
  "scientific_promotion": False,
  "thresholds_changed": False,
  "model_readiness_percent": 24
}
print(json.dumps(result, indent=2, sort_keys=True))
