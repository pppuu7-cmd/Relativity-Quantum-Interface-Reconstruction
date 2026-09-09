# RECOVERY DELTA — ITERATION 661

Date: 2026-09-09

## Authority entering
Iter660 fixed the support/routing geometry of the Iter655 soft family. Iter658 supplies the quotient-safe plus-TT functional; Iter594 supplies exact K1/K2 vertices; Iter653 supplies the common normalized closed-SK parent.

## Raw-valid result
Canonical run `34340069225`, job `102428518922`, head `c8efdc4da0dbf434689aa1d14b2722c90bd25df7`, artifact `10099348470`, artifact/ZIP SHA-256 `89c8eddf4e2c757c507dc29da0fce30a9a1452cb7fe26cab21d7684e2c4cafe3`, raw JSON SHA-256 `1817b437a4dd86743d6cef8bbbc55dd84c9f44e90d108e2a7222ab673c2cf758`.

`failures=[]`, `blocked=[]`, `scientific_gate_pass=true`. Six prospective `(s,epsilon)` points were evaluated. q1/q2 bubbles and both triangle orientations remain finite on the sampled cut surfaces; minimum sampled absolute uncut triangle denominator is `0.011201904523433559`, and maximum cut-shell error is `7.77e-16`. q3 transfer remains an analytic no-massive-cut topology, not a zero-filled amplitude.

All numerical +TT densities are tiny (`5.67e-23` through `4.60e-19`) with zero reported imaginary parts. These are NOT promoted as nonzero physics: the all-plus tensor choice and axial soft kinematics suggest an exact pi/2 transverse-rotation selection rule, so a symmetry audit is mandatory before epsilon-leading extraction.

## Guardrails
Candidate values unused. Source/Born subtraction `NOT_PERFORMED`. Native soft T_cut not yet formed. zero-fill=false. ANSATZ-003/Fisher/resources remain forbidden.

MODEL_READINESS: 24%

## Exact next gate
Iter662: prove or reject exact transverse quarter-turn antisymmetry of every frozen +++ K1K2/K1^3 cut integrand. If exact, classify Iter661 tiny values as floating-point angular residue and carry an exact zero for this measurement only, without claiming the whole tensor amplitude is zero.
