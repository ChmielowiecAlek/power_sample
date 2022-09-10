import pytest

from imc import MatchingNetwork, ImpedanceTuner


@pytest.fixture
def matching_network():
    return MatchingNetwork()


def test_impedance_tuner_abstraction():
    impedance_tuner = ImpedanceTuner(matching_network, 1)
    assert impedance_tuner
    with pytest.raises(NotImplementedError):
        impedance_tuner.trigger()


class ImpedanceTunerImpl(ImpedanceTuner):
    def __init__(self, matching_network: MatchingNetwork, triggering_ratio):
        super(ImpedanceTunerImpl, self).__init__(matching_network, triggering_ratio)
        self.trigger_count = 0

    def _trigger_impl(self):
        self.trigger_count += 1


@pytest.fixture(params=['always', 'every_fifth_time'])
def impedance_tuner(request, matching_network):
    if request.param == 'always':
        impedance_tuner = ImpedanceTunerImpl(matching_network, 1)
    elif request.param == 'every_fifth_time':
        impedance_tuner = ImpedanceTunerImpl(matching_network, 5)
    return impedance_tuner


def test_impedance_tuner_create(impedance_tuner):
    assert impedance_tuner


def test_impedance_tuner_trigger(impedance_tuner):
    count = 17
    for i in range(0, count):
        impedance_tuner.trigger()
    assert impedance_tuner.trigger_count == int(count / impedance_tuner.triggering_ratio)
