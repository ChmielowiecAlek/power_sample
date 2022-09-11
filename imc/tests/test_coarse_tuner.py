import pytest
from unittest.mock import patch
from imc import CoarseTuner, MatchingNetwork


@pytest.fixture
def matching_network():
    matching_network = MatchingNetwork()
    return matching_network


@pytest.fixture
def tuner(matching_network):
    tuner = CoarseTuner(matching_network)
    return tuner


def test_tuner_initialization(tuner):
    assert tuner


@patch.object(CoarseTuner, '_trigger_impl')
def test_tuner_triggering(coarse_tuner_mock, tuner):
    assert CoarseTuner._trigger_impl is coarse_tuner_mock
    assert tuner._trigger_impl is coarse_tuner_mock
    for i in range(tuner.triggering_ratio - 1):
        tuner.trigger()
    assert coarse_tuner_mock.call_count == 0
    tuner.trigger()
    assert coarse_tuner_mock.call_count == 1
