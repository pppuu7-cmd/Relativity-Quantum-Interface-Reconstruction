# RQIR Iteration 090 — External Multimode Apparatus Compatibility Audit

**Date:** 2026-08-30  
**Status:** external-data/apparatus-closure audit; no hardware forecast and no new-physics claim.

## 1. Purpose

Iteration 089 completed the interval-rate algebra needed for a robust Toy009/Toy014 wall-clock comparison. The next admissible gate is to test whether current published multimode levitated platforms already provide enough measured quantities to instantiate that certificate without inventing an ASD, cross-PSD or source-metrology rate.

This audit uses published platform facts only as **external anchors**. It does not claim that any cited experiment implements RQIR.

## 2. External anchor A — simultaneous two-mode levitated nanoparticle control

Piotrowski et al., *Nature Physics* 19, 1009–1013 (2023), DOI `10.1038/s41567-023-01956-1`, report simultaneous ground-state cooling of two centre-of-mass modes of one optically levitated silica nanoparticle.

Published apparatus quantities include:

- nominal particle diameter `143 +/- 6 nm`;
- mass `3.4 +/- 0.4 fg`;
- bare COM frequencies
  - `Omega_x/2pi = 224 +/- 2 kHz`,
  - `Omega_y/2pi = 268 +/- 2 kHz`,
  - `Omega_z/2pi = 80 +/- 1 kHz`;
- cavity linewidth `kappa/2pi = 330 +/- 9 kHz`;
- simultaneous heterodyne PSDs containing both transverse modes;
- fitted occupations near `0.83 +/- 0.10` and `0.81 +/- 0.12` at the reported optimum.

Reference: `https://doi.org/10.1038/s41567-023-01956-1`.

These results demonstrate that simultaneous multimode detection/control of one levitated particle is experimentally real; RQIR therefore should not impose a false single-mode limitation.

## 3. Frequency-ratio check against the present RQIR two-harmonic discriminator

The current D2 discriminator uses two source harmonics at frequencies in the ratio

`omega_4/omega_2 = 2`.

Using the published one-sigma mode-frequency intervals as simple independent ranges, the possible larger/smaller frequency ratios are:

- x/z: about `2.7407` to `2.8608`;
- y/x: about `1.1770` to `1.2162`;
- y/z: about `3.2840` to `3.4177`.

None contains the required ratio `2`.

This does **not** rule out tuning the trap or using different modes/platforms. It only says that the published Piotrowski operating point cannot be inserted directly as the present RQIR `n=2,n=4` pair.

Reproducibility: `analysis/external_multimode_compatibility_iteration090.py`.

## 4. External anchor B — full spectral covariance has now been demonstrated in levitated multimode optics

Pontin et al., arXiv:2604.26790 (submitted 29 April 2026), report optical squeezing mediated by two centre-of-mass modes of a levitated nanoparticle, both cooled below unit occupation. Their abstract explicitly states that heterodyne analysis resolves the **full spectral covariance matrix** of the optical output field and reports a sub-shot-noise band around `70–95 kHz` with minimum variance about `0.98`.

Reference: `https://arxiv.org/abs/2604.26790`.

This is directly relevant to RQIR-NG-036/038 in one methodological sense: measuring off-diagonal spectral covariance in a multimode levitated system is experimentally realizable, so the RQIR requirement for a full matrix spectral likelihood is not merely formal.

However, the published `70–95 kHz` sub-shot-noise band itself has span ratio only

`95/70 ~= 1.357 < 2`,

so that band alone cannot simultaneously contain both `f` and `2f`. More importantly, an optical quadrature covariance matrix is not automatically an **input-referred force** PSD/cross-PSD matrix for the RQIR gravitational-force template; the force transduction Jacobian and nuisance profile must be calibrated explicitly.

## 5. External anchor C — current multimode force-sensing direction

Iacoponi, Rademacher and Monteiro, *Physical Review Research*, accepted 16 June 2026, DOI `10.1103/wrd3-t5cf`, analyze cavity-levitated nanoparticle arrays for quantum sensing and identify a mechanical-mode-comb structure with potential force-sensing advantages.

Reference: `https://doi.org/10.1103/wrd3-t5cf`.

This is a useful candidate architecture class for future RQIR broadband/multiband work, but it is a theoretical/spectral proposal rather than the complete measured RQIR apparatus certificate required by RESOURCE-042.

## 6. RQIR-APP-002 — published multimode capability is not yet a complete RQIR apparatus envelope

The literature now independently demonstrates several pieces RQIR needs:

1. simultaneous multimode levitated detection/control;
2. measured multimode PSDs;
3. reconstruction of full spectral covariance matrices in levitated optomechanics;
4. active development of multimode/comb force-sensing architectures.

But the current audit did **not** find one published platform data set that simultaneously supplies, in one physical coordinate system:

- calibrated RQIR science transfer at two bands in the required `2:1` relation;
- the full **input-referred force** PSD/cross-PSD at both bands with uncertainty;
- seven same-time dual-probe calibration Jacobians and matrix Fisher blocks;
- independent Toy009/Toy014 hidden-source-amplitude metrology (`R_src`) including preparation success, visibility, coupling, reset/readout and coherence;
- campaign timing/geometry/additive/gain stability and duty.

Therefore the Iteration-089 absolute Toy009/Toy014 NG-030 comparison remains **data-underdetermined**, not algebra-underdetermined.

This is a negative apparatus-closure result, not a no-go for the experiment.

## 7. RQIR-NG-040 — multimode PSDs cannot be composed across papers as one apparatus

It is tempting to take:

- a force sensitivity from one experiment;
- a full covariance matrix from another;
- mode frequencies from a third;
- source-metrology assumptions from the toy model;

and combine them into a numerical wall-clock forecast.

That is not admissible unless a physical mapping demonstrates that all quantities refer to the same transfer normalization, bandwidth/window, force coordinate, acceptance/duty and correlated nuisance model.

**RQIR-NG-040:** independently published best-in-class subsystem numbers do not form a valid joint apparatus likelihood by concatenation.

They may define a **design envelope**, but not an experimental forecast.

## 8. What can be retained quantitatively now

The external audit supports the following conservative conclusions:

- simultaneous multimode levitated sensing/control is experimentally established;
- full spectral covariance reconstruction is experimentally established in a levitated multimode optical readout;
- the specific published Piotrowski frequency triplet does not directly supply the RQIR `2:1` pair;
- the reported Pontin `70–95 kHz` sub-shot-noise band cannot itself contain both `f` and `2f`;
- neither source supplies the complete input-referred force/calibration/source-metrology rate vector required for RESOURCE-042.

No absolute RQIR `R_beta`, `H_cal`, `R_src` or total days/hours are inferred from these papers.

## 9. Next gate

The next useful apparatus-level calculation should be a **parameterized tunable dual-mode envelope**, not a fabricated fixed apparatus:

1. impose two detector modes or two broadband response points at `f` and `2f`;
2. parameterize their input-referred force PSDs and cross-correlation with uncertainty;
3. propagate through Iteration 087 to `R_beta^-`;
4. parameterize the seven matrix calibration rates using the same spectral matrix and transduction family;
5. combine a robust Ramsey/pointer `R_src^-` and duty through Iteration 089;
6. solve for the minimum detector/source performance surfaces where Toy009 or Toy014 becomes feasible and where NG-030 dominance becomes possible.

This would turn the missing experimental data into explicit engineering targets while preserving the distinction between a design envelope and a measured apparatus.

## 10. Reproducibility

Run

`python analysis/external_multimode_compatibility_iteration090.py`.

The script checks the published Piotrowski mode-frequency intervals against the exact RQIR factor-two harmonic requirement and verifies that a `70–95 kHz` band cannot itself contain both `f` and `2f`.
