# QG-NL-EXP-001 — exponential covariant nonlocal form-factor comparator

**Frozen in:** Iteration 158  
**Status:** fixed comparator, linear TT sector instantiated; nonlinear sector BLOCKED  
**Not a Candidate Gravity ansatz.**

## Action and parameter convention

Freeze the covariant metric action

\[
S=\frac{M_{\rm Pl}^2}{2}\int d^4x\sqrt{-g}\left[
R+G_{\mu\nu}\,\mathcal F(\Box)R^{\mu\nu}
\right]+S_m[g,\Psi],
\]

with

\[
\mathcal F(\Box)=\frac{e^{-\Box/M^2}-1}{\Box},
\qquad \lambda\equiv M^{-2}>0.
\]

Metric/source convention is inherited from Iteration 149:

\[
g_{\mu\nu}=\eta_{\mu\nu}+\kappa h_{\mu\nu},
\]

with a conserved matter source obtained from the same `S_m[g,Psi]` map.

The entire exponential form factor is chosen as one explicit member of the ghost-free infinite-derivative/nonlocal gravity family. Literature anchors for the flat-space propagator and exponential form-factor models include Biswas, Koivisto & Mazumdar, arXiv:1302.0532, and Boos, Frolov & Zelnikov, arXiv:1802.09573.

## Scoped linear TT response

On the frozen spacelike TT sector with `x=k^2>0`, use the normalized spin-2 inverse kernel

\[
K_2(x)=x e^{\lambda x},
\]

and therefore

\[
\chi^R_{\rm NL}(x;\lambda)=\frac{e^{-\lambda x}}{x}.
\]

Iteration 158 freezes the finite reference point

\[
\lambda_0=1
\]

in the dimensionless momentum units already used by the six-probe protocol. The tangent is

\[
\partial_\lambda\chi^R_{\rm NL}\big|_{\lambda_0}
=-e^{-x}.
\]

No claim is made here for the scalar sector, nonlinear vertex, loop noise, or a full UV completion.

## C5 local quadratic comparison convention

The local quantum-gravity EFT comparator is frozen through operator dimension 12. In the TT two-point sector, the independent local spin-2 inverse-kernel corrections from

\[
R_{\mu\nu}\Box^n R^{\mu\nu},\qquad n=0,1,2,3,4,
\]

produce response tangents proportional to

\[
1,x,x^2,x^3,x^4.
\]

A conservative common response-gain nuisance contributes the GR response `1/x`.

Thus the six-row nuisance/comparator matrix is

\[
M_{\rm lin}=[x^{-1},1,x,x^2,x^3,x^4].
\]

## Iteration-158 certificate

On the six frozen `p^2` values from Iteration 149:

- `rank(M_lin)=6/6`;
- `smin/smax = 3.8241112956843014e-08`;
- condition number `=2.6149866535750397e7`.

Because the six-row space is saturated, both the finite nonlocal response and its lambda tangent are exactly representable on this protocol by the C5-local+gain columns. Direct solve reconstruction errors are below `5e-16`.

## Interpretation

This is **REGIME-SPECIFIC NON-IDENTIFIABILITY / PROTOCOL SATURATION**, not exact comparator identity.

The nonlocal function is not globally a finite polynomial. The zero residual arises because six sampled linear TT coordinates are exactly saturated by six allowed nuisance/comparator directions. Therefore linear six-probe data cannot certify nonlocality against the frozen dimension-12 C5 local EFT completion.

Retain:

`QG-NL-NG-001 — SIX_PROBE_LINEAR_TT_SPACE_SATURATED_BY_LOCAL_EFT_PLUS_GAIN`.

Retain guardrail:

`NG-FUNNEL-015 — FINITE_SAMPLE_SATURATION_IS_NOT_THEORY_IDENTITY`.

## BLOCKED sectors

- cubic/nonlinear `chi2R` from the same nonlocal action;
- source-completed nonlinear Ward check;
- nonlocal `N2/C3sym`;
- scalar/non-TT completion;
- full quotient against C3/C4/C5/nonlocal/asymptotic-safety.

No `ANSATZ-003`, Fisher, or resource calculation is permitted from this comparator alone.
