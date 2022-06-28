import numpy as np
import matplotlib.pyplot as plt


from precision import precision
from clasificar import clasificar
from generar_datos_clasificacion import generar_datos_clasificacion
from inicializar_pesos import inicializar_pesos
from train import train


def iniciar(numero_clases, numero_ejemplos, graficar_datos = False):
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

    # print(pesos["b1"][0])
    # plt.plot(pesos["b1"][0])
    # plt.show()


    # # Entrena
    LEARNING_RATE=1
    EPOCHS=10000
    return train(x, t, pesos, LEARNING_RATE, EPOCHS)
    
    


# Iniciamos el modelo con
#   > 3 Clases
#   > 300 Ejemplares
#   > Haciendo una grafica inicial (True o False)
pesos, loss = iniciar(3,300)
x,t = generar_datos_clasificacion(300,3)

res = clasificar(x,pesos)
precision(res,t)


plt.plot(np.array(range(len(loss)))*10,loss)
plt.grid()
plt.show()