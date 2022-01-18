from math import log10
import matplotlib.pyplot as plt
"""
 Stellen Sie die Werte von $A_{db}(omega)$ in einem Diagramm über der Frequenz dar.
 Verwenden Sie eine logarithmisch skalierte Frequenzachse.
"""


def berechne_daempfung(s21):
    return 10 * log10(1 / (s21 ** 2))


if __name__ == "__main__":
    frequencies = [0.1, 0.3, 0.6, 0.8, 0.9, 1, 1.3, 1.8, 2, 2.5, 3.5, 6, 10, 20]
    transmittanzen = [0.05, 0.14, 0.29, 0.35, 0.384, 0.422, 0.516, 0.636, 0.684, 0.768, 0.856, 1, 1, 1]
    daempfungen = [berechne_daempfung(transmittanz) for transmittanz in transmittanzen]

    fig = plt.figure()
    ax = fig.add_subplot(2, 1, 1)
    ax.plot(frequencies, daempfungen, marker='D', mfc='red', mec='k')
    ax.set_xscale('log')
    ax.set_xlabel('Frequenz')
    ax.set_ylabel("Daempfung - A($\omega$)")
    plt.show()
