"""RQIR Iteration 076: timing-recertification duty and control-aware Toy014 wall clock.

Extends Iteration 071/075 by converting the transparent timing-reference and
Brownian-diffusion cadence model into a fractional recertification duty.  The
result is parametric in the drift diffusion coefficient and event jitter; it is
not an oscillator or apparatus forecast.
"""
from __future__ import annotations

# Retained physical/projected resource factors.
QS14 = 3.5333858994461136
QC14 = 3.484828228881006
QP14 = 0.6705404602700137

# Timing benchmarks at 100 Hz.
TARGET14_US = 3.9771527420283626
TCOH14_S = 0.006813266351407684
TARGET009_US = 9.190010830110957
TCOH009_S = 0.00794318793930142

DEAD_S = 1e-3
P = 0.5
SIGMA_EVENT_US = 10.0
REF_FRACTION = 1.0/3.0


def reference_block_s(target_us: float, cycle_s: float,
                      sigma_event_us: float = SIGMA_EVENT_US,
                      p: float = P, ref_fraction: float = REF_FRACTION) -> float:
    sigma_ref = ref_fraction*target_us
    return cycle_s/p*(sigma_event_us/sigma_ref)**2


def cadence_s(target_us: float, diffusion_us2_per_h: float,
              ref_fraction: float = REF_FRACTION, floor_us: float = 0.0) -> float:
    sigma_ref = ref_fraction*target_us
    numerator = target_us**2-floor_us**2-sigma_ref**2
    if numerator <= 0.0:
        return 0.0
    return 3600.0*2.0*numerator/diffusion_us2_per_h


def duty_fraction(target_us: float, cycle_s: float, diffusion_us2_per_h: float,
                  sigma_event_us: float = SIGMA_EVENT_US,
                  p: float = P, ref_fraction: float = REF_FRACTION,
                  floor_us: float = 0.0) -> float:
    cad = cadence_s(target_us,diffusion_us2_per_h,ref_fraction,floor_us)
    if cad <= 0:
        return 1.0
    return reference_block_s(target_us,cycle_s,sigma_event_us,p,ref_fraction)/cad


def payload_multiplier(duty: float) -> float:
    if duty >= 1.0:
        return float('inf')
    return 1.0/(1.0-duty)


def toy014_boundary(d14: float, d009: float):
    """Return y0,slope for control-duty-aware Toy014<Toy009 boundary.

    Reference payload models:
      T14 = m14*(QS14 + QC14*x + QP14*y)
      T09 = m09*(1+x+y)
    with m=1/(1-duty).
    """
    eta = payload_multiplier(d009)/payload_multiplier(d14)
    denom = eta-QP14
    if denom <= 0:
        return eta,float('inf'),float('inf')
    y0 = (QS14-eta)/denom
    slope = (QC14-eta)/denom
    return eta,y0,slope


def main():
    cycle14 = TCOH14_S+DEAD_S
    cycle09 = TCOH009_S+DEAD_S

    # With reference target = final target/3 and zero floor, the analytic law is
    # duty = const * D * sigma_event^2 * cycle / target^4.
    # Regression-check it numerically for the two retained drift examples.
    for D in (100.0,1000.0):
        d14 = duty_fraction(TARGET14_US,cycle14,D)
        d09 = duty_fraction(TARGET009_US,cycle09,D)
        eta,y0,slope = toy014_boundary(d14,d09)
        print('D',D,'Toy014/Toy009 duty',d14,d09,'ratio',d14/d09)
        print('payload multipliers',payload_multiplier(d14),payload_multiplier(d09))
        print('control-aware boundary y >',y0,'+',slope,'x; eta',eta)

    d14_100 = duty_fraction(TARGET14_US,cycle14,100.0)
    d14_1000 = duty_fraction(TARGET14_US,cycle14,1000.0)
    d09_100 = duty_fraction(TARGET009_US,cycle09,100.0)
    d09_1000 = duty_fraction(TARGET009_US,cycle09,1000.0)

    assert abs(d14_100-0.0008782862410895392) < 3e-12
    assert abs(d14_1000-0.008782862410895393) < 3e-12
    assert abs(d09_100-3.5263115489462467e-05) < 3e-12
    assert abs(d09_1000-0.00035263115489462475) < 3e-12
    assert abs(d14_100/d09_100-24.9066546985) < 3e-8

    eta100,y0100,m100 = toy014_boundary(d14_100,d09_100)
    eta1000,y01000,m1000 = toy014_boundary(d14_1000,d09_1000)
    assert abs(y0100-7.71181317284) < 3e-8
    assert abs(m100-7.56404922153) < 3e-8
    assert abs(y01000-7.91779000679) < 3e-8
    assert abs(m1000-7.76653241412) < 3e-8

    # Diffusion levels at which the Toy014 reference duty alone reaches 10%
    # and 100% in this white-event / zero-floor benchmark.
    D10 = 1000.0*0.1/d14_1000
    D100 = 1000.0/d14_1000
    print('Toy014 D for 10% / 100% timing-reference duty',D10,D100)
    assert abs(D10-11385.8096964) < 3e-5
    assert abs(D100-113858.096964) < 3e-4


if __name__ == '__main__':
    main()
