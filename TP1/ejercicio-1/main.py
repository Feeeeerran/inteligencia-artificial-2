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


# El usuario determina punto de entrada y llegada
p1 = int(input("Determine el id de estanteria de salida "))
p2 = int(input("Determine el id de estanteria de llegada "))



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

        if nodo.id == p1:
            if p1%2 == 0:
                p1 = grilla[f][c+1]
            else:
                p1 = grilla[f][c-1]
        if nodo.id == p2:
            if p2%2 == 0:
                p2 = grilla[f][c+1]
            else:
                p2 = grilla[f][c-1]





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

listaAbierta.append(p1)
listaAbierta[0].setF(p2,0)

nodoActual = listaAbierta[0]

while len(listaAbierta) != 0 and nodoActual != p2:
    # Evaluar los vecinos y calcular f
    menorF = listaAbierta[0].f
    for i in range(len(listaAbierta)):

        if listaAbierta[i].f <= menorF:
            menorF = listaAbierta[i].f
            nodoActual = listaAbierta[i]
        
    
    print(nodoActual.x)
    print(nodoActual.y)
    print(nodoActual.h)
    print("\n")

    for i in range(len(nodoActual.vecinos)):
        if nodoActual.vecinos[i] not in listaAbierta and not nodoActual.vecinos[i].estanteria:
            nodoActual.vecinos[i].setF(p2,nodoActual.c + 1/2)
            listaAbierta.append(nodoActual.vecinos[i])

    listaAbierta.remove(nodoActual)
    listaCerrada.append(nodoActual)


print("Estamos en el nodo final ",nodoActual.c)
print(len(listaAbierta))
print(len(listaCerrada))

        
        









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