from p5 import *

class Nodo:
    def __init__(self,x,y,id = 0):
        self.x = x
        self.y = y
        self.id = id
        self.estanteria = False
        self.vecinos = []
        self.abierta = False
        self.cerrada = False
        self.f = None
        self.c = None
        self.h = None
        self.anterior = False

    def setF(self,p2,costo):
        self.h = pow(pow(p2.x-self.x,2)+pow(p2.y-self.y,2),0.5)
        self.c = costo
        self.f = costo + self.h

    def mostrar(self,R,G,B,escala):
        fill(R,G,B)
        rect(self.x*escala,self.y*escala,escala,escala)


# Faltan como propiedades la heuristica, el g y la f
