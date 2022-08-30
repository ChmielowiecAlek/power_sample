import logging
from imc import *


class FineTuneController:
    def __init__(self, mn: MatchingNetwork):
        self.mn = mn

    def trigger_20(self):
        logging.info("In FineTuneController.trigger_20")
        gamma = self.mn.gamma()
        logging.info("gamma=%.E+j%.E", gamma.real, gamma.imag)

        gain = pow((1.0 - abs(gamma)), 2)
        logging.info("gain=%.E", gain)

        ct_delta = -1.0 * gain * gamma.real
        self.mn.update_tune(ct_delta)

        cl_delta = -1.0 * gain * gamma.imag
        self.mn.update_load(cl_delta)
