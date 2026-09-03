# RQIR Candidate Gravity Recovery Delta — Iteration 383

Date: 2026-09-04

MODEL_READINESS: 24%

## Authority

Iteration 383 closes the **ordinary two-simple-particle, channel-resolved normalized determinant absorptive vector** after the Iteration-380 replacement of the sole formerly BLOCKED triangle channel.

Freeze:

`PASS_COMPLETE_CHANNEL_RESOLVED_NORMALIZED_DETERMINANT_ORDINARY_SIMPLE_CUT_ABSORPTIVE_VECTOR`

Validated Actions provenance:

- successful run `33817475548`
- job `100852689209`
- workflow head `72a06217529f4e2f47736542397afdeb4fa65f27`
- artifact `9917045046`, `iteration383-result`
- artifact digest `sha256:4de76d7ce811ca34a17b9e21b6408c38a632c2850c41b3008f94292a78504c00`
- scientific JSON SHA-256 `7c00c0d7e959375d9b8e4614994a16e482dc21c7444e0f589ec8d40c531560f4`
- exactly one top-level JSON object, sentinel `383`, `scientific_authority_pass=true`.

The immediately preceding first run `33817415864` failed only a provenance-string assertion because Iteration 337 stores the full equality `D_s I[F] = -8*pi*int dPhi2 F = -sphere_mean(F)` rather than the shortened text. No physical input, value, sign, routing or threshold was modified in the repair.

## Inputs and normalization

- Iteration 333: three bubble means and the two already-converged triangle means;
- Iteration 380: replacement authority only for the formerly BLOCKED `q^2=-1` triangle;
- Iteration 337: `D_s C_det = -sphere_mean` for the ordinary two-simple-line cut;
- Iteration 338: `Gamma_det=+i C_det`, hence `D_s Gamma_det=-i sphere_mean`.

The internal graviton `1/2` and ghost `-1` determinant weights are already contained in the physical route coordinate and are not applied again.

## Frozen channel-resolved vector

Distinct `q^2` coordinates are retained separately and never summed.

### `q^2=-1`

- bubble mean: `-0.004517862848697545`
- triangle mean: `+0.006875651912582228`
- total normalized angular mean: `+0.002357789063884683`
- `D_s C_det=-0.002357789063884683`
- `D_s Gamma_det=-0.002357789063884683 i`
- status: `NONZERO`.

### `q^2=-0.34`

- bubble mean: `+9.802036921027348e-05`
- triangle mean: `-0.0015607797207829275`
- total normalized angular mean: `-0.001462759351572654`
- `D_s C_det=+0.001462759351572654`
- `D_s Gamma_det=+0.001462759351572654 i`
- status: `NONZERO`.

### `q^2=-0.14`

- bubble mean: `+0.00013296877895753044`
- triangle mean: `-0.0013719252833873717`
- total normalized angular mean: `-0.0012389565044298413`
- `D_s C_det=+0.0012389565044298413`
- `D_s Gamma_det=+0.0012389565044298413 i`
- status: `NONZERO`.

## Scope boundary

This is **not** the complete finite-dimensional determinant and does not supersede the Iteration-297 evanescent/regulator warning. It is also not Source/Ward/contact completed, not matched-`K2` subtracted, not comparator-quotiented and not a candidate residual.

No `ANSATZ-003`, Fisher information or resource claim is authorized.

## Readiness

MODEL_READINESS remains 24%. This closes a hard ordinary-simple determinant sub-sector, but no full readiness bucket because the repeated `Tr U1^2`/`Tr U2` sectors and comparator-subtracted observable remain open.

## Exact next gate

Retain this determinant vector as immutable normalized origin accounting. Complete the active repeated `Tr U1^2` and repeated `Tr U2` sectors. Only after full physical operator coordinates are closed may the e=2 combination and then Source/Ward/contact + matched `K2` subtraction be assembled.
