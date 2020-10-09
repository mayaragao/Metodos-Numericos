import numpy as np

tol = 0.0001
it_max = 100

V = np.array([1, 1, 1])
V2 = np.array([2, 3])


def f(V):
    x, y, z = V
    S = np.array([16*x**4+16*y**4+z**4-16,
                  x**2+y**2+z**2-3,
                  x**3-y+z-1
                  ])
    return S


def j(V):
    x, y, z = V
    J = np.array([[64*x**3, 64*y**3, 4*z**3],
                  [2*x, 2*y, 2*z],
                  [3*x**2, -1, 1]
                  ])
    return J


def f2(V):
    x, y = V
    S = np.array([x+2*y-2,
                  x**2+4*y**2-4
                  ])
    return S


def j2(V):
    x, y = V
    J = np.array([[1, 2],
                  [2*x, 8*y]])
    return J

# utilizando a funcao do numpy np.linalg.inv para
# matriz inversa do jacobiano e np.linalg.norm
# para calculo da norma euclidiana de um vetor


def newton(V, tol, it_max):
    it = 0
    err = 10

    while (err >= tol) and (it < it_max):
        J = j(V)
        F = f(V)
        inv_J = np.linalg.inv(J)

        delta = - inv_J.dot(F)
        V = V + delta
        err = np.linalg.norm(delta)/np.linalg.norm(V)

        X = arredondando(V, 3)
        print("ITER ", it, "|X = ", X, " | Err = %.5f" % err)

        it += 1

    return (V, it)


def arredondando(A, x):
    n = np.shape(A)[0]
    X = np.copy(A)
    for i in np.arange(n):
        X[i] = round(A[i], x)
    return X


print("\nMÉTODO DE NEWTON MULTI-DIMENSIONAL\n")
X, i = newton(V, tol, it_max)
X = arredondando(X, 3)
if i == it_max:
    print("O método não convergiu")
print("\nSolução X = ",  X)
