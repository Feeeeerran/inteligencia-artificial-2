import os


def AStar(p1,p2,grilla):
    listaAbierta = []
    listaCerrada = []
    # Encontramos los nodos de partida y llegada
    # No partimos desde la estanteria, partimos desde el frente de la misma
    for f in range(grilla.filas):
        for c in range(grilla.columnas):
            nodo = grilla.grilla[f][c]
            if nodo.id == p1:
                if p1%2 == 0:
                    p1 = grilla.grilla[f][c+1]
                else:
                    p1 = grilla.grilla[f][c-1]
            if nodo.id == p2:
                if p2%2 == 0:
                    p2 = grilla.grilla[f][c+1]
                else:
                    p2 = grilla.grilla[f][c-1]

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
                nodoActual.vecinos[i].setF(p2,nodoActual.c + 1/2)
                # Metemos los nodos vecinos a la listaAbierta
                listaAbierta.append(nodoActual.vecinos[i])

                # Para reconocer el path #########################################
                # if nodoActual.vecinos[i] not in listaCerrada:
                #     # Les decimos a los nodos vecinos que "vienen" del nodoActual
                #     nodoActual.vecinos[i].anterior = nodoActual

        listaAbierta.remove(nodoActual)
        listaCerrada.append(nodoActual)
    
    os.system("cls")
    print("Llegamos a destino")
    return nodoActual.c
