import numpy as np


def peso(N):
    if N == 1:
        w = np.array([0.0])
        x = np.array([1.7724538509055160272981674833411])
    elif N == 2:
        w = np.array(
            [0.8862269254527580136491, 0.8862269254527580136491])
        x = np.array([-0.7071067811865475244008, 0.7071067811865475244008])
    elif N == 3:
        w = np.array([0.295408975150919337883,
                      1.181635900603677351532, 0.295408975150919337883])
        x = np.array([-1.224744871391589049099, 0.0, 1.224744871391589049099])
    elif N == 4:
        w = np.array([0.081312835447245177143, 0.8049140900055128365061,
                      0.8049140900055128365061, 0.08131283544724517714303])
        x = np.array([-1.650680123885784555883, -0.5246476232752903178841,
                      0.5246476232752903178841, 1.650680123885784555883])
    elif N == 5:
        w = np.array([0.01995324205904591320774, 0.3936193231522411598285,
                      0.9453087204829418812257, 0.393619323152241159828, 0.01995324205904591320774])
        x = np.array([-2.020182870456085632929, -0.9585724646138185071128,
                      0.0, 0.9585724646138185071128, 2.020182870456085632929])
    elif N == 6:
        w = np.array([0.004530009905508845640857, 0.1570673203228566439163, 0.7246295952243925240919,
                      0.724629595224392524092, 0.1570673203228566439163, 0.004530009905508845640857])
        x = np.array([-2.350604973674492222834, -1.335849074013696949715, -0.4360774119276165086792,
                      0.436077411927616508679, 1.335849074013696949715, 2.350604973674492222834])
    elif N == 7:
        w = np.array([9.71781245099519154149e-4, 0.05451558281912703059218,
                      0.4256072526101278005203, 0.810264617556807326765,
                      0.4256072526101278005203, 0.0545155828191270305922,
                      9.71781245099519154149e-4])
        x = np.array([-2.651961356835233492447, -1.673551628767471445032,
                      -0.8162878828589646630387, 0.0, 0.8162878828589646630387,
                      1.673551628767471445032, 2.651961356835233492447])
    elif N == 8:
        w = np.array([1.99604072211367619206E-4, 0.0170779830074134754562, 0.2078023258148918795433, 0.6611470125582412910304,
                      0.6611470125582412910304, 0.2078023258148918795433, 0.0170779830074134754562, 1.996040722113676192061E-4])
        x = np.array([-2.930637420257244019224, -1.981656756695842925855, -1.157193712446780194721, -0.3811869902073221168547,
                      0.3811869902073221168547, 1.157193712446780194721, 1.981656756695842925855, 2.930637420257244019224])
    elif N == 9:
        w = np.array([3.960697726326438190459E-5, 0.00494362427553694721722, 0.088474527394376573288, 0.4326515590025557501998,
                      0.7202352156060509571243, 0.4326515590025557502, 0.088474527394376573288, 0.004943624275536947217225, 3.96069772632643819046E-5])
        x = np.array([-3.19099320178152760723, -2.266580584531843111802, -1.468553289216667931667, -0.7235510187528375733226,
                      0.0, 0.7235510187528375733226, 1.468553289216667931667, 2.266580584531843111802, 3.19099320178152760723])
    elif N == 10:
        w = np.array([7.64043285523262062916E-6, 0.001343645746781, 0.03387439445548, 0.2401386110823146864165, 0.61086263373257987836,
                      0.6108263373532, 0.24013861108, 0.033874394455481, 0.00134364574812326, 7.64043285523262062916E-6])
        x = np.array([-3.436159118837737603327, -2.532731674232789796409, -1.756683649299881773451, -1.036610829789513654178, -0.3429013272237046087892,
                      0.3429013272237046087892, 1.036610829789513654178, 1.756683649299881773451, 2.532731674232789796409, 3.436159118837737603327])
    else:
        w = np.zeros(N)
        x = np.ones(N)
    return w, x


def hermite(N):
    w, x = peso(N)
    soma = 0
    for i in np.arange(N):
        soma += f(x[i])*w[i]
    return soma


def f1(x):
    y = 1/np.sqrt(2*pi)*2/sqrt(2)*exp(-u**2)
    return y


def f(x):
    y = np.exp(-(x**2)/2)/(np.sqrt(2*np.pi))
    return y


N = int(input('''
**********************************************************************
    INTEGRAÇÃO NUMÉRICA - Gauss Hermite\n
    Quantos pontos deseja usar na integração?
    Escolha: '''))
if (N < 0) or (N > 10):
    N = 2

soma = hermite(N)
print("\n\n     Integral: ", round(soma, 6), "para ", N, " pontos \n")
