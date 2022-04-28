import random

from a_estrella.a_estrella import *
from grilla.grilla import *
from ejercicio_2.temple_simulado import *
from genoma import Genoma

def geneticAlg(G, listaOrdenes):

    individuo = Genoma(1)
    delta = 0.1             # Ver cual es el valor optimo

    # Recorrer la grilla evaluando cada nodo de la misma
    # Formar un arreglo con los id de cada nodo
    i = 0
    for f in range(G.filas):
        for c in range(G.columnas):
            if G.grilla[f][c].id != 0:
                individuo.listaIds[i] = G.grilla[f][c].id
                i += 1

    # Creo los individuos de la primera generacion 
    poblacion = []
    f = 0
    for i in range(15):                  # 15 = tamano de la poblacion
        poblacion[i] = Genoma(i)                                                    # Estoy sobreescribiendo genoma(1)?
        poblacion[i].listaIds = random.sample(individuo.listaIds, k = len(individuo.listaIds))
        
        j = 0
        for f in range(G.filas):
            for c in range(G.columnas):
                G.grilla[f][c].id = poblacion[i].listaIds[j]
                j += 1

        poblacion[i].setFitness(listaOrdenes, G)
        f = f + poblacion[i].fitness
    
    pobAnterior = poblacion
    fitnessPobAnterior = f / len(pobAnterior)       # Promedio, esta bien?

    it = 0
    while(1):
        it += 1
        f1 = 0
        pobActual = pobAnterior         # Le doy el mismo valor que la poblacion anterior y luego cambio los genes que mutan
        
        # Nueva poblacion -> Mutacion
        for i in range(len(poblacion)):   
            cambios1 = random.sample(range(len(poblacion[i].listaIds)), k = 3)
            cambios2 = random.sample(cambios1, k=len(cambios1))
            for q in range(len(cambios1)):
                pobActual[i].listaIds[cambios1[q]] = pobAnterior[i].listaIds[cambios2[q]]

            # Se modifica la grilla con los nuevos id 
            j = 0
            for f in range(G.filas):
                for c in range(G.columnas):
                    G.grilla[f][c].id = pobActual[i].listaIds[j]
                    j += 1

            pobActual[i].setFitness(listaOrdenes, G)
            f1 = f1 + pobActual[i].fitness
        
        fitnessPobActual = f1 / len(pobActual)       # Promedio, esta bien?

        if (fitnessPobActual - fitnessPobAnterior) <= delta:
            break

        if it >= 100:
            break

        pobAnterior = pobActual             # Esta bien esta atualizacion?

    # Se elige al mejor INDIVIDUO de la poblacion 
    fit = []
    for i in range(len(pobActual)): 
        fit[i] = pobActual[i].fitness

    mejorFit = min(fit)
    i_min = fit.index(mejorFit)
    mejorIndividuo = pobActual[i_min]

    print(mejorIndividuo)