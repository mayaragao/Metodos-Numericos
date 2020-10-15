import numpy as np

a = 0
b = 1


def f1(x):
    y = np.exp(-x**2)
    return y


def f(x):
    y = np.exp(-(x**2)/2)/(np.sqrt(2*np.pi))
    return y


def peso(a, b, X, N):
    V = np.eye(N)
    y = np.zeros(N)
    for i in np.arange(N):
        y[i] = (b**(i+1) - a**(i+1))/(i+1)
        for j in np.arange(N):
            V[i, j] = X[j]**i

    w = np.linalg.solve(V, y)
    return w


def polinomial(a, b, N):
    X = np.linspace(a, b, N)
    P = peso(a, b, X, N)
    soma = 0
    for i in np.arange(N):
        y = f(X[i])
        soma += y*P[i]
    return (X, soma)


print("\nINTEGRAÇÃO NUMÉRICA - Interpolação Polinomial\n")
N = int(input('''
**********************************************************************
    INTEGRAÇÃO NUMÉRICA - Interpolação Polinomial\n
    Quantos pontos deseja usar na integração?
    Escolha: '''))


X, soma = polinomial(a, b, N)
print("\n\n       Integral: ", round(soma, 6), "nos pontos ", np.round(X, 4))
