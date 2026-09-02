#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 287.

Reduce the complete actual-oracle degree<=4 bubble-a/b numerators of Iteration
285 against 1/[(l^2)^2((l+q)^2)] and extract the coefficient of log_R(-q^2)
in the scalar orbit trace, normalized by i*pi^(D/2).

The reduction uses Feynman parameters and D=4-2eps isotropic tensor moments.
Only the 1/eps residue is required because (-q^2)^(-eps)=1-eps log(-q^2)+... .
The normalized discontinuity coefficient is therefore minus that residue.
"""
import importlib.util, itertools, json, math
from pathlib import Path
import numpy as np

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('i285',HERE/'iteration285_actual_numerator_basis_audit.py')
i285=importlib.util.module_from_spec(spec); spec.loader.exec_module(i285)
ETA=i285.ETA; MON4=i285.MON4


def fit_coeffs(fam,q,seed):
    rng=np.random.default_rng(seed)
    tr=rng.uniform(-1.15,1.15,(110,4))
    ho=rng.uniform(-1.25,1.25,(36,4))
    X=np.array([i285.mon(MON4,l) for l in tr])
    H=np.array([i285.mon(MON4,l) for l in ho])
    y=np.array([i285.bubble_trace(fam,q,l) for l in tr])
    z=np.array([i285.bubble_trace(fam,q,l) for l in ho])
    c=np.linalg.lstsq(X,y,rcond=None)[0]
    r=H@c-z
    return c,{
      'rank':int(np.linalg.matrix_rank(X)), 'basis_size':len(MON4),
      'condition_number':float(np.linalg.cond(X)),
      'heldout_max_abs':float(np.max(np.abs(r))),
      'heldout_rms':float(np.sqrt(np.mean(r*r))),
      'heldout_relative_max':float(np.max(np.abs(r))/max(np.max(np.abs(z)),1e-30)),
    }


def angular(indices):
    if len(indices)==0: return 1.0
    if len(indices)==2:
        return float(ETA[indices[0],indices[1]])
    if len(indices)==4:
        i,j,k,l=indices
        return float(ETA[i,j]*ETA[k,l]+ETA[i,k]*ETA[j,l]+ETA[i,l]*ETA[j,k])
    return 0.0


def monomial_disc(exps,q):
    """Coefficient of log_R(-q^2), equivalently normalized D_q for one monomial."""
    q=np.asarray(q,float); q2=float(q@ETA@q)
    out=0.0
    for r in itertools.product(*[range(e+1) for e in exps]):
        R=sum(r)
        if R%2 or R>4: continue
        P=sum(exps)-R
        comb=float(np.prod([math.comb(e,rr) for e,rr in zip(exps,r)]))
        shift=comb*float(np.prod([(-q[i])**(exps[i]-r[i]) for i in range(4)]))
        indices=[]
        for i,rr in enumerate(r): indices += [i]*rr
        ang=angular(indices)
        if ang==0.0: continue
        if R==0:
            # Endpoint pole exists only for the scalar numerator P=0.
            if P==0: out += shift*ang/q2
        elif R==2:
            # -Res[2*C1*Beta(2-eps,1+P-eps)/D]
            out += shift*ang*(-1.0/(2.0*(P+1)*(P+2)))
        elif R==4:
            # -Res[2*C2*Beta(3-eps,2+P-eps)/(D(D+2))]
            out += shift*ang*(q2/(2.0*(P+2)*(P+3)*(P+4)))
    return out


def reduce_coeffs(c,q):
    pieces=np.array([monomial_disc(e,q) for e in MON4])
    return float(c@pieces),pieces


def transformed_reflection_coeffs(c):
    # N'(l)=N(-l): total-degree parity on fixed-coordinate monomials.
    return np.array([cc*((-1)**sum(e)) for cc,e in zip(c,MON4)])


def poly_coeff_for_l2():
    c=np.zeros(len(MON4))
    lookup={e:i for i,e in enumerate(MON4)}
    for mu in range(4):
        e=[0]*4; e[mu]=2
        c[lookup[tuple(e)]]=ETA[mu,mu]
    return c


def poly_coeff_for_l2sq():
    c=np.zeros(len(MON4)); lookup={e:i for i,e in enumerate(MON4)}
    for mu in range(4):
      for nu in range(4):
        e=[0]*4; e[mu]+=2; e[nu]+=2
        c[lookup[tuple(e)]] += ETA[mu,mu]*ETA[nu,nu]
    return c


def audit_one(fam,q,seed):
    c,fit=fit_coeffs(fam,q,seed)
    disc,_=reduce_coeffs(c,q)
    cref=transformed_reflection_coeffs(c)
    disc_ref,_=reduce_coeffs(cref,-np.asarray(q))
    return {
      'fit':fit,
      'q':np.asarray(q,float).tolist(),
      'q2':float(np.asarray(q)@ETA@np.asarray(q)),
      'normalized_log_discontinuity_coefficient':disc,
      'loop_reflected_coefficient':disc_ref,
      'loop_reflection_abs_residual':abs(disc-disc_ref),
      'coefficient_l2_norm':float(np.linalg.norm(c)),
      'largest_abs_polynomial_coefficient':float(np.max(np.abs(c))),
    }

# Algebraic DR/scaleless sanity checks independent of the oracle fit.
qa=i285.KA
l2_disc,_=reduce_coeffs(poly_coeff_for_l2(),qa)
l2sq_disc,_=reduce_coeffs(poly_coeff_for_l2sq(),qa)
scalar=np.zeros(len(MON4)); scalar[MON4.index((0,0,0,0))]=1.0
scalar_disc,_=reduce_coeffs(scalar,qa)

A=audit_one('bubble_a',i285.KA,28701)
B=audit_one('bubble_b',i285.KB,28702)

result={
 'iteration':287,
 'model_readiness_percent':24,
 'normalization':'coefficient of log_R(-q^2) after dividing loop integral by i*pi^(D/2); D_q log_R(-q^2)=1',
 'sanity_checks':{
   'scalar_expected_1_over_q2':scalar_disc,
   'scalar_target_1_over_q2':1.0/float(qa@ETA@qa),
   'l2_expected_minus_one':l2_disc,
   'l2_squared_scaleless_expected_zero':l2sq_disc,
 },
 'bubble_a':A,
 'bubble_b':B,
 'classification':'PASS_COMPLETE_70_MONOMIAL_BUBBLE_TENSOR_MOMENT_REDUCTION_NONZERO' if (
    A['fit']['heldout_relative_max']<1e-6 and B['fit']['heldout_relative_max']<1e-6 and
    A['loop_reflection_abs_residual']<1e-9 and B['loop_reflection_abs_residual']<1e-9 and
    abs(A['normalized_log_discontinuity_coefficient'])>1e-8 and abs(B['normalized_log_discontinuity_coefficient'])>1e-8
 ) else 'BLOCKED_BUBBLE_REDUCTION_AUDIT',
 'candidate_residual':False,
 'guardrail':'THESE_ARE_SAME_PARENT_SCALAR_ORBIT_TRACE_BUBBLE CUT COEFFICIENTS, NOT YET SOURCE/WARD/CONTACT-COMPLETED T_cut',
 'next_gate':288,
}
assert abs(scalar_disc-1.0/float(qa@ETA@qa))<1e-12
assert abs(l2_disc+1.0)<1e-12
assert abs(l2sq_disc)<1e-12
assert A['fit']['rank']==70 and B['fit']['rank']==70
print(json.dumps(result,indent=2,sort_keys=True))
