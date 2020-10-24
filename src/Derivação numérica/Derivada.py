import numpy as np


def f(x):
    return x**3 + 1/np.exp(x)

# regra=[1] - Diferença central
# regra=[2] - Passo à frente
# regra=[3] - Passo atrás


def derivada(x, delta, regra):
    if regra == 1:
        df = (f(x+delta) - f(x-delta))/(2*delta)
    elif regra == 2:
        df = (f(x+delta)-f(x))/delta
    else:
        df = (f(x) - f(x-delta))/delta
    return df

#p = {1,2}
# segue as mesmas regras de cima


def derivada_richard(x, delta, regra, p):
    df1 = derivada(x, delta, regra)
    delta2 = delta/2
    df2 = derivada(x, delta2, regra)
    q = delta/delta2
    a0 = df1 + (df1-df2)/(q**(-p) - 1)
    return a0


delta = 1.0e-4
x = 3
d = derivada(x, delta, 1)
dr = derivada_richard(x, delta, 1, 2)
print('A derivada no ponto x=', x, ' é:', d, '\nA derivada de richard é: ', dr)
