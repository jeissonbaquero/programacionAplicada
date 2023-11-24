#para la creacion de matrice se utiliz la funcion np.array(elementos que contine)
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)

print(type(arr))

import numpy as np

arr = np.array((1, 2, 3, 4, 5))

print(arr)

#matrices de 0D(continene un solo elemeto)
import numpy as np

arr = np.array(42)

print(arr)
#matrices de 1D(continene variose lemtneos dentro de una)
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)
#matrices de 2D(continene variose lemtneos dentro de filas y columnas)
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

print(arr)
#matrices de 23D(continene variose elementos dentro de filas y columnas)
import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(arr)


#como saber que dimencion tinee un arreglo se utiliaza
import numpy as np

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

#como crea un arreglo de verasdimenciones 
import numpy as np

arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('number of dimensions :', arr.ndim)
