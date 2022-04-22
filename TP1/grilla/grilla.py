from grilla.nodo import Nodo
import os


class Grilla:

    def __init__(self):
        self.filasEstanterias = 3
        self.columnasEstanterias = 3
        self.largoEstanteria = 2
        self.filas = None
        self.columnas = None
        self.grilla = []
        self.estanterias = None





    def setEstanterias(self):
        os.system("cls")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        self.filasEstanterias = int(input("Ingrese cantidad de filas de estanterias: "))
        self.columnasEstanterias = int(input("Ingrese cantidad de columnas de estanterias: "))
        self.largoEstanteria = int(input("Ingrese largo de la estanteria (suma filas): "))
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        
        self.setFilasColumnas()

        #Podriamos hacer una doble confirmacion de las filas y columnas (grilla por defecto) -> ponerlo en el main

    def setFilasColumnas(self):
        # Las estanterias estan separadas entre si por un espacio entre filas y columnas
        # El espacio no depende del largo de la estanteria
        self.filas = (self.filasEstanterias*self.largoEstanteria) + self.filasEstanterias + 1
        self.columnas = self.columnasEstanterias*2 + self.columnasEstanterias + 1
        self.estanterias = self.filasEstanterias*self.columnasEstanterias*self.largoEstanteria*2

        # Mostrar grilla graficamente

    # Setup de la grilla 
    def setGrilla(self):
        cont = 1
        for f in range(self.filas):
            self.grilla.append([])
            for c in range(self.columnas):
                # No es pasillo
                if f%(self.largoEstanteria + 1) != 0 and c%3 != 0:
                    self.grilla[f].append(Nodo(c,f,cont))      
                    self.grilla[f][c].estanteria = True        
                    cont += 1
                else:
                    self.grilla[f].append(Nodo(c,f))

    def asignarVecinos(self):
        grilla = self.grilla
        filas = self.filas
        columnas = self.columnas

        for f in range(filas):
            for c in range(columnas):
                nodo = grilla[f][c]

                # Vecinos horizontales
                if nodo.x > 0 and nodo.x < columnas-1:
                    grilla[f][c].vecinos.append(grilla[f][c+1])
                    grilla[f][c].vecinos.append(grilla[f][c-1])
                elif nodo.x == 0:
                    grilla[f][c].vecinos.append(grilla[f][c+1])
                elif nodo.x == columnas-1:
                    grilla[f][c].vecinos.append(grilla[f][c-1])

                # Vecinos verticales
                if nodo.y > 0 and nodo.y < filas-1:
                    grilla[f][c].vecinos.append(grilla[f+1][c])
                    grilla[f][c].vecinos.append(grilla[f-1][c])
                elif nodo.y == 0:
                    grilla[f][c].vecinos.append(grilla[f+1][c])
                elif nodo.y == filas-1:
                    grilla[f][c].vecinos.append(grilla[f-1][c])




# Añadir metodos para dibujarla
# Entonces decimos que la grilla tiene "estados" y a veces pinta imprimirla para verla

