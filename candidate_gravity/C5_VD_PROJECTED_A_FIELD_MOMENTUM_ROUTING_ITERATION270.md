# C5 VD projected A field-momentum routing — Iteration 270

## Scope

This iteration continues from the corrected routed physical orbit layer of Iteration 269. It does **not** claim a numerical nonzero `B3`. It closes an implementation/provenance requirement that must be satisfied before the frozen eight-representative `B3[s,a,b]` target can be evaluated physically.

The projected same-parent identity is

\[
A_{\gamma\delta}=K^j_{\gamma\delta}E_j.
\]

In condensed-index/Fourier space the contracted field-space index `j` contains a spacetime momentum. Therefore the momentum carried by `E_j` is not a spectator label: it participates in the orbit-kernel support of `K^j_{\gamma\delta}`.

## Exact routing statement

Adopt the frozen Iteration-267 convention that a background insertion carrying total momentum `K` maps the orbit momentum as

\[
p_{out}=p_{in}+K.
\]

For a polarized projected term

\[
K_m[S]E_n[T],
\]

where `S` is the subset of external background legs carried explicitly by the `K` coefficient and `T` is the subset carried by the EOM coefficient, translational support requires

\[
p_{out}-p_{in}=k_S+q_j,
\]

and contraction with `E[T]` fixes

\[
q_j=k_T.
\]

Hence

\[
\boxed{p_{out}-p_{in}=k_S+k_T}.
\]

The total shift is correct only if the momentum `q_j` of the contracted EOM/field index remains explicit until the `K E` contraction is performed.

## Consequence for A1/A2/A3

The already frozen polarized algebra remains unchanged:

\[
A_1[x]=K_0E_1[x],
\]

\[
A_2[x,y]=K_0E_2[x,y]+K_1[x]E_1[y]+K_1[y]E_1[x],
\]

and

\[
\begin{aligned}
A_3[x,y,z]={}&K_0E_3[x,y,z]
+K_1[x]E_2[y,z]+K_1[y]E_2[x,z]+K_1[z]E_2[x,y]\\
&+K_2[x,y]E_1[z]+K_2[x,z]E_1[y]+K_2[y,z]E_1[x].
\end{aligned}
\]

What changes is the implementation contract: each `K_m` must be represented with enough routing information to retain the contracted field/EOM momentum. A local finite matrix `K_m(p)` labelled only by orbit momentum and the explicit background subset is not yet the physical Fourier kernel.

For the frozen null-soft condition `E1[s]=0`, the route enumerator reproduces exactly:

- `A1[s]`: 0 surviving projected terms;
- `A2[s,a]`: 2 survivors;
- `A2[s,b]`: 2 survivors;
- `A2[a,b]`: 3 survivors;
- `A3[s,a,b]`: 6 survivors.

Every survivor carries the expected total support of its external legs only when the contracted EOM momentum is included.

## B3 implication

The eight independent forward representatives retained from Iteration 266 still all have total support

\[
\boxed{k_s+k_a+k_b}.
\]

Iteration 269 corrected `Q2`; this iteration shows that the remaining `A` side must be routed with a two-sided/contracted-field momentum label before those corrected resolvents can be multiplied into a physical `B3` kernel.

This prevents a false-positive nonzero numerator from multiplying finite matrices whose visible external shifts add correctly while the internal field-space convolution has been dropped.

## Frozen status

`PASS_EXACT_PROJECTED_A_CONTRACTED_FIELD_MOMENTUM_ROUTING`

Guardrails:

`NO_DROP_CONTRACTED_EOM_MOMENTUM_IN_K_KERNEL`

`NO_PREMATURE_LOCAL_MATRIX_K_TIMES_E_AS_PHYSICAL_A`

This is an implementation/provenance certificate. It is **not** a consistency FAIL, exact comparator identity, non-identifiability result, near-degeneracy result, novelty certificate, or Candidate Gravity residual.

## Scientific state

C5 remains

`BLOCKED_4D_EINSTEIN_VD_RESOLVENT_VERTEX_LIBRARY_TENSOR_REDUCTION_AND_SOURCE_PROJECTION`

with

`BLOCKED_NOT_ZERO`.

No `ANSATZ-003`; Fisher/resources and blind heavy full-C5 integration remain forbidden.
