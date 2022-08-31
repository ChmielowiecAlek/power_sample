import logging
import math
import numpy as np


class MatchingNetwork:
    def __init__(self):
        self.OMEGA = 2 * math.pi * 13.56e6  # circular frequency
        self.ZO = complex(50)  # transmission line impedance (== RF gen impedance)
        self.cl = 1000e-12  # MN load capacitance
        self.ct = 150e-12  # MN tune capacitance

        # MN capacitance limits
        self.CL_LIMITS = {"min": 600e-12, "max": 1600e-12}
        logging.info("CL_LIMITS min=%.E", self.CL_LIMITS["min"])
        logging.info("CL_LIMITS max=%.E", self.CL_LIMITS["max"])
        self.CT_LIMITS = {"min": 50e-12, "max": 250e-12}
        logging.info("CT_LIMITS min=%.E", self.CT_LIMITS["min"])
        logging.info("CT_LIMITS max=%.E", self.CT_LIMITS["max"])

        # MN load impedance
        self.zl = 0
        self.update_load(0)

        # MN tune impedance
        self.zt = 0
        self.update_tune(0)

    def update_load(self, delta_cl):
        logging.info("update_load called with delta_cl=%.E", delta_cl)
        new_cl = self.cl + delta_cl
        if new_cl < self.CL_LIMITS["min"]:
            new_cl = self.CL_LIMITS["min"]
            logging.warning('cl saturated on the lower limit')
        elif new_cl > self.CL_LIMITS["max"]:
            new_cl = self.CL_LIMITS["min"]
            logging.warning('cl saturated on the upper limit')
        self.cl = new_cl
        self.zl = 1 / complex(0, self.OMEGA * self.cl)

    def update_tune(self, delta_ct):
        logging.info("update_tune called with delta_ct=%.E", delta_ct)
        new_ct = self.ct + delta_ct
        if new_ct < self.CT_LIMITS["min"]:
            new_ct = self.CT_LIMITS["min"]
            logging.warning('ct saturated on the lower limit')
        elif new_ct > self.CT_LIMITS["max"]:
            new_ct = self.CT_LIMITS["max"]
            logging.warning('ct saturated on the upper limit')
        self.ct = new_ct
        self.zt = 1 / complex(0, self.OMEGA * self.ct)

    # reflection coefficient
    def gamma(self):
        gamma: complex = (self.zl - self.ZO) / (self.zl + self.ZO)
        return gamma


class Theory:
    def __init__(self, omega=2 * math.pi * 13.56e6, zo=complex(50, 0)):
        self.OMEGA: float = omega  # circular frequency
        self.ZO: complex = zo  # transmission line impedance

    # plasma impedance
    # def zpl(self):
    #    zpl = complex.conjugate(self.zt + (self.ZO * self.zl) / (self.ZO + self.zl))
    #    return zpl

    def gamma(self, cl, ct):
        zl = complex(1, 0) / complex(0, self.OMEGA * cl)
        zt = complex(1, 0) / complex(0, self.OMEGA * ct)
        gamma: complex = (zl - self.ZO) / (zl + self.ZO)
        return gamma

    def gamma_modulus(self, cl, ct):
        return abs(self.gamma(cl, ct))

    def calculate_function(self,
                           cl_min=600e-12, cl_max=1650e-12,
                           ct_min=50e-12, ct_max=300e-12,
                           step=50e-12):
        x = np.arange(cl_min, cl_max, step)
        y = np.arange(ct_min, ct_max, step)
        X, Y = np.meshgrid(x, y)

        z = np.array(self.gamma_modulus(np.ravel(X), np.ravel(Y)))
        Z = z.reshape(X.shape)
        return X, Y, Z


        #array(list(map(self.gamma_modulus, x, y)))

        #cl = cl_min
        #while cl <= cl_max:
        #    ct = ct_min
        #    while ct <= ct_max:
        #        print("cl=", cl, " ct=", ct)
        #        x = np.append(x, cl)
        #        y = np.append(y, ct)
        #        z = np.append(z, abs(self.gamma(cl, ct)))
        #
        #        ct += step
        #    cl += step
        #
