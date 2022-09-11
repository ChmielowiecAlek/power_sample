import pytest
from unittest.mock import patch
from imc import FineTuner, MatchingNetwork


@pytest.fixture
def matching_network():
    matching_network = MatchingNetwork()
    return matching_network


@pytest.fixture
def tuner(matching_network):
    tuner = FineTuner(matching_network)
    return tuner


def test_tuner_initialization(tuner):
    assert tuner


@patch.object(FineTuner, '_trigger_impl')
def test_tuner_triggering(fine_tuner_mock, tuner):
    assert FineTuner._trigger_impl is fine_tuner_mock
    assert tuner._trigger_impl is fine_tuner_mock
    assert fine_tuner_mock.call_count == 0
    tuner.trigger()
    assert fine_tuner_mock.call_count == 1
    tuner.trigger()
    assert fine_tuner_mock.call_count == 2

