import numpy as np

def ejecutar_adelante(x, pesos, func_h = 0):
    # Funcion de entrada (a.k.a. "regla de propagacion") para la primera capa oculta
    z = x.dot(pesos["w1"]) + pesos["b1"]

    if func_h == 1:
        # Funcion sigmoide
        h = 1/(1 + np.exp(-z)) 
    else:
        # Funcion de activacion ReLU para la capa oculta (h -> "hidden")
        h = np.maximum(0, z)


    # Salida de la red (funcion de activacion lineal). Esto incluye la salida de todas
    # las neuronas y para todos los ejemplos proporcionados
    y = h.dot(pesos["w2"]) + pesos["b2"]

    return {"z": z, "h": h, "y": y}