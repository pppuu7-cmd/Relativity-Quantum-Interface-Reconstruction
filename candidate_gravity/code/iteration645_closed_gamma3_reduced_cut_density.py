#!/usr/bin/env python3
"""Iteration 645: numerator-weighted ordinary s-channel cut density, fail-closed.

Uses only frozen authorities through Iter644.  It computes the *reduced* two-body
spectral numerator on the closed-Gamma3 family, with the exact Iter594 MSSC001
K1/K2 machinery and frozen Tensor-Transport-V1.  It deliberately does not guess
an overall closed-CTP effective-action phase/loop-measure normalization.  If that
absolute normalization is not supplied by an explicit committed authority, the
scientific classification remains BLOCKED while the reduced densities are kept
as a reproducible intermediate result.
"""
from __future__ import annotations
import contextlib, io, json, math, runpy
from pathlib import Path
import numpy as np

ITERATION=645
ROOT=Path(__file__).resolve().parents[2]
MASS=0.7
T0=0.14
U0=0.34
THRESH=4*MASS*MASS
ETA=np.diag([1.,-1.,-1.,-1.])
SAMPLES=(1.96,2.0,2.25,2.5,3.0,4.0)
N_MU=96
N_PHI=128

parent=runpy.run_path(str(ROOT/'analysis'/'source_full_cubic_routed_assembly_iteration594.py'))
K1=parent['K1']; K2=parent['K2']; mdot=parent['mdot']; G=parent['G']

# Exact Iter368/588 anchor tensors, inherited rather than retyped.
p368=ROOT/'candidate_gravity'/'code'/'iteration368_tru1sq_timelike_full_prepruning_routing.py'
src=p368.read_text(); marker='# Cache expensive same-parent blocks by routed loop momentum.'
if src.count(marker)!=1:
    raise SystemExit('iteration368 setup boundary drift')
ns={'__name__':'iteration645_parent368_fixture','__file__':str(p368)}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(src.split(marker,1)[0],str(p368),'exec'),ns,ns)
M=ns['M']
hs={x:np.asarray(M[x][1],float) for x in ('s','a','b')}

# Tensor-Transport-V1: these coordinate-frame tensors are held fixed.

def q_family(s: float):
    rt=math.sqrt(s)
    Ea=(U0-s-T0)/(2*rt)
    k2=Ea*Ea-T0
    if k2 < -5e-15:
        raise ValueError(('left real branch',s,k2))
    k=math.sqrt(max(0.0,k2))
    e1=np.array([0.,1/math.sqrt(2),1/math.sqrt(2),0.])
    qs=np.array([rt,0.,0.,0.])
    qa=np.array([Ea,0.,0.,0.])+k*e1
    qb=-qs-qa
    return {'s':qs,'a':qa,'b':qb}


def sphere_average(fun):
    mu,w=np.polynomial.legendre.leggauss(N_MU)
    acc=0.0
    for m,wm in zip(mu,w):
        r=math.sqrt(max(0.0,1-m*m))
        for j in range(N_PHI):
            ph=2*math.pi*(j+0.5)/N_PHI
            n=np.array([r*math.cos(ph),r*math.sin(ph),m])
            acc += wm*fun(n)/N_PHI
    # leggauss integrates dmu and phi average already divides by 2pi;
    # divide by 2 to obtain the full-sphere average 1/(4pi) int dOmega.
    return acc/2.0


def row_at_s(s: float):
    qs=q_family(s); rt=math.sqrt(s); E=rt/2
    beta=math.sqrt(max(0.0,1-THRESH/s))
    kk=rt*beta/2
    # With q_s = p_plus - p_minus, both p^2=m^2 and energies have opposite sign.
    def pieces(n):
        p0=np.array([-E,*(kk*n)])
        p1=p0+qs['s']
        # ordinary s-cut on-shell checks
        e0=abs(MASS*MASS-mdot(p0)); e1=abs(MASS*MASS-mdot(p1))
        # closed bubble representative: K1_s K2_ab
        bub=K1(hs['s'],p1,p0)*K2(hs['a'],hs['b'],p0,p1)
        # two closed triangle orientations.  The uncut propagator is retained.
        p2a=p1+qs['a']
        p2b=p1+qs['b']
        dena=MASS*MASS-mdot(p2a); denb=MASS*MASS-mdot(p2b)
        tr_ab=(K1(hs['s'],p1,p0)*K1(hs['a'],p2a,p1)*K1(hs['b'],p0,p2a)/dena)
        tr_ba=(K1(hs['s'],p1,p0)*K1(hs['b'],p2b,p1)*K1(hs['a'],p0,p2b)/denb)
        return np.array([bub,tr_ab,tr_ba,e0,e1,abs(dena),abs(denb)],float)
    av=sphere_average(pieces)
    # Standard reduced Lorentz-invariant 2-body phase-space factor for D_s,
    # before the unresolved global closed-CTP effective-action phase convention.
    phase=beta/(16*math.pi*math.pi)
    return {
      's':s,'beta':beta,'phase_space_reduced_factor_beta_over_16pi2':phase,
      'angular_average':{
        'bubble_K1s_K2ab':float(av[0]),
        'triangle_sab':float(av[1]),
        'triangle_sba':float(av[2])},
      'reduced_Ds_density':{
        'bubble_K1s_K2ab':float(phase*av[0]),
        'triangle_sab':float(phase*av[1]),
        'triangle_sba':float(phase*av[2])},
      'max_cut_shell_error':float(max(av[3],av[4])),
      'minimum_sampled_abs_uncut_triangle_denominator':float(min(av[5],av[6]))
    }


def main():
    failures=[]
    rows=[row_at_s(s) for s in SAMPLES]
    for r in rows:
        if r['max_cut_shell_error']>2e-12:
            failures.append(f"cut shell drift at s={r['s']}: {r['max_cut_shell_error']}")
        if r['minimum_sampled_abs_uncut_triangle_denominator']<=1e-10 and r['s']>THRESH+1e-12:
            failures.append(f"unexpected sampled triangle uncut pole at s={r['s']}")
    # At exact threshold the phase-space density must vanish analytically.
    if abs(rows[0]['beta'])>2e-8:
        failures.append(f"threshold beta drift {rows[0]['beta']}")

    result={
      'iteration':ITERATION,'date':'2026-09-09','MODEL_READINESS':'24%',
      'classification':('BLOCKED_ITER645_ABSOLUTE_CLOSED_CTP_CUT_NORMALIZATION_NOT_YET_BOUND__REDUCED_NUMERATOR_DENSITIES_COMPUTED__NON_RESIDUAL'
                        if not failures else 'FAIL_ITER645_REDUCED_CUT_NUMERATOR_EVALUATION'),
      'scientific_gate_pass':False,
      'reduced_numerator_computation_pass':not failures,
      'failures':failures,
      'frozen_inputs':{
        'mass':MASS,'threshold':THRESH,'t0':T0,'u0':U0,
        'tensor_transport':'MSSC001-CLOSED-GAMMA3-TENSOR-TRANSPORT-V1',
        'state':'MSSC001-SCALAR-STATE-V1',
        'native_Ds':'Disc_s/(2*pi*i)'},
      'closed_trace_family_map':{
        'K3':'analytic/contact; no ordinary finite s-cut, retained and not zero-filled',
        'K1K2':{
          's_channel_representative':'K1(h_s) K2(h_a,h_b)',
          'other_singletons':'K1(h_a)K2(h_s,h_b) and K1(h_b)K2(h_s,h_a) have fixed t/u two-line channel invariants below 4m^2 and therefore no ordinary s-channel two-particle support',
          'source_13_family_provenance':'both endpoint orderings are retained as source-family provenance; closed trace uses cyclic quotient'},
        'K1cubed':{
          'closed_orientations':['s-a-b','s-b-a'],
          'source_13_family_provenance':'all six ordered source chains retained; cyclic triples map to the two closed orientations'}},
      'samples':rows,
      'normalization_status':{
        'reduced_phase_space_factor_used':'beta/(16*pi^2)',
        'absolute_closed_CTP_effective_action_phase_prefactor':'BLOCKED_NOT_ASSUMED',
        'reason':'Iter630/632 fix causal slots and G_K=2*pi*i delta(D), but this evaluator does not infer an overall closed effective-action phase/loop-measure convention from topology alone.'},
      'zero_fill':False,'candidate_values_used':False,
      'source_born_subtraction':'NOT_PERFORMED','native_Y_Tcut_projection':'NOT_PERFORMED',
      'comparator_quotient':'NOT_PERFORMED','ANSATZ_003':'FORBIDDEN','Fisher_resources':'FORBIDDEN',
      'next_gate':'Bind the single overall closed-CTP scalar-loop effective-action phase/measure normalization from explicit same-parent committed authority; then promote these reduced family densities to absolute native-D_s densities without refitting any family.'
    }
    out=ROOT/'results'/'iteration645_closed_gamma3_reduced_cut_density'
    out.mkdir(parents=True,exist_ok=True)
    (out/'result.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps(result,indent=2,sort_keys=True))
    if failures: raise SystemExit(2)

if __name__=='__main__':
    main()
