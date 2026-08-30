#!/usr/bin/env python3
"""RQIR Iteration 082: external D2 apparatus frequency-compatibility audit.

This script checks whether a published narrowband levitated-force sensitivity can be
inserted into the current two-band RQIR D2 likelihood without an additional transfer
model. It deliberately does not convert the published resonance ASD into RQIR hours.
"""

from math import isclose, sqrt

# Externally reported detector anchor (Liang et al., Fundamental Research 3, 57-62 (2023))
f_res_hz = 193_800.0
linewidth_hz = 19.60  # reported feedback-cooled damping-rate central value
force_asd_zN_sqrtHz = 6.33
force_asd_unc_zN_sqrtHz = 1.62
best_force_asd_zN_sqrtHz = 4.34
allan_optimal_time_s = 2751.0
stable_force_resolution_yN = 166.40
stable_force_resolution_unc_yN = 55.48

# Current RQIR two-band convention: science bands n=2 and n=4 of f_gap.
fgap_if_n2_on_res_hz = f_res_hz / 2.0
f4_if_n2_on_res_hz = 4.0 * fgap_if_n2_on_res_hz
fgap_if_n4_on_res_hz = f_res_hz / 4.0
f2_if_n4_on_res_hz = 2.0 * fgap_if_n4_on_res_hz

separation_n2_case_hz = abs(f4_if_n2_on_res_hz - f_res_hz)
separation_n4_case_hz = abs(f_res_hz - f2_if_n4_on_res_hz)
separation_n2_in_linewidths = separation_n2_case_hz / linewidth_hz
separation_n4_in_linewidths = separation_n4_case_hz / linewidth_hz
fractional_linewidth = linewidth_hz / f_res_hz

# Current stored physical D2 information from Toy014, and its ratio to Toy009.
S_eff_014 = 1.6356852494e-4
S_eff_014_over_009 = 0.28301465746
S_eff_009 = S_eff_014 / S_eff_014_over_009
amp_eff_009 = sqrt(S_eff_009)
amp_eff_014 = sqrt(S_eff_014)

assert isclose(fgap_if_n2_on_res_hz, 96_900.0)
assert isclose(f4_if_n2_on_res_hz, 387_600.0)
assert isclose(fgap_if_n4_on_res_hz, 48_450.0)
assert isclose(f2_if_n4_on_res_hz, 96_900.0)
assert separation_n2_in_linewidths > 9_000
assert separation_n4_in_linewidths > 4_000
assert fractional_linewidth < 2e-4
assert isclose(S_eff_009, 5.779507196128809e-4, rel_tol=1e-12)

print("RQIR Iteration 082 external D2 frequency-compatibility audit")
print(f"published resonance = {f_res_hz/1e3:.3f} kHz")
print(f"published damping/linewidth proxy = {linewidth_hz:.2f} Hz")
print(f"fractional linewidth = {fractional_linewidth:.6e}")
print()
print("If n=2 is placed on resonance:")
print(f"  f_gap = {fgap_if_n2_on_res_hz/1e3:.3f} kHz")
print(f"  n=4 band = {f4_if_n2_on_res_hz/1e3:.3f} kHz")
print(f"  separation from resonance = {separation_n2_in_linewidths:.1f} linewidths")
print("If n=4 is placed on resonance:")
print(f"  f_gap = {fgap_if_n4_on_res_hz/1e3:.3f} kHz")
print(f"  n=2 band = {f2_if_n4_on_res_hz/1e3:.3f} kHz")
print(f"  separation from resonance = {separation_n4_in_linewidths:.1f} linewidths")
print()
print(f"Toy009 S_eff = {S_eff_009:.12e}, sqrt = {amp_eff_009:.12e}")
print(f"Toy014 S_eff = {S_eff_014:.12e}, sqrt = {amp_eff_014:.12e}")
print()
print("External force anchor (not inserted into RQIR Fisher without transfer at both bands):")
print(f"  force ASD = {force_asd_zN_sqrtHz:.2f} +/- {force_asd_unc_zN_sqrtHz:.2f} zN/sqrt(Hz)")
print(f"  best run ASD = {best_force_asd_zN_sqrtHz:.2f} zN/sqrt(Hz)")
print(f"  Allan-optimal time = {allan_optimal_time_s:.0f} s")
print(f"  stable force resolution = {stable_force_resolution_yN:.2f} +/- {stable_force_resolution_unc_yN:.2f} yN")
print("PASS: a single narrow resonance cannot be used as a two-band RQIR apparatus normalization without a measured off-resonance/second-band transfer+PSD or a retuned sequential likelihood.")
