from random import *
from numpy import arange

from a_estrella.a_estrella import *
from grilla.grilla import *
from ejercicio_2.temple_simulado import *
from ejercicio_3.genoma import Genoma

def geneticAlg(listaOrdenes,G):

    # Ver cual es el valor optimo
    delta = 0.1

    # Recorrer la grilla evaluando cada nodo de la misma
    # Formar un arreglo con los id de cada nodo
    i = 0


    # ❌ Estabamos sacando ids de la grilla cuando ya existe una propiedad llamada estanterias que trae la cantidad de estanterias
    # lista = []
    # for f in range(G.filas):
    #     for c in range(G.columnas):
    #         if G.grilla[f][c].id != 0:
    #             lista.append(G.grilla[f][c].id)
    #             i += 1
    
    # Creo los individuos de la primera generacion 
    poblacion = []
    f = 0

    for i in range(10):                
        poblacion.append(Genoma(i+1))
        poblacion[i].listaIds = sample(range(1,G.estanterias + 1),G.estanterias)
        
        j = 0
        for f in range(1,G.filas):
            for c in range(1,G.columnas):
                if G.grilla[f][c].id != 0:
                    G.grilla[f][c].id = poblacion[i].listaIds[j]
                    j += 1


        
        f += poblacion[i].setFitness(listaOrdenes, G)
    
    print("Antes de entrar al while")
    pobAnterior = poblacion
    fitnessPobAnterior = f / len(pobAnterior)    

    it = 0
    while(True):
        it += 1

        # Agregar crossover
        # Mutacion 
        pobActual,fitnessPobActual = mutacion(pobAnterior,G,listaOrdenes)            

        if (fitnessPobActual - fitnessPobAnterior) <= delta:
            break

        if it >= 100:
            break

        pobAnterior = pobActual          

    # Se elige al mejor INDIVIDUO de la poblacion 
    fit = []
    for i in range(len(pobActual)): 
        fit.append(pobActual[i].fitness)

    mejorFit = min(fit)
    i_min = fit.index(mejorFit)
    mejorIndividuo = pobActual[i_min]

    print(mejorIndividuo)

def mutacion(pobAnterior,G,listaOrdenes):
    # Le doy el mismo valor que la poblacion anterior y luego cambio los genes que mutan
    pobActual = pobAnterior

    f1 = 0
    for i in range(len(pobActual)):   
        cambios1 = sample(range(len(pobActual[i].listaIds)), k = 3)
        cambios2 = sample(cambios1, k=len(cambios1))
        for q in range(len(cambios1)):
            pobActual[i].listaIds[cambios1[q]] = pobAnterior[i].listaIds[cambios2[q]]

        # Se modifica la grilla con los nuevos id 
        j = 0
        for f in range(G.filas):
            for c in range(G.columnas):
                if G.grilla[f][c].id != 0:
                    G.grilla[f][c].id = pobActual[i].listaIds[j]
                    j += 1

        f1 += pobActual[i].setFitness(listaOrdenes, G)
    fitnessPobActual = f1 / len(pobActual) 

    return pobActual, fitnessPobActual

# def crossover(pobAnterior):

#     pobActual = pobAnterior
#     l = len(pobAnterior[0].listaIds)

#     for i in range(len(pobAnterior) - 1):
#         c = random.sample(range(l), k = 2)
#         c1 = min(c)
#         c2 = max(c)
#         # c = [ , ]
#         # Cross entre pobAnterior[i] y pobAnterior[i+1]

#         pobActual[i].listaIds[c1:c2] = pobAnterior[i+1].listaIds[c1:c2]
#         pobActual[i+1].listaIds[c1:c2] = pobAnterior[i].listaIds[c1:c2]


#         for j in range(c1, c2):
#             del pobAnterior[i].listaIds[j]
        
#         while k != c1:
#             pobActual[i].listaIds[k] = 
#             if k = len(pobActual) 

