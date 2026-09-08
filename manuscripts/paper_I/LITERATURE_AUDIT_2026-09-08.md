# RQIR Paper I — literature audit

Date: 2026-09-08
Status: working submission audit
Scope: metadata/coverage check for references already used or directly motivated by `manuscripts/paper_I/main.tex`.

## Verified recent records

The following working-bibliography records were checked against publisher or canonical preprint pages and are consistent with the current manuscript metadata:

- **Aziz & Howl (2025)**, *Classical theories of gravity produce entanglement*, Nature **646**, 813–817. DOI: `10.1038/s41586-025-09595-7`.
- **Chen & Giacomini (2025)**, *Quantum Effects in Gravity Beyond the Newton Potential from a Delocalized Quantum Source*, Phys. Rev. X **15**, 031063. DOI: `10.1103/hl1c-t8z9`.
- **Feng, Vedral & Marletto (2026)**, *Collapse-based models for gravity do not violate the entanglement-based witness of nonclassicality*, Phys. Rev. D **113**, 104055. DOI: `10.1103/83rl-nygv`.
- **Miki et al. (2025)**, *Role of quantum measurements when testing the quantum nature of gravity*, Phys. Rev. D **111**, 104084. DOI: `10.1103/PhysRevD.111.104084`.
- **Marletto & Vedral (2025)**, *Quantum-information methods for quantum gravity laboratory-based tests*, Rev. Mod. Phys. **97**, 015006. DOI: `10.1103/RevModPhys.97.015006`.
- **Lami, Pedernales & Plenio (2024)**, *Testing the Quantumness of Gravity without Entanglement*, Phys. Rev. X **14**, 021022. DOI: `10.1103/PhysRevX.14.021022`.
- **Diósi (2025)**, *A healthier stochastic semiclassical gravity: world without Schrödinger cats*, Gen. Relativ. Gravit. **57**, 62. DOI: `10.1007/s10714-025-03396-z`.

## Metadata correction queued

The current `TangEtAl2025` entry uses `and others`. The canonical arXiv record `2512.13675` lists:

Ziqian Tang, Chen Yang, Zizhao Han, Zikuan Kan, Yulong Liu, Hanyu Xue.

If retained in the manuscript, this should remain explicitly labelled as a preprint unless a peer-reviewed version is identified before submission.

## Quantum-clock coverage gap

The introduction currently names quantum clocks among the relevant experimental architectures, but the working bibliography has no canonical quantum-clock reference. Two suitable anchors are:

1. **Albert Roura (2020)**, *Gravitational Redshift in Quantum-Clock Interferometry*, Phys. Rev. X **10**, 021014. DOI: `10.1103/PhysRevX.10.021014`.
2. **Eyuri Wakakuwa (2026)**, *Detectability of post-Newtonian classical and quantum gravity via quantum clock interferometry*, Phys. Rev. D **113**, 086008. DOI: `10.1103/hjfx-rlfj`.

Roura 2020 is the stronger canonical anchor for the general introduction; Wakakuwa 2026 is useful if Paper I wants an explicitly current post-Newtonian/quantum-gravity-facing clock comparator.

## Novelty-positioning consequence

Paper I should not claim novelty for the existence of mean/noise/response distinctions, informational incompleteness, CTP response structure, or quantum-clock gravitational sensitivity. Its defensible novelty remains the RQIR combination of:

- a declared finite calibration quotient on physically admissible source states;
- a positivity-preserving calibration-nullspace response discriminant;
- constructive detector-facing realization;
- calibration steering as an interface co-design variable;
- strict separation between source-level distinguishability, statistical identifiability, resource closure and comparator uniqueness.

## Remaining literature blockers before submission

- Add/cite at least one canonical quantum-clock reference in `main.tex`.
- Normalize the Tang preprint author metadata if retained.
- Perform a final Crossref/INSPIRE/APS metadata pass for all bibliography entries.
- Run a targeted prior-art search specifically for the conjunction `positive-state calibration quotient + nullspace response discriminant + calibration steering`; generic tomography/nullspace citations alone are not sufficient to close the novelty audit.
