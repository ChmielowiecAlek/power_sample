from imc import MatchingNetwork


class ImpedanceTuner:
    def __init__(self, matching_network: MatchingNetwork, triggering_ratio):
        self.matching_network = matching_network
        self.triggering_ratio = triggering_ratio
        self.triggering_counter = 0

    def trigger(self):
        self.triggering_counter += 1
        if self.triggering_counter == self.triggering_ratio:
            self.triggering_counter = 0
            self._trigger_impl()

    def _trigger_impl(self):
        raise NotImplementedError
