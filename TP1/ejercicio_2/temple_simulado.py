import numpy as np
from math import *
from random import *

# Propias
from a_estrella.a_estrella import *
from grilla.grilla import *


# Con la funcion templeSimulado se busca pasarle una orden, en base a dicha orden la funcion va a buscar la mejor combinacion de estanterias (l que genera menor coste)

# IMPORTANTE
# Hay que añadir la bahia de carga y descarga

def simAnnealing(orden,G):
    
    carga = G.carga
    descarga = G.descarga

    # Funcion T (momentaneamente lineal, podria pasarse como parametro)
    T = 1

    # Arreglo de ordenes para no repetir calculos
    ordenes = []
    ordenes.append(orden)

    # Arreglo para guardar el orden final (seleccionado a retornar)
    ordenSel = orden

    # Pasamos la orden a orden de nodos --> para poder usar AStar
    for i in range(len(orden)):
        flag = False
        for f in range(G.filas):
            for c in range(G.columnas):
                if G.grilla[f][c].id == orden[i]:
                    orden[i] = G.grilla[f][c]
                    flag = True
                    break
            if flag == True:
                break

    
    # Hacemos un setup para sacar el coste inicial
    costo = costoTotal(orden,carga,descarga)
    print("Coste inicial ",costo)
    # Tomamos la orden y calculamos su E, el cual nos sirve para comparar con otras combinaciones 
    while T != 0:
        # Hacemos el shuffle a los elementos del arreglo (nodos)
        # np.random.shuffle(orden)

        orden = permutar(orden)



        # Sacamos nuevo E
        nuevoCosto = costoTotal(orden,carga,descarga)

        # Evitamos revisar combinaciones ya revisadas y que no tengan el mismo costo
        if (aLista(orden) not in ordenes and costo != nuevoCosto):
            if nuevoCosto < costo:
                # Si el nuevo valor de E es menor al anterior, reemplazamos por esa orden
                # Pasamos los id de estanterias a una lista
                ordenSel = aLista(orden)
                

                # Agregamos la orden evaluada a la lista de ordenes
                ordenes.append(ordenSel)
                costo = nuevoCosto

            else:
                # Si la orden es peor, la agarramos segun una probabilidad
                probabilidad = pow(e,(costo - nuevoCosto)/T) > random()
                # probabilidad es un booleano
                if probabilidad:
                    ordenSel = aLista(orden)

                    # Agregamos la orden evaluada a la lista de ordenes
                    ordenes.append(ordenSel)
                    costo = nuevoCosto


        # Por ahora lineal 😬
        T -= 1 

    
        if T == 0:
            return ordenSel, costo 
        
    


     
# La funcion calcula el costo total en base a una orden
# Se puede agregar que revise si una distancia ya se calculo anteriormente
def costoTotal(orden,carga,descarga):
    "Calcula el costo total de la trayectoria segun una lista de ordenes. Se tiene en cuenta nodos de carga y descarga"
    suma = 0
    # Añadimos el calculo de carga
    print("Llama a estrella 1")
    suma = AStar(carga,orden[0])
    print("Sale de estrella 1")

    # Calculamos el intermedio
    print("Llama a estrella 2")
    for i in range(len(orden) - 1):
        suma +=  AStar(orden[i],orden[i+1])
    print("Sale de estrella 2")
    
    # Añadimos el calculo de descarga
    print("Sale de estrella 3")
    suma += AStar(orden[len(orden) - 1],descarga)
    # os.system('cls')
    print("Sale de estrella 3")


    return suma


def aLista(nodos):
    "Convierte una lista de nodos a una lista con el mismo orden pero de sus id"
    lista = [None] * len(nodos)
    for i in range(len(nodos)):
        lista[i] = nodos[i].id
    return lista

def permutar(orden):
    pos = randint(1,len(orden)-2)
    # Escogemos si tirar permutar a la derecha o a la izquierda
    # Permuta a a la derecha, si randint devuelve 0, entonces permutamos a la izquierda (prob 50%)
    per = 1
    if randint(0,1) == 0:
        per = -1


    nodoPermuta = orden[pos]
    orden[pos] = orden[pos + per]
    orden[pos + per] = nodoPermuta

    return orden