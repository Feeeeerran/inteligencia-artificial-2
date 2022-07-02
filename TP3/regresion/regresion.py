import matplotlib.pyplot as plt
import numpy as np



from iniciar import iniciar
from ejecutar_adelante import ejecutar_adelante


pesos,loss = iniciar(300)


x_test = np.linspace(0,3,300).reshape(300,1)
y_test = np.cos(x_test)
values = ejecutar_adelante(x_test,pesos) 


plt.plot(x_test,values["y"],'r',x_test,y_test,'b')
plt.grid()
plt.show()


# Algunas cosas importantes
# El set de train comprende un linspace que va de A hasta B, donde B > A
# El test  no puede ser mayor al rango que comprennde el set de enntrenamiento, ya que si no da errores en los pesos
# es decir que si el rango de train es B - A = R_train
# Entonces el rango de test R_test < R_train

# Tambien, respecto a clasificacion se ajusta el learning rate, ya que el valor
# que venia de clasificacion (valor de 1) era demasiado alto y aumentaba las salidas
# de manera exponencial, demmasiado inconsistente
# Entonces se ajusto el learning rate a 0.01




