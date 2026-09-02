#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 286.

Complete the two remaining raised-triangle degree<=6 / 210-monomial
held-out numerator reconstructions using the actual denominator-stripped
same-parent primitive oracle frozen in Iteration 285.

This is a completeness gate only.  It does not perform IBP, source completion,
comparator subtraction, Fisher profiling, or ansatz promotion.
"""
import importlib.util, json
from pathlib import Path
import numpy as np

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('i285',HERE/'iteration285_actual_numerator_basis_audit.py')
i285=importlib.util.module_from_spec(spec); spec.loader.exec_module(i285)


def audit_sector(sec, seed):
    q1,q2=i285.PAIR[sec]
    rng=np.random.default_rng(seed)
    tr=rng.uniform(-0.95,0.95,(232,4))
    ho=rng.uniform(-1.05,1.05,(36,4))
    y=np.array([i285.tri_trace(sec,l) for l in tr])
    z=np.array([i285.tri_trace(sec,l) for l in ho])
    X=np.array([i285.mon(i285.MON6,l) for l in tr])
    H=np.array([i285.mon(i285.MON6,l) for l in ho])
    metric=i285.fitmetric(X,H,y,z)
    metric['q1']=np.array(q1,float).tolist()
    metric['q2']=np.array(q2,float).tolist()
    return metric

sectors={
    'tri_(0.0, 0.21)':audit_sector('tri_(0.0, 0.21)',28601),
    'tri_(0.21, 0.41)':audit_sector('tri_(0.21, 0.41)',28602),
}

# Carry forward the already-certified third sector for a single complete ledger.
prior=i285.tri210
all_rel=[prior['heldout_rel_max']]+[v['heldout_rel_max'] for v in sectors.values()]
all_rank=[prior['train_rank']]+[v['train_rank'] for v in sectors.values()]

result={
    'iteration':286,
    'model_readiness_percent':24,
    'degree_bound_triangle':6,
    'basis_size':210,
    'already_certified_sector':{
        'sector':'tri_(0.0, 0.41)',
        'heldout_rel_max':prior['heldout_rel_max'],
        'train_rank':prior['train_rank'],
    },
    'new_sector_certificates':sectors,
    'all_three_full_rank':bool(all(r==210 for r in all_rank)),
    'worst_all_three_heldout_rel_max':float(max(all_rel)),
    'classification':'PASS_COMPLETE_ALL_THREE_RAISED_TRIANGLE_DEGREE6_210_ORACLE_RECONSTRUCTION' if max(all_rel)<1e-7 and all(r==210 for r in all_rank) else 'BLOCKED_TRIANGLE_RECONSTRUCTION_COMPLETENESS',
    'candidate_residual':False,
    'ansatz_003_created':False,
    'next_gate':287,
    'next_gate_description':'Translate the validated 70/210 fixed-coordinate polynomial numerator coefficients into a tensor-moment/IBP representation or an explicitly complete covariant basis including soft momentum and TT polarizations; only then extract hard-channel logarithmic/discontinuity coefficient functions.',
}

assert result['all_three_full_rank']
assert result['worst_all_three_heldout_rel_max'] < 1e-7
print(json.dumps(result,indent=2,sort_keys=True))

# Workflow trigger marker: authoritative Iteration 286 execution.
