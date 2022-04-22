import os

# Propios
from grilla.grilla import Grilla
from ejercicio_2.temple_simulado import simAnnealing
# from a_estrella.a_estrella import AStar

os.system("cls")


# Instanciamos grilla
G = Grilla()
# Menu para seleccionar que usar 🤔?


# La grilla viene por defecto con estanterias 3x3x2 (36 estanterias)
# Decimos que viene con esos valores por defecto, preguntamos si se quiere o no
# Si se quieren entonces seteamos filas y columnas
G.setFilasColumnas()
G.setGrilla()
G.asignarVecinos()

# Deberiamos tener una grilla 3x3x2


# Probando temple simulado
orden = [12,5,8,1,3,6]
carga = G.grilla[0][0]
descarga = G.grilla[0][0]


nuevoOrden,costo = simAnnealing(orden,carga,descarga,G)
print(nuevoOrden)
print("Costo", costo)



