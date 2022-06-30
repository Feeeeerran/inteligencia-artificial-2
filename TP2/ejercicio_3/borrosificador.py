from scipy import constants
import numpy as np
import matplotlib.pyplot as plt
# Tags para sacar el nombre del conjunto borroso
tags = ["NG","NP","Z","PP","PG"]




# Borrosificador
# Entra el valor a borrosificar y el dominio de conjuntos borrosos
# Se busca a que conjunto borroso pertenece
# Se devuelve el valor de pertenencia de x --> mu(x) --> y con la siguiente forma
# {"NOMBRE" : valor} donde nombre es el nombre segun las tags y valor es el valor de pertenencia
def borrosificar(entrada,dominio):
    pertenencias = {} 
    pendiente = 1/dominio[2][1]
    for tag in range(len(dominio)):
        conjunto = dominio[tag]
        # Separamos conjuntos centrales de los hombros
        # Vemos si cae dentro del dominio o no
        if entrada > conjunto[0] and entrada < conjunto[1]:
            # Vamos a la funcion y retornamos su valor pero tenemos que normalizar el valor al dominio
            y = valor_pertenencia(entrada,conjunto,pendiente,tag)
            pertenencias[tags[tag]] = y         # NO ENTIENDO ESTA LINEA, NO SERIA pertenencias[tags][tag]?
    
    return pertenencias


def valor_pertenencia(x,conjunto,m,tag):
    centro = (conjunto[1] - conjunto[0])/2 + conjunto[0]
    # Tratamos a los hombros primero
    if tag == 0:
        if x < centro:
            return 1
        else:
            -1*m*x + -1
    
    if tag == 4:
        if x > centro:
            return 1
        else:
            1*m*x + -1      # la pendiente es +

    if x == centro:
        return 1
    elif x < centro:
        return m*x + (3 - tag)
    else:
        return -1*m*x + (tag - 1)
        



