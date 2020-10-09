import numpy as np

tol = 0.0001
x0 = 10
it_max = 100


def f1(x): return x**2 - 4*np.cos(x)


def f(x): return 4*np.cos(x) - np.exp(2*x)


cte = (9.806*0.00341)**0.5
def f3(x): return np.log(np.cosh(x * cte))-50


def secante(x0, tol, it_max):
    delta = 0.001
    x1 = x0 + delta
    fa = f(x0)
    it = 0
    err = 10
    while (err >= tol) and (it < it_max):
        fi = f(x1)
        x2 = x1 - (fi*(x1-x0)/(fi-fa))
        err = abs(x2-x1)
        print("ITER ", it, "|x", it, " = %.3f" % x0, "|x", it+1, " = %.3f" % x1, "|x", it+2, " = %.4f" %
              x2, "| Err = %.5f" % err)
        x0 = x1
        x1 = x2

        fa = fi
        it += 1

    return (x1, it)


print("\nMÉTODO DE SECANTE\n")
x, i = secante(x0, tol, it_max)
if i == it_max:
    print("O método não convergiu")
print("Raiz encontrada x= %.5f" % x)
