# RQIR Recovery Delta — Iteration 098

**Date:** 2026-08-30

Paper III source-metrology resource closure.

Retain:

- standard independent source Fisher target `C_src=225`;
- Toy009 zero-reset Ramsey optimum `phi~=1.09231`, `q=0.0025234392`;
- Toy014 zero-reset Ramsey optimum `phi=0.9264295097660072`, `q=0.0037632915041337926`.

New formulas:

`N_acc=C_src/F_copy`, `N_try=C_src/(p_E F_copy)`;

`T_src=N_try(t_reset+phi/Omega_E)=C_src/[p_E Omega_E q(V,tau_reset)]`.

New labels:

- RESOURCE-051: finite accepted/attempted source-copy budget;
- RESOURCE-052: wall-clock source floor becomes `p_E Omega_E > [m C_src/T_cap]/q`;
- NG-051: extra detector exposure cannot replace missing independent source-copy Fisher.

Zero-reset accepted-copy counts:

- Toy009 `~81628.866`;
- Toy014 `~64536.035`.

Files: `analysis/source_metrology_shot_certificate_iteration098.py`, `docs/PAPER_III_SOURCE_METROLOGY_SHOT_CERTIFICATE_ITERATION098.md`, research log.
