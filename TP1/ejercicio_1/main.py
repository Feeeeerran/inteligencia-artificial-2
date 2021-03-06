from p5 import *
import os

# Clases propias
from nodo import Nodo

# Faltaria un while para revisar que este todo ok? 
os.system("cls")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
filas = int(input("Ingrese cantidad de filas de estanterias: "))
columnas = int(input("Ingrese cantidad de columnas de estanterias: "))
largo = int(input("Ingrese largo de la estanteria (suma filas): "))
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

# Las estanterias estan separadas entre si por un espacio entre filas y columnas
# El espacio no depende del largo de la estanteria
filas = (filas*largo) + filas + 1
columnas = columnas*2 + columnas + 1

grilla = None
listaAbierta = None
listaCerrada = None



# El usuario determina punto de entrada y llegada
p1 = int(input("Determine el id de estanteria de salida "))
p2 = int(input("Determine el id de estanteria de llegada "))
        
        
# #################### Tema libreria y tal ############################
def setup():
    # Traemos las variables para poder trabajar dentro del scope
    global filas, columnas
    global grilla
    global listaAbierta, listaCerrada
    global p1, p2
    
    
    size(columnas*100,filas*100)
    # size(500,500)
    background(255)



    # Setup de la grilla 
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
    
    listaAbierta = []
    listaCerrada = []

    listaAbierta.append(p1)
    listaAbierta[0].setF(p2,0)

    

    

# # Usamos draw directamente a modo de bucle, usamos la funcion no_loop para dejar de dibujar y a su vez iterar
flag = False
nodoActual = False
def draw():
    global filas, columnas
    global grilla
    global listaAbierta, listaCerrada
    global p1, p2


    # Para dibujar la grilla una sola vez
    global flag
    global nodoActual
    # Escala de los cuadros de la grilla
    escala = 75

    # Imprimimos la grilla una sola vez
    if not flag:
        for f in range(filas):
            for c in range(columnas):
                grilla[f][c].mostrar(255,255,255,escala)
                if grilla[f][c].estanteria:
                    grilla[f][c].mostrar(90,90,120,escala)
        flag = True


    
    if len(listaAbierta) != 0 and nodoActual != p2:
        menorF = listaAbierta[0].f
        for i in range(len(listaAbierta)):

            if listaAbierta[i].f <= menorF:
                menorF = listaAbierta[i].f
                nodoActual = listaAbierta[i]

        
        for i in range(len(nodoActual.vecinos)):
            if nodoActual.vecinos[i] not in listaAbierta and not nodoActual.vecinos[i].estanteria:
                # Seteamos el f = h + c

                # ################ Si disminuimos el coste a 1/2 el algoritmo es mas preciso
                nodoActual.vecinos[i].setF(p2,nodoActual.c + 1/2)
                # Metemos los nodos vecinos a la listaAbierta
                listaAbierta.append(nodoActual.vecinos[i])


                if nodoActual.vecinos[i] not in listaCerrada:
                    # Les decimos a los nodos vecinos que "vienen" del nodoActual
                    nodoActual.vecinos[i].anterior = nodoActual
                    nodoActual.vecinos[i].mostrar(82,255,136,escala)

        listaAbierta.remove(nodoActual)
        listaCerrada.append(nodoActual)
        
    else: 
        os.system("cls")
        print("Llegamos a destino")
        no_loop()

        # Funcion para cerrar la ventana
        # exit()
    

    for i in range(len(listaCerrada)):
        listaCerrada[i].mostrar(247,74,139,escala)

    nodoPath = nodoActual
    while nodoPath.anterior:
        nodoPath.mostrar(238,247,74,escala)
        nodoPath = nodoPath.anterior



def mouse_pressed():
    redraw()

# Para ver el grafico descomentar run()
run()