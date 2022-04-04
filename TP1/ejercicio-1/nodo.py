class Nodo:
    def __init__(self,x,y,id = 0):
        self.x = x
        self.y = y
        self.id = id
        self.estanteria = False

    def heuristica(self, p2):
        return pow(pow(p2.x-self.x,2)+pow(p2.y-self.y,2),0.5)

# Faltan como propiedades la heuristica, el g y la f
