# Necesitamos una funcion que
#   > Tome como entradas
#       -/ fuerza al carro
#       -/ posicion angular
#       -/ velocidad angular
#   > Segun las constantes del sistema, podamos obtener
#       -/ posicion angular
#       -/ velocidad angular

import numpy as np
from scipy import constants


M_CARRITO = 2
M_PERTIGA = 1
L_PENDULO = 1

# Discretizacion del tiempo en intervalos delta T (dT)
dT = 0.0001



def response(pos, vel, f):
    "Funcion que da respuesta al sistema diseñado. Toma como entradas la posicion, velocidad y fuerzas del sistema en t y devuelve la posicion y velocidad en t + 1"
    acel = aceleracion(pos, vel, f)
    vel = vel + acel*dT
    pos = pos + vel*dT + (acel*np.power(dT,2)/2)

    return pos, vel



def aceleracion(theta,v,f):
    numerador = constants.g * np.sin(theta) + np.cos(theta) * ((-f - M_PERTIGA * L_PENDULO * np.power(v, 2) * np.sin(theta)) / (M_CARRITO + M_PERTIGA))

    denominador = L_PENDULO * (4/3 - (M_PERTIGA * np.power(np.cos(theta), 2) / (M_CARRITO + M_PERTIGA)))

    return numerador/denominador


