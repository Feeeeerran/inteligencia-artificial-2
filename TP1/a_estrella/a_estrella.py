import os

# P1 y p2 tienen que ser nodos (instancias de Nodo) de la grilla
def AStar(p1,p2,grilla):
    listaAbierta = []
    listaCerrada = []
    # Encontramos los nodos de partida y llegada
    # No partimos desde la estanteria, partimos desde el frente de la misma
    if p1.id%2 == 0:
        p1 = grilla.grilla[p1.y][p1.x+1]
    else:
        p1 = grilla.grilla[p1.y][p1.x-1]
    if p2.id%2 == 0:
        p2 = grilla.grilla[p2.y][p2.x+1]
    else:
        p2 = grilla.grilla[p2.y][p2.x-1]

    # Set inicial para que el algoritmo arranque tranquilo 😎
    listaAbierta.append(p1)
    listaAbierta[0].setF(p2,0)
    nodoActual = None


    while len(listaAbierta) != 0 and nodoActual != p2:
        menorF = listaAbierta[0].f
        for i in range(len(listaAbierta)):

            if listaAbierta[i].f <= menorF:
                menorF = listaAbierta[i].f
                nodoActual = listaAbierta[i]

        
        for i in range(len(nodoActual.vecinos)):
            if nodoActual.vecinos[i] not in listaAbierta and not nodoActual.vecinos[i].estanteria:
                # Seteamos el f = h + c

                # ################ Si disminuimos el coste a 1/2 el algoritmo es mas preciso
                nodoActual.vecinos[i].setF(p2,nodoActual.c + 1)
                # Metemos los nodos vecinos a la listaAbierta
                listaAbierta.append(nodoActual.vecinos[i])

                # Para reconocer el path #########################################
                # if nodoActual.vecinos[i] not in listaCerrada:
                #     # Les decimos a los nodos vecinos que "vienen" del nodoActual
                #     nodoActual.vecinos[i].anterior = nodoActual

        listaAbierta.remove(nodoActual)
        listaCerrada.append(nodoActual)
        # break
    
    # os.system("cls")
    # print("Llegamos a destino")
    return nodoActual.c
