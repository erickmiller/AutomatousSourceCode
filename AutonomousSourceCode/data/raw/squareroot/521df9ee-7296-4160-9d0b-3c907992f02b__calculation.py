import numpy as np


def root_mean_square(array):
    return (np.mean(array ** 2)) ** 0.5


def normalized(array):
    return array / max(array)


def spectrum(array):
    array *= np.hamming(len(array))  # window
    complex_array = np.fft.fft(array)  # fft
    complex_array = complex_array[:len(complex_array) // 2]  # del mirror part
    array = list(map(abs, complex_array))  # complex to float
    return array


def cepstrum(array):
    array *= np.hamming(len(array))
    complex_array = np.fft.fft(array)
    array = abs(complex_array)
    array = array[:(len(array) // 2)]
    complex_array = np.fft.ifft(array)
    array = abs(complex_array)
    array = array[:(len(array) // 2)]
    return array


def energy(array, size_chunk):
    list_energy = []
    for i in range(len(array) // size_chunk):
        l = array[i * size_chunk:i * size_chunk + size_chunk]
        list_energy.append(root_mean_square(l))
    l = []
    for i in range(len(list_energy) - 1):
        l.append(sum(list_energy[i:i + 2]) / 2)
    return l


def derivative(array):
    d = []
    for i in range(len(array) - 1):
        d.append(array[i + 1] - array[i])
    return d
