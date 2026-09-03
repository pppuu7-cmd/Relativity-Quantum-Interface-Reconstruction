# Candidate Gravity Current Front

**Updated:** 2026-09-03  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **24%**  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Active promotable ansatz:** none  
**Latest validated Candidate Gravity authority:** **Iteration 366**

Repository commits, raw schema-validated Actions artifacts, primary-authority audits and recovery material are source of truth. A green workflow conclusion alone is never scientific authority. Iteration numbering may contain independent branches; a later validated independent iteration does not imply that every earlier active computation is closed.

## Authoritative state

- Iteration 246 closes generic connection `e=3,c=0`; do not reopen it.
- Iteration 307 freezes complete eight-family `e=1,c=2` actual `Tr U1` normalized cut.
- Iterations 308-310 freeze historical `e=2,c<=1` bookkeeping, typed `U2` contract and the null-soft-fixture `Tr U1^2` routing. The old Iteration-310 8-class physical pruning is NOT transferable to the later timelike fixture without re-audit because Iteration 350 invalidates the singleton-null-soft physical pruning premise there.
- Iterations 312-338 freeze determinant topology, same-parent physical components, timelike absorptive family authority, exact phase space and repository simple-cut/effective-action normalization. One determinant `q^2=-1` triangle channel remains analytic/symbolic-reduction BLOCKED; Iteration 335 attempts ended operationally and must not be blindly retried.
- Iterations 339-345 freeze shifted graviton inverse routing, Vilkovisky U2 orientation/sign, physical A1/A2, N/Y bridge and functional-transpose routing. Historical Iterations 343-344 are scoped implementation FAILs in an auxiliary handwritten oracle, not model FAILs.
- Iteration 350 proves the timelike rebase invalidates the old singleton-soft pruning heuristic.
- Iterations 351-353 rebuild all 30 physical timelike U2 routes and expand them into 42 additive denominator subterms.
- Iteration 354 finds 30 denominator translation candidates; Iteration 355 proves `0/9` multi-member candidates are numerator-equivalent, so all 42 remain distinct physical numerator+denominator families. This is a scoped negative quotient result, not consistency FAIL.
- Iteration 356 classifies all `42/42` as direct timelike cut-capable topologies; `12/42` are simple-distinct-pole families and `30/42` contain repeated pole momentum.
- Iteration 357 freezes the method split: 12 simple families / 36 ordinary-simple typed channels versus 30 repeated-pole families.
- Iteration 358 is preserved as `OPERATIONAL_FAIL_ITERATION358_MD0T_ARITY__NO_PHYSICS_GATE_EVALUATED`.
- Iteration 359 freezes repeated-pole structure: all 30 repeated families contain exactly one double-pole group and no higher poles; 48 timelike channels cut the repeated group; 18 additional timelike simple-simple cuts in repeated `(2,1,1)` families leave the double pole uncut.
- Iteration 360 freezes the ordinary-simple on-shell prerequisite: all 12 simple families / 36 typed channels are `REGULAR`; `ZERO=0`, `BLOCKED=0`; max shell error `3.434752482434078e-16`; analytic minimum uncut-pole separation `0.11857864376269048`.
- Iteration 361 freezes normalized ordinary-simple `Tr U2` integration. All `36/36` channels converge, `BLOCKED=0`; max shell error `3.1176990904323794e-16`, max scaled convergence error `2.481513269677227e-10` under frozen `2e-5`. The nonzero routed channels cancel separately in every stored q2 bucket:
  - `D_s TrU2_simple(q^2=-1)=0`;
  - `D_s TrU2_simple(q^2=-0.34)=0`;
  - `D_s TrU2_simple(q^2=-0.14)=0`.
  This is a scoped ordinary-simple-sector cancellation only.
- Iteration 362 validates the repeated-pole auxiliary-mass derivative/distributional bridge with fixed same-`i0` prescription:
  `1/(D+i0)^2 = - d/d(mu^2) [1/(D+mu^2+i0)]|_0`.
- Iteration 363 freezes the kinematic prerequisite for the 48 channels whose cut passes through the double pole. `REGULAR=48`, `BLOCKED=0` for `mu^2={-1e-5,0,+1e-5}`; minimum analytic full-sphere uncut squared-momentum separation is `0.11857405797625284` above the frozen `1e-10` threshold.
- Iteration 365 freezes the independent prerequisite for the 18 simple-simple channels in repeated `(2,1,1)` families. `REGULAR=18`, `BLOCKED=0`; minimum analytic uncut double-pole separation `0.11857864376269048`; direct `D^-2` versus auxiliary derivative factor agreement `1.2724338053133424e-11` under fixed `1e-8`.
- **Iteration 366 freezes the physical normalized integration of those 18 simple-simple repeated-family channels. All `18/18` converge, `BLOCKED=0`; max shell error `1.5830329958809877e-16`; max angular convergence error `1.755966985998638e-08` under fixed `2e-5`; max direct-vs-aux representation error `1.3870141151275523e-11` under fixed `2e-8`. The q2-resolved sector sums are nonzero:**
  - `D_s TrU2_repeat_simple(q^2=-1) = -6.812363349599648e-05`;
  - `D_s TrU2_repeat_simple(q^2=-0.34) = -8.405976034846215e-05`;
  - `D_s TrU2_repeat_simple(q^2=-0.14) = -7.069545900379072e-05`.

Iteration-366 authority:
`PASS_U2_REPEATED_FAMILY_SIMPLE_SIMPLE_18_PHYSICAL_CUTS__ALL_CONVERGED__DIRECT_AUX_AGREE`.

Provenance: run `33801929554`, job `100803251999`, artifact `9911685784`, artifact digest `sha256:2e05202456e9b5820d88b17e242d24864a8274a2d49950b5b856b058fe5f35b7`, raw scientific JSON SHA-256 `df86388db9ecfd9a0df565cba050bea679267fbc5698bb6ba04030c66c38e0e6`, workflow head `a7b12b674d9f648a2f2b24b981f9d061b5cad07c`.

## Active computation

**Iteration 364 remains active and must not be duplicated:** run `33801351823`, job `100801347762`, workflow `rqir-iteration364-u2-repeated-pole-symmetric-aux-derivative-cut`.

Iteration 364 evaluates the 48 physical channels where the cut itself passes through the unique double-pole group using a symmetric pointwise auxiliary-`mu^2` derivative. Frozen checks include low/high angular grids, half-phi shift, derivative step `h=5e-6` versus `h/2=2.5e-6`, max scaled convergence threshold `2e-5`, and shell threshold `2e-10`. Do not weaken thresholds. If a subset is `BLOCKED_CONVERGENCE`, isolate only those channels; do not zero-fill or duplicate the full run.

## Active sectors

- connection `e=1,c<=2`: actual `Tr U1` cut frozen by Iteration 307.
- connection `e=2,c<=1`, `Tr U2`: ordinary-simple 36-channel sector is closed and cancels q2-by-q2; repeated-family simple-simple 18-channel sector is closed and NONZERO q2-by-q2; 48 cut-through-double-pole channels remain pending Iteration 364. Therefore the full physical `Tr U2` is NOT yet frozen.
- connection `e=2,c<=1`, `Tr U1^2`: open. Historical Iteration-310 null-soft pruning cannot be promoted to the current timelike fixture without a full physical re-audit beginning from the pre-pruning placement set.
- determinant `e=0,c<=3`: three bubbles NONZERO; triangle family NONZERO in two certified channels; one `q^2=-1` triangle channel remains BLOCKED pending analytic/symbolic angular reduction.

## Exact next gates

1. Consume Iteration 364 raw artifact. If all 48 channels converge, freeze complete pure `Tr U2` q2-resolved sums by combining only within each q2 bucket:
   `D_s TrU2_total = D_s TrU2_simple_361 + D_s TrU2_cut_through_double_364 + D_s TrU2_repeat_simple_366`.
   Do not fold the `+i/2` effective-action coefficient and do not include `Tr U1^2` in this pure-`Tr U2` closure.
2. In parallel, rebase `Tr U1^2` onto the same physical timelike fixture. Start from the full pre-pruning routing set; do not assume the old singleton-soft kills from Iteration 310. Reuse same-parent physical U1 primitives and require executable routing/contraction authority before any cut integration.
3. Only after complete `Tr U2` and physical `Tr U1^2` closure may the eom-degree2 connection combination `+(i/2)Tr U2 -(i/4)Tr U1^2` be assembled.
4. Source/Ward/contact completion and matched `K2` subtraction remain downstream. Source/Born subtraction is forbidden before normalized origin accounting is complete.

Iteration-297 evanescent/regulator warning remains binding for the full finite DR remainder. No Candidate residual may be declared before the fixed C3/C4/C5/nonlocal/asymptotic-safety comparator quotient is executable and survived.

## Stable readiness rubric

- comparator foundation `24/25`
- robust unique residual `0/20`
- frozen parent dynamics/ANSATZ `0/20`
- consistency/positivity/Ward/causality `0/15`
- identifiability/Fisher `0/10`
- resource/experiment closure `0/10`

MODEL_READINESS: 24%

Change through Iteration 366: `0 pp`. A genuine nonzero physical U2 sub-sector is now closed with direct/auxiliary cross-checks, but the 48 cut-through-double-pole channels, full `Tr U2`, physical `Tr U1^2`, full eom-degree2 connection sector and robust comparator-subtracted residual remain open.

## Retained guardrails

Unsupported is `BLOCKED`, never zero-filled. Negative/scoped results remain preserved. Operational failure is not scientific FAIL. Null-soft pruning is not transferable to timelike fixtures unless re-proven. Denominator equivalence is not numerator equivalence. Repeated poles are never ordinary simple cuts. Family cut-capability is not a nonzero discontinuity certificate. In U2 distinguish `K`, `K^-1`, and `Hinv_VD=-K^-1`; shifted incoming momentum and functional-transpose routing are mandatory. Distinct q2 discontinuity variables are never summed together. Do not create `ANSATZ-003` before a concrete robust comparator-subtracted residual survives the fixed comparator quotient. Fisher/resources remain forbidden until then. No blind heavy full-C5.

## Candidate state

No robust Candidate Gravity residual exists.  
`ANSATZ-003`: NOT CREATED.  
Fisher/resources: FORBIDDEN.  
Blind heavy full-C5 run: NOT AUTHORIZED.
