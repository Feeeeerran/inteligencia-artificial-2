import random

from a_estrella.a_estrella import *
from grilla.grilla import *
from ejercicio_2.temple_simulado import *


def geneticAlg(G, listaOrdenes)
# Instanciar una Grilla
# Recorrer la grilla evaluando cada nodo de la misma
#i = 0
#for f in range(filas):
#    for c in range(columnas):
#        if nodo.id != 0:
#            individuo1[i] = nodo.id
#            i += 1

individuo1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
individuo2 = random.sample(individuo1, k = len(individuo1))
individuo3 = random.sample(individuo1, k = len(individuo1))
individuo4 = random.sample(individuo1, k = len(individuo1))
individuo5 = random.sample(individuo1, k = len(individuo1))

#print(individuo1)
#if individuo2 != individuo1: print(individuo2)
#if individuo3 != individuo1: print(individuo3)
#if individuo4 != individuo1: print(individuo4)
#if individuo5 != individuo1: print(individuo5)

# Con temple simulado se calculan los costos de cada individuo

# Se seleccionan los mas aptos / Se suman todos sus costos: Esa es la medida de fitness de esa disposicion del almacen
# Se eligen algunos o directamente se evalua si son buenos o no?

# Mutacion / Crossover
individuo1Cambios = random.sample(individuo1, k = 2)
print(individuo1Cambios)
random.shuffle(individuo1Cambios)
print(individuo1Cambios)

#if nodo.id == individuo1Cambios[i]:
