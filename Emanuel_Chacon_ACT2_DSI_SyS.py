import numpy as np
import matplotlib.pyplot as plt

# Parametros
Fs = 1000       # Frecuencia de muestreo
T = 1/Fs
N = 1024
t = np.linspace(-1, 1, N)

# Señales
rect = np.where(np.abs(t) < 0.2, 1, 0)          # Pulso rectangular
u = np.where(t >= 0, 1, 0)                      # Escalon unitario
seno = np.sin(2*np.pi*5*t)                      # Senoidal 5 Hz

# Funcion de Fourier y graficas
def plot_fft(signal, title):
    S = np.fft.fft(signal)
    freq = np.fft.fftfreq(len(signal), T)
    mag = np.abs(S)
    fase = np.angle(S)

    plt.figure(figsize=(12,6))
    plt.subplot(1,3,1)
    plt.plot(t, signal)
    plt.title(f'{title} - Tiempo')
    plt.subplot(1,3,2)
    plt.stem(freq[:N//2], mag[:N//2])
    plt.title(f'{title} - Magnitud')
    plt.subplot(1,3,3)
    plt.stem(freq[:N//2], fase[:N//2])
    plt.title(f'{title} - Fase')
    plt.tight_layout()
    plt.show()

# Ejecutar
plot_fft(rect, "Pulso rectangular")
plot_fft(u, "Escalon unitario")
plot_fft(seno, "Señal senoidal")