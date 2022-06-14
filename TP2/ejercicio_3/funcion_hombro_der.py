
import numpy as np
import matplotlib.pyplot as plt

def sigmoidal (x): # Onda sigmoidal derecha
    z = np.exp(-x)
    sig = 1 / (1 + z)
    return sig

x=np.linspace(-100,100,200)
y=np.array([sigmoidal(t) for t in x])
#plt.ylim(0,4)
plt.plot(x,y)
plt.show()

