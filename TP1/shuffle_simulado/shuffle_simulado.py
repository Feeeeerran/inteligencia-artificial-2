import numpy as np
from math import *
import random

# Propias
from a_estrella.a_estrella import *
from grilla.grilla import *


# Con la funcion templeSimulado se busca pasarle una orden, en base a dicha orden la funcion va a buscar la mejor combinacion de estanterias (l que genera menor coste)

# IMPORTANTE
# Hay que añadir la bahia de carga y descarga

def shuffleSim(orden,G):
    carga = G.carga
    descarga = G.descarga

    # Funcion T (momentaneamente lineal, podria pasarse como parametro)
    T = 300

    # Arreglo de ordenes para no repetir calculos
    ordenes = []
    ordenes.append(orden)

    # Arreglo para guardar el orden final (seleccionado a retornar)
    ordenSel = [None] * len(orden)

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
    print("Costo inicial", costo)
    # Tomamos la orden y calculamos su E, el cual nos sirve para comparar con otras combinaciones 
    while T != 0:
        # Hacemos el shuffle a los elementos del arreglo (nodos)
        np.random.shuffle(orden)
        print("Primer elemento",orden[0].id)
        print("Segundo elemento",orden[1].id)
        # Sacamos nuevo E
        nuevoCosto = costoTotal(orden,carga,descarga)
        print("nuevo costo = ",nuevoCosto)
        print("\n")

        # Evitamos revisar combinaciones ya revisadas
        if (aLista(orden) not in ordenes):
            if nuevoCosto < costo:
                # Si el nuevo valor de E es menor al anterior, reemplazamos por esa orden
                # Pasamos los id de estanterias a una lista
                ordenSel = aLista(orden)
                
                print(ordenSel)

                # Agregamos la orden evaluada a la lista de ordenes
                ordenes.append(ordenSel)
                costo = nuevoCosto

            # 👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇
            # Se tenia pensado como temple simulado, pero se descubrio que sin probabilidad obteniamos mejores resultados (combinaciones con menor costo) que si usabamos probabilidad
            # Por eso mismo la parte de probabilidad esta comentada
            
            # Ahora, lo obtenido es un hill climbing con reinicio aleatorio, lo cual sirve para ordenes medianas y prqueñas (cerca de 10) pero no para grandes ordenes (> 10)


            # else:
            #     # Si la orden es peor, la agarramos segun una probabilidad
            #     probabilidad = pow(e,(costo - nuevoCosto)/T) > random.random()

            #     # probabilidad es un booleano
            #     if probabilidad:
            #         ordenSel = aLista(orden)

            #         # Agregamos la orden evaluada a la lista de ordenes
            #         ordenes.append(ordenSel)
            #         costo = nuevoCosto


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
    suma = AStar(carga,orden[0])
    
    # Calculamos el intermedio
    for i in range(len(orden) - 1):
        suma +=  AStar(orden[i],orden[i+1])
    
    # Añadimos el calculo de descarga
    suma += AStar(orden[len(orden) - 1],descarga)
    # os.system('cls')
    return suma


def aLista(nodos):
    "Convierte una lista de nodos a una lista con el mismo orden pero de sus id"
    lista = [None] * len(nodos)
    for i in range(len(nodos)):
        lista[i] = nodos[i].id
    return lista