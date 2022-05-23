from random import *


from a_estrella.a_estrella import *
from grilla.grilla import *
from ejercicio_2.temple_simulado import *
from ejercicio_3.genoma import Genoma

def geneticAlg(listaOrdenes,G):
    cantInd = 8

    # poblacion contiene a x = cantInd cantidad de individuos
    poblacion = []

    # Instanciamos los individuos segun cantidad de individuos
    for i in range(cantInd):                
        poblacion.append(Genoma(i+1))
        poblacion[i].lista = sample(range(1,G.estanterias + 1),G.estanterias)
        poblacion[i].setFitness(listaOrdenes,G)
    


    # Una vez terminado el setup de la poblacion, con un fitness inicial, se empieza iterar, mutando y haciendo crossover a traves de las generaciones
    # generaciones es una lista de diccionarios, la cual lleva la cuenta de los fitness y los ids relacionados
    generaciones = []
    # Cantidad de generaciones a representar
    gen = 10
    
    for generacion in range(gen):

        
        generaciones.append({})

        # Se genera una lista aleatoria para hacer crossover aleatorio
        randPos = sample(range(cantInd),cantInd)

        # CrossOver 👇
        for i in range(0,len(poblacion),2):
            # Entonces como poblacion esta ordenado de mejor fitness a peor fitness nos aseguramos el mejor cross over con los dos primeros
            crossover(poblacion[randPos[i]],poblacion[randPos[i+1]])


        
        # Mutacion 👇
        for i in range(len(poblacion)):
            # Probabilidad para saber si mutar
            rand = random()
            if rand < 0.3:
                # Mutamos un individuo y obtenemos su fitness y la lista correspondiente
                fitIndividuo = mutacion(poblacion[i],listaOrdenes,3,G) 
                if generacion > 0:
                    # Para generaciones >2 intentamos mutar x veces mientras el fitness obtenido sea peor que el peor (u otro individuo) fitness de la generacion anterior
                    intentos = 10
                    while fitIndividuo > sorted(generaciones[generacion - 1])[-1] and intentos != 0:
                        fitIndividuo = mutacion(poblacion[i],listaOrdenes,i+1,G) 
                        intentos -= 1 
            
            # Agregamos al historial de fitness por generacion
            generaciones[generacion][poblacion[i].setFitness(listaOrdenes,G)] = poblacion[i].lista 



        # Ordenamos la poblacion de mejor fitness (mas bajo) al peor fitness (mas alto)
        poblacion.sort(key = lambda x: x.fitness)

    


    # Recorremos a lo largo de las generaciones
    mejores = []
    mejorFit = sorted(generaciones[0])[0]
    mejorGen = 0
    mejorComb = generaciones[0][mejorFit]

    for i in range(len(generaciones)):
        print("Generacion ",i + 1)
        promedio = (sorted(generaciones[i])[0] + sorted(generaciones[i])[-1])/2
        print("Promedio fitness = ",promedio)
        print("Mejor fitness = ",sorted(generaciones[i])[0])
        mejores.append(sorted(generaciones[i])[0])
        # print("Orden de ids -> ",generaciones[i][sorted(generaciones[i])[0]])
        print("\n\n")

        if mejorFit > sorted(generaciones[i])[0]:
            mejorFit = sorted(generaciones[i])[0]
            mejorGen = i + 1
            mejorComb = generaciones[i][mejorFit]

    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Mejor Fitness logrado = ",mejorFit) 
    print("De la generacion ",mejorGen) 
    print("",mejorComb)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


    return generaciones, mejores






def mutacion(individuo,listaOrdenes,n,G):
    "Mutacion toma 3 parametros, el individuo, la lista de ordenes u orden y la grilla. Muta la propiedad lista de ids segun n cantidad de elementos. Luego devuelve su valor en fitness"

    # Tomamos n elementos de la lista de ids a mutar
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

    return fitness

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
