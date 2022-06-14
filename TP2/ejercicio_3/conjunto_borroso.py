import numpy as np
import matplotlib.pyplot as plt

# def conjuntoTriangular(univ_dis,inicio,fin,medio):
pico = 1
univ_dis = np.arange(-45,46)
univ_dis = np.array(univ_dis)
inicio = -30
fin = 0
medio = -15

y = len(univ_dis)*[0]
for i in np.arange(inicio,fin+1):
    # print(i)
    if i< medio:
        ii = np.where(univ_dis == i)[0][0]
        y[ii] = abs(i-inicio)/abs(medio-inicio)
    elif i == medio:
        ii = np.where(univ_dis == i)[0][0]
        y[ii] = 1
    else:
        ii = np.where(univ_dis == i)[0][0]
        y[ii] = abs(fin-i)/abs(fin-medio)

print(univ_dis)
print(y)

fig, ax = plt.subplots()
ax.plot(univ_dis, y)
plt.show()