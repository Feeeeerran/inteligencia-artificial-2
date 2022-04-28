from ejercicio_2.temple_simulado import *

class Genoma:
    def __init__(self, n):
        self.numeroIndividuo = n
        self.listaIds = []
        self.fitness = None

    def setFitness(self, listaOrdenes, G):
        costo = 0
        for i in range(len(listaOrdenes)):
            orden, costoTemple = simAnnealing(listaOrdenes[i], G)
            costo = costo + costoTemple
        self.fitness = costo
        return costo