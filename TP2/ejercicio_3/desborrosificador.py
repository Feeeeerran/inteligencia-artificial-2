


def desborrosificar(conjunto,dominios,tags):
    centros = []
    ancho = 6
    num = 0
    den = 1
    dt = int(len(conjunto)/19)       
    for i in tags:
        if i == "NG":
            num += conjunto[3*dt] * -6
            den += conjunto[3*dt]
        if i == "NP":
            num += conjunto[6*dt] * -3
            den += conjunto[6*dt]
        if i == "Z":
            num += 0
            den += conjunto[9*dt]
        if i == "PP":
            num += conjunto[12*dt] * 3
            den += conjunto[12*dt]
        if i == "PG":
            num += conjunto[15*dt] * 6
            den += conjunto[15*dt]

    return num/den



    # Si el universo del dusciruso es de -9 a 9
    # En paso de 1 son 19 unidades
    # En paso 0.1 son 190
    # En paso 0.01 son 1900

