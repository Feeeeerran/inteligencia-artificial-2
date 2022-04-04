# Ferran is here
# import numpy as np
from p5 import *

# Clases propias
from nodo import Nodo

# Faltaria un while para revisar que este todo ok? 
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
filas = int(input("Ingrese cantidad de filas de estanterias: "))
columnas = int(input("Ingrese cantidad de columnas de estanterias: "))
largo = int(input("Ingrese largo de la estanteria (suma filas): "))
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

# Las estanterias estan separadas entre si por un espacio entre filas y columnas
# El espacio no depende del largo de la estanteria
filas = (filas*largo) + filas + 1
columnas = columnas*2 + columnas + 1

# Grilla para llevar la cuenta y dibujar
grilla = []


cont = 1
for f in range(filas):
    grilla.append([])
    for c in range(columnas):
        # No es pasillo
        if f%(largo + 1) != 0 and c%3 != 0:
            grilla[f].append(Nodo(c,f,cont))
            grilla[f][c].estanteria = True
            cont += 1
        else:
            grilla[f].append(Nodo(c,f))



# print(grilla)
print('Filas son',len(grilla),' bloques')
print('Columnas',len(grilla[0]),' bloques')


for f in range(filas):
    for c in range(columnas):
        nodo = grilla[f][c]
        print("Nodo pos x:{} y:{}".format(nodo.x,nodo.y))
        print("Nodo id = {}".format(nodo.id))
        print("\n")


# p1 = int(input("Ingrese punto de salida: "))
# p2 = int(input("Ingrese punto de llegada: "))


# Se necesitan 2 listas
# Lista abierta
#   Van los nodos que no hemos visitado y tenemos que evaluar
# Lista cerrada
#   Van los nodos que ya hemos visitado y no volvemos a visitar







# #################### Tema libreria y tal ############################

def setup():
    size(columnas*100,filas*100)
    background(255)

def draw():
    for f in range(filas):
        for c in range(columnas):
            nodo = grilla[f][c]
            fill(255)
            if nodo.estanteria:
                fill(155)
            rect(nodo.x*75,nodo.y*75,75,75)
            no_fill()







run()