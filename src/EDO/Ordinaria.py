import numpy as np
import matplotlib


def f(t, y):
    return -2*t*y**2


def edo_1_ordem(t0, tf, x0, h, metodo):
    N = int((tf - t0)/h)
    X = np.zeros(N+1)
    T = np.zeros(N+1)
    X[0] = x0
    T[0] = t0
    for k in np.arange(1, N+1):
        T[k] = k*h
        if metodo == 1:
            # Método de Euler:
            K = f(T[k-1], X[k-1])
            X[k] = X[k-1] + K*h
        elif metodo == 2:
            # Método Runge-Kutta segunda ordem:
            K1 = f(T[k-1], X[k-1])
            K2 = f(T[k-1]+h, X[k-1] + h*K1)
            X[k] = X[k-1] + h*(K1+K2)/2
        else:
            K1 = f(T[k-1], X[k-1])
            K2 = f(T[k-1] + h/2, X[k-1] + (h/2)*K1)
            K3 = f(T[k-1] + h/2, X[k-1] + (h/2)*K2)
            K4 = f(T[k-1] + h, X[k-1] + h*K3)

            X[k] = X[k-1] + h*(K1 + 2*K2 + 2*K3 + K4)/6
    return T, X


t, x = edo_1_ordem(0, 10, 1, 0.5, 3)
N = np.size(t)
print("t[N]          x[N]\n")
for i in np.arange(N):
    print(t[i], '      ', round(x[i], 5))
