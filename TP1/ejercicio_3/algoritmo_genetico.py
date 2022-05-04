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

    for i in range(8):                
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
        for i in range(0,len(poblacion),2):
            crossover(poblacion[i],poblacion[i+1])


        # Mutacion 👇
        totalFit.append({})
        for i in range(len(poblacion)):
            
            # ❗❗❗
            # La mutacion deberia ser igual en todos los individuos
            # Es decir que mutamos la misma cantidad de genes, podria evaluarse la posibilidad de mutar segun una probabilidad

            fitIndividuo,listaMutada = mutacion(poblacion[i],listaOrdenes,3,G) 
            # Tratamos de mutar a algo mejor, entonces
            if gen > 0:
                # Intentamos mutar 3 veces mientras el fitness obtenido sea peor que el peor (u otro individuo) fitness de la generacion anterior
                intentos = 0
                while fitIndividuo > sorted(totalFit[gen - 1])[-1] and intentos != 3:
                    fitIndividuo,listaMutada = mutacion(poblacion[i],listaOrdenes,i,G) 
                    intentos += 1 
            
            # Agregamos al historial de fitness por generacion
            totalFit[gen][fitIndividuo] = listaMutada 

        gen += 1

        # Ordenamos la poblacion de mejor fitness (mas bajo) al peor fitness (mas alto)
        poblacion.sort(key = lambda x: x.fitness)

        # if (fitGenActual - fitGenAnterior) <= delta:
        #     break
    
        if gen == 20: 
            break

        if err == 0:
            break



    # Recorremos a lo largo de las generaciones
    mejorFit = sorted(totalFit[0])[0]
    mejorGen = 0
    mejorComb = totalFit[0][mejorFit]

    for i in range(len(totalFit)):
        print("Generacion ",i + 1)
        print("Promedio fitness = ",sum(sorted(totalFit[i]))/len(poblacion))
        print("Mejor fitness = ",sorted(totalFit[i])[0])
        # print("Orden de ids -> ",totalFit[i][sorted(totalFit[i])[0]])
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






def mutacion(individuo,listaOrdenes,n,G):
    "Mutacion toma 3 parametros, el individuo, la lista de ordenes u orden y la grilla. Muta la propiedad lista de ids segun n cantidad de elementos. Luego devuelve un arreglo del id mutado y su valor en fitness"
    # Tomamos 3 elementos de la lista de ids a mutar
    cambios = sample(individuo.lista,n)
    # Sacamos las posiciones de los cambios
    pos = []
    for i in range(len(cambios)):
        pos.append((individuo.lista).index(cambios[i]))

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

def crossover(individuo1, individuo2):
    "La funcion toma dos individuos, de cada uno extrae la lista y realiza el crossover. No retorna nada ya que trabaja directamente con el objeto individuo"
    lista1 = individuo1.lista
    lista2 = individuo2.lista

    # La porcion a cambiar sea de 3 elementos (ver como cambiar)
    initPos = randint(1,len(lista1) - 3)
    finalPos = initPos + 3

    porcion1 = lista1[initPos:finalPos]
    porcion2 = lista2[initPos:finalPos]

    relleno1 = []
    relleno2 = []

    # Llenamos el relleno en el orden de la lista dada, para ello usamos dos for, uno que recorre desde donde termina el corte hasta el final de la lista
    # y otro que va desde 0 hasta donde termina el corte (sin incluir esa posicion)

    for i in range(finalPos,len(lista1)):
        if lista1[i] not in porcion2:
            relleno1.append(lista1[i])
        if lista2[i] not in porcion1:
            relleno2.append(lista2[i])

    for i in range(finalPos):
        if lista1[i] not in porcion2:
            relleno1.append(lista1[i])
        if lista2[i] not in porcion1:
            relleno2.append(lista2[i])

    # Metemos las porciones en las listas y ya solo queda rellenar para no tener repetidos ni faltantes
    individuo1.lista[initPos:finalPos] = porcion2
    individuo2.lista[initPos:finalPos] = porcion1

    # Se empieza a rellenar desde donde termina el corte
    # pos funciona a modo de puntero que da la posicion desde donde se tiene que ir llenando
    pos = finalPos
    i = 0

    while(True):
        if pos < (len(lista1)):
            individuo1.lista[pos] = relleno1[i]
            individuo2.lista[pos] = relleno2[i]
            pos += 1
            i +=1
        else:
            pos = 0

        if pos == initPos:
            break
