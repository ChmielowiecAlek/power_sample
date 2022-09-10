import logging
from imc import *


class CoarseTuner(ImpedanceTuner):
    def __init__(self, _matching_network: MatchingNetwork):
        super(CoarseTuner, self).__init__(_matching_network, 5)
        self.trigger_count = 0
        self.gamma_1 = self.matching_network.gamma()  # previous gamma value
        self.ct_direction = 1.0

    # it is a bit strange: it takes gamma value from the past load (from the sensor, delayed)
    # but it uses it to adjust the tune capacitor
    # TODO: maybe something is wrong (I'm taking the gamma basing on the load capacitor)
    def _trigger_impl(self):
        logging.info("In CoarseTuner._trigger_impl")
        gamma = self.matching_network.gamma()
        epsilon = 0.002  # visible in Fig. 8 - diagram from the article

        logging.info("|gamma_1|=%.E, |gamma|=%.E", abs(self.gamma_1), abs(gamma))
        if abs(gamma) - abs(self.gamma_1) > epsilon:
            self.ct_direction *= -1.0
            logging.info("changing direction to %f", self.ct_direction)

        gain = 0.1
        factor = self.ct_direction * abs(gamma) * gain
        self.matching_network.adjust_tune(factor * self.matching_network.get_tune_cap())

        self.gamma_1 = gamma
