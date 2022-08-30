from imc import *


class ImpedanceMatchingController:
    def __init__(self):
        self.mn = MatchingNetwork()
        self.ctc = CoarseTuneController(self.mn)
        self.ftc = FineTuneController(self.mn)

        # the fine controller uses a sampling period of 20ms
        # the coarse controller uses a sampling period of 100ms
        self.tick_ratio = 100 / 20

    def run(self, fine_ticks):
        for tick in range(fine_ticks):
            self.ftc.trigger_20()
            if (tick % self.tick_ratio) == 0:
                self.ctc.trigger_100()

