from math import log10
import matplotlib.pyplot as plt
"""
Stellen Sie die Werte von $A_{db}(omega)$ zusammen mit den Werten der Dämpfung aus Aufgabe 1 in einem Diagramm über der Frequenz dar.
"""


def berechne_daempfung(s21):
    return 10 * log10(1 / (s21 ** 2))


if __name__ == "__main__":
    frequencies = [0.1, 0.3, 0.6, 0.8, 0.9, 1, 1.3, 1.8, 2, 2.5, 3.5, 6, 10, 20]

    transmittanzen_aufgabe_1 = [0.05, 0.14, 0.29, 0.35, 0.384, 0.422, 0.516, 0.636, 0.684, 0.768, 0.856, 1, 1, 1]
    transmittanzen = [0.004, 0.008, 0.01, 0.01, 0.01, 0.01, 0.076, 0.38, 0.56, 0.7, 0.68, 0.76, 0.88, 0.964]
    daempfungen = [berechne_daempfung(transmittanz) for transmittanz in transmittanzen]
    daempfungen_aufgabe_1 = [berechne_daempfung(transmittanz) for transmittanz in transmittanzen_aufgabe_1]

    fig = plt.figure()
    ax = fig.add_subplot(2, 1, 1)
    ax.plot(frequencies, daempfungen, marker='D', mfc='red', mec='k')
    ax.plot(frequencies, daempfungen_aufgabe_1, marker='x', mfc='blue', mec='k')
    ax.set_xscale('log')
    ax.set_xlabel('Frequenz')
    ax.set_ylabel("Phase - A($\omega$)")
    plt.show()
