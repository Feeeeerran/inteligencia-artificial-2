
def orders(archivo):
    ordenes = []
    ruta = "./ordenes/" + archivo + ".txt"
    with open(ruta,"r") as archivo:
        orden = []
        for linea in archivo:
            if "Order" not in linea and linea.split():
                orden.append(int(linea[1:-1]))
            elif "Order" not in linea:
                ordenes.append(orden)
                orden = []
    
    return ordenes