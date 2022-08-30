import math


class MatchingNetwork:
    def __init__(self):
        self.OMEGA = 2 * math.pi * 13.56e6  # circular frequency
        self.ZO = complex(50)               # transmission line impedance (== RF gen impedance)
        self.cl = 1000e-12                  # MN load capacitance
        self.ct = 150e-12                   # MN tune capacitance

        # MN capacitance limits
        self.CL_LIMITS = {"min": 600e-12, "max": 1600e-12}
        self.CT_LIMITS = {"min": 50e-12, "max": 250e-12}

        # MN load impedance
        self. zl = 0
        self.update_load(0)

        # MN tune impedance
        self.zt = 0
        self.update_tune(0)

    def update_load(self, delta_cl):
        new_cl = self.cl + delta_cl
        if new_cl < self.CL_LIMITS["min"] or new_cl > self.CL_LIMITS["max"]:
            raise ValueError
        self.cl = new_cl
        self.zl = 1 / complex(0, self.OMEGA * self.cl)

    def update_tune(self, delta_ct):
        new_ct = self.ct + delta_ct
        if new_ct < self.CT_LIMITS["min"] or new_ct > self.CT_LIMITS["max"]:
            raise ValueError
        self.ct = new_ct
        self.zt = 1 / complex(0, self.OMEGA * self.ct)

    # plasma impedance
    def zpl(self):
        zpl = complex.conjugate(self.zt + (self.ZO * self.zl) / (self.ZO + self.zl))
        return zpl

    # reflection coefficient
    def gamma(self):
        gamma = (self.zl - self.zo) / (self.zl + self.zo)
        return gamma

