#!/usr/bin/env python3
"""Iteration 419: operational repair of Iteration 418 only.

No scientific convention changes.  The Iteration-418 parent-source sentinel
incorrectly required the textual marker `start=time.perf_counter()` to occur
exactly once, while the frozen Iteration-407 source contains two textual
occurrences.  Use the final occurrence, which is the executable start marker,
and otherwise execute Iteration 418 byte-for-byte after changing only its
iteration identifier.
"""
from pathlib import Path

root = Path(__file__).resolve().parent
parent = root / "iteration418_tru1sq_channel2_mass_derivative_cancellation_audit.py"
src = parent.read_text()

old = '''marker = "start=time.perf_counter()"
if src.count(marker) != 1:
    raise RuntimeError(("iteration407_start_marker_drift", src.count(marker)))
prefix = src.split(marker, 1)[0]'''
new = '''marker = "start=time.perf_counter()"
if src.count(marker) < 1:
    raise RuntimeError(("iteration407_start_marker_missing", src.count(marker)))
prefix = src.rsplit(marker, 1)[0]'''
if src.count(old) != 1:
    raise RuntimeError(("iteration418_repair_anchor_drift", src.count(old)))
src = src.replace(old, new, 1)
if src.count("ITERATION = 418") != 1:
    raise RuntimeError(("iteration418_identity_drift", src.count("ITERATION = 418")))
src = src.replace("ITERATION = 418", "ITERATION = 419", 1)
ns = {"__name__": "__main__", "__file__": str(parent)}
exec(compile(src, str(parent), "exec"), ns, ns)
