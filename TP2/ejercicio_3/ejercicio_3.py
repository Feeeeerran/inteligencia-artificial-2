# from TP2.ejercicio_3.controlador import controlador_disfuso
from respuesta import response
from conjuntos import *
from borrosificador import *
from controlador import *

import matplotlib.pyplot as pl
# FAM #################################################################

# Primer entrada por posicion (theta) y segunda entrada con velociad (theta')
# Por ejemplo, thetha[NP] con theta'[NG] --> NP
# reglas = [
#     ["NG","NG","NP","NP","Z"],
#     ["NP","NP","NP","Z","PP"],
#     ["NP","NP","Z","PP","PP"],
#     ["NP","Z","PP","PP","PG"],
#     ["Z","PP","PP","PG","PG"],
# ]


reglas = {'NG':{'NG':'NG','NP':'NP','Z':'NP','PP':'NP','PG':'Z'},
               'NP':{'NG':'NG','NP':'NP','Z':'NP','PP':'Z','PG':'PP'},              
               'Z':{'NG':'NP','NP':'NP','Z':'Z','PP':'PP','PG':'PP'},
               'PP':{'NG':'NP','NP':'Z','Z':'PP','PP':'PP','PG':'PG'},
               'PG':{'NG':'Z','NP':'PP','Z':'PP','PP':'PG','PG':'PG'}}


# Desde el archivo de conjuntos, traemos los dominios necesarios para trabajar


# Definir parametros iniciales != 0
pos_0 = pi/20
vel_0 = -pi/40
f_0 = 0


# Se obtienen posicion y velocidad consecuentes
pos, vel = response(pos_0, vel_0, f_0)

# Empieza la iteracion hasta lograr el equilibrio --> dado por las reglas
for i in range(3000):

    # Borrosificamos partiendo de los valores de pos y vel
    pertenencia_pos = borrosificar(pos,dom_posicion)
    pertenencia_vel = borrosificar(vel,dom_posicion)

    # print(pertenencia_pos)
    # print(pertenencia_vel)

    # Con los valores borrosificados, aplicamos el controlador
    f = controlador_difuso(pertenencia_pos, pertenencia_vel, conjunto_fuerza, dom_fuerza, reglas)
    
    pos, vel = response(pos, vel, f)

    print(pos*180/pi)


