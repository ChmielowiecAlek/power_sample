import pytest
from unittest.mock import patch
from imc import Controller, FineTuner, CoarseTuner


@pytest.fixture
def controller():
    controller = Controller()
    return controller


def test_controller_initialization(controller):
    assert controller


@patch.object(FineTuner, '_trigger_impl')
def test_controller_running(fine_tuner_mock, controller):
    assert FineTuner._trigger_impl is fine_tuner_mock
    assert controller.ftc._trigger_impl is fine_tuner_mock
    count = 17
    controller.run(count)
    assert fine_tuner_mock.call_count == int(count / controller.ftc.triggering_ratio)

