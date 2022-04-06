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

print(columnas)
print(filas)



# El usuario determina punto de entrada y llegada
p1 = int(input("Determine el id de estanteria a llegar"))
p2X = int(input("Determine la coordenada x de entrada"))
p2Y = int(input("Determine la coordenada y de entrada"))




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
            
            if cont == p1:
                p1 = grilla[f][c]

            cont += 1
        else:
            grilla[f].append(Nodo(c,f))
        
        if f == p2Y and c == p2X:
            p2 = grilla[f][c]

        # Podria calcularse la f para cada nodo 🤔 (ver info.txt)


# Una vez obtenida la grilla con sus nodos, debemos determinar que vecinos comparte cada nodo
for f in range(filas):
    for c in range(columnas):
        nodo = grilla[f][c]

        # Vecinos horizontales
        if nodo.x > 0 and nodo.x < columnas-1:
            grilla[f][c].vecinos.append(grilla[f][c+1])
            grilla[f][c].vecinos.append(grilla[f][c-1])
        elif nodo.x == 0:
            grilla[f][c].vecinos.append(grilla[f][c+1])
        elif nodo.x == columnas-1:
            grilla[f][c].vecinos.append(grilla[f][c-1])

        # Vecinos verticales
        if nodo.y > 0 and nodo.y < filas-1:
            grilla[f][c].vecinos.append(grilla[f+1][c])
            grilla[f][c].vecinos.append(grilla[f-1][c])
        elif nodo.y == 0:
            grilla[f][c].vecinos.append(grilla[f+1][c])
        elif nodo.y == filas-1:
            grilla[f][c].vecinos.append(grilla[f-1][c])





# print(grilla)
# print('Filas son',len(grilla),' bloques')
# print('Columnas',len(grilla[0]),' bloques')


# Se necesitan 2 listas
# Lista abierta
#   Van los nodos que no hemos visitado y tenemos que evaluar
# Lista cerrada
#   Van los nodos que ya hemos visitado y no volvemos a visitar
listaAbierta = []
listaCerrada = []








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



# Para ver el grafico descomentar run()
# run()