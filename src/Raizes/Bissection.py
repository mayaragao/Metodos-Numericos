import math


a = 0
b = 10
tol = 0.0001


def f2(x):
    y = 4*math.cos(x) - math.exp(2*x)
    return y


def f3(x):
    g = 9.806
    k = 0.00341
    y = math.log(math.cosh(x * (g*k)**0.5))-50
    return y


def f(x):
    y = x**2 - 4*math.cos(x)
    return y


def ordena(a, b):
    if a < b:
        return a, b
    return b, a


def bissecao(a, b, tol):
    a, b = ordena(a, b)
    err = abs(b-a)
    aux = a
    it = 0

    while err >= tol:
        x = (a+b)/2.0
        print("ITER ", it, "|a = %.5f" % a, "|b = %.5f" % b, "|x = %.5f" % x, "|f(x) = %.4f" %
              f(x), "| Err = %.4f" % err)
        if f(x)*f(a) < 0:
            b = x
        elif f(x)*f(a) > 0:
            a = x
        else:
            return x
        err = abs(x-aux)
        aux = x
        it += 1
    print("ITER ", it, "|a = %.5f" % a, "|b = %.5f" % b, "|x = %.5f" % x, "|f(x) = %.4f" %
          f(x), "| Err = %.4f" % err)
    return x


x = bissecao(a, b, tol)
print("A raiz exata é x= %.5f" % x)
