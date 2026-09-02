#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 289.

Audit the epsilon asymptotics of the raw Iteration-288 triangle common-cut
scans.  The original 288 workflow used an ordinary polynomial fit in epsilon,
which is valid for the l^2 calibration but invalid for actual numerator scans
when a 1/epsilon term is present.

For each scan y(eps), fit z(eps)=eps*y(eps).  The intercept z(0) is the Laurent
residue A in y=A/eps+B+O(eps).  We compare cubic interpolation (four points)
with quadratic regression as a robustness diagnostic.  The derivative of the
cubic z fit at zero is reported as a diagnostic finite coefficient B, but it is
not promoted while the total IR residue is nonzero.
"""
import json
from pathlib import Path
import numpy as np

HERE=Path(__file__).resolve().parent
RAW=HERE.parent/'results'/'iteration288_triangle_common_cut_raw_scan.json'
r=json.loads(RAW.read_text())
EPS=np.array([.02,.01,.005,.0025],float)


def audit_scan(vals):
    y=np.array(vals,float); z=EPS*y
    pc=np.polyfit(EPS,z,3)  # z=A+B eps+C eps^2+D eps^3
    pq=np.polyfit(EPS,z,2)
    A=float(pc[-1]); B=float(pc[-2]); Aq=float(pq[-1])
    return {
      'eps_times_cut':z.tolist(),
      'laurent_residue_A_cubic':A,
      'laurent_residue_A_quadratic_crosscheck':Aq,
      'residue_method_abs_difference':abs(A-Aq),
      'diagnostic_finite_B_cubic':B,
    }

cal={k:audit_scan(v['eps_scan']) for k,v in r['calibration'].items()}
sec={k:audit_scan(v['eps_scan']) for k,v in r['triangle_sectors'].items()}
Acal=max(abs(v['laurent_residue_A_cubic']) for v in cal.values())
Amin=min(abs(v['laurent_residue_A_cubic']) for v in sec.values())
Atot=sum(v['laurent_residue_A_cubic'] for v in sec.values())
Btot=sum(v['diagnostic_finite_B_cubic'] for v in sec.values())
rob=max(v['residue_method_abs_difference'] for v in sec.values())

result={
 'iteration':289,
 'model_readiness_percent':24,
 'epsilon_points':EPS.tolist(),
 'calibration':cal,
 'triangle_sectors':sec,
 'max_abs_calibration_ir_residue':Acal,
 'min_abs_actual_sector_ir_residue':Amin,
 'total_triangle_common_cut_ir_residue':float(Atot),
 'diagnostic_triangle_finite_part_sum_before_pole_completion':float(Btot),
 'max_cubic_vs_quadratic_residue_difference':rob,
 'supersedes_iteration288_workflow_finite_values':True,
 'classification':('PASS_DETECTED_ROBUST_UNCANCELLED_TRIANGLE_COMMON_CUT_IR_POLE__FINITE_COEFFICIENT_BLOCKED'
   if Acal<1e-6 and Amin>1e-4 and abs(Atot)>1e-4 and rob<1e-5 else
   'BLOCKED_TRIANGLE_IR_POLE_CLASSIFICATION'),
 'candidate_residual':False,
 'guardrails':[
   'ITERATION288_POLYNOMIAL_EPS_EXTRAPOLATED_ACTUAL_TRIANGLE_VALUES_ARE_NOT_FINITE_PHYSICAL_COEFFICIENTS',
   'DO_NOT_PROMOTE_DIAGNOSTIC_FINITE_B_WHILE_TOTAL_1_OVER_EPS_RESIDUE_IS_NONZERO',
   'NEXT_PHYSICAL_GATE_IS_LINKED_SOURCE_WARD_CONTACT_IR_POLE_CANCELLATION_BEFORE_FINITE_MASTER_DECOMPOSITION'
 ],
 'next_gate':'derive the 1/epsilon pole contributions of the missing source/Ward/contact and same-parent K2-linked pieces in T_cut=D Gamma3-W[D K2], and test cancellation before extracting a finite C5 comparator coordinate'
}
assert result['classification'].startswith('PASS_DETECTED')
print(json.dumps(result,indent=2,sort_keys=True))
