"""RQIR Iteration 122: external same-apparatus evidence audit.

This is a transparent literature-evidence matrix, not a numerical apparatus
forecast.  Entries encode only features explicitly reported in the cited works
as audited on 2026-08-31.
"""
from __future__ import annotations

PAPERS = {
    "Pontin_PRR_2023": dict(
        simultaneous_multimode=True,
        cross_spectrum=True,
        measured_transfer_or_mode_model=True,
        exact_f_2f=False,
        force_calibrated_full_f2f_matrix=False,
        rqir_mean7=False,
        rqir_covariance8=False,
        source_metrology=False,
        duty_drift=False,
    ),
    "Fu_OLE_2022": dict(
        simultaneous_multimode=False,
        cross_spectrum=False,
        measured_transfer_or_mode_model=True,
        exact_f_2f=False,
        force_calibrated_full_f2f_matrix=False,
        rqir_mean7=False,
        rqir_covariance8=False,
        source_metrology=False,
        duty_drift=False,
    ),
    "Gosling_PRR_2024": dict(
        simultaneous_multimode=True,
        cross_spectrum=True,
        measured_transfer_or_mode_model=True,
        exact_f_2f=False,
        force_calibrated_full_f2f_matrix=False,
        rqir_mean7=False,
        rqir_covariance8=False,
        source_metrology=False,
        duty_drift=False,
    ),
    "Gosling_RSI_2026": dict(
        simultaneous_multimode=True,
        cross_spectrum=True,
        measured_transfer_or_mode_model=True,
        exact_f_2f=False,
        force_calibrated_full_f2f_matrix=False,
        rqir_mean7=False,
        rqir_covariance8=False,
        source_metrology=False,
        duty_drift=False,
    ),
    "Song_NatCommun_2026": dict(
        simultaneous_multimode=True,
        cross_spectrum=False,
        measured_transfer_or_mode_model=False,
        exact_f_2f=True,
        force_calibrated_full_f2f_matrix=False,
        rqir_mean7=False,
        rqir_covariance8=False,
        source_metrology=False,
        duty_drift=False,
    ),
}

REQUIRED_FOR_NUMERICAL_U = (
    "force_calibrated_full_f2f_matrix",
    "rqir_mean7",
    "rqir_covariance8",
    "source_metrology",
    "duty_drift",
)


def main() -> None:
    # No audited paper supplies the complete RQIR numerical-u dataset.
    complete = []
    for name, row in PAPERS.items():
        ok = all(row[k] for k in REQUIRED_FOR_NUMERICAL_U)
        if ok:
            complete.append(name)
    assert complete == []

    # Important positive evidence: exact f:2f simultaneous mechanical readout/control
    # now exists as an experimental platform class (Song et al. 2026).
    assert PAPERS["Song_NatCommun_2026"]["exact_f_2f"]
    assert PAPERS["Song_NatCommun_2026"]["simultaneous_multimode"]

    # Cross-spectral multimode measurements and transfer/control models also exist,
    # but in different apparatus/data products.
    assert PAPERS["Gosling_PRR_2024"]["cross_spectrum"]
    assert PAPERS["Gosling_RSI_2026"]["cross_spectrum"]
    assert PAPERS["Fu_OLE_2022"]["measured_transfer_or_mode_model"]

    print("audited papers", len(PAPERS))
    print("complete numerical-u datasets", complete)
    print("exact f:2f platform evidence", "Song_NatCommun_2026")


if __name__ == "__main__":
    main()
