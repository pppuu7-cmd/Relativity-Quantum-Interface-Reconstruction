# C4-DRGT-001 — fixed nonlinear ghost-free massive-spin-2 comparator

**Iteration:** 156  
**Status:** SCOPED / TT TREE COMPARATOR  
**Reference metric:** `f_mn=eta_mn`

## Frozen action

Use the standard dRGT two-parameter ghost-free massive-gravity family in the convention

`S = M_Pl^2/2 int d4x sqrt(-g) [ R + m^2/2 (L2[K] + alpha3 L3[K] + alpha4 L4[K]) ] + S_m[g]`,

`K = I - sqrt(g^{-1} eta)`,

with `alpha0=alpha1=0`, `alpha2=1`, and matter minimally coupled to the physical metric `g`.

The `L_n` convention is the standard epsilon-epsilon convention:

`L2=2([K]^2-[K^2])`,

`L3=[K]^3-3[K][K^2]+2[K^3]`.

Literature anchors:

- C. de Rham, *Massive Gravity*, Living Reviews in Relativity 17, 7 (2014), especially the metric action and `L_n` definitions;
- S. F. Hassan and R. A. Rosen, arXiv:1106.3344, nonlinear Hamiltonian constraint / absence of the BD ghost;
- de Rham, Gabadadze & Tolley, arXiv:1107.3820 and arXiv:1108.4521 for Stückelberg/helicity structure.

The repository treats ghost freedom here as a literature-established property of the declared dRGT family, not as a new RQIR proof.

## Frozen finite reference point

Protocol units:

`m^2=0.04`, `alpha3=0`, `alpha4=0`.

Tangent parameters:

`theta_C4=(log m^2, alpha3)`.

Use the same six spacelike TT momentum triplets, deterministic polarizations and Gaussian windows `(tau,L)=(0.8,0.6)` used by the source-completed C5 protocol.

## Cubic TT potential

For `g=eta+h`, define mixed `H=eta h`. On TT legs, `Tr H=0`.

Expanding

`K = 1/2 H - 3/8 H^2 + 5/16 H^3 + ...`

gives

`L2^(3)=3/4 Tr(H^3)`,

`L3^(3)=1/4 Tr(H^3)`.

Therefore the cubic dRGT potential contribution in the action bracket is

`V3_dRGT = m^2(3+alpha3)/8 Tr(H^3)`.

`L4` starts at fourth order, so `alpha4` is **blind in the present cubic TT protocol**. This is a protocol/order limitation, not the statement that alpha4 is absent from dRGT physics.

## Full scoped tree response

The finite tree response uses

- the EH cubic vertex;
- the dRGT cubic potential above;
- massive TT propagators `1/(k^2+m^2)` on the frozen spacelike probes.

At the frozen reference point the six response values are

`[0.41598902695785883,-1.0421653262124124,-9.30686701147015,-12.449001654539147,4.0683399477607995,-2.3313492002174723]`.

## Tangent certificate

For `(log m^2,alpha3)`, the six-by-two tangent is

`[[0.08410827495950812,0.06014797241478866],`
` [0.3388004414024848,0.017411147214802865],`
` [2.2537493574606224,-0.1670416960113702],`
` [1.7936161583555166,-0.6470043472565035],`
` [-0.690425234550442,0.17218037853655313],`
` [0.39855343699621354,-0.14310845340580042]]`.

Rank: **2/2**.

Singular values:

`[3.062684454379795,0.4175708275716087]`.

`smin/smax=0.13634144772501477`.

## Comparison with the existing local C5 R^3 span

Projecting the two dRGT tangent columns onto the existing Ward-validated C5 local `6x2` span (`Ricci^3`, `Riemann^3`) leaves residual norms approximately

`[0.57999745,0.09656019]`,

corresponding to residual fractions

`[0.19275682,0.13647969]`.

The combined matrix

`[V_C5_local, V_C4_dRGT]`

has rank **4**, versus rank 2 for either scoped two-column block alone.

Combined singular values:

`[5.62719921,1.53092825,0.39407597,0.06156025]`.

This establishes only that the chosen dRGT TT tree tangent contains directions outside the **currently implemented two-column C5 local R^3 span**. It is not a distinction from the full C5 EFT, whose higher-local and loop/nonanalytic directions remain BLOCKED.

## Retained results

### `C4-NG-001 — ALPHA4_CUBIC_TT_BLIND`

The cubic TT protocol cannot identify `alpha4` because the dRGT `L4` interaction starts at quartic order. Higher-point or non-TT observables are required.

Classification: regime/order-specific non-identifiability, not FAIL.

### `C4-NG-002 — DRGT_EXPANDS_SCOPED_NONLINEAR_COMPARATOR_SPAN`

At the frozen nonzero-mass reference point, `(log m^2,alpha3)` supplies two independent finite TT nonlinear-response directions, and the combined rank with the existing local C5 R^3 block rises from 2 to 4.

Classification: positive comparator result. It makes the novelty funnel stricter; it is not evidence for the future candidate.

## Blocked sectors

- helicity-0/helicity-1 finite RQIR completion: BLOCKED;
- Vainshtein/nonperturbative response: BLOCKED;
- C4 `N2` and `C3sym`: BLOCKED;
- alpha4 higher-point direction: BLOCKED_AT_CUBIC_ORDER;
- full C4 quotient: BLOCKED.

No blocked row is set to zero.

## Reproducibility

- `analysis/c4_drgt_nonlinear_tangent_iteration156.py`
- `results/c4_drgt_nonlinear_tangent_iteration156.json`
