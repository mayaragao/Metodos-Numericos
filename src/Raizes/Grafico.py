import matplotlib.pyplot as plt
import numpy as np

# Cria uma lista de pontos igualmente espaçados:
# numpy.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None, axis=0)
X = np.linspace(-5, 5, 100)


def f(x): return 4 * np.cos(x) - np.exp(2*x)


def f3(x):
    g = 9.806
    k = 0.00341
    y = np.log(np.cosh(x * np.sqrt(g*k)))-50
    return y


def f4(x):
    y = x**2 - 4*np.cos(x)
    return y


# modificar a funcao aqui
F = np.vectorize(f)

plt.plot(X, F(X))
plt.ylim(-20, 30)
plt.grid()
plt.show()
