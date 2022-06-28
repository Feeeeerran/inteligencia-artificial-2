import numpy as np
import matplotlib.pyplot as plt

def triangular(x, ancho, centro, pendiente):
    if x <= centro - (ancho/2):
        return 0
    if x >= centro + (ancho/2):
        return 0

    if x > centro - (ancho/2) and x < centro:
        return pendiente*x + (-(centro -ancho/2)/(ancho/2))
    if x > centro and x < centro + (ancho/2):
        return -pendiente*x - (-(centro + ancho/2)/(ancho/2))
    
    return 1


def hombro_der(x, ancho, centro, pendiente):
    if x <= centro:
        return 1
    if x >= centro + (ancho/2):
        return 0

    if x > centro and x < centro + (ancho/2):
        return -pendiente*x - (-(centro + ancho/2)/(ancho/2))


def hombro_izq(x, ancho, centro, pendiente):
    if x < centro - (ancho/2):
        return 0
    if x >= centro:
        return 1

    if x >= centro - (ancho/2) and x < centro:
        return pendiente*x + (-(centro -ancho/2)/(ancho/2))


# Ploteo para verificar las formas
# x=np.linspace(-9,9,1000)
# y=np.array([hombro_izq(t,6,3,1/3) for t in x])
# plt.ylim(0,2)
# plt.plot(x,y)
# plt.show()