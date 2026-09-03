#!/usr/bin/env python3
"""Infrastructure-only JSON-safe launcher for RQIR Iteration 305.

The scientific reducer is imported unchanged.  This launcher only teaches the
final json.dumps call how to serialize NumPy scalar/container types.  It does
not modify formulas, inputs, thresholds, assertions, kinematics, quadrature,
Laurent fitting or scientific classification.
"""
import importlib.util
from pathlib import Path
import json as _json
import numpy as np

HERE=Path(__file__).resolve().parent
SRC=HERE/'iteration305_direct_timelike_tru1_triangle_cut.py'
spec=importlib.util.spec_from_file_location('iteration305_science',SRC)
m=importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
_original_dumps=_json.dumps


def _numpy_default(obj):
    if isinstance(obj,np.integer):
        return int(obj)
    if isinstance(obj,np.floating):
        return float(obj)
    if isinstance(obj,np.ndarray):
        return obj.tolist()
    raise TypeError(f'Object of type {obj.__class__.__name__} is not JSON serializable')


def _safe_dumps(obj,*args,**kwargs):
    kwargs.setdefault('default',_numpy_default)
    return _original_dumps(obj,*args,**kwargs)

m.json.dumps=_safe_dumps
m.main()
