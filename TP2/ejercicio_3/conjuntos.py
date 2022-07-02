# Funciones conjunto
from random import triangular
from scipy import constants
import numpy as np
from funciones import *
pi = constants.pi


# Declaramos y definimos los conjuntos borrosos con los que trabajar ////////////////////
# Conjuntos borrosos para la posicion
dom_posicion = [
    [-3*pi/20, -pi/20],
    [-pi/10, 0],
    [-pi/20, pi/20],
    [0,      pi/10],
    [pi/20,  3*pi/20],
]

# Conjunto borroso para la velocidad
dom_velocidad = [
    [-pi/20, -pi/40],
    [-pi/20, 0],
    [-pi/40, pi/40],
    [0,      pi/20],
    [pi/40,  pi/20],
]

# Conjuntos borrosos de fuerza
dom_fuerza = {
    "NG":[-9,-3],
    "NP":[-6,0],
    "Z":[-3,3],
    "PP":[0,6],
    "PG":[3,9],
}

conjunto_fuerza = {}

# Tags nombres para conjuntos
tags = ["NG","NP","Z","PP","PG"]


# Generando los conjuntos para la F
ancho = dom_fuerza["PP"][1]
for i in range(len(tags)):
    cont = 0
    dom = dom_fuerza[tags[i]]
    centro = dom[0] + ancho/2
    vec = []
    dt = 0.1

    if i == 0:    
        for x in np.arange(-9,10,dt):           # POR QUE ESE RANGO? POR QUE EL 10?, NO ES 9+dt? o es aleatorio?
            xC = round(x,4)
            vec.append(round(hombro_der(xC,ancho,centro,1/3),4))
        conjunto_fuerza[tags[i]] = vec
        continue
    if i == 4:
        
        for x in np.arange(-9,10,dt):
            xC = round(x,4)
            vec.append(round(hombro_izq(xC,ancho,centro,1/3),4))
        conjunto_fuerza[tags[i]] = vec
        continue
    
    
    for x in np.arange(-9,10,dt):
        xC = round(x,4)
        vec.append(round(triangular(xC,ancho,centro,1/3),4))
    conjunto_fuerza[tags[i]] = vec



# reglas = {          
#     'NG':{
#         'NG':'NG',
#         'NP':'NP',
#         'Z':'NP',
#         'PP':'NP',
#         'PG':'Z'
#         },
#     'NP':{
#         'NG':'NG',
#         'NP':'NP',
#         'Z':'NP',
#         'PP':'Z',
#         'PG':'PP'
#         },
#     'Z':{
#         'NG':'NP',
#         'NP':'NP',
#         'Z':'Z',
#         'PP':'PP',
#         'PG':'PP'
#         },
#     'PP':{
#         'NG':'NP',
#         'NP':'Z',
#         'Z':'PP',
#         'PP':'PP',
#         'PG':'PG'
#         },
#     'PG':{
#         'NG':'Z',
#         'NP':'PP',
#         'Z':'PP',
#         'PP':'PG',
#         'PG':'PG'}
# }

    
