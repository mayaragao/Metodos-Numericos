import numpy as np

tol = 0.0005
x0 = 10
it_max = 100


def f1(x): return x**2 - 4*np.cos(x)
def f1der(x): return 2*x + 4*np.sin(x)


def f(x): return 4*np.cos(x) - np.exp(2*x)
def fder(x): return (-4*np.sin(x) - np.exp(2*x)*2)


cte = (9.806*0.00341)**0.5
def f3(x): return np.log(np.cosh(x * cte))-50
def f3der(x): return (cte*np.sinh(x * cte)/np.cosh(x * cte))


def newton(x0, tol, it_max):
    it = 0
    err = 10

    while (err >= tol) and (it < it_max):
        x = x0 - f(x0)/fder(x0)
        err = abs(x-x0)
        print("ITER ", it, "|x = %.3f" % x0, "|f(x) = %.4f" %
              f(x0), "| f'(x) = %.4f" % fder(x0), "| Err = %.5f" % err)
        x0 = x
        it += 1

    return (x, it)


print("\nMÉTODO DE NEWTON\n")
x, i = newton(x0, tol, it_max)
if i == it_max:
    print("O método não convergiu")
print("Raiz encontrada x= %.5f" % x)
