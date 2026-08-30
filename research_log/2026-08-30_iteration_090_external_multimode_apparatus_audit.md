# RQIR Research Log — Iteration 090

**Date:** 2026-08-30

## Goal

Test whether current published multimode levitated platforms already supply enough measured data to instantiate the Iteration-089 robust Toy009/Toy014 apparatus certificate without mixing incompatible subsystem numbers.

## External anchors checked

1. Piotrowski et al., *Nature Physics* 19, 1009–1013 (2023), DOI `10.1038/s41567-023-01956-1`: simultaneous two-mode ground-state cooling and heterodyne PSDs of a levitated silica nanoparticle; published bare frequencies `224+/-2`, `268+/-2`, `80+/-1 kHz`.
2. Pontin et al., arXiv:2604.26790 (2026): levitated multimode optical squeezing with heterodyne reconstruction of the full spectral covariance matrix; reported sub-shot-noise band `70–95 kHz`.
3. Iacoponi, Rademacher, Monteiro, PR Research accepted 16 June 2026, DOI `10.1103/wrd3-t5cf`: multimode/mechanical-mode-comb force-sensing architecture proposal.

## Result

The Piotrowski mode-frequency uncertainty intervals give pair-ratio ranges approximately

- x/z `2.7407–2.8608`;
- y/x `1.1770–1.2162`;
- y/z `3.2840–3.4177`.

None contains the present RQIR harmonic ratio `2`.

The Pontin `70–95 kHz` sub-shot-noise band has span ratio `1.357<2`, so that band alone cannot contain both `f` and `2f`.

The literature demonstrates that simultaneous multimode readout and full spectral covariance reconstruction are experimentally real capabilities, but this audit did not identify one published apparatus data set supplying the full RQIR science force transfer/cross-PSD, seven calibration Fisher blocks, hidden-source metrology and campaign control duty in one common normalization.

New **RQIR-APP-002**: published multimode capability is not yet a complete RQIR apparatus envelope.

New **RQIR-NG-040**: best-in-class numbers from different experiments cannot be concatenated as though they were one joint apparatus likelihood. Cross-paper subsystem values may define a design envelope only after an explicit physical normalization/mapping.

## Reproduce

`python analysis/external_multimode_compatibility_iteration090.py`

## Document

`docs/PAPER_III_EXTERNAL_MULTIMODE_APPARATUS_AUDIT_ITERATION090.md`

## Next gate

Build a parameterized tunable dual-mode `f,2f` apparatus envelope using one common transfer/noise coordinate. Propagate uncertain force PSD/cross-PSD through Iteration 087, seven calibration blocks through Iteration 088, robust source metrology and duty through Iteration 089, then solve minimum performance surfaces rather than fabricating a fixed experimental forecast.
