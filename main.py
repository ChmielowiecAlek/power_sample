import logging
import sys

from imc import Controller


def main():
    logging.getLogger().setLevel(logging.NOTSET)
    logging.info("Impedance matching in progress...")
    imc = Controller()
    imc.run(2000)  # 40 sec in 20 ms ticks
    logging.info("...impedance matching has finished")


if __name__ == '__main__':
    sys.exit(main())
