import numpy as np
from scipy import linalg

tol = 0.0001
it_max = 100

X1 = np.array([1, 1, 1])
X = np.array([2, 3])


def f1(V):
    x, y, z = V
    S = np.array([16*x**4+16*y**4+z**4-16,
                  x**2+y**2+z**2-3,
                  x**3-y+z-1
                  ])
    return S


def j1(V):
    x, y, z = V
    J = np.array([[64*x**3, 64*y**3, 4*z**3],
                  [2*x, 2*y, 2*z],
                  [3*x**2, -1, 1]
                  ])
    return J


def f(V):
    x, y = V
    S = np.array([x+2*y-2,
                  x**2+4*y**2-4])
    return S


def j(V):
    x, y = V
    J = np.array([[1, 2],
                  [2*x, 8*y]])
    return J


# utilizando a funcao do numpy np.linalg.inv para
# matriz inversa do jacobiano e np.linalg.norm
# para calculo da norma euclidiana de um vetor

# B = np.eye(2)
B = j(X)


def broyden(X, B):
    it = 0
    err = 10
    while (err >= tol) and (it < it_max):
        J = np.copy(B)

        F = f(X)
        F = np.reshape(F, (-1, 1))

        delta = linalg.solve(J, -F)

        X = np.reshape(X, (-1, 1)) + delta
        X = X + delta

        Y = f(X)
        Y = np.reshape(Y, (-1, 1))
        Y = Y - F
        err = np.linalg.norm(delta)/np.linalg.norm(X)

        print("ITER ", it, "|X = ", np.reshape(np.round(X, 3), (1, -1)), " | Err = %.5f" % err,  "|\n delta:",
              np.reshape(np.round(delta, 3), (1, -1)), "\n B:\n", np.round(B, 3))

        aux = (Y - np.dot(B, delta))
        numerador = np.dot(aux, np.transpose(delta))
        denominador = np.dot(np.transpose(delta), delta)
        B = B + np.divide(numerador, denominador)
        it += 1

    return (X, it)


print("\nMÉTODO DE BROYDEN MULTI-DIMENSIONAL\n")
X, i = broyden(X, B)

if i == it_max:
    print("O método não convergiu")
print("\nSolução X = ",  np.reshape(np.round(X, 3), (1, -1)))
