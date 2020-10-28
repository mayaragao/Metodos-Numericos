import numpy as np
import matplotlib


def f(t, y):
    return -2*t*y**2


def ode_2_ordem(t0, tf, x0, der_x0, h, metodo):
    N = int((tf - t0)/h)
    X = np.zeros(N+1)
    T = np.zeros(N+1)
    T[0] = t0
    X[0] = x0
    der_X = der_x0
    for k in np.arange(1, N+1):
        T[k] = k*h
        if metodo == 1:
            # Serie de Taylor
            K = f(T[k-1], X[k-1], der_X)
            X[k] = X[k-1] + der_X*h + (K/2)*(h**2)
            der_X += K*h

        else:
            # Runge-Kutta-Nystron:
            K1 = (h/2)*f(T[k-1], X[k-1], der_X)
            Q = (h/2) * (der_X + K1/2)
            K2 = (h/2)*f(T[k-1] + h/2, X[k-1] + Q, der_X + K1)
            K3 = (h/2)*f(T[k-1] + h/2, X[k-1] + Q, der_X + K2)
            L = h*(der_X + K3)
            K4 = (h/2)*f(T[k-1] + h, X[k-1] + L, der_X + 2*K3)

            X[k] = X[k-1] + h*(der_X + (K1+K2+K3)/3)
            der_X += (K1 + 2*K2 + 2*K3 + K4)/3
    return T, X


t, x1 = ode_2_ordem(0, 10, 1, 1, 0.5, 1)
t2, x2 = ode_2_ordem(0, 10, 1, 1, 0.5, 2)
t3, x3 = ode_2_ordem(0, 10, 1, 1, 0.5, 3)

N = np.size(t)
print("t[N]    euler       rk2         rk4\n")
for i in np.arange(N):
    print(t[i], '   ', round(x1[i], 5), '   ',
          round(x2[i], 5), '   ', round(x3[i], 5))
