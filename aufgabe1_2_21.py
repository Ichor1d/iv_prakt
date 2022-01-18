import matplotlib.pyplot as plt
"""
 Stelle Sie die Werte von B(omega) in einem Diagramm über der Frequenz dar.
 Verwenden Sie für eine logarithmische skalierte Frequenzachse.
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
    nulls = [-12.5, -0.8, 1.3, -0.26, -0.23, -0.2, -0.908, -1.188, -0.068, 0.346, 0.542, -0.178, -0.305, -0.151]
    betriebsphasen = [calculate_phase(frequencies[i], null) for i, null in enumerate(nulls)]

    fig = plt.figure()
    ax = fig.add_subplot(2, 1, 1)
    ax.plot(frequencies, betriebsphasen, marker='D', mfc='red', mec='k')
    ax.set_xscale('log')
    ax.set_xlabel('Frequenz')
    ax.set_ylabel("Phase - B($\omega$)")
    plt.show()
