import random #Este módulo implementa generadores de números pseudoaleatorios para varias distribuciones.
#from matplotlib import pyplot as plt # la libreria matplotlib.pyplot es una coleccion de funciones deestilo de comando que hacen que matplotlib funcione como MATLAB

numero_a=range(1,13) # se geneera nu
numero_b=[random.randint(1,1000)for i in range (12)]
#plt.plot(numero_a,numero_b)# grafica un dato ocn respecto al otro cogiendo a numero_a en el eje X y numero_b en el eje Y
#plt.show()
print(numero_a)
print(numero_b)
print(numero_b + numero_a)