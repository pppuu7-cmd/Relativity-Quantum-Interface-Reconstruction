#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 421.

Collision-safe recovery of the prospectively frozen symmetric-cross physical
channel-2 gate that was race-created under Iteration 420 immediately before an
independent automation canonically assigned Iteration 420 to the cancellation
interpretation contract.

Scientific arithmetic is inherited byte-for-byte from the race-created
iteration420_tru1sq_channel2_symmetric_cross_derivative.py.  Only the executable
iteration identifier is changed from 420 to 421.  No node, radius, fit basis,
threshold, integrand, sign, normalization, structural check or direct-integrand
check is changed.
"""
from pathlib import Path

root=Path(__file__).resolve().parent
parent=root/'iteration420_tru1sq_channel2_symmetric_cross_derivative.py'
src=parent.read_text()
old='ITERATION=420\nTARGET_INDEX=2'
if src.count(old)!=1:
    raise RuntimeError(('iteration420_executable_identity_anchor_drift',src.count(old)))
src=src.replace(old,'ITERATION=421\nTARGET_INDEX=2',1)
ns={'__name__':'__main__','__file__':str(parent)}
exec(compile(src,str(parent),'exec'),ns,ns)
