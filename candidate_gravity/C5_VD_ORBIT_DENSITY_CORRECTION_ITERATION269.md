# RQIR Candidate Gravity — Iteration 269

## Primary-authority orbit-density correction and restoration of routed N2/Q2 transpose

**Date:** 2026-09-02  
**MODEL_READINESS: 24%**

## Why this correction was required

Iteration 268 correctly froze the routed inverse-recursion structure, but a follow-up endpoint-transpose test exposed a second-order mismatch in the physical `N2/Q2` layer. `N1/Q1` passed endpoint reversal at `~1e-10`, while `N2/Q2` did not. This localized the problem below the proposed `B3` assembly.

The primary authority resolves the issue. In Giacchini–de Paula Netto–Shapiro, *Vilkovisky unique effective action in quantum gravity*, Phys. Rev. D 102, 106006 (2020), Eq. (5) defines the orbit metric `N_orb`, Eq. (14) defines `Nhat=Y^up N_orb`, Eq. (48) writes the explicit gravity gauge-fixing density `sqrt(|g|) chi_alpha g^{alpha beta} chi_beta`, and Eq. (53) gives the local minimal ghost matrix without a residual density factor. Therefore, in condensed-index normalization and up to the frozen overall sign,

`Y^up = g^{-1}/sqrt(|g|)`,

`Y_down = sqrt(|g|) g`,

so

`N_orb = Y_down Nhat = sqrt(|g|) g Nhat`.

Iterations 252/258 had used the inverse density placement in the representative local weight, `sqrt(|g|) g^{-1}` for `Y^up`, which implied `Y_down=g/sqrt(|g|)`. For a TT perturbation the determinant has no linear variation, so this mistake is invisible at first order. It first changes the second-order density coefficient.

## Correct TT second-order density coefficient

For

`g=eta+t eps`, `tr(eta^-1 eps)=0`,

let `H=eta^-1 eps`. Then

`sqrt(|g|)=1-(t^2/4) tr(H^2)+O(t^3)`.

Hence

`Y_down=sqrt(|g|)g`

has the coefficient

`V0=eta`,

`V1=eps`,

`V2=-(tr(H^2)/4) eta`.

The `+` sign frozen in Iteration 258 is superseded.

Importantly, the first-order result from Iteration 252 survives:

`delta Y^up = -eps^up`

for TT `h`, because `delta sqrt(|g|)=0`.

## Corrected routed inverse layer

The routing algebra from Iteration 268 remains exactly correct:

`Q1[x](p)=-Q0(p+k_x) N1[x](p) Q0(p)`

and

`Q2[x,y](p)=Q0(p+k_x+k_y)[N1[x](p+k_y)Q0(p+k_y)N1[y](p)+N1[y](p+k_x)Q0(p+k_x)N1[x](p)-N2[x,y](p)]Q0(p)`.

Only the second-order physical `N2`, and therefore numerical `Q2`, needed correction.

At `p=(0.7,-0.4,0.5,0.9)` and finite-difference steps `h1=3e-5`, `h2=2e-4`:

- `||Q1[s]||_F=1.5811155821`, `||Q1[a]||_F=2.6872621916`, `||Q1[b]||_F=2.3701956668`;
- first-order inverse residuals are `<=1.11e-16`;
- `Q1` endpoint-transpose residuals are `<=1.42e-10`.

Corrected mixed second-order values:

- `||N2[s,a]||_F=2.3195427490`, `||Q2[s,a]||_F=1.8689138370`;
- `||N2[s,b]||_F=2.0809119657`, `||Q2[s,b]||_F=3.5158966341`;
- `||N2[a,b]||_F=3.0307449035`, `||Q2[a,b]||_F=1.0700741894`.

All second-order routed inverse identities close at `<=4.45e-16`. Mixed-leg exchange residuals are `<=4.41e-9`.

Most importantly, endpoint-reversed Fourier transpose is restored:

- corrected `N2` transpose residuals: `3.54e-8`, `1.38e-8`, `1.04e-8`;
- corrected `Q2` transpose residuals: `4.49e-8`, `1.67e-8`, `7.69e-9`.

The residual decreases with the mixed finite-difference step until roundoff, consistent with a numerical differentiation envelope.

By contrast, the superseded density factor gives `N2` endpoint-transpose residuals

`0.03165`, `0.21036`, `0.62805`,

which remain finite as the derivative step is reduced. This is a decisive regression certificate.

Freeze:

`PASS_PRIMARY_AUTHORITY_ORBIT_DENSITY_CORRECTION_AND_ROUTED_N2_Q2_TRANSPOSE_RESTORATION`.

Guardrail:

`USE_Y_UP=g^-1/sqrt|g| AND Y_DOWN=sqrt|g|*g; DO_NOT_USE_THE_INVERTED_DENSITY_FACTOR`.

## Scope of supersession

Supersede only the following parts of earlier iterations:

- Iteration 252: the explicit density representative for `Y^up`; the exact factorization `Nhat=Y^up N_orb` and TT first variation `delta Y^up=-eps^up` remain valid.
- Iteration 258: `Y_down=g/sqrt|g|`, the `+tr(H^2)/4` second-order density sign, and derived `Norb2` numerical values.
- Iteration 259: second-order `Q2` numerical certificate inherited from the superseded `Norb2`; the exact inverse-recursion algebra remains valid.
- Iteration 268: second-order physical `N2/Q2` numerical values; its Fourier routing rules, `Q1`, inverse-recursion structure and rejection of same-`p` routing remain valid.

No earlier topology, polarization, `E2/E3`, `K`-primitive or transpose-class result is revoked.

## Scientific status

This is a correction and strengthening of the C5 comparator construction. It prevents a false second-order orbit kernel from entering the physical `B3` numerator. It is not a Candidate Gravity residual and does not yet authorize tensor integration.

Retain

`BLOCKED_4D_EINSTEIN_VD_RESOLVENT_VERTEX_LIBRARY_TENSOR_REDUCTION_AND_SOURCE_PROJECTION`,

`BLOCKED_NOT_ZERO`.

## Readiness

`MODEL_READINESS: 24%`

No percentage increase. A provenance/consistency error was removed and the routed second-order orbit layer is now compatible with the exact same-parent transpose identity, but the physical `B3` comparator numerator is not yet fully certified.

## Exact next gate — Iteration 270

Rebuild the routed physical `K0/K1/K2 -> A1/A2/A3` layer and assemble the 8 independent `+K` `B3[s,a,b]` representatives using the corrected `Q2`. Validate all seven transpose partners by endpoint reversal into the real `-K` Fourier sector. Only if all transpose regressions pass may the full 15-term physical `B3` be classified as explicitly nonzero. Tensor reduction, Fisher/resources and `ANSATZ-003` remain forbidden until then.
