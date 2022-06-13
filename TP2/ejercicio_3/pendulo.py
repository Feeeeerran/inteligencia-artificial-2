import numpy as np
import matplotlib.pyplot as plt
from scipy import constants

CONSTANTE_M = 4 # Masa del carro (original: 2)
CONSTANTE_m = 3 # Masa de la pertiga (original: 1)
CONSTANTE_l = 1 # Longitud dela pertiga

th = []     #Vector de theta
veloc = []
acel = []
fuerza = []

t_max = 10
delta_t = 0.001
theta_0 = (20 * np.pi) / 180
v_0 = 0
a_0 = 0
f_0 = controladorDisfuso(conj_brorrosos_tita, conj_brorrosos_v, conj_brorrosos_F, theta_0, v_0)

def modelo(t_max, delta_t, theta_0, v_0, a_0, f_0):
    theta = theta_0
    v = v_0
    a = a_0
    f = f_0

    # Vector de tiempo
    x = np.arange(0, t_max, delta_t)
    for t in x:
        a = calcula_aceleracion(theta, v, f)
        v = v + a * delta_t
        theta = theta + v * delta_t + a * np.power(delta_t, 2) / 2
        f = controladorDisfuso(conj_brorrosos_tita, conj_brorrosos_v, conj_brorrosos_F, theta, v)

        th.append(theta)
        veloc.append(v)
        acel.append(a)
        fuerza.append(f)

    fig, ax = plt.subplots()
    ax.plot(x, th)

    ax.set(xlabel='time (s)', ylabel='theta', title='Delta t = ' + str(delta_t) + " s")
    ax.grid()

    plt.show()


# Calcula la aceleracion en el siguiente instante de tiempo dado el angulo y la velocidad angular actual, y la fuerza ejercida
def calcula_aceleracion(theta, v, f):
    numerador = constants.g * np.sin(theta) + np.cos(theta) * ((-f - CONSTANTE_m * CONSTANTE_l * np.power(v, 2) * np.sin(theta)) / (CONSTANTE_M + CONSTANTE_m))
    denominador = CONSTANTE_l * ((CONSTANTE_M/CONSTANTE_m) - (CONSTANTE_m * np.power(np.cos(theta), 2) / (CONSTANTE_M + CONSTANTE_m)))
    return numerador / denominador