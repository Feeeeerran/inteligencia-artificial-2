from random import *
from typing import OrderedDict
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

    # Creo los individuos de la primera generacion 
    poblacion = []
    # f sera el fitness total de todas las poblaciones
    f = 0

    for i in range(10):                
        poblacion.append(Genoma(i+1))
        poblacion[i].lista = sample(range(1,G.estanterias + 1),G.estanterias)
        
        # Recorremos la grilla para setear nuevos valores de id a cada estanteria
        j = 0
        for f in range(1,G.filas - 1):
            for c in range(1,G.columnas - 1):
                if G.grilla[f][c].id != 0:
                    G.grilla[f][c].id = poblacion[i].lista[j]
                    j += 1


        # Despues no se usa 🤔
        f += poblacion[i].setFitness(listaOrdenes, G)
    
    # genAnterior = poblacion
    # fitGenAnterior = f / len(genAnterior)

    # Una vez terminado el setup de la poblacion, con un fitness inicial, se empieza iterar, mutando y haciendo crossover a traves de las generaciones
    # totalFit es un arreglo de diccionarios, la cual lleva la cuenta de los fitness y los ids relacionados
    totalFit = []
    err = 200
    gen = 0
    
    while(True):
        err -= 1
        # Agregar Crossover 👇
        # Crossover deberia ser una funcion que tome de a dos
        # Entonces como poblacion esta ordenado de mejor fitness a peor fitness nos aseguramos el mejor cross over con los dos primeros

        # Recorre toda la poblacion
        for i in range(len(poblacion)-1):
            # Evalua el primer y segundo individuo
            crossover([poblacion[i].lista,poblacion[i+1].lista])    
            # Ver como reemplazo los individuos viejos por los nuevos

        # Mutacion 👇
        totalFit.append({})
        for i in range(len(poblacion)):
            fitIndividuo,listaMutada = mutacion(poblacion[i],listaOrdenes,i,G) 
            # Tratamos de mutar a algo mejor, entonces
            if gen > 0:
                # Intentamos mutar 3 veces mientras el fitness obtenido sea peor que el peor (u otro individuo) fitness de la generacion anterior
                intentos = 0
                while fitIndividuo > sorted(totalFit[gen - 1])[2] and intentos != 3:
                    fitIndividuo,listaMutada = mutacion(poblacion[i],listaOrdenes,i,G) 
                    intentos += 1 
            
            # Agregamos al historial de fitness por generacion
            totalFit[gen][fitIndividuo] = listaMutada 

        gen += 1

        # Ordenamos la poblacion de mejor fitness (mas bajo) al peor fitness (mas alto)
        poblacion.sort(key = lambda x: x.fitness)

        # if (fitGenActual - fitGenAnterior) <= delta:
        #     break
    
        if gen == 40: 
            break

        if err == 0:
            break



    # Recorremos a lo largo de las generaciones
    mejorFit = sorted(totalFit[0])[0]
    mejorGen = 0
    mejorComb = totalFit[0][mejorFit]

    for i in range(len(totalFit)):
        print("Generacion ",i + 1)
        print("Mejor fitness = ",sorted(totalFit[i])[0])
        print("Orden de ids -> ",totalFit[i][sorted(totalFit[i])[0]])
        print("\n\n")

        if mejorFit > sorted(totalFit[i])[0]:
            mejorFit = sorted(totalFit[i])[0]
            mejorGen = i + 1
            mejorComb = totalFit[i][mejorFit]

    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Mejor Fitness logrado = ",mejorFit) 
    print("De la generacion ",mejorGen) 
    print("",mejorComb)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")





# Le doy el mismo valor que la poblacion anterior y luego cambio los genes que mutan
# Mutacion devuelve un arreglo de ids mutado y el fitness total con la lista de ordenes 
def mutacion(individuo,listaOrdenes,n,G):
    "Mutacion toma 3 parametros, el individuo, la lista de ordenes u orden y la grilla. Muta la propiedad lista de ids segun n cantidad de elementos. Luego devuelve un arreglo del id mutado y su valor en fitness"
    # Tomamos 3 elementos de la lista de ids a mutar
    cambios = sample(individuo.lista,n)
    # Sacamos las posiciones de los cambios
    pos = []
    for i in range(len(cambios)):
        pos.append(cambios.index(cambios[i]))   #pos.append((individuo.lista).index(cambios[i]))

    # Sale shuffle
    shuffle(cambios)

    # Incorporamos los cambios a las posiciones
    for i in range(len(cambios)):
        individuo.lista[pos[i]] = cambios[i] 


    # Se modifica la grilla con los nuevos id 
    j = 0
    for f in range(1,G.filas - 1):
        for c in range(1,G.columnas - 1):
            if G.grilla[f][c].id != 0:
                G.grilla[f][c].id = individuo.lista[j]
                j += 1

    fitness = individuo.setFitness(listaOrdenes, G)

    return fitness, individuo.lista


# Crossover deberia ser una funcion que tome de a dos
# Entonces como poblacion esta ordenado de mejor fitness a peor fitness nos aseguramos el mejor cross over con los dos primeros

def crossover(individuo1, individuo2):     # genAnterior: Arreglo de 2 individuos

    #genActual = genAnterior
    genActual = []
    genActual.append = genAnterior[0]     # genActual[0]
    genActual.append = genAnterior[1]     # genActual[1]
    l = len(genAnterior[0])

    #for i in range(len(genAnterior) - 1):
    c = random.sample(range(l), k = 2)
    c1 = min(c)
    c2 = max(c)
    # c = [ , ]
    # Cross entre genAnterior[i] y genAnterior[i+1]

    genActual[0][c1:c2] = genAnterior[1][c1:c2]
    genActual[1][c1:c2] = genAnterior[0][c1:c2]
    
    relleno = []
    k = c2 + 1
    it = 0
    while(1):

        for h in range(c1, c2+1):
            
            if genAnterior[0][k] == genActual[0][h]:
                k += 1
                break
            else: 
                it += 1
            
            if it == len(c):
                relleno.append(genAnterior[0][k])
                if k == len(genAnterior[0]):
                    k = 0
                else: 
                    k += 1
        
        if k == (c2 + 1):
            break