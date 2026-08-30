# RQIR Research Log — Iteration 098

**Date:** 2026-08-30  
**Track:** Paper III physical source-preparation/resource closure.

Converted the retained `C_src=225` independent source-amplitude Fisher requirement into accepted-copy, attempted-preparation and wall-clock budgets for Toy009/Toy014 Ramsey metrology.

New results:

- **RESOURCE-051:** `N_acc=C_src/F_copy`, `N_try=C_src/(p_E F_copy)`.
- **RESOURCE-052:** source-only wall-clock feasibility is equivalently `p_E Omega_E > [m C_src/T_cap]/q`.
- **NG-051:** detector exposure cannot substitute for missing independent source copies; this is the finite-shot form of NG-005/NG-041.

Zero-reset `V=1` repository coefficients give:

- Toy009: `F_copy~=0.00275637787`, `N_acc~=81628.866`;
- Toy014: `F_copy~=0.00348642430`, `N_acc~=64536.035`.

At the transparent `100 Hz`, `p_E=0.5`, zero-reset benchmark:

- Toy009 `T_src~=283.818 s`;
- Toy014 `T_src~=190.311 s`.

These are source-metrology-only timing slices, not full apparatus forecasts.

Reproducibility: `analysis/source_metrology_shot_certificate_iteration098.py`.
