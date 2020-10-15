import numpy as np

tol = 0.0001
it_max = 100

B1 = np.array([0, 1])

B = np.array([0, 1, 2])


def f(B):
    X = np.array([1, 2, 3])
    Y = np.array([1, 2, 9])
    b0, b1, b2 = B

    S = np.array([b0 + b1*(X[0]**b2) - Y[0],
                  b0 + b1*(X[1]**b2) - Y[1],
                  b0 + b1*(X[2]**b2) - Y[2],
                  ])
    return S


def j(B):
    b0, b1, b2 = B

    J = np.array([[1,  1,  0],
                  [1,  2**b2,  b1*(2**b2)*np.log(2)],
                  [1,  3**b2,  b1*(3**b2)*np.log(3)]
                  ])
    return J


def f1(B):
    X = np.array([1, 2, 3])
    Y = np.array([1.995, 1.41, 1.26])
    a, b = B
    S = np.array([np.exp((X[0]**a)/b) - Y[0],
                  np.exp((X[1]**a)/b) - Y[1],
                  np.exp((X[2]**a)/b) - Y[2]
                  ])
    return S


def j1(B):
    X = np.array([1, 2, 3])
    Y = np.array([1.995, 1.41, 1.26])
    a, b = B

    J = np.array([[X[0]**a * np.log(X[0])/b * np.exp((X[0]**a)/b),
                   -X[0]**a * (X[0]**a)/(b**2) * np.exp((X[0] ** a)/b)],
                  [X[1]**a * np.log(X[1])/b * np.exp((X[1]**a)/b),
                   -X[1]**a * (X[1]**a)/(b**2) * np.exp((X[1] ** a)/b)],
                  [X[2]**a * np.log(X[2])/b * np.exp((X[2]**a)/b),
                   -X[2]**a * (X[2]**a)/(b**2) * np.exp((X[2] ** a)/b)]
                  ])
    return J


# utilizando a funcao do numpy np.linalg.inv para
# matriz inversa do jacobiano e np.linalg.norm
# para calculo da norma euclidiana de um vetor

def minimos(B, tol, it_max):
    it = 0
    err = 10

    while (err >= tol) and (it < it_max):
        J = j(B)
        F = f(B)
        #F = np.reshape(F, (-1, 1))

        delta = np.linalg.solve(
            np.dot(np.transpose(J), J),  np.dot(np.transpose(J), -F))

        #B = np.reshape(B, (-1, 1)) + delta
        B = B + delta

        err = np.linalg.norm(delta)/np.linalg.norm(B)

        x = np.round(B, 3)
        print("ITER ", it, "|X = ",  x, " | Err = %.5f" % err)

        it += 1

    return (B, it)


print("\nMÉTODO DE MINIMOS QUADRADOS MULTI-DIMENSIONAL\n")
V, i = minimos(B, tol, it_max)
V = np.round(V, 4)
if i == it_max:
    print("O método não convergiu")
print("\nSolução X = ",  V)
