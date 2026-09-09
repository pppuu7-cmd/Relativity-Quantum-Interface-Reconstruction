# Paper III clean reproduction request

This branch exists solely to trigger the repository's independent `pull_request` clean-reproduction workflow for the strengthened Paper-III chain.

The run must execute from a fresh GitHub-hosted Ubuntu environment with Python 3.12 and freshly installed NumPy/SciPy, then pass all tracked Paper-III structural, covariance, same-apparatus, physical-PSD, detector-facing and chirp-reference audits.

A green run may be used as the independent clean-reproduction authority. A failed or missing run must not be treated as closure.

Synchronization marker: second PR event after the workflow was enabled on `main`.
