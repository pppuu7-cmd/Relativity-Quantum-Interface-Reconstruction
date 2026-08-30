# RQIR Recovery Delta — Iteration 090

**Date:** 2026-08-30

## New retained external-data result

Iteration 090 audits current multimode levitated literature against the complete Iteration-089 apparatus certificate.

External anchors:

- Piotrowski et al., Nature Physics 19, 1009–1013 (2023), DOI `10.1038/s41567-023-01956-1`;
- Pontin et al., arXiv:2604.26790 (2026);
- Iacoponi, Rademacher, Monteiro, PR Research accepted 16 June 2026, DOI `10.1103/wrd3-t5cf`.

### Frequency compatibility

Piotrowski published bare mode intervals:

- x `222–226 kHz`;
- y `266–270 kHz`;
- z `79–81 kHz`.

No pair-ratio interval contains the current RQIR requirement `omega4/omega2=2`.

Pontin's reported `70–95 kHz` sub-shot-noise band has span ratio `95/70<2`, so that band alone cannot host both `f` and `2f`.

### RQIR-APP-002

Current literature demonstrates simultaneous multimode levitated control/readout and even full spectral covariance reconstruction, but this audit did not identify one published apparatus data set that simultaneously supplies the complete RQIR input-referred force transfer/cross-PSD, seven calibration matrix rates, hidden-source metrology and campaign control duty in one normalization.

### RQIR-NG-040

Do not concatenate best-in-class subsystem numbers from different papers as though they define one apparatus likelihood. Such numbers may be used only to form an explicitly parameterized design envelope after a physical normalization/mapping.

## Reproducibility

- `analysis/external_multimode_compatibility_iteration090.py`
- `docs/PAPER_III_EXTERNAL_MULTIMODE_APPARATUS_AUDIT_ITERATION090.md`
- `research_log/2026-08-30_iteration_090_external_multimode_apparatus_audit.md`

## Next gate

Construct a tunable dual-mode `f,2f` design envelope in one common physical coordinate and solve minimum science/calibration/source/control performance surfaces with Iterations 087–089. Keep the result as a design target until one measured apparatus closes APP-002.
