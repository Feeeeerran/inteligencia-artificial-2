from respuesta import response
from scipy import signal
import matplotlib.pyplot as pl
# FAM #################################################################
# Primer entrada por posicion (theta) y segunda entrada con velociada (theta')
# Por ejemplo, thetha[NP] con theta'[NG] --> NP

reglas = [
    ["NG","NG","NP","NP","Z"],
    ["NP","NP","NP","Z","PP"],
    ["NP","NP","Z","PP","PP"],
    ["NP","Z","PP","PP","PG"],
    ["Z","PP","PP","PG","PG"],
]


# Definir parametros iniciales != 0
pos_0 = 0
vel_0 = 0
f_0 = 0

# Se obtienen posicion y velocidad consecuentes
pos, vel = response(pos_0, vel_0, f_0)

# Empieza la iteracion hasta lograr el equilibrio --> dado por las reglas
for i in range(10):
    