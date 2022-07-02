from TP3.clasif.precision import precision
import numpy as np

from iniciar import iniciar
from clasificar import clasificar
from generar_datos_clasificacion import generar_datos_clasificacion

# Iniciamos el entrenamiennto (esto es generar un train set y entrenar sobre el mismo)
# Tambien se agrega una funcion de validacion, que compara valores de loss con un set de validacion
pesos, loss = iniciar(300,3)


# Una vez obtenido los pesos podemos clasificar, para ello podemos generar mas datos
# o tomar datos de la carpeta data_sets ubicado en la raiz de este archivo
x,t = generar_datos_clasificacion(300,3)
clasificacion = clasificar(x,pesos)


# Y finalmente calcular la precision con la funcion precision
precision(clasificacion,t)


# Para ver abrir los data sets .npz
# Usar el metodo load() de numpy
# data = np.load('data_sets/setX.npz')

# Data sera un objeto con los dos arreglos, x y t
# Si no tuvieran esos nombres, podemos ver como se llaman los arreglos haciendo
# data.files

# Luego para acceder a cada arreglo de datos 
# x = data["x"]
# t = data["t"]


# En la carpeta de data_sets hay 5 datasets

