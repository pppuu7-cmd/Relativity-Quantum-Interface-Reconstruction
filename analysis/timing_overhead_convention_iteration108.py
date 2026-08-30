#!/usr/bin/env python3
"""RQIR Iteration 108 — exact timing overhead/live-fraction convention.

Reconciles Iteration 076's T_ref/T_cad quantity with the exact finite-periodic
schedule convention introduced in Iteration 107.  Retained Toy009/Toy014 timing
numbers are regression benchmarks, not apparatus forecasts.
"""
from __future__ import annotations

import math

# Iteration-076 retained values: reference-time / allowed-live-cadence ratio.
R14_100 = 0.0008782862410895392
R14_1000 = 0.008782862410895393
R09_100 = 3.5263115489462467e-05
R09_1000 = 0.00035263115489462475

QS14 = 3.5333858994461136
QC14 = 3.484828228881006
QP14 = 0.6705404602700137


def wall_duty_from_overhead(r):
    """If r=T_ref/T_live, return fraction of total wall time spent in reference."""
    assert r >= 0
    return r/(1.0+r)


def live_fraction_from_overhead(r):
    return 1.0/(1.0+r)


def wall_multiplier_from_overhead(r):
    return 1.0+r


def corrected_boundary(r14, r09):
    """Projected Iteration-074 boundary with exact pure-dead overhead convention."""
    eta = wall_multiplier_from_overhead(r09)/wall_multiplier_from_overhead(r14)
    denom = eta-QP14
    if denom <= 0:
        return eta, math.inf, math.inf
    return eta, (QS14-eta)/denom, (QC14-eta)/denom


def main():
    for D,r14,r09 in ((100.0,R14_100,R09_100),(1000.0,R14_1000,R09_1000)):
        d14=wall_duty_from_overhead(r14)
        d09=wall_duty_from_overhead(r09)
        eta,y0,slope=corrected_boundary(r14,r09)
        print('D',D,'overhead/live',r14,r09)
        print('exact wall duties',d14,d09,'live-fraction ratio',eta)
        print('corrected projected boundary y >',y0,'+',slope,'x')

    assert abs(wall_duty_from_overhead(R14_100)-0.0008775155312720806)<2e-16
    assert abs(wall_duty_from_overhead(R14_1000)-0.008706395338542117)<2e-16
    assert abs(wall_duty_from_overhead(R09_100)-3.526187204599614e-05)<2e-16
    assert abs(wall_duty_from_overhead(R09_1000)-0.000352506849997002)<2e-16

    eta100,y0100,s100=corrected_boundary(R14_100,R09_100)
    eta1000,y01000,s1000=corrected_boundary(R14_1000,R09_1000)
    assert abs(y0100-7.7117927731414255)<2e-13
    assert abs(s100-7.564029167841297)<2e-13
    assert abs(y01000-7.915669008795735)<2e-13
    assert abs(s1000-7.764447391074998)<2e-13

    # Iteration-076 Toy014 overhead/live ratio is linear in D in the declared
    # zero-floor Brownian/reference model.
    k14=R14_1000/1000.0
    # Exact total-wall 10% duty means r=d/(1-d)=1/9, not r=0.1.
    D10=(0.1/0.9)/k14
    D50=(0.5/0.5)/k14
    assert abs(D10-12650.899662651507)<2e-9
    assert abs(D50-113858.09696386354)<2e-8
    print('Toy014 D for exact 10% total-wall duty =',D10)
    print('Toy014 D for exact 50% total-wall duty =',D50)

    # No finite r corresponds to 100% total-wall reference duty.
    for r in (1.0,10.0,1000.0):
        assert wall_duty_from_overhead(r)<1.0

    print('PASS Iteration 108 exact timing overhead convention')


if __name__=='__main__':
    main()
