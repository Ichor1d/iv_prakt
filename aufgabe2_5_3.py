from math import log10
import matplotlib.pyplot as plt
"""
Rechnen Sie die Werte von $|S_{21}(j \omega)|$ in Werte der Betriebsdämpfung $A_{db}(\omega)$ um
"""


def berechne_daempfung(s21):
    return 10 * log10(1 / (s21 ** 2))


if __name__ == "__main__":
    transmittanzen = [0.004, 0.008, 0.01, 0.01, 0.01, 0.01, 0.076, 0.38, 0.56, 0.7, 0.68, 0.76, 0.88, 0.964]
    daempfungen = [berechne_daempfung(transmittanz) for transmittanz in transmittanzen]

    for daempfung in daempfungen:
        print(f"{daempfung:.2f} & ", end="")

