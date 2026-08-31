# Research Log — Iteration 167

**Date:** 2026-08-31

## Objective

Make the Iteration-166 timelike absorptive pre-protocol operational in a fixed conserved-TT linear source channel and remove the universal constant massless-log onset before searching for sub-leading spectral shape.

## Work performed

1. Clarified that `A_odd` is frequency-odd `Im chi1R`, not post-Gaussian `chi2R_odd`.
2. Froze a conserved traceless external stress tensor `diag(1,-1,0)/sqrt(2)` on the same eight timelike rows.
3. Verified conservation, trace, spin-2 projection and frequency-independent source overlap.
4. Built a target-independent QR quotient of the constant vector from the eight-row space.
5. Verified that leading C5 and leading-IR AS logarithmic absorptive vectors vanish in the seven-dimensional quotient to machine precision.
6. Verified that three test sub-leading shapes `(x,x^2,x^3)` retain rank 3/3.
7. Audited a fourth finite-difference null of cubic envelopes and rejected it as the primary representation because its white-noise amplification is `sqrt(70)`.
8. Updated the Lorentzian AS comparator to its 2026 Physics Letters B publication and kept its finite-frequency numerical shape blocked until data or controlled reproduction exist.

## Numerical summary

- source conservation/trace/projector errors: `0`;
- overlap deviation from 1: `2.22e-16`;
- shape-space dimension after constant profile: `7`;
- max shape/constant overlap: `2.22e-16`;
- orthonormality error: `4.44e-16`;
- projected C5 leading-log norm: `3.80e-16`;
- projected AS leading-IR-log norm: `1.44e-16`;
- `(x,x^2,x^3)` quotient rank: `3/3`.

## Interpretation

The causal protocol now has an operational source map and is automatically blind to the universal leading logarithmic onset. This is a stronger search space than the spacelike finite-shape protocols, but no Candidate Gravity residual is defined because sub-leading C5 and finite-frequency AS comparator columns are not yet closed.

`MODEL_READINESS: 24%` unchanged.
