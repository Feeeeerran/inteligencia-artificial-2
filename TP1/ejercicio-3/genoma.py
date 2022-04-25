from ejercicio_2.temple_simulado import *

class Genoma:
    def __init__(self, n):
        self.numeroIndividuo = n
        self.listaIds = []
        self.fitness = None

    def setFitness(self, listaOrdenes, G):

        costo = 0
        for i in range(len(listaOrdenes)):
            costoTemple = simAnnealing(listaOrdenes[i], G)      # que pasa con el otro valor que devuelve simAnnealing?
            costo = costo + costoTemple                         # cambiar los argumentos de entrada de simAnnealing

        self.fitness = costo