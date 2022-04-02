import numpy as np

filas = int(input("Ingrese cantidad de filas (de estanterias): "))
columnas = int(input("Ingrese cantidad de columnas (de estanterias): "))
largo = int(input("Ingrese largo de la estanteria: "))

filas = filas*largo+filas+1
columnas = columnas*2+columnas+1
grilla = np.zeros((filas, columnas))

cont=1
for f in range(filas):
    for c in range(columnas):
        if f%(largo+1) != 0 and c%3 != 0:        #No es un pasillo
            grilla[f, c] = cont
            cont += 1

print(grilla)

p1 = int(input("Ingrese punto de salida: "))
p2 = int(input("Ingrese punto de llegada: "))