import math

from matching_network import MatchingNetwork


class CoarseTuneController:
    def __init__(self, mn: MatchingNetwork):
        self.mn = mn
        self.gamma_1 = mn.gamma()  # previous gamma value

    # the coarse controller uses a sampling period of 100ms
    def trigger_100(self):
        gamma = self.mn.gamma()
        change_ct_direction = math.abs(gamma) > math.abs(self.gamma_1)

        if change_ct_direction:
            self.mn.update_tune(-1 * self.mn.ct)

        self.gamma_1 = gamma
