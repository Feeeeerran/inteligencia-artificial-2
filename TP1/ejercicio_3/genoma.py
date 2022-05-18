from ejercicio_2.temple_simulado import *

class Genoma:
    def __init__(self, n):
        self.numeroIndividuo = n
        # Lista de ids --> resultado final cual buscamos optimizar
        self.lista = []
        self.fitness = None

    def setFitness(self, listaOrdenes, G):
        costo = 0
        for i in range(len(listaOrdenes)):
            orden, costoTemple = simAnnealing(listaOrdenes[i], G)
            costo += costoTemple
        
        self.fitness = costo
        return costo

