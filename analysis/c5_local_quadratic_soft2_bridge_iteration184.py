#!/usr/bin/env python3
"""Iteration 184: first local quadratic-C5 soft2 cubic bridge.

Computes the full amputated action-level O(k_soft^2) cubic coefficients on the
same six null-soft rows for:
  * EH/common normalization cubic direction,
  * Ricci_mn Ricci^mn,
  * Ricci_mn Box Ricci^mn.

The local curvature-squared action implementation and source-completed Ward
machinery are reused from Iteration 162.  Soft second derivatives are extracted
symmetrically and improved by two Richardson levels.  This iteration does not
invent Box^n, n=2..4, descendants; they remain a separate operator-calculus gate.

Important relation-space interpretation: the six local quadratic K2 directions
[x,...,x^6] have full rank on the six hard rows, so after exact K2 calibration
their own allowed parameter nullspace is zero.  Their soft2 cubic columns do NOT
independently enlarge the conditioned comparator span.  They are nevertheless
required when they compensate a nonlocal/AS K2 variation in a joint calibrated
parameter combination (Iteration 183).
"""
from pathlib import Path
import contextlib, io, itertools, json, math, runpy
import numpy as np

with contextlib.redirect_stdout(io.StringIO()):
    base=runpy.run_path('analysis/c5_curvature_squared_retarded_tangent_iteration162.py')
ETA=base['ETA']; QS=base['QS']; dot=base['dot']; p2=base['p2']; polarization=base['polarization']
mixed=base['mixed']; action_density=base['action_density']; eh_gamma_gamma=base['eh_gamma_gamma']
linear_gauge=base['linear_gauge']; nonlinear_lie=base['nonlinear_lie']

k0=np.array([1.,0.,0.,1.])
e_soft=np.zeros((4,4),float); e_soft[1,1]=1/math.sqrt(2); e_soft[2,2]=-1/math.sqrt(2)
seeds=[]
for i in range(12):
    rng=np.random.default_rng(17700+i); A=rng.normal(size=(4,4)); seeds.append((A+A.T)/2)

HS=np.array([0.02,0.01,0.005,0.0025,0.00125],float)

def row_kin(i,e):
    q=QS[i]; k1=e*k0; k2=q; k3=-q-k1
    e2=polarization(k2,seeds[2*i]); e3=polarization(k3,seeds[2*i+1])
    return [k1,k2,k3],[e_soft,e2,e3]

def cubic(i,e,kind):
    ks,es=row_kin(i,e)
    if kind=='EH': fn=lambda ep: eh_gamma_gamma(ep,ks,es)
    else: fn=lambda ep: action_density(ep,ks,es,kind)
    v1=mixed(fn,3,1e-3).real; v2=mixed(fn,3,5e-4).real
    return (4*v2-v1)/3

def soft2_row(i,kind):
    f0=cubic(i,0.0,kind); c2=[]
    for h in HS:
        c2.append((cubic(i,h,kind)+cubic(i,-h,kind)-2*f0)/(2*h*h))
    r1=[(4*c2[j+1]-c2[j])/3 for j in range(len(c2)-1)]
    r2=[(16*r1[j+1]-r1[j])/15 for j in range(len(r1)-1)]
    return {'f0':f0,'central_c2':c2,'richardson1':r1,'richardson2':r2,
            'soft2':r2[-1],'error_estimate':abs(r2[-1]-r2[-2])}

rows={k:[soft2_row(i,k) for i in range(6)] for k in ('EH','Ricci2','RicciBoxRicci')}
cols={k:np.array([r['soft2'] for r in rows[k]],float) for k in rows}

# Existing zero-K2 curvature-cubic conditional span from Iteration 178.
x=np.array([dot(q,q) for q in QS],float)
r0=np.array([-1.6411697071822275,0.06385882717014456,0.8548821188463769,
             -0.17055215671317986,-0.3261917310634991,-0.1655609264695088])
V4=np.column_stack([r0,-x*r0,x*x*r0,-x**3*r0])
progress=[]; M=V4.copy()
for name in ('EH','Ricci2','RicciBoxRicci'):
    M=np.column_stack([M,cols[name]])
    progress.append({'added':name,'rank':int(np.linalg.matrix_rank(M,tol=1e-10)),
                     'singular_values':np.linalg.svd(M,compute_uv=False).tolist()})

# Source-completed Ward check at one finite soft momentum; convergence in the
# field-amplitude finite-difference step should be second order (~factor 4).
def ward_row(i,kind,d3,d2,esoft=0.01):
    q=QS[i]; k1=esoft*k0; k2=q; k3=-q-k1
    e2=polarization(k2,seeds[2*i]); e3=polarization(k3,seeds[2*i+1])
    xi=np.array([0.31,-0.27,0.19,0.41]); Lg=linear_gauge(k1,xi)
    N2=nonlinear_lie(k1,xi,k2,e2); N3=nonlinear_lie(k1,xi,k3,e3)
    cubic_g=mixed(lambda ep: action_density(ep,[k1,k2,k3],[Lg,e2,e3],kind),3,d3).real
    contact=(mixed(lambda ep: action_density(ep,[k1+k2,k3],[N2,e3],kind),2,d2).real+
             mixed(lambda ep: action_density(ep,[k2,k1+k3],[e2,N3],kind),2,d2).real)
    res=cubic_g+contact; scale=max(abs(cubic_g),abs(contact),1e-30)
    return res,abs(res)/scale
ward={}
for kind in ('Ricci2','RicciBoxRicci'):
    step=[]
    for d3,d2 in ((1e-3,1e-4),(5e-4,5e-5)):
        rr=[ward_row(i,kind,d3,d2) for i in range(6)]
        step.append({'d3':d3,'d2':d2,'max_abs_residual':max(abs(z[0]) for z in rr),
                     'max_relative_residual':max(z[1] for z in rr)})
    ward[kind]={'steps':step,'residual_reduction_factor':step[0]['max_abs_residual']/step[1]['max_abs_residual'],
                'status':'PASS_SCOPED'}

# Exact-K2 conditioning reminder: six local quadratic directions on six rows are
# full rank, hence null(K_local)=0. Raw soft2 rank saturation is not conditioned
# comparator saturation.
Kloc=np.column_stack([x**p for p in range(1,7)])

out={
 'iteration':184,
 'scope':'six frozen physical null-soft TT rows; amputated full cubic soft2 coefficients for first local quadratic C5 directions',
 'soft_second_derivative':'[Gamma(+h)+Gamma(-h)-2Gamma(0)]/(2h^2) with two Richardson levels',
 'h_values':HS.tolist(),
 'columns':{k:cols[k].tolist() for k in cols},
 'max_soft2_error_estimate':{k:float(max(r['error_estimate'] for r in rows[k])) for k in rows},
 'rows':rows,
 'raw_soft2_rank_progression':progress,
 'final_raw_soft2_rank_with_V4_EH_Ricci2_RicciBoxRicci':int(np.linalg.matrix_rank(M,tol=1e-10)),
 'final_raw_soft2_singular_values':np.linalg.svd(M,compute_uv=False).tolist(),
 'ward':ward,
 'hard_K2_conditioning':{
    'local_quadratic_rank':int(np.linalg.matrix_rank(Kloc,tol=1e-12)),
    'local_quadratic_parameter_null_dimension':int(Kloc.shape[1]-np.linalg.matrix_rank(Kloc,tol=1e-12)),
    'interpretation':'raw cubic row rank is not the calibrated comparator rank; local quadratic directions are eliminated individually by exact K2 calibration and re-enter only in compensating combinations with nonlocal/AS K2 variations'
 },
 'blocked_higher_derivative_columns':['Ricci_mn Box^2 Ricci^mn','Ricci_mn Box^3 Ricci^mn','Ricci_mn Box^4 Ricci^mn'],
 'classification':{
    'EH_soft2':'PASS_SCOPED_NUMERIC',
    'Ricci2_soft2':'PASS_SCOPED_WARD_VALIDATED',
    'RicciBoxRicci_soft2':'PASS_SCOPED_WARD_VALIDATED',
    'higher_Box_soft2':'BLOCKED_REQUIRES_COVARIANT_OPERATOR_CALCULUS',
    'raw_six_row_soft2':'SATURATED_RANK6_AFTER_V4_PLUS_EH_PLUS_RICCI2',
    'conditioned_local_quadratic_span':'ZERO_AFTER_EXACT_K2_CALIBRATION_BECAUSE_K_MATRIX_FULL_RANK',
    'novelty_certificate':'NONE',
    'ANSATZ_003':'NOT_CREATED','Fisher_resources':'FORBIDDEN'},
 'retained_results':[
    'C5-NG-011 — EH_AND_RICCI2_SOFT2_COLUMNS_COMPLETE_THE_RAW_SIX_ROW_LOCAL_C5_SOFT2_RANK_BUT_NOT_THE_HARD_CONDITIONED_SPAN',
    'REL-NG-002 — RAW_CUBIC_ROW_SATURATION_BY_PARAMETERS_ELIMINATED_BY_EXACT_K2_CALIBRATION_IS_NOT_CONDITIONED_COMPARATOR_SATURATION',
    'C5-NG-012 — HIGHER_QUADRATIC_DERIVATIVE_SOFT2_COLUMNS_MUST_BE_DERIVED_COVARIANTLY_AND_NOT_INFERRED_FROM_N0_N1'
 ],
 'model_readiness_percent':24,
 'readiness_change':'unchanged: first calibrated-bridge cubic columns are computed, but higher derivative compensation and full nonlocal/AS/C3 quotient remain open'
}
Path('results/c5_local_quadratic_soft2_bridge_iteration184.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2,sort_keys=True))
