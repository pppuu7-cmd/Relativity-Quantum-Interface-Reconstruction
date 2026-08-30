#!/usr/bin/env python3
"""RQIR Iteration 099 — primitive apparatus certificate audit.

Repository-backed source/model quantities are separated from apparatus-measured
quantities.  The audit refuses an absolute NG-030 architecture decision when a
required common-normalization cut is incomplete.
"""
from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class Entry:
    value: Optional[float]
    uncertainty: Optional[float]
    r_char: Optional[float]
    floor: Optional[float]
    provenance: str

    @property
    def characterized(self):
        return all(x is not None for x in (self.value, self.uncertainty, self.r_char, self.floor))


# Source-model quantities that are genuinely repository-backed.
MODEL = {
    '009.ramsey_phi0': Entry(1.09231, 0.0, None, None, 'repository-source-model'),
    '009.ramsey_q0': Entry(0.0025234392, 0.0, None, None, 'repository-source-model'),
    '009.gamma_mean': Entry(1.830264703e6, 0.0, None, None, 'repository-source-model'),
    '009.gamma_cov': Entry(5.901272925e5, 0.0, None, None, 'repository-source-model'),
    '014.ramsey_phi0': Entry(0.9264295097660072, 0.0, None, None, 'repository-source-model'),
    '014.ramsey_q0': Entry(0.0037632915041337926, 0.0, None, None, 'repository-source-model'),
    '014.gamma_mean': Entry(5.6776851e6, 0.0, None, None, 'repository-source-model'),
    '014.gamma_cov': Entry(2.7186736e6, 0.0, None, None, 'repository-source-model'),
}

# Required apparatus primitives. None are fabricated here.
REQUIRED_BY_ARCH = ('a2', 'a4', 'rho',
                    'k1', 'k2', 'k3', 'k4', 'k5', 'k6', 'k7',
                    'p_E', 'Omega_E', 't_reset', 'visibility', 'duty')


def empty_apparatus_certificate():
    out = {}
    for arch in ('009', '014'):
        for name in REQUIRED_BY_ARCH:
            out[f'{arch}.{name}'] = Entry(None, None, None, None, 'required-common-apparatus')
    out['common.R0'] = Entry(None, None, None, None, 'required-common-apparatus')
    return out


def missing_characterized(certificate):
    return [k for k, v in certificate.items() if not v.characterized]


def aggregate_decision_ready(certificate):
    # A robust absolute RESOURCE-045/NG-030 decision requires every primitive
    # cut to be closed or an equivalent directly measured aggregate interval.
    return len(missing_characterized(certificate)) == 0


def cut_report(certificate):
    groups = {
        'common detector scale': ['common.R0'],
        'Toy009 science': [f'009.{x}' for x in ('a2','a4','rho')],
        'Toy014 science': [f'014.{x}' for x in ('a2','a4','rho')],
        'Toy009 calibration': [f'009.k{i}' for i in range(1,8)],
        'Toy014 calibration': [f'014.k{i}' for i in range(1,8)],
        'Toy009 source apparatus': [f'009.{x}' for x in ('p_E','Omega_E','t_reset','visibility')],
        'Toy014 source apparatus': [f'014.{x}' for x in ('p_E','Omega_E','t_reset','visibility')],
        'duty/control': ['009.duty','014.duty'],
    }
    return {g: [k for k in keys if not certificate[k].characterized]
            for g, keys in groups.items()}


def main():
    cert = empty_apparatus_certificate()
    report = cut_report(cert)

    # Current repository-backed source-model constants do not by themselves
    # close any absolute apparatus cut because R_char/floors and physical
    # common normalization remain apparatus-specific.
    assert MODEL['009.ramsey_q0'].value > 0
    assert MODEL['014.ramsey_q0'].value > MODEL['009.ramsey_q0'].value
    assert not aggregate_decision_ready(cert)
    assert all(len(v) > 0 for v in report.values())

    # Demonstrate logical closure: once every declared primitive is supplied
    # with value, uncertainty, characterization rate and floor, the certificate
    # becomes decision-ready. Numbers here are placeholders solely for schema
    # regression and are never interpreted physically.
    filled = {k: Entry(1.0, 0.1, 2.0, 0.0, 'schema-regression') for k in cert}
    assert aggregate_decision_ready(filled)

    print('PASS Iteration 099 primitive certificate audit')
    print('current absolute decision ready:', aggregate_decision_ready(cert))
    for group, missing in report.items():
        print(group, 'missing', len(missing), 'fields:', ', '.join(missing))


if __name__ == '__main__':
    main()
