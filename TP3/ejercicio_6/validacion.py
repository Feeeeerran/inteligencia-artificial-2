import numpy as np

from ejecutar_adelante import ejecutar_adelante

def validacion(xv,tv,pesos):
    m = np.size(tv) 

    resultados_feed_forward = ejecutar_adelante(xv, pesos)
    y = resultados_feed_forward["y"]

    # LOSS
    # a. Exponencial de todos los scores (e^ y[...])
    exp_scores = np.exp(y)

    # b. Suma de todos los exponenciales de los scores, fila por fila (ejemplo por ejemplo).
    #    Mantenemos las dimensiones (indicamos a NumPy que mantenga la segunda dimension del
    #    arreglo, aunque sea una sola columna, para permitir el broadcast correcto en operaciones
    #    subsiguientes)
    sum_exp_scores = np.sum(exp_scores, axis=1, keepdims=True)

    # c. "Probabilidades": normalizacion de las exponenciales del score de cada clase (dividiendo por 
    #    la suma de exponenciales de todos los scores), fila por fila
    p = exp_scores / sum_exp_scores

    # d. Calculo de la funcion de perdida global. Solo se usa la probabilidad de la clase correcta, 
    #    que tomamos del array t ("target")
    loss = (1 / m) * np.sum( -np.log( p[range(m), tv] ))

    return loss