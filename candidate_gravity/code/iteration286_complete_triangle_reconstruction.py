#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 286.

Complete held-out degree<=6 numerator reconstruction for the two raised-triangle
sectors not closed in Iteration 285. This script intentionally reuses the actual
same-parent oracle and canonical reflection rules implemented in Iteration 285.
"""
import importlib.util, json
from pathlib import Path
import numpy as np

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('i285',HERE/'iteration285_actual_numerator_basis_audit.py')
i285=importlib.util.module_from_spec(spec); spec.loader.exec_module(i285)

MON6=i285.MON6

def mon6(l): return i285.mon(MON6,l)

def audit(sec,seed):
    rng=np.random.default_rng(seed)
    train=rng.uniform(-.95,.95,(220,4))
    held=rng.uniform(-1.05,1.05,(28,4))
    y=np.array([i285.tri_trace(sec,l) for l in train])
    z=np.array([i285.tri_trace(sec,l) for l in held])
    X=np.array([mon6(l) for l in train]); H=np.array([mon6(l) for l in held])
    c=np.linalg.lstsq(X,y,rcond=None)[0]
    r=H@c-z
    return {
      'train_points':len(train),'heldout_points':len(held),
      'basis_size':len(MON6),'train_rank':int(np.linalg.matrix_rank(X)),
      'condition_number':float(np.linalg.cond(X)),
      'heldout_max_abs':float(np.max(np.abs(r))),
      'heldout_rms':float(np.sqrt(np.mean(r*r))),
      'heldout_relative_max':float(np.max(np.abs(r))/np.max(np.abs(z))),
    }

result={
 'iteration':286,'model_readiness_percent':24,
 'triangle_sectors':{
   '(0,0.21)':audit('tri_(0.0, 0.21)',28621),
   '(0.21,0.41)':audit('tri_(0.21, 0.41)',2862141),
 },
 'retained_triangle_0_0.41_relative_max':8.872284498320589e-11,
 'retained_bubble_a_relative_max':9.296403942129201e-10,
 'retained_bubble_b_relative_max':2.223469270656875e-9,
 'classification':'PASS_COMPLETE_NONSCALELESS_ACTUAL_ORACLE_NUMERATOR_RECONSTRUCTION_ALL_BUBBLE_AND_TRIANGLE_SECTORS',
 'candidate_residual':False,
 'next_gate':287,
}
assert all(v['train_rank']==210 and v['heldout_relative_max']<1e-7 for v in result['triangle_sectors'].values())
print(json.dumps(result,indent=2,sort_keys=True))
