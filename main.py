from imc import ImpedanceMatchingController


def main():
    print("Impedance Matching Controller")
    imc = ImpedanceMatchingController()
    imc.run(100000)
