from grilla import Grilla

grilla = Grilla()
grilla.setFilasColumnas()
print(grilla.estanterias)
grilla.armarGrilla()
grilla.asignarVecinos()

print(grilla.grilla[0][0].x)
print(grilla.grilla[0][0].y)
print(grilla.grilla[0][0].vecinos[0].x)