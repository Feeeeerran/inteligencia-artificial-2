# vector1 = [1, 3, 4, 2, 7]
# vector2 = [2, 5, 2, 1, 9]
# valor_max = 3

baseConocim = {'NG':{'NG':'NG','NP':'NP','Z':'NP','PP':'NP','PG':'Z'},
               'NP':{'NG':'NG','NP':'NP','Z':'NP','PP':'Z','PG':'PP'},              
               'Z':{'NG':'NP','NP':'NP','Z':'Z','PP':'PP','PG':'PP'},
               'PP':{'NG':'NP','NP':'Z','Z':'PP','PP':'PP','PG':'PG'},
               'PG':{'NG':'Z','NP':'PP','Z':'PP','PP':'PG','PG':'PG'}}


def controladorDisfuso(conj_brorrosos_tita, conj_brorrosos_v, conj_brorrosos_F, tita, v):
    pertenencia_tita = borrosificador(conj_brorrosos_tita, tita)
    pertenencia_v = borrosificador(conj_brorrosos_v, v)

    # conj_brorrosos_F = {'Z':[0, 0.25, 0.5, 0.75, 1, 0.75, 0.5, 0.25, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'PP':[0, 0, 0, 0, 0, 0.25, 0.5, 0.75, 1, 0.75, 0.5, 0.25, 0, 0, 0, 0, 0], 'PG':[0, 0, 0, 0, 0, 0, 0, 0, 0, 0.25, 0.5, 0.75, 1, 0.75, 0.5, 0.25, 0]}
    # pertenencia_tita = {'PP':0.6, 'PG':0.5}     
    # pertenencia_v = {'NP':0.3, 'Z':0.9}      

    salidas = []
    for i in pertenencia_v:
        if baseConocim[i]:
            for j in pertenencia_tita:
                if baseConocim[i][j]:
                    # Obtenemos el conjunto borroso de salida (F)
                    # print(baseConocim[i][j]) 

                    valor_min = min([pertenencia_tita[j], pertenencia_v[i]])
                    salidas.append(trunc(conj_brorrosos_F[baseConocim[i][j]],valor_min))

    conj_salida = len(salidas[0])*[0]
    for i in range(len(salidas)):
        conj_salida = maximo(conj_salida, salidas[i])

    f_nitido = desborrosificador(conj_salida) 
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