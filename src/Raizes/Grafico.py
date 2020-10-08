import matplotlib.pyplot as plt
import numpy as np
import math

# Cria uma lista de pontos igualmente espaçados:
# numpy.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None, axis=0)
X = np.linspace(-50, 100, 100)


def f(x): return x**3-9*x+3


def f2(x):
    y = 4*math.cos(x)
    g = - math.exp(2*x)
    return ( y + g )


def f3(x):
    g = 9.806
    k = 0.00341
    y = math.log(math.cosh(x * (g*k)**0.5))-50
    return y


def f4(x):
    y = x**2 - 4*math.cos(x)
    return y

F = np.vectorize(f2)

plt.plot(X, F(X))
plt.grid()
plt.show()
