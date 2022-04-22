import numpy as np
from math import *
import random

# Propias
from a_estrella.a_estrella import *
from grilla.grilla import *


# Con la funcion templeSimulado se busca pasarle una orden, en base a dicha orden la funcion va a buscar la mejor combinacion de estanterias (l que genera menor coste)

# IMPORTANTE
# Hay que añadir la bahia de carga y descarga

def simAnnealing(orden,carga,descarga,G):

    # Funcion T (momentaneamente lineal, podria pasarse como parametro)
    T = 10

    # Arreglo de ordenes para no repetir calculos
    ordenes = []
    ordenes.append(orden)

    # Arreglo para guardar el orden final (seleccionado a retornar)
    ordenFinal = [None] * len(orden)

    # Pasamos la orden a orden de nodos
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

    
    # Hacemos un setup para sacar el coste

    costo = costoTotal(orden,carga,descarga,G)

    # Tomamos la orden y calculamos su E, el cual nos sirve para comparar con otras combinaciones 
    while T != 0:
        # Hacemos el shuffle a los elementos del arreglo
        np.random.shuffle(orden)

        # Sacamos E nuevo
        nuevoCosto = costoTotal(orden,carga,descarga,G)

        # Quitamos la carga y descarga
        
        if nuevoCosto < costo:
            # Si el nuevo valor de E es menor al anterior, reemplazamos por esa orden
            # Pasamos los id de estanterias a una lista
            for i in range(len(orden)):
                ordenFinal[i] = orden[i].id

            # Agregamos la orden evaluada a la lista de ordenes
            ordenes.append(ordenFinal)
            costo = nuevoCosto
        # else:
            # Si la orden es peor, la agarramos segun una probabilidad
            # print(pow(e,(costo - nuevoCosto)/T))

            # ¡¡¡ Es realmente necesaria la probabilidad 🤔 !!!

        # Por ahora lineal 😬
        T -= 1 


        if T == 0:
            return ordenFinal, costo 
        
    


     
# La funcion calcula el costo total en base a una orden
# Se puede agregar que revise si una distancia ya se calculo anteriormente
def costoTotal(orden,carga,descarga,G):
    suma = 0
    # Añadimos el calculo de carga
    suma = AStar(carga,orden[0],G)
    
    # Calculamos el intermedio
    for i in range(len(orden) - 1):
        suma +=  AStar(orden[i],orden[i+1],G)
    
    # Añadimos el calculo de descarga
    suma += AStar(orden[len(orden) - 1],descarga,G)
    # os.system('cls')
    return suma

