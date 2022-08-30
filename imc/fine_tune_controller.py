from imc import *


class FineTuneController:
    def __init__(self, mn: MatchingNetwork):
        self.mn = mn

    def trigger_20(self):
        gamma = self.mn.gamma()

        ct_delta = complex.real(gamma)
        self.mn.update_tune(ct_delta)

        cl_delta = complex.imag(gamma)
        self.mn.update_load(cl_delta)
