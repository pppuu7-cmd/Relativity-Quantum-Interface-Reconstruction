# Derivation Map — ANSATZ-PQG-EFT-001 v0.1

| ID | Input | Derived object | Approximation/order | RQIR object | Status | Authority |
|---|---|---|---|---|---|---|
| D-001 | Einstein-Hilbert + scalar action | `g=eta+kappa h` perturbative field content | weak field | model variables | DERIVED/DECLARED | `MODEL.md` |
| D-002 | matter action variation wrt metric | stress tensor `T_mn` | exact covariant definition | source operator | DERIVED/DECLARED | `MODEL.md` |
| D-003 | first-order metric expansion | `S_int^(1)=-(kappa/2) int h_mn T^mn` | O(kappa) | matter-gravity coupling | DERIVED/DECLARED | `MODEL.md` |
| D-004 | matter state `rho_m` + `T_mn` | `J=<T>` | state-parametric | first moment | DEFINED | `MODEL.md` |
| D-005 | same `rho_m,T` | centered symmetrized `N` | second connected order | noise kernel | DEFINED | `MODEL.md` |
| D-006 | same `rho_m,T` | retarded commutator `chi^R` | linear response | ordered/retarded response | DEFINED | `MODEL.md` |
| D-007 | same SK/CTP generating functional | higher connected stress correlators | declared truncation required | higher hierarchy | STRUCTURAL | `MODEL.md` |
| D-008 | ansatz theory-class definition | identity with comparator C5 | exact at declared class level | comparator map | PROVED_BY_DEFINITION | Iteration 133 closure doc |
| D-009 | D-008 | no independent C5-distinguishing beta direction | exact | QG-007 | FAIL | `GATE_STATUS.yaml` |

## Required future derivations if this reference is deepened

1. Explicit linearized constraint/BRST reduction and relational RQIR observable map.
2. Tree static exchange -> Newtonian potential with convention checks.
3. Renormalized/smeared scalar stress-tensor `J,N,chi^R` in one chosen source state.
4. CTP influence action showing the common origin of dissipation/noise kernels.
5. Detector mapping only after a nontrivial comparison coordinate is defined.

Because the branch is an exact C5 reference, items 1–4 are useful validation work but cannot turn QG-007 into PASS without changing the model class/version.
