import numpy as np
import matplotlib.pyplot as plt
import random as rand

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
    NEURONAS_CAPA_OCULTA = rand.randrange(50, 300, 1)
    print("Neuronas: ", NEURONAS_CAPA_OCULTA)
    # NEURONAS_CAPA_OCULTA = 100
    NEURONAS_ENTRADA = 2
    pesos = inicializar_pesos(n_entrada=NEURONAS_ENTRADA, n_capa_2=NEURONAS_CAPA_OCULTA, n_capa_3=numero_clases)

    # print(pesos["b1"][0])
    # plt.plot(pesos["b1"][0])
    # plt.show()


    # # Entrena
    LEARNING_RATE = rand.random()
    print("LR: ", LEARNING_RATE)
    # LEARNING_RATE=1
    EPOCHS=10000
    return train(x, t, pesos, LEARNING_RATE, EPOCHS)
    

# Iniciamos el modelo con
#   > 3 Clases
#   > 300 Ejemplares
#   > Haciendo una grafica inicial (True o False)

presv = 0

# Lo ideal seria hacerlo en un for una cierta cantidad de veces y elegir los parametros para los cuales se obtiene la mejor precision 
while(presv < 96):
    # Train
    pesos, loss = iniciar(3,300)

    # Validacion
    xv,tv = generar_datos_clasificacion(100,3)
    resv = clasificar(xv,pesos)
    presv = precision(resv,tv)
print("En la validacion\n")

# Test
x,t = generar_datos_clasificacion(300,3)

# Funcion ReLu
res = clasificar(x,pesos)
precision(res,t)
print("Con funcion ReLu\n")

# Funcion sigmoide
res = clasificar(x,pesos, 1)
precision(res,t)
print("Con funcion sigmoide\n")

plt.plot(np.array(range(len(loss)))*10,loss)
plt.grid()
plt.show()