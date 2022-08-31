import logging
import sys

from imc import ImpedanceMatchingController


def main():
    logging.getLogger().setLevel(logging.NOTSET)
    logging.info("The Impedance Matching Controller will run...")
    imc = ImpedanceMatchingController()
    imc.run(2000)  # 40 sec in 20 ms ticks
    logging.info("The Impedance Matching Controller has finished")

if __name__ == '__main__':
    sys.exit(main())
