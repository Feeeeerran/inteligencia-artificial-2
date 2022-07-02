import numpy as np
import matplotlib.pyplot as plt
import random as rand



from generar_datos_clasificacion import generar_datos_clasificacion
from inicializar_pesos import inicializar_pesos
from train import train

def iniciar(numero_ejemplos,numero_clases, graficar_datos = False):
    # Generamos datos
    x, t = generar_datos_clasificacion(numero_ejemplos, numero_clases)

    # Graficamos los datos si es necesario
    if graficar_datos:
        # Parametro: "c": color (un color distinto para cada clase en t)
        plt.scatter(x[:, 0], x[:, 1], c=t)
        plt.show()

    # Inicializa pesos de la red
    NEURONAS_CAPA_OCULTA = 100
    NEURONAS_ENTRADA = 2
    pesos = inicializar_pesos(n_entrada=NEURONAS_ENTRADA, n_capa_2=NEURONAS_CAPA_OCULTA, n_capa_3=numero_clases)

    # # Entrena
    LEARNING_RATE=1
    EPOCHS=10000
    return train(x, t, pesos, LEARNING_RATE, EPOCHS)
    




