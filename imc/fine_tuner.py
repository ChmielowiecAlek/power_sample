import logging
from imc import *


class FineTuner(ImpedanceTuner):
    def __init__(self, _matching_network: MatchingNetwork):
        super(FineTuner, self).__init__(_matching_network, 1)

    # it uses gamma value from formula (4) from the article
    # which in my opinion is valid only for a coarse tuning
    # TODO: maybe something is wrong
    def _trigger_impl(self):
        logging.info("In FineTuneController.trigger_20")
        gamma = self.matching_network.gamma()
        logging.info("gamma=%.E+j%.E", gamma.real, gamma.imag)

        gain = pow((1.0 - abs(gamma)), 2)
        logging.info("gain=%.E", gain)

        ct_delta = -1.0 * gain * gamma.real
        self.matching_network.adjust_tune(ct_delta)

        cl_delta = +1.0 * gain * gamma.imag
        self.matching_network.adjust_load(cl_delta)
