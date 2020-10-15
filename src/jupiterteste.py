import numpy as np
import matplotlib.pyplot as plt
%matplotlib notebook

X = np.linspace(-5, 5, 100)


def f(x): return 4 * np.cos(x) - np.exp(2*x)


F = np.vectorize(f)

plt.plot(X, F(X))
plt.ylim(-20, 30)
plt.grid()
plt.show()
