from desborrosificador import *

def controlador_difuso(pertenencia_pos, pertenencia_vel, conjunto_f, dominio_f, reglas):
    salidas = []
    tags = []
    for i in pertenencia_pos:
        for j in pertenencia_vel:
            # Obtenemos el conjunto borroso de salida (F)
            # print(reglas[i][j]) 

            valor_min = min([pertenencia_pos[i], pertenencia_vel[j]])
            salidas.append(trunc(conjunto_f[reglas[i][j]],valor_min))
            if reglas[i][j] not in tags:
                tags.append(reglas[i][j])

    
    if len(salidas) == 0:
        salidas.append([0])
    # print(salidas)

    conj_salida = len(salidas[0])*[0]
    for i in range(len(salidas)):
        conj_salida = maximo(conj_salida, salidas[i])

    f_nitido = desborrosificar(conj_salida,dominio_f,tags) 
    return f_nitido


def minimo(vector1, vector2):
    conjuncion = len(vector1)*[0]
    for k in range(len(vector1)):
        if vector1[k] <= vector2[k]:
            conjuncion[k] = vector1[k]
        else:
            conjuncion[k] = vector2[k]
    return conjuncion


def maximo(vector1, vector2):
    disyuncion = len(vector1)*[0]
    for k in range(len(vector1)):
        if vector1[k] >= vector2[k]:
            disyuncion[k] = vector1[k]
        else:
            disyuncion[k] = vector2[k]
    return disyuncion


def trunc(vector1, valor_max):
    truncado = len(vector1)*[0]
    for k in range(len(vector1)):
        if vector1[k] >= valor_max:
            truncado[k] = valor_max
        else:
            truncado[k] = vector1[k]
    return truncado