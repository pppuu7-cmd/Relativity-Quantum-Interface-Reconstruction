#!/usr/bin/env python3
"""RQIR Iteration 096 — decision value per characterization Fisher-second.

This is a deterministic Paper-III resource/decision certificate. It converts
Iteration-094 interval value-of-information into a measurement-time priority by
attaching a physical Fisher rate to the characterization of each uncertain
coordinate. Synthetic boxes/rates are regression tests only, not apparatus
forecasts.
"""
from math import sqrt, isclose

import crossover_value_of_information_iteration094 as i94


def eta_from_fisher_time(nu, t):
    """Half-width contraction for constant normalized Fisher rate nu=R/I0."""
    assert nu >= 0 and t >= 0
    return 1.0 / sqrt(1.0 + nu*t)


def time_for_contraction(eta, nu):
    """Exact time to reach h/h0=eta under I(t)=I0+R t."""
    assert 0 < eta <= 1 and nu > 0
    return (eta**-2 - 1.0) / nu


def fractional_decision_shrink_rate(leverage, nu):
    """Initial -(1/W)dW/dt for one independently characterized interval."""
    assert leverage >= 0 and nu >= 0
    return 0.5 * leverage * nu


def synthetic_rows():
    a09=i94.ArchBox(1.0,1.1,1.0,1.1,0.02,0.04)
    a14=i94.ArchBox(3.3,3.8,1.4,1.6,0.03,0.06)
    W=i94.width(a09,a14)
    rows=[]
    for arch in ('09','14'):
        for field in ('A','R','d'):
            dw=i94.contraction_derivative(a09,a14,arch,field)
            rows.append((arch,field,dw,dw/W))
    return a09,a14,W,rows


def main():
    a09,a14,W,rows=synthetic_rows()
    lev={f'{a}.{f}':lam for a,f,_dw,lam in rows}

    # Reproduce the corrected Iteration-094 ordering.
    ranking=sorted(lev, key=lev.get, reverse=True)
    assert ranking == ['14.R','09.R','14.A','14.d','09.d','09.A']

    # RESOURCE-048: exact Fisher-to-interval contraction law.
    for nu in (1e-3, 0.02, 0.7):
        t50=time_for_contraction(0.5,nu)
        assert isclose(t50,3.0/nu,rel_tol=1e-14)
        assert isclose(eta_from_fisher_time(nu,t50),0.5,rel_tol=1e-14)

    # DESIGN-010: local measurement priority is Lambda * nu, not Lambda alone.
    # Equal normalized Fisher rates reproduce the VOI-only ordering.
    nu_equal={k:0.02 for k in lev}
    rank_equal=sorted(lev, key=lambda k:fractional_decision_shrink_rate(lev[k],nu_equal[k]), reverse=True)
    assert rank_equal == ranking

    # A faster characterization channel can invert the raw-VOI ranking.
    # 14.A overtakes 14.R exactly when nu_A/nu_R > Lambda_R/Lambda_A.
    break_even_A_over_R=lev['14.R']/lev['14.A']
    assert 2.86 < break_even_A_over_R < 2.87
    nu_flip=nu_equal.copy(); nu_flip['14.A']=0.08
    assert fractional_decision_shrink_rate(lev['14.A'],nu_flip['14.A']) > fractional_decision_shrink_rate(lev['14.R'],nu_flip['14.R'])

    # The same threshold logic for selected pairs.
    break_even_R09_over_R14=lev['14.R']/lev['09.R']
    break_even_d14_over_R14=lev['14.R']/lev['14.d']
    assert 1.21 < break_even_R09_over_R14 < 1.22
    assert 3.26 < break_even_d14_over_R14 < 3.27

    # Direct finite-time regression for one active interval.
    nu=0.02
    dt=1e-5
    eta=eta_from_fisher_time(nu,dt)
    Wt=i94.width(a09,i94.contract(a14,'R',eta))
    finite=(W-Wt)/(W*dt)
    theory=fractional_decision_shrink_rate(lev['14.R'],nu)
    assert isclose(finite,theory,rel_tol=3e-7,abs_tol=2e-10)

    print('PASS Iteration 096 characterization Fisher value')
    print('W synthetic =',W)
    print('raw VOI ranking =',ranking)
    print('break-even nu_14A/nu_14R =',break_even_A_over_R)
    print('break-even nu_09R/nu_14R =',break_even_R09_over_R14)
    print('break-even nu_14d/nu_14R =',break_even_d14_over_R14)
    print('finite/theory 14.R fractional shrink rate =',finite,theory)


if __name__=='__main__':
    main()
