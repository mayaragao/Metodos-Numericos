import matplotlib.pyplot as plt
import numpy as np
% matplotlib inline

# Cria uma lista de pontos igualmente espaçados:
# numpy.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None, axis=0)
X = np.linspace(-5, 5, 21)


def f(x): return x**3-9*x+3


plt.plot(X, f(X))
plt.grid()
plt.show()
