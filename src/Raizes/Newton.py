import numpy as np

tol = 0.0005
x0 = 10
it_max = 100


def f(x): return x**2 - 4*np.cos(x)
def fder(x): return 2*x + 4*np.sin(x)


def f2(x): return 4*np.cos(x) - np.exp(2*x)
def f2der(x): return (-4*np.sin(x) - np.exp(2*x)*2)


def f3(x):
    g = 9.806
    k = 0.00341
    y = math.log(math.cosh(x * (g*k)**0.5))-50
    return y


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


x, i = newton(x0, tol, it_max)
if i == it_max:
    print("O método nao convergiu")
print("A raiz exata é x= %.5f" % x)
