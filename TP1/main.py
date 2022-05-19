import os
import plotly.express as px

# Propios
# from a_estrella.a_estrella import AStar
from grilla.grilla import Grilla
from ejercicio_2.temple_simulado import simAnnealing
from ordenes.get_orders import orders
from ejercicio_3.algoritmo_genetico import geneticAlg
# from a_estrella.a_estrella import AStar

os.system("cls")


# Instanciamos grilla (una sola vez)
G = Grilla()

print("#######################################################################")
print("#######################################################################\n")
print("Bienvenido profe al trabajo practico Nº 1 de Inteligencia artificial 2")
print("\n\nIntegrantes:")
print(" >> Costamagna Luciana")
print(" >> Felicito Milady")
print(" >> Martinez Ferran")
print("\n\n\n\n\n")


# La grilla viene por defecto con estanterias 3x3x2 (36 estanterias 10 x 10)
# Decimos que viene con esos valores por defecto, preguntamos si se quiere o no
# Si se quieren entonces seteamos filas y columnas

# G.setEstanterias()
# Por ahora no le preguntamos a nadie, seteamos directamente desde aqui todo
G.setFilasColumnas()
G.setGrilla()
G.asignarVecinos()

# Definimos cuales van a ser los nodos o posiciones de carga y descarga
G.carga = G.grilla[0][0]
G.descarga = G.grilla[0][0]



ordenes = orders("ordenes")
# result,mejores = geneticAlg(ordenes[0:5],G)

# # simAnnealing(ordenes[0],G)
# xx = range(3)
# print(len(result))
# fig = px.bar(x = range(len(result)), y = mejores)
# fig.write_html('plots/gen_fitness.html', auto_open = True)
 

# geneticAlg(ordenes[0:1],G)
