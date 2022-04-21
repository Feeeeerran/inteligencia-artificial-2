# Que arranque el milady 😎

from grilla.grilla import Grilla
from a_estrella.a_estrella import *
#from grilla.nodo import Nodo
import math
import random
import numpy as np

iteraciones = 100
temp = 10
tempFinal = 0.1
step = 0.9
M = Grilla()
orden = [1,5,4]

rutaInicial = []
for i in range(len(orden)+1):
    if i == 0 : continue 
    rutaInicial.append(i)

np.random.shuffle(rutaInicial)
print(rutaInicial)

#Necesito calcular la dist de toda la ruta no de 2 puntos 
def dist(ruta): 
  for i in range(len(rutaInicial)): 
    coste = AStar(ruta[i],ruta[i+1],M)
    i += 1
    return coste 


for i in range (iteraciones):
  temp = 1-(i+1)/iteraciones
  rutaActual = rutaInicial[:]
  nuevaRuta = rutaInicial [:]
  distActual = dist(rutaInicial)
  nuevaDist = dist(rutaInicial)


  while temp > tempFinal:
   nodosRandom = np.random.randint(1,len(rutaActual)+1, size=(1,2))
   puntos = [nodosRandom.item(0), nodosRandom.item(1) ]
   p1 = puntos[0]
   p2 = puntos[1]
   coste1 = dist(nuevaRuta)
   nuevaRuta[puntos[0],puntos[1]] = nuevaRuta[puntos[1],puntos[0]] 
   coste2 = dist(nuevaRuta)

   nuevaDist = nuevaDist - coste1 + coste2 
   deltaE =  coste2 - coste1

   if deltaE < 0 or math.exp(-deltaE/temp) :
     rutaActual = nuevaRuta[:]
     distActual = nuevaDist

   else:
     nuevaRuta = rutaActual[:]
     nuevaDist = distActual

   








   








