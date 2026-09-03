#!/usr/bin/env python3
"""RQIR Iteration 334: resolve the sole Iteration-333 q^2=-1 triangle channel.

Iteration 333 certified all three bubble discontinuities NONZERO and the signed-
affine triangle family NONZERO through two channels, while the q^2=-1 channel
remained BLOCKED solely because two 26-point spherical cubatures disagreed above
the frozen 2e-5 normalized convergence threshold.  This gate changes no parent,
fixture, route, numerator, causal prescription, or threshold.  It only replaces
that under-resolved angular integration by deterministic high-resolution
Fibonacci-sphere sequences at N=96,192,384 and a phase-shifted N=384 design.

The third propagator was already proven bounded away from zero in this channel,
so no PV/i0 ambiguity is introduced here.  This remains a family/channel
absorptive certificate, not a finite DR remainder or comparator residual.
"""
from __future__ import annotations
import contextlib, io, json, math
from pathlib import Path
import numpy as np

ROOT=Path(__file__).resolve().parent
src=(ROOT/'iteration333_det_direct_timelike_discontinuity_family_reduction.py').read_text()
prefix=src.split('bubble_results=[]',1)
if len(prefix)!=2: raise RuntimeError('Iteration-333 boundary changed; refuse implicit rebase')
ns={'__name__':'rqir_iteration334_parent','__file__':str(ROOT/'iteration333_det_direct_timelike_discontinuity_family_reduction.py')}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(prefix[0],'iteration334_parent','exec'),ns,ns)

triangle_groups=ns['triangle_groups']; family_num=ns['family_num']; rest_basis=ns['rest_basis']; mdot=ns['mdot']; denom=ns['denom']
if len(triangle_groups)!=1: raise RuntimeError(f'expected one triangle family, got {len(triangle_groups)}')
rep,group=next(iter(triangle_groups.items()))
shifts=[np.asarray(s,float)/100.0 for s in rep]

# Find exactly the q^2=-1 two-line channel from Iteration 333.
pair=None
for i,j in ((0,1),(0,2),(1,2)):
    q2=mdot(shifts[j]-shifts[i],shifts[j]-shifts[i])
    if abs(q2+1.0)<1e-12:
        pair=(i,j,({0,1,2}-{i,j}).pop(),q2); break
if pair is None: raise RuntimeError('q^2=-1 triangle channel not found')
i,j,kidx,q2=pair
Q=shifts[j]-shifts[i]; M,u,basis=rest_basis(Q); sk=shifts[kidx]

# Exact affine range of the uncut denominator on this cut sphere.
R=sk-shifts[i]; A=R-0.5*Q; Aperp=A+mdot(A,u)*u
const=mdot(A,A)+M*M/4; amp=M*math.sqrt(max(0.0,mdot(Aperp,Aperp)))
dmin=const-amp; dmax=const+amp
third_bounded=(dmin>2e-9 or dmax<-2e-9)


def fibonacci_design(n,phase=0.0):
    ga=math.pi*(3.0-math.sqrt(5.0)); out=[]
    for r in range(n):
        z=1.0-2.0*(r+0.5)/n; rho=math.sqrt(max(0.0,1.0-z*z)); phi=ga*(r+phase)
        xyz=np.array([rho*math.cos(phi),rho*math.sin(phi),z])
        v=sum((xyz[a]*basis[a] for a in range(3)),np.zeros(4))
        out.append(v)
    return out


def cut_k(nvec):
    l=-0.5*Q+0.5*M*nvec
    return l-shifts[i]


def mean_for(n,phase):
    z=0j; mx=0.0; shell=0.0; minthird=float('inf')
    for nv in fibonacci_design(n,phase):
        kk=cut_k(nv)
        d0=abs(denom(kk+shifts[i])); d1=abs(denom(kk+shifts[j])); shell=max(shell,d0,d1)
        third=denom(kk+sk); minthird=min(minthird,abs(third))
        val=family_num(group,kk)/third
        z+=val; mx=max(mx,float(abs(val)))
    return z/n,mx,shell,minthird

runs=[]
for n,phase in ((96,0.0),(192,0.0),(384,0.0),(384,0.3819660112501051)):
    z,mx,shell,minthird=mean_for(n,phase)
    runs.append({'n':n,'phase':phase,'mean':[float(z.real),float(z.imag)],'max_abs_sample':mx,'max_cut_shell_error':shell,'min_abs_third_denominator':minthird})

z96=complex(*runs[0]['mean']); z192=complex(*runs[1]['mean']); z384=complex(*runs[2]['mean']); z384p=complex(*runs[3]['mean'])
scale=max(r['max_abs_sample'] for r in runs)
conv=max(abs(z384-z192),abs(z384p-z384))/max(scale,1e-30)
nonzero_ratio=abs(0.5*(z384+z384p))/max(scale,1e-30)
THRESH=2e-5; NONZERO_RATIO=2e-6
resolved=bool(third_bounded and max(r['max_cut_shell_error'] for r in runs)<1e-10 and conv<THRESH and nonzero_ratio>NONZERO_RATIO)
status='NONZERO_TWO_PARTICLE_CHANNEL_DISCONTINUITY_CERTIFICATE_HIGHRES' if resolved else 'BLOCKED_HIGHRES_CUBATURE_CONVERGENCE'
result={
 'iteration':334,'model_readiness_percent':24,'scientific_gate_pass':resolved,
 'classification':('PASS_TRIANGLE_Q2_MINUS1_HIGHRES_DISCONTINUITY_RESOLUTION' if resolved else 'BLOCKED_TRIANGLE_Q2_MINUS1_HIGHRES_DISCONTINUITY_RESOLUTION'),
 'candidate_residual':False,
 'scope':{'inherits':'Iteration-333 stripped physical numerator and exact Iteration-332 timelike fixture','q2':q2,'cut_pair':[i,j],'uncut_index':kidx,'quadrature':'deterministic Fibonacci sphere N=96,192,384 plus phase-shifted N=384','threshold_unchanged_from_iteration333':THRESH},
 'third_denominator_exact_range':[float(dmin),float(dmax)],'third_propagator_bounded_away_from_zero':third_bounded,
 'runs':runs,'convergence_to_sample_ratio':float(conv),'central_to_sample_ratio':float(nonzero_ratio),'status':status,
 'physical_status':{'all_three_bubbles':'NONZERO_FROM_ITERATION333','triangle_other_two_channels':'NONZERO_FROM_ITERATION333','triangle_q2_minus1':status,
                    'full_finite_DR_remainder':'BLOCKED_BY_ITERATION297','source_born_subtraction':'FORBIDDEN_UNTIL_NORMALIZED_DETERMINANT_CUT_AND_MATCHED_ORIGIN_CLASSIFICATION','comparator_subtracted_residual':'ABSENT'},
 'guardrails':['NO_THRESHOLD_WEAKENING','NO_NUMERATOR_OR_PARENT_CHANGE','NO_PV_REQUIRED_THIRD_PROPAGATOR_BOUNDED','NO_ANSATZ003','NO_FISHER_RESOURCES'],
 'next_gate':('freeze complete channel-resolved direct-timelike determinant absorptive vector and assemble normalized determinant e=0,c<=3 cut with exact phase-space normalization/provenance' if resolved else 'preserve BLOCKED; derive analytic angular integral or independent higher-order cubature without weakening threshold')
}
print(json.dumps(result,indent=2,sort_keys=True))
if not resolved: raise SystemExit(2)
