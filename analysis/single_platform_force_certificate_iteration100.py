#!/usr/bin/env python3
"""RQIR Iteration 100 — single-platform broadband force-certificate audit.

External anchor: Fu et al., force detection sensitivity spectrum calibration
with a levitated nanoparticle (arXiv:2109.02437; Optics and Lasers in
Engineering 152, 106957 (2022)).

The numerical values below are publication-reported apparatus facts or explicit
RQIR target transforms. They are not a complete apparatus forecast.
"""
from math import sqrt, isclose

Z = 5.0

# Publication-backed frequency/measurement facts.
SWEEP_MIN_HZ = 1.0e3
SWEEP_MAX_HZ = 500.0e3
PSD_SAMPLE_RATE_HZ = 937.0e3
PSD_SAMPLE_TIME_S = 0.270
HIGH_PRESSURE_AVERAGES = 10
CAL_X_MV_PER_NM = 80.7
CAL_X_MV_PER_NM_ERR = 0.5
RADIUS_NM = 80.8
RADIUS_NM_ERR = 3.1
Z_CROSSTALK_HZ = 48.5e3
Z_CROSSTALK_EPS = 0.008
OFF_RESONANCE_ASD_N_RT_HZ = 1.0e-17  # reported order of magnitude
THERMAL_LIMIT_ASD_N_RT_HZ = 4.39e-20
THERMAL_LIMIT_ERR_N_RT_HZ = 0.62e-20
THERMAL_LIMIT_PRESSURE_MBAR = 2.4e-6


def factor_two_fundamental_interval(fmin=SWEEP_MIN_HZ, fmax=SWEEP_MAX_HZ):
    """All f for which both f and 2f lie in the measured transfer sweep."""
    assert fmin > 0 and fmax > 2*fmin
    return fmin, fmax/2.0


def balanced_raw_rate(target_time_s, z=Z):
    """Per-band raw Fisher rate for balanced independent bands.

    R_beta=2 r when r2=r4=r, so T=Z^2/R_beta -> r=Z^2/(2T).
    """
    assert target_time_s > 0
    return z*z/(2.0*target_time_s)


def required_force_harmonic(asd, target_time_s, kappa_psd=1.0, z=Z):
    """Science-only force harmonic threshold from r=kappa*|dF|^2/S_F.

    kappa_psd is convention dependent and remains explicit in RQIR. Setting it
    to 1 is only a transparent scale slice.
    """
    assert asd > 0 and kappa_psd > 0
    r=balanced_raw_rate(target_time_s,z)
    return asd*sqrt(r/kappa_psd)


def main():
    lo,hi=factor_two_fundamental_interval()
    assert isclose(lo,1.0e3)
    assert isclose(hi,250.0e3)

    # The transfer sweep itself therefore has enough frequency span for f,2f.
    for f in (1e3, 10e3, 100e3, 200e3, 250e3):
        assert SWEEP_MIN_HZ <= f <= SWEEP_MAX_HZ
        assert SWEEP_MIN_HZ <= 2*f <= SWEEP_MAX_HZ

    targets={
        '1_day':86400.0,
        '7_day':7*86400.0,
        '30_day':30*86400.0,
    }
    out={}
    for name,T in targets.items():
        r=balanced_raw_rate(T)
        dF=required_force_harmonic(OFF_RESONANCE_ASD_N_RT_HZ,T,1.0)
        out[name]=(r,dF)

    # Regressions against the mature Iteration-084 target rates.
    assert isclose(out['1_day'][0],1.4467592592592592e-4,rel_tol=1e-14)
    assert isclose(out['7_day'][0],2.0667989417989417e-5,rel_tol=1e-14)
    assert isclose(out['30_day'][0],4.822530864197531e-6,rel_tol=1e-14)

    # Publication measurement window facts.
    assert PSD_SAMPLE_RATE_HZ*PSD_SAMPLE_TIME_S > 2.5e5
    assert HIGH_PRESSURE_AVERAGES == 10

    print('PASS Iteration 100 single-platform force certificate audit')
    print('factor-two fundamental interval [Hz] =',lo,hi)
    for name,(r,dF) in out.items():
        print(name,'balanced r [1/s]=',r,
              'dF at ASD=1e-17, kappa=1 [N]=',dF)
    print('reported x displacement calibration [mV/nm] =',
          CAL_X_MV_PER_NM,'+/-',CAL_X_MV_PER_NM_ERR)
    print('reported z crosstalk =',Z_CROSSTALK_HZ,Z_CROSSTALK_EPS)
    print('high-vacuum thermal-limit ASD [N/sqrtHz] =',
          THERMAL_LIMIT_ASD_N_RT_HZ,'+/-',THERMAL_LIMIT_ERR_N_RT_HZ,
          'at',THERMAL_LIMIT_PRESSURE_MBAR,'mbar')


if __name__=='__main__':
    main()
