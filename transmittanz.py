from math import pi, sqrt, log10
import matplotlib.pyplot as plt

frequencies = [0.1, 0.3, 0.6, 0.8, 0.9, 1, 1.3, 1.8, 2, 2.5, 3.5, 6, 10, 20]
amplitudes_in_mV = [25, 70, 145, 175, 192, 211, 258, 318, 342, 384, 428, 500, 500, 500]
omegas = [2*pi*x for x in frequencies]
r = 50
c = 680*(10**(-9))


def calc_trans(i):
    omega = omegas[i] * 1000
    s21 = (2*r*omega*c) / sqrt((2*r*omega*c)**2 + 1)
    return s21


if __name__ == '__main__':
    amps_in_V = [x * 10**-3 for x in amplitudes_in_mV]
    transmittanzen = [2*x for x in amps_in_V]
    trans_per_func = [calc_trans(i) for i, _ in enumerate(amps_in_V)]

    daempfung = [(10 * log10(1/x))**2 for x in transmittanzen]

    fig = plt.figure()
    ax = fig.add_subplot(2, 1, 1)
    ax.plot(frequencies, daempfung, marker='D', mfc='red', mec='k')
    ax.set_xscale('log')
    ax.set_xlabel('Frequenz')
    ax.set_ylabel("Daempfung - A($\omega$)")
    plt.show()
