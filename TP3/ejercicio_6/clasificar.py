import numpy as np

from ejecutar_adelante import ejecutar_adelante

def clasificar(x, pesos, h = 0):
    # Corremos la red "hacia adelante"
    # Esto retorna 3 datos
    # {z, h, y} 
    resultados_feed_forward = ejecutar_adelante(x, pesos, h)
    # Buscamos la(s) clase(s) con scores mas altos (en caso de que haya mas de una con 
    # el mismo score estas podrian ser varias). Dado que se puede ejecutar en batch (x 
    # podria contener varios ejemplos), buscamos los maximos a lo largo del axis=1 
    # (es decir, por filas)
    max_scores = np.argmax(resultados_feed_forward["y"], axis = 1)

    # Tomamos el primero de los maximos (podria usarse otro criterio, como ser eleccion aleatoria)
    # Nuevamente, dado que max_scores puede contener varios renglones (uno por cada ejemplo),
    # retornamos la primera columna
    return max_scores