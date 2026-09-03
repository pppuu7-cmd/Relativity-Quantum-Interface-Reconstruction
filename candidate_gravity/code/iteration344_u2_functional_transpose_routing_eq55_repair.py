#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 344.

Repair of the preserved Iteration-343 gate implementation FAIL.  The functional
transpose routing hypothesis and all its pairing/phase tests passed in 343, but
the independent hand-coded linear Eq.(55) oracle omitted the factor i in the
ordinary Fourier derivatives nabla_rho R^{mu nu}=i q_rho R^{mu nu} and
nabla_rho R=i q_rho R.  This wrapper changes only those two oracle terms and
iteration/classification labels. Thresholds and the transpose-routing rule are
unchanged.
"""
from pathlib import Path
p=Path(__file__).with_name('iteration343_u2_functional_transpose_momentum_routing.py')
src=p.read_text()
repls={
 "T[mu,nu]+=-q[rho]*RicUp[mu,nu]":"T[mu,nu]+=1j*q[rho]*RicUp[mu,nu]",
 "T[mu,nu]+=0.5*eta[mu,nu]*q[rho]*Rsc":"T[mu,nu]+=-0.5j*eta[mu,nu]*q[rho]*Rsc",
 "'iteration':343":"'iteration':344",
 "PASS_U2_FUNCTIONAL_TRANSPOSE_FOURIER_ROUTING_A_T_Q_K_EQUALS_A_Q_MINUSKMINUSQ_T__PHYSICAL_ASSEMBLY_ROUTING_FROZEN":"PASS_U2_FUNCTIONAL_TRANSPOSE_FOURIER_ROUTING_A_T_Q_K_EQUALS_A_Q_MINUSKMINUSQ_T__CORRECTED_EQ55_ORACLE__PHYSICAL_ASSEMBLY_ROUTING_FROZEN",
 "FAIL_U2_FUNCTIONAL_TRANSPOSE_FOURIER_ROUTING":"FAIL_U2_FUNCTIONAL_TRANSPOSE_FOURIER_ROUTING_EQ55_REPAIR"
}
for old,new in repls.items():
    if src.count(old)!=1:
        raise RuntimeError(f'Iteration343 repair signature changed for {old!r}: count={src.count(old)}')
    src=src.replace(old,new,1)
exec(compile(src,str(p),'exec'),{'__name__':'__main__','__file__':str(p)})
