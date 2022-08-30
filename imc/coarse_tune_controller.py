import logging
from imc import *


class CoarseTuneController:
    def __init__(self, mn: MatchingNetwork):
        self.mn = mn
        self.gamma_1 = mn.gamma()  # previous gamma value
        self.ct_direction = 1.0

    def trigger_100(self):
        logging.info("In CoarseTuneController.trigger_100")
        gamma = self.mn.gamma()

        logging.info("|gamma_1|=%.E, |gamma|=%.E", abs(self.gamma_1), abs(gamma))
        if abs(gamma) - abs(self.gamma_1) > 0.002:
            self.ct_direction *= -1.0
            logging.info("changing direction to %f", self.ct_direction)

        gain = 0.1
        factor = self.ct_direction * abs(gamma) * gain
        self.mn.update_tune(factor * self.mn.ct )

        self.gamma_1 = gamma
