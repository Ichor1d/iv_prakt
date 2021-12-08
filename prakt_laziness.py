import matplotlib.pyplot as plt

frequencies = [0.1, 0.3, 0.6, 0.8, 0.9, 1, 1.3, 1.8, 2, 2.5, 3.5, 6, 10, 20]


def calculate_phase(i, t):
    # da der Zeitpunkt t in ms, die Frequenz in ks kürzt sich sich die Einheiten vollständig raus.
    phase = (-360) * frequencies[i] * t
    if phase < 0:
        while phase < 0:
            phase += 360
    else:
        while phase > 360:
            phase -= 360

    return phase


if __name__ == '__main__':
    amplitudes = []
    # Zeitpunkt eines Nulldurchlaufs in ms
    nulls = [-12.5, -0.8, 1.3, -0.26, -0.23, -0.2, -0.908, -1.188, -0.068, 0.346, 0.542, -0.178, -0.305, -0.151]
    phases = [calculate_phase(i, t) for i, t in enumerate(nulls)]

    print(phases)

    fig = plt.figure()
    ax = fig.add_subplot(2, 1, 1)
    ax.plot(frequencies, phases, marker='D', mfc='red', mec='k')
    ax.set_xscale('log')
    ax.set_xlabel('Frequenz')
    ax.set_ylabel("Phase - B($\omega$)")
    plt.show()
