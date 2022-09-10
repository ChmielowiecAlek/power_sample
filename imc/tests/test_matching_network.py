from collections import namedtuple

import pytest
from imc import Theory, MatchingNetwork

EXPECTED_GEN_FREQ = 13.56e6
EXPECTED_OMEGA = 85199992.765355193
EXPECTED_ZO = 50

EXPECTED_CL_MIN = 600e-12
EXPECTED_CL_MAX = 1600e-12
EXPECTED_CT_MIN = 50e-12
EXPECTED_CT_MAX = 250e-12

EXPECTED_INITIAL_CL = 700e-12
EXPECTED_INITIAL_CT = 125e-12


def test_theory_class_is_static():
    theory = None
    with pytest.raises(NotImplementedError):
        theory = Theory()
    assert theory is None


def test_theory_class_complex_one_is_constant():
    assert Theory.const.COMPLEX_ONE == complex(1, 0)
    with pytest.raises(AttributeError):
        Theory.const.COMPLEX_ONE = complex(2, 0)
    assert Theory.const.COMPLEX_ONE == complex(1, 0)


def test_theory_class_circular_freq():
    omega = Theory.circular_freq(EXPECTED_GEN_FREQ)
    assert omega == pytest.approx(EXPECTED_OMEGA, 1e-15)


def test_theory_class_zc():
    omega = EXPECTED_OMEGA
    c = 150e-12
    zc = Theory.zc(omega, c)
    expected = complex(0, -78.2472680)  # calculated with octave
    assert zc == pytest.approx(expected, 1e-9)


@pytest.fixture(params=['default', 'custom_pgf', 'custom_pgf_and_pgi'])
def matching_network(request):
    if request.param == 'default':
        matching_network = MatchingNetwork()
    elif request.param == 'custom_pgf':
        matching_network = MatchingNetwork(1e6)
    elif request.param == 'custom_pgf_and_pgi':
        matching_network = MatchingNetwork(1e6, 75)
    return matching_network


def test_matching_network_create(matching_network):
    assert matching_network


def test_matching_network_default_parameters():
    mn = MatchingNetwork()
    assert mn.POWER_GEN_FREQ == EXPECTED_GEN_FREQ
    assert mn.ZO == complex(EXPECTED_ZO, 0)
    assert mn.get_load_cap() == 700e-12
    assert mn.get_tune_cap() == 125e-12
    assert mn._limits["CL"].min == EXPECTED_CL_MIN
    assert mn._limits["CL"].max == EXPECTED_CL_MAX
    assert mn._limits["CT"].min == EXPECTED_CT_MIN
    assert mn._limits["CT"].max == EXPECTED_CT_MAX


CapLimit = namedtuple("CapLimit", "actual expected")


@pytest.fixture(params=['below_min', 'equal_min', 'within_scope', 'equal_max', 'greater_than_max'])
def load_cap_limit(request):
    # 3.10 style instead of if-elif-else
    match request.param:
        case 'below_min':
            return CapLimit(100e-12, EXPECTED_CL_MIN)
        case 'equal_min':
            return CapLimit(EXPECTED_CL_MIN, EXPECTED_CL_MIN)
        case 'within_scope':
            return CapLimit(1100e-12, 1100e-12)
        case 'equal_max':
            return CapLimit(1600e-12, EXPECTED_CL_MAX)
        case 'greater_than_max':
            return CapLimit(2000e-12, EXPECTED_CL_MAX)


def test_matching_network_check_limits(matching_network, load_cap_limit):
    saturated = matching_network.check_limits("CL", load_cap_limit.actual)
    assert saturated == load_cap_limit.expected


def test_matching_network_get_load_cap(matching_network):
    assert matching_network.get_load_cap() == EXPECTED_INITIAL_CL


def test_matching_network_get_tune_cap(matching_network):
    assert matching_network.get_tune_cap() == EXPECTED_INITIAL_CT


def test_matching_network_adjust_load(matching_network):
    delta_cl = 50e-12
    matching_network.adjust_load(delta_cl)
    assert matching_network.get_load_cap() == pytest.approx(EXPECTED_INITIAL_CL + delta_cl, 1e-30)
    matching_network.adjust_load(-2 * delta_cl)
    assert matching_network.get_load_cap() == pytest.approx(EXPECTED_INITIAL_CL - delta_cl, 1e-30)
