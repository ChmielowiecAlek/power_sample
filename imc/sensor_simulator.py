import logging
import math
from random import random


class SensorSimulator:
    def __init__(self):
        self.gain = 100.0
        self.phase = 0.0

    def trigger(self):
        logging.info("the sensor simulator has been trigger")
        self.gain = random(0.0, 1.0)
        self.phase = random(0.0, 2 * math.pi)
