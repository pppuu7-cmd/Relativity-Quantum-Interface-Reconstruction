# C5 Cubic Response — Iteration 150

**Status:** scoped PASS for the explicit local tree sub-block; full C5 retarded comparator remains incomplete.

## Frozen scope

This iteration keeps every Iteration-149 choice fixed: physical metric `g=eta+kappa h`, conserved stress-tensor source map, six spacelike triplets, TT spin-2 projectors, Gaussian windows, and the interacting-vacuum retarded convention.

No on-shell or EOM-reduced amplitude chart is imported.

## Einstein-Hilbert cubic block

The EH cubic coefficient is evaluated directly as the trilinear coefficient of

`sqrt(-g) g^{mn}(Gamma^a_mb Gamma^b_na - Gamma^a_mn Gamma^b_ab)`

for a superposition of three off-shell plane-wave metric modes with momenta `(p,-q,-r)`, `p=q+r`.

A symmetric central mixed derivative and Richardson extrapolation are used. Across the six probes the maximum permutation asymmetry is `8.13e-14`; the maximum final halving-step change is `9.22e-6` before Richardson extrapolation.

The projected EH response values are:

`[0.3000300, -1.4617905, -12.0348738, -14.4346815, 4.8675218, -2.7789128]`.

This closes the previous `BLOCKED_VERTEX_IMPLEMENTATION` for the EH TT sub-block only.

## First explicit local EFT directions

Two unreduced covariant curvature-cubic directions were implemented in the same metric convention:

1. `Tr(Ricci^3) = R_m^n R_n^r R_r^m`;
2. `Riemann_mn^rs Riemann_rs^ab Riemann_ab^mn`.

Because each curvature is needed only to linear order for these cubic operators, their trilinear response is obtained exactly from the three linearized curvature tensors and summed over all leg permutations.

After the same propagator/window weighting, the finite tangent matrix has shape `6 x 2` and

`rank = 2/2`,

with singular values

`[4.83562189, 1.10930485]`

and

`s_min/s_max = 0.2294027268`.

Hence the frozen six-probe protocol distinguishes these first two explicit local curvature-cubic C5 directions.

## Ward diagnostic: new correction to the planned gate

A naive replacement of one TT polarization by a longitudinal pure-gauge tensor does **not** vanish for the isolated off-shell 1PI cubic vertex. The six diagnostic values are finite and nonzero.

This is not classified as a GR consistency failure. Off shell, gauge identities are Ward/Slavnov-Taylor identities relating a vertex contraction to inverse-propagator and contact/source terms; a standalone three-vertex is not generally required to satisfy an on-shell-style longitudinal null. The classic covariant-gravity literature derives gravitational Ward identities at the level of complete Green-function/vertex relations (DeWitt, Phys. Rev. 162, 1239 (1967)).

### NG-FUNNEL-010 — OFFSHELL_VERTEX_LONGITUDINAL_NULL_IS_NOT_THE_WARD_IDENTITY

For a finite off-shell nonlinear-response comparator, `k·Gamma3 = 0` is not a valid standalone acceptance rule. The source-completed Ward-Takahashi/Slavnov-Taylor relation must include the appropriate inverse-propagator/contact terms in the same field/source convention.

Classification: methodological correction / operational BLOCKED, **not** C5 consistency FAIL.

## Scoped scientific claim

The first explicit local tree C5 nonlinear-response tangent now exists in the frozen protocol, but only for the EH baseline plus two curvature-cubic directions. It is a real finite tangent certificate, not a broad class-capability mask.

The following remain unsupported and are not set to zero:

- full source-completed off-shell Ward-Takahashi identity;
- higher-dimension local directions beyond this first two-column block;
- loop/nonanalytic columns;
- `N2` and `C3sym` post-Gaussian sectors.

No candidate residual against the full fixed C5/C3/C4/nonlocal/AS quotient exists yet, so Fisher/resources remain inadmissible and `ANSATZ-003` remains withheld.

## Reproducibility

- `analysis/c5_cubic_response_iteration150.py`
- `results/c5_cubic_response_iteration150.json`

## Next gate

Iteration 151 should derive and implement the correct off-shell gravitational Ward-Takahashi completion for this exact EH sub-block (inverse-propagator plus source/contact pieces), verify it numerically on the same six probes, and only then extend the local C5 tangent or proceed to the first fixed C3 tangent if the completed identity passes.
