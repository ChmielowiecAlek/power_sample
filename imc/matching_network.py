import logging
import math
from collections import namedtuple


class Theory(object):
    _Const = namedtuple("_Const", "COMPLEX_ONE")
    const = _Const(complex(1, 0))

    # this is a static class
    def __init__(self):
        raise NotImplementedError

    # circular frequency
    @staticmethod
    def circular_freq(f):
        return 2 * math.pi * f

    # impedance of a capacitor: zero real part, negative imaginary part
    @staticmethod
    def zc(omega, c):
        z = Theory.const.COMPLEX_ONE / complex(0, omega * c)
        return z


class MatchingNetwork:
    def __init__(self, pgf=13.56e6, pgi=50):
        self.POWER_GEN_FREQ = pgf  # [Hz] RF power generator standard
        self.POWER_GEN_IMP = pgi  # [Ω] RF power generator impedance

        self.OMEGA = Theory.circular_freq(self.POWER_GEN_FREQ)  # [rad/s] circular frequency
        self.ZO = complex(self.POWER_GEN_IMP)  # [Ω] transmission line impedance (== RF gen impedance)

        # initial values were taken from experiments (jupyter notebook)
        self._cl = 700e-12  # [F] MN load capacitance
        self._ct = 125e-12  # [F] MN tune capacitance

        # MN capacitance limits from Fig.6 in the article
        _Limit = namedtuple("_Limit", "min max")
        self._limits = {"CL": _Limit(600e-12, 1600e-12),
                        "CT": _Limit(50e-12, 250e-12),
                       }
        logging.info("CL min=%.E", self._limits["CL"].min)
        logging.info("CL max=%.E", self._limits["CL"].max)
        logging.info("CT min=%.E", self._limits["CT"].min)
        logging.info("CT max=%.E", self._limits["CT"].max)

    def check_limits(self, key, value):
        saturated = value
        if value < self._limits[key].min:
            saturated = self._limits[key].min
            logging.warning("%s saturated on the lower limit %.E", key, saturated)
        elif value > self._limits[key].max:
            saturated = self._limits[key].max
            logging.warning("%s saturated on the upper limit %.E", key, saturated)
        return saturated


    def get_load_cap(self):
        return self._cl

    def get_tune_cap(self):
        return self._ct

    def adjust_load(self, delta_cl):
        logging.info("adjust_load called with delta_cl=%.E", delta_cl)
        new_cl = self._cl + delta_cl
        new_cl = self.check_limits("CL", new_cl)
        self._cl = new_cl

    def adjust_tune(self, delta_ct):
        logging.info("adjust_tune called with delta_ct=%.E", delta_ct)
        new_ct = self._ct + delta_ct
        new_ct = self.check_limits("CT", new_ct)
        self._ct = new_ct
