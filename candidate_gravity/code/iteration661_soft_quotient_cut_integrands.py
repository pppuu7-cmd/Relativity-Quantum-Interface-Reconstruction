#!/usr/bin/env python3
"""Iteration 661: quotient-safe plus-TT numerator-weighted soft-family D_s integrands.

Prospective gate. Uses frozen Iter655 soft kinematics, Iter658 quotient-safe +TT
measurement, exact Iter594 K1/K2 vertices, Iter659 topology signs and Iter660
support routing.  It evaluates at fixed epsilon>0 only.  The q3 bubble is retained
as a no-cut topology, not zero-filled.  No Source/Born subtraction is performed.
"""
from __future__ import annotations
import json, math, runpy
from pathlib import Path
import numpy as np

ITERATION=661
ROOT=Path(__file__).resolve().parents[2]
MASS=0.7
M2=MASS*MASS
THRESH=4*M2
ETA=np.diag([1.,-1.,-1.,-1.])
# Prospective audit grid, fixed before any Iter661 output is observed.
SAMPLES=(2.25,3.0,4.0)
EPSILONS=(0.05,0.02)
N_MU=48
N_PHI=64

parent=runpy.run_path(str(ROOT/'analysis'/'source_full_cubic_routed_assembly_iteration594.py'))
K1=parent['K1']; K2=parent['K2']; mdot=parent['mdot']
rt2=math.sqrt(2.0)
H=np.zeros((4,4),float); H[1,1]=1.0/rt2; H[2,2]=-1.0/rt2


def q_family(s,eps):
    q1=np.array([math.sqrt(s),0.,0.,0.])
    q3=np.array([eps,0.,0.,eps])
    q2=-q1-q3
    return q1,q2,q3


def boost(v,p):
    v=np.asarray(v,float); p=np.asarray(p,float)
    v2=float(v@v)
    if v2<1e-30: return p.copy()
    g=1.0/math.sqrt(1.0-v2)
    vp=float(v@p[1:])
    out=np.empty(4,float)
    out[0]=g*(p[0]+vp)
    out[1:]=p[1:]+(((g-1.0)*vp/v2)+g*p[0])*v
    return out


def cut_pair(Q,n):
    """Return r0,r1 with r1-r0=Q and r0^2=r1^2=m^2."""
    Q=np.asarray(Q,float)
    qsq=float(mdot(Q))
    if qsq<=THRESH: raise ValueError(('below threshold',qsq))
    sig=1.0 if Q[0]>=0 else -1.0
    F=sig*Q
    M=math.sqrt(qsq); E=M/2.0; k=math.sqrt(max(0.0,E*E-M2))
    a=np.array([-E,*(k*n)],float); b=np.array([E,*(k*n)],float)
    v=F[1:]/F[0]
    a=boost(v,a); b=boost(v,b)
    if sig>0: r0,r1=a,b
    else: r0,r1=b,a
    return r0,r1


def sphere_average(fun):
    mu,w=np.polynomial.legendre.leggauss(N_MU)
    acc=None
    for m,wm in zip(mu,w):
        r=math.sqrt(max(0.0,1-m*m))
        for j in range(N_PHI):
            ph=2*math.pi*(j+0.5)/N_PHI
            n=np.array([r*math.cos(ph),r*math.sin(ph),m])
            x=np.asarray(fun(n),complex)
            acc=(np.zeros_like(x) if acc is None else acc)+wm*x/N_PHI
    return acc/2.0


def bubble(Q,h_single,h_left,h_right):
    qsq=float(mdot(Q)); beta=math.sqrt(max(0.0,1-THRESH/qsq))
    phase=beta/(16*math.pi*math.pi)
    def f(n):
        r0,r1=cut_pair(Q,n)
        num=K1(h_single,r1,r0)*K2(h_left,h_right,r0,r1)
        e=max(abs(M2-mdot(r0)),abs(M2-mdot(r1)))
        return [num,e]
    av=sphere_average(f)
    return complex(phase*av[0]),float(abs(av[1])),beta


def tri_value(q1,q2,q3,orientation,cut_label):
    # Cycles encode Iter660 denominator routing exactly.
    # A: r0=l, r1=l+q3, r2=l-q2; edges q3,q1,q2.
    # B: r0=l, r1=l+q3, r2=l-q1; edges q3,q2,q1.
    Q={'q1':q1,'q2':q2}[cut_label]
    qsq=float(mdot(Q)); beta=math.sqrt(max(0.0,1-THRESH/qsq))
    phase=beta/(16*math.pi*math.pi)
    min_abs=1e300; sign_seen=set(); max_shell=0.0
    def f(n):
        nonlocal min_abs,max_shell
        a,b=cut_pair(Q,n)
        if orientation=='A' and cut_label=='q1':
            r1,r2=a,b; r0=r1-q3; uncut=r0
        elif orientation=='A' and cut_label=='q2':
            r2,r0=a,b; r1=r0+q3; uncut=r1
        elif orientation=='B' and cut_label=='q2':
            r1,r2=a,b; r0=r1-q3; uncut=r0
        elif orientation=='B' and cut_label=='q1':
            r2,r0=a,b; r1=r0+q3; uncut=r1
        else: raise ValueError((orientation,cut_label))
        if orientation=='A':
            num=K1(H,r1,r0)*K1(H,r2,r1)*K1(H,r0,r2)
        else:
            num=K1(H,r1,r0)*K1(H,r2,r1)*K1(H,r0,r2)
        den=M2-mdot(uncut)
        min_abs=min(min_abs,abs(float(den)))
        if den>1e-12: sign_seen.add(1)
        elif den<-1e-12: sign_seen.add(-1)
        max_shell=max(max_shell,abs(M2-mdot(a)),abs(M2-mdot(b)))
        return [num/den]
    av=sphere_average(f)
    return complex(phase*av[0]),max_shell,min_abs,sorted(sign_seen),beta


def cj(z): return {'re':float(np.real(z)),'im':float(np.imag(z))}


def main():
    failures=[]; blocked=[]; rows=[]
    # Fail closed against required parent authority files.
    for p in [
      ROOT/'candidate_gravity/results/iteration655_soft_tcut_kinematic_contract.json',
      ROOT/'candidate_gravity/results/iteration658_null_quotient_plus_tt_measurement.json',
      ROOT/'candidate_gravity/results/iteration659_closed_sk_soft_gamma3_topology_census.json',
      ROOT/'candidate_gravity/results/iteration660_soft_family_routing_threshold_landau.json']:
        if not p.exists(): failures.append(f'missing authority file {p.relative_to(ROOT)}')
    if failures:
        result={'iteration':ITERATION,'scientific_gate_pass':False,'failures':failures,'MODEL_READINESS':'24%'}
    else:
      d658=json.loads((ROOT/'candidate_gravity/results/iteration658_null_quotient_plus_tt_measurement.json').read_text())
      if d658.get('scientific_gate_pass') is not True: failures.append('Iter658 quotient authority not PASS')
      for s in SAMPLES:
       for eps in EPSILONS:
        q1,q2,q3=q_family(s,eps); q2sq=float(mdot(q2))
        if q2sq<=THRESH: failures.append(f'prospective point below q2 threshold s={s},eps={eps}') ; continue
        b1,e1,beta1=bubble(q1,H,H,H)
        b2,e2,beta2=bubble(q2,H,H,H)
        tris={}
        for ori in ('A','B'):
         for lab in ('q1','q2'):
          v,es,md,sg,beta=tri_value(q1,q2,q3,ori,lab)
          tris[f'{ori}_{lab}']={'density':cj(v),'max_cut_shell_error':es,'min_abs_uncut_denominator':md,'uncut_denominator_signs':sg,'beta':beta}
          if es>2e-11: failures.append(f'triangle shell drift {ori}/{lab} s={s} eps={eps}: {es}')
          if len(sg)>1 or md<1e-9:
              blocked.append(f'uncut triangle pole/PV prescription required for {ori}/{lab} at s={s}, eps={eps}')
        if max(e1,e2)>2e-11: failures.append(f'bubble shell drift s={s} eps={eps}')
        rows.append({'s':s,'epsilon':eps,'q2_squared':q2sq,
          'bubble_q1_density':cj(b1),'bubble_q2_density':cj(b2),
          'bubble_q1_beta':beta1,'bubble_q2_beta':beta2,
          'triangles':tris})
      gate=(not failures and not blocked)
      classification=('PASS_ITER661_QUOTIENT_SAFE_PLUS_TT_NUMERATOR_WEIGHTED_DS_INTEGRANDS_FIXED_EPS__NON_RESIDUAL' if gate else
        'BLOCKED_ITER661_TRIANGLE_UNCUT_POLE_CAUSAL_PRESCRIPTION_REQUIRED__BUBBLE_INTEGRANDS_RETAINED__NON_RESIDUAL' if not failures else
        'FAIL_ITER661_SOFT_CUT_INTEGRAND_CONSTRUCTION')
      result={
       'iteration':ITERATION,'date':'2026-09-09','MODEL_READINESS':'24%',
       'classification':classification,'scientific_gate_pass':gate,'failures':failures,'blocked':sorted(set(blocked)),
       'contract':{
        'soft_kinematics':'MSSC001-CLOSED-SK-SOFT-TCUT-KIN-V1',
        'measurement':'Iter658 quotient-safe plus-TT; same fixed e_plus inserted on all three external legs',
        'vertices':'exact Iter594 K1/K2',
        'parent_normalization':'Iter653 common +i/2 retained as parent authority; reported densities are the cut-measure numerator factors prior to multiplying the common parent i/2',
        'topology_signs':'Iter659: K1K2 coefficient -1; K1^3 coefficient +1',
        'Ds':'Disc_s/(2*pi*i), evaluated at fixed epsilon>0 before epsilon->0+',
        'two_body_cut_measure':'beta/(16*pi^2) times sphere-averaged exact numerator'
       },
       'support':{'q1_bubble':'ordinary cut','q2_bubble':'ordinary cut','q3_bubble':'NO_MASSIVE_ORDINARY_CUT_TOPOLOGY_RETAINED_NOT_ZERO_FILLED','triangles':'q1 and q2 two-line hard-cut branches retained'},
       'samples':rows,
       'candidate_values_used':False,'zero_fill':False,'source_born_subtraction':'NOT_PERFORMED','native_soft_Tcut':'NOT_YET_FORMED',
       'ANSATZ_003':'FORBIDDEN','Fisher_resources':'FORBIDDEN',
       'next_gate':('Bind the retarded/CTP prescription for any uncut triangle denominator encountered on the fixed-epsilon two-line cut, from same-parent Iter630/653 authority, then consume the retained Iter661 bubble/triangle integrands without fitting.' if blocked else 'Take the prescribed epsilon-leading coefficient of the raw-valid fixed-epsilon quotient-safe D_s integrands on compact domains away from threshold, then construct the matched W[D_s K2] term before any Source/Born subtraction.')
      }
    out=ROOT/'candidate_gravity/results/iteration661_soft_quotient_cut_integrands.json'
    out.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps(result,indent=2,sort_keys=True))
    if failures: raise SystemExit(2)

if __name__=='__main__': main()
