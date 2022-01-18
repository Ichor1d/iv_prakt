import matplotlib.pyplot as plt
"""
 Stellen Sie die Werte von $B(omega)$ zusammen mit den Werten von $B(omega)$ aus Aufgabe 1 in einem Diagramm
 über der Frequenz dar.
"""


def calculate_phase(f, t):
    # da der Zeitpunkt t in ms, die Frequenz in kHz kürzt sich sich die Einheiten vollständig raus.
    phase = (-360) * f * t
    if phase < 0:
        while phase < 0:
            phase += 360
    elif phase > 360:
        while phase > 360:
            phase -= 360

    return phase


if __name__ == '__main__':
    # die Frequenzen in kHz
    frequencies = [0.1, 0.3, 0.6, 0.8, 0.9, 1, 1.3, 1.8, 2, 2.5, 3.5, 6, 10, 20]

    # Zeitpunkt des Nulldurchlaufs einer positiven Taktflanke in ms
    nulls_aufgabe_1 = [-12.5, -0.8, 1.3, -0.26, -0.23, -0.2, -0.908, -1.188, -0.068, 0.346, 0.542, -0.178, -0.305, -0.151]
    nulls_aufgabe_2 = [-2.5, -1, -0.5, 2, -5, -2.6, -2, -0.2999, -0.2335, -0.1275, 0.2225, -0.0275, -0.0105, 0.047]
    betriebsphasen_aufgabe_1 = [calculate_phase(frequencies[i], null) for i, null in enumerate(nulls_aufgabe_1)]
    betriebsphasen_aufgabe_2 = [calculate_phase(frequencies[i], null) for i, null in enumerate(nulls_aufgabe_2)]

    fig = plt.figure()
    ax = fig.add_subplot(2, 1, 1)
    ax.plot(frequencies, betriebsphasen_aufgabe_1, marker='D', mfc='red', mec='k')
    ax.plot(frequencies, betriebsphasen_aufgabe_2, marker='x', mfc='red', mec='k')
    ax.set_xscale('log')
    ax.set_xlabel('Frequenz')
    ax.set_ylabel("Phase - B($\omega$)")
    plt.show()
