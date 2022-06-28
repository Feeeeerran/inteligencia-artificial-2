import numpy as np
import matplotlib.pyplot as plt

def hombro_der(x, ancho, centro, pendiente):
    if x < centro:
        return 1
    if x > centro + (ancho/2):
        return 0

    if x > centro and x < centro + (ancho/2):
        return -pendiente*x - (-(centro + ancho/2)/(ancho/2))


# x=np.linspace(-9,9,1000)
# y=np.array([hombro_der(t,6,-6,1/3) for t in x])
# plt.plot(x,y)
# plt.show()