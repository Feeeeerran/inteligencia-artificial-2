import os

# Propios
from grilla.grilla import Grilla
from a_estrella.a_estrella import *



os.system("cls")


# Instanciamos grilla
# Menu para seleccionar que usar 🤔?

print("Ejercicio 1")
M = Grilla()

# La grilla viene por defecto con estanterias 3x3x2 (36 estanterias)
# Decimos que viene con esos valores por defecto, preguntamos si se quiere o no
# Si se quieren entonces seteamos filas y columnas
M.setFilasColumnas()
M.setGrilla()
M.asignarVecinos()

# Deberiamos tener una grilla 3x3x2

# print(M.grilla[3][4].x)
# print(M.grilla[3][4].y)
# print(M.grilla[3][4].id)
print("Filas ",M.filas)
print("Columnas ",M.columnas)

coste = AStar(1,30,M)
print(coste)




