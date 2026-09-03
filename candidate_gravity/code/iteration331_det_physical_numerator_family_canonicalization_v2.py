#!/usr/bin/env python3
"""RQIR Iteration 331: corrected version of Iteration 330 numerator-family gate.

Iteration 330 preserved a scoped gate-design FAIL because its auxiliary
`qdiff_nonzero` assertion incorrectly included TARGET=(1,1,1).  On the frozen
closed triad q(TARGET)=q1+q2+q3=0 by construction, while every proper nonzero
subindex that defines a bubble/triangle external denominator difference must be
nonzero.  All physical route maps and held-out numerator reconstructions in 330
had already passed at ~1e-16.

This new gate changes only that logically incorrect meta-assertion and the
iteration/classification labels. Parent dynamics, topology weights, loop maps,
held-out momenta and the 5e-10 numerical threshold are unchanged.
"""
from pathlib import Path

p=Path(__file__).with_name('iteration330_det_physical_numerator_family_canonicalization.py')
src=p.read_text()
old="qdiff_nonzero=all(any(x for x in qint(a)) for a in NZ)"
new="qdiff_nonzero=all(any(x for x in qint(a)) for a in NZ if a != TARGET)"
if src.count(old)!=1:
    raise RuntimeError('Iteration-330 qdiff gate signature changed; refuse implicit rebase')
src=src.replace(old,new,1)
if src.count("'iteration':330")!=1:
    raise RuntimeError('Iteration-330 sentinel signature changed; refuse implicit rebase')
src=src.replace("'iteration':330","'iteration':331",1)
src=src.replace('PASS_PHYSICAL_CUBIC_DETERMINANT_NUMERATOR_SIGNED_AFFINE_FAMILY_RECONSTRUCTION',
                'PASS_PHYSICAL_CUBIC_DETERMINANT_NUMERATOR_SIGNED_AFFINE_FAMILY_RECONSTRUCTION_V2_CLOSED_TARGET_EXCLUDED_FROM_NONZERO_PROPER_SUBINDEX_CHECK')
src=src.replace('FAIL_PHYSICAL_CUBIC_DETERMINANT_NUMERATOR_SIGNED_AFFINE_FAMILY_RECONSTRUCTION',
                'FAIL_PHYSICAL_CUBIC_DETERMINANT_NUMERATOR_SIGNED_AFFINE_FAMILY_RECONSTRUCTION_V2_CLOSED_TARGET_EXCLUDED_FROM_NONZERO_PROPER_SUBINDEX_CHECK')
exec(compile(src,str(p),'exec'),{'__name__':'__main__','__file__':str(p)})
