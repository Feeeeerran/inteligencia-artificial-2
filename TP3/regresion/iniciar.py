import numpy as np
import matplotlib.pyplot as plt


from inicializar_pesos import inicializar_pesos
from train import train

def iniciar(numero_ejemplos, graficar_datos = False):


    # Generacion de datos, podria mejorarse y probar para mas entradas y otro tipo de funciones
    x = np.linspace(0,8,numero_ejemplos).reshape(numero_ejemplos,1)
    t = np.cos(x)

    # Inicializa pesos de la red
    NEURONAS_CAPA_OCULTA = 100
    NEURONAS_ENTRADA = 1
    NEURONAS_SALIDA = 1
    pesos = inicializar_pesos(n_entrada=NEURONAS_ENTRADA, n_capa_2=NEURONAS_CAPA_OCULTA, n_capa_3=NEURONAS_SALIDA)


    # # Entrena
    LEARNING_RATE=0.01
    EPOCHS=10000
    return train(x, t, pesos, LEARNING_RATE, EPOCHS)
    




