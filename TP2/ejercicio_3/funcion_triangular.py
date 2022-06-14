import numpy as np
import matplotlib.pyplot as plt

def func_triangular (x, ancho, amp): #Una onda triangular con amplitud  amp, ancho ancho y pendiente  amp / 2*ancho
     if x>=ancho/2:
          r = 0.0
     elif x<=-ancho/2:
          r = 0.0
     elif x > -ancho/2 and x<0:
          r=2*x/ancho * amp + amp
     else:
          r=-2*x/ancho * amp + amp
     return r

x=np.linspace(-3,3,1000)
y=np.array([func_triangular(t,4.0,1.0) for t in x])
plt.ylim(0,2)
plt.plot(x,y)
plt.show()