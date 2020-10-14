import numpy as np

tol = 0.0001
x = [3, 5, 10]
x2 = [-0.1, 0, 0.5]
x3 = [200, 250, 300]
it_max = 100


def f(x): return x**2 - 4*np.cos(x)


def f2(x): return 4*np.cos(x) - np.exp(2*x)


cte = (9.806*0.00341)**0.5
def f3(x): return np.log(np.cosh(x * cte))-50


def maior_indice(y):
    if y[0] > y[1]:
        maior = 0
    else:
        maior = 1
    if maior > y[2]:
        return maior
    return 2


def inversa(x):
    it = 0
    err = 10
    x = sorted(x)
    x0 = 10**10
    y = [0, 0, 0]
    y[0] = f(x[0])
    y[1] = f(x[1])
    y[2] = f(x[2])

    while (err >= tol) and (it < it_max):
        phi0 = ((y[1]*y[2])/((y[0]-y[1])*(y[0]-y[2])))
        phi1 = ((y[0]*y[2])/((y[1]-y[0])*(y[1]-y[2])))
        phi2 = ((y[0]*y[1])/((y[2]-y[0])*(y[2]-y[1])))
        aux = phi0*x[0] + phi1*x[1] + phi2*x[2]

        err = abs(aux - x0)

        print("ITER ", it, "|x", it, " = %.3f" % x[0],
              "|x", it+1, " = %.3f" % x[1], "|x", it+2, " = %.4f" %
              x[2], "|y", it, " = %.3f" % y[0],
              "|y", it+1, " = %.3f" % y[1], "|y", it+2, " = %.4f" %
              y[2], "| x* = %.5f" % aux, "| Err = %.5f" % err)

        i = maior_indice(y)
        x[i] = aux
        y[i] = f(aux)
        x = sorted(x)
        y = sorted(y)
        x0 = aux
        it += 1

    return (aux, it)


print("\nMÉTODO DA INTERPOLAÇÃO INVERSA\n")
aux, i = inversa(x)
if i == it_max:
    print("O método não convergiu")
print("Raiz encontrada x= %.5f" % aux)
