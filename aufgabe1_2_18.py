"""
18. Rechnen Sie |S_{21}(j omega)| in Werte der Betriebsdämpfung A_{db}(omega) um.
"""
from math import log10


def berechne_daempfung(s21):
    return 10 * log10(1 / (s21 ** 2))


if __name__ == "__main__":
    transmittanzen = [0.05, 0.14, 0.29, 0.35, 0.384, 0.422, 0.516, 0.636, 0.684, 0.768, 0.856, 1, 1, 1]
    daempfungen = [berechne_daempfung(transmittanz) for transmittanz in transmittanzen]

    for daempfung in daempfungen:
        print(f"{daempfung:.2f} & ")
