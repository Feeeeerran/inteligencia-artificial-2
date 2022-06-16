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
vel_0 = pi/40
f_0 = 0
dT = 0.001

# Se obtienen posicion y velocidad consecuentes
pos, vel, acel = response(pos_0, vel_0, f_0, dT)

largo = 10000
vector_t = [0]*largo
vector_pos = [0]*largo
vector_vel = [0]*largo
vector_acel = [0]*largo

# Empieza la iteracion hasta lograr el equilibrio --> dado por las reglas
for i in range(largo):

        # Borrosificamos partiendo de los valores de pos y vel
        pertenencia_pos = borrosificar(pos,dom_posicion)
        pertenencia_vel = borrosificar(vel,dom_velocidad)

        # print(pertenencia_pos)
        # print(pertenencia_vel)

        # Con los valores borrosificados, aplicamos el controlador
        f = controlador_difuso(pertenencia_pos, pertenencia_vel, conjunto_fuerza, dom_fuerza, reglas)

        pos, vel, acel = response(pos, vel, f, dT)

        if i != 0:
                vector_t[i] = vector_t[i-1] + dT

        vector_pos[i] = pos
        vector_vel[i] = vel
        vector_acel[i] = acel

#     print(pos*180/pi)

fig, ax = plt.subplots()
ax.plot(vector_t, vector_pos)

ax.set(xlabel='time (s)', ylabel='theta')       #, title='Delta t = ' + str(delta_t) + " s")
ax.grid()

fig1, ax1 = plt.subplots()
ax1.plot(vector_t, vector_vel)

ax1.set(xlabel='time (s)', ylabel='veloc')       #, title='Delta t = ' + str(delta_t) + " s")
ax1.grid()

fig2, ax2 = plt.subplots()
ax2.plot(vector_t, vector_acel)

ax2.set(xlabel='time (s)', ylabel='acel')       #, title='Delta t = ' + str(delta_t) + " s")
ax2.grid()

plt.show()
