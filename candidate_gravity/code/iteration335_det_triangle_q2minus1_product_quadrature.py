#!/usr/bin/env python3
"""RQIR Iteration 335: independent product-quadrature resolution of the sole blocked q^2=-1 triangle channel.

This gate changes no parent dynamics, external fixture, routing, physical numerator,
cut surface, causal prescription, or scientific threshold. It replaces the
Iteration-334 Fibonacci-sphere integration by an independent tensor-product rule:
Gauss-Legendre in z=cos(theta) and periodic trapezoidal azimuth integration,
including a phase-shifted azimuth cross-check. Already-certified channels are not
recomputed. Unsupported remains BLOCKED.
"""
from __future__ import annotations
import contextlib, io, json, math
from pathlib import Path
import numpy as np

ROOT=Path(__file__).resolve().parent
src=(ROOT/'iteration333_det_direct_timelike_discontinuity_family_reduction.py').read_text()
prefix=src.split('bubble_results=[]',1)
if len(prefix)!=2:
    raise RuntimeError('Iteration-333 boundary changed; refuse implicit rebase')
ns={'__name__':'rqir_iteration335_parent','__file__':str(ROOT/'iteration333_det_direct_timelike_discontinuity_family_reduction.py')}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(prefix[0],'iteration335_parent','exec'),ns,ns)

triangle_groups=ns['triangle_groups']; family_num=ns['family_num']; rest_basis=ns['rest_basis']; mdot=ns['mdot']; denom=ns['denom']
if len(triangle_groups)!=1:
    raise RuntimeError(f'expected one triangle family, got {len(triangle_groups)}')
rep,group=next(iter(triangle_groups.items()))
shifts=[np.asarray(s,float)/100.0 for s in rep]

pair=None
for i,j in ((0,1),(0,2),(1,2)):
    q2=mdot(shifts[j]-shifts[i],shifts[j]-shifts[i])
    if abs(q2+1.0)<1e-12:
        pair=(i,j,({0,1,2}-{i,j}).pop(),q2); break
if pair is None:
    raise RuntimeError('q^2=-1 triangle channel not found')
i,j,kidx,q2=pair
Q=shifts[j]-shifts[i]; M,u,basis=rest_basis(Q); sk=shifts[kidx]

R=sk-shifts[i]; A=R-0.5*Q; Aperp=A+mdot(A,u)*u
const=mdot(A,A)+M*M/4; amp=M*math.sqrt(max(0.0,mdot(Aperp,Aperp)))
dmin=const-amp; dmax=const+amp
third_bounded=(dmin>2e-9 or dmax<-2e-9)

def cut_k(nvec):
    l=-0.5*Q+0.5*M*nvec
    return l-shifts[i]

def product_mean(nz,nphi,phase=0.0):
    z_nodes,z_weights=np.polynomial.legendre.leggauss(nz)
    total=0j; max_sample=0.0; shell=0.0; minthird=float('inf')
    # Sphere mean = (1/4pi) int_{-1}^1 dz int_0^{2pi} dphi f.
    for z,w in zip(z_nodes,z_weights):
        rho=math.sqrt(max(0.0,1.0-float(z)*float(z)))
        ring=0j
        for m in range(nphi):
            phi=2.0*math.pi*(m+phase)/nphi
            xyz=np.array([rho*math.cos(phi),rho*math.sin(phi),float(z)])
            nv=sum((xyz[a]*basis[a] for a in range(3)),np.zeros(4))
            kk=cut_k(nv)
            d0=abs(denom(kk+shifts[i])); d1=abs(denom(kk+shifts[j])); shell=max(shell,d0,d1)
            third=denom(kk+sk); minthird=min(minthird,abs(third))
            val=family_num(group,kk)/third
            ring+=val; max_sample=max(max_sample,float(abs(val)))
        total += float(w)*(ring/nphi)
    mean=0.5*total
    return mean,max_sample,shell,minthird

configs=((24,48,0.0),(36,72,0.0),(48,96,0.0),(48,96,0.37123456789),(64,128,0.0),(64,128,0.37123456789))
runs=[]
for nz,nphi,phase in configs:
    z,mx,shell,minthird=product_mean(nz,nphi,phase)
    runs.append({'nz':nz,'nphi':nphi,'phase':phase,'mean':[float(z.real),float(z.imag)],'max_abs_sample':mx,'max_cut_shell_error':shell,'min_abs_third_denominator':minthird})

vals=[complex(*r['mean']) for r in runs]
scale=max(r['max_abs_sample'] for r in runs)
# Require both order refinement and independent phase stability at the highest order.
conv=max(abs(vals[4]-vals[2]),abs(vals[5]-vals[4]))/max(scale,1e-30)
nonzero_ratio=abs(0.5*(vals[4]+vals[5]))/max(scale,1e-30)
THRESH=2e-5; NONZERO_RATIO=2e-6
resolved=bool(third_bounded and max(r['max_cut_shell_error'] for r in runs)<1e-10 and conv<THRESH and nonzero_ratio>NONZERO_RATIO)
status='NONZERO_TWO_PARTICLE_CHANNEL_DISCONTINUITY_CERTIFICATE_PRODUCT_QUADRATURE' if resolved else 'BLOCKED_PRODUCT_QUADRATURE_CONVERGENCE'
result={
 'iteration':335,
 'model_readiness_percent':24,
 'scientific_gate_pass':resolved,
 'classification':('PASS_TRIANGLE_Q2_MINUS1_PRODUCT_QUADRATURE_DISCONTINUITY_RESOLUTION' if resolved else 'BLOCKED_TRIANGLE_Q2_MINUS1_PRODUCT_QUADRATURE_DISCONTINUITY_RESOLUTION'),
 'candidate_residual':False,
 'scope':{
   'inherits':'Iteration-333 stripped physical numerator and exact Iteration-332 timelike fixture',
   'q2':q2,'cut_pair':[i,j],'uncut_index':kidx,
   'quadrature':'Gauss-Legendre in z times periodic azimuth trapezoid; independent phase-shift cross-check',
   'configs':[[a,b,c] for a,b,c in configs],
   'threshold_unchanged_from_iteration333':THRESH
 },
 'third_denominator_exact_range':[float(dmin),float(dmax)],
 'third_propagator_bounded_away_from_zero':bool(third_bounded),
 'runs':runs,
 'convergence_to_sample_ratio':float(conv),
 'central_to_sample_ratio':float(nonzero_ratio),
 'status':status,
 'physical_status':{
   'all_three_bubbles':'NONZERO_FROM_ITERATION333',
   'triangle_other_two_channels':'NONZERO_FROM_ITERATION333',
   'triangle_q2_minus1':status,
   'full_finite_DR_remainder':'BLOCKED_BY_ITERATION297',
   'source_born_subtraction':'FORBIDDEN_UNTIL_NORMALIZED_DETERMINANT_CUT_AND_MATCHED_ORIGIN_CLASSIFICATION',
   'comparator_subtracted_residual':'ABSENT'
 },
 'guardrails':['NO_THRESHOLD_WEAKENING','NO_NUMERATOR_OR_PARENT_CHANGE','NO_RECOMPUTE_CERTIFIED_CHANNELS','NO_PV_REQUIRED_THIRD_PROPAGATOR_BOUNDED','NO_ANSATZ003','NO_FISHER_RESOURCES'],
 'next_gate':('freeze complete channel-resolved determinant absorptive vector and assemble normalized determinant e=0,c<=3 cut with exact phase-space normalization/provenance' if resolved else 'preserve BLOCKED; derive symbolic/analytic angular reduction without weakening threshold')
}
print(json.dumps(result,indent=2,sort_keys=True))
if not resolved:
    raise SystemExit(2)
