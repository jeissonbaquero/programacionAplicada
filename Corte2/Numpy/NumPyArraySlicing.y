#para recortar arreglos o coger un cierto rango de la matrices
#matriz 1D
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5])

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[4:])

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[:4])

#rebanado negsativo, coge el rango al reves
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[-3:-1])

#en el siguiente codigo se da dos pasos en el recorte del arreglo

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5:2])

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[::2])
#matriz 2d
import numpy as np

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[1, 1:4])

import numpy as np

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[0:2, 2])

import numpy as np

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[0:2, 1:4])
