import numpy as np
import matplotlib.pyplot as plt

# Definimos la función cuadrada que queremos analizar


def f(t, A, T):
    return A * np.sign(np.sin(2*np.pi*t/T))


# Definimos el intervalo de tiempo en el que queremos analizar la función (en este caso, de 0 a T)
T = 5   # Periodo de la señal
t = np.linspace(0, T, 10000)

# Definimos la amplitud de la señal
A = 5

# Definimos el número de términos de la serie de Fourier que queremos calcular
num_terminos = 50

# Calculamos los coeficientes de la serie de Fourier utilizando la fórmula correspondiente
a0 = 1/T * np.trapz(f(t, A, T), t)
an = np.zeros(num_terminos)
bn = np.zeros(num_terminos)
for n in range(1, num_terminos+1):
    an[n-1] = 2/T * np.trapz(f(t, A, T) * np.cos(2*np.pi*n*t/T), t)
    bn[n-1] = 2/T * np.trapz(f(t, A, T) * np.sin(2*np.pi*n*t/T), t)

# Calculamos la aproximación de la función original utilizando la serie de Fourier
f_aprox = a0/2
for n in range(1, num_terminos+1):
    f_aprox += an[n-1] * np.cos(2*np.pi*n*t/T) + \
        bn[n-1] * np.sin(2*np.pi*n*t/T)

# Graficamos la función original y su aproximación utilizando la serie de Fourier
plt.plot(t, f(t, A, T), label='Función original')
plt.plot(t, f_aprox, label=f'Serie de Fourier ({num_terminos} términos)')
plt.xlabel('Tiempo')
plt.ylabel('Amplitud')
plt.title('Aproximación de la función cuadrada utilizando la serie de Fourier')
plt.legend()
plt.grid(True)
plt.show()
