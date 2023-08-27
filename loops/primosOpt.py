#el primer codigo realiza un sondeo de un rango de numero inciando desde cero hasta un tope, esto con el fin de imprimir los numeros primos

#  9)Imprimir los números primos existentes entre 0 y 30
tope_rango=30
n = 0
primo = True
while (n < tope_rango):# con el while se hace un barrido por los diversos numeros eneteres dentro del rango
    for div in range(2, n):#con este for se utiliza para realizar la divicion de los diversos numero menores a este y mayores a 1 ,
                           # se descartam el numero 1 y el mismo numero porque esto son los que son divisores de los numeros primos
        if (n % div == 0):# con este condicional se descarta o no si es un numeor primo puesto que si cumple esta condicion el 
                           # numero tedran tres divisores algo para descartarlo como primo
            primo = False
    if (primo):# coneste condicional se sabe si imprime o no el numero depdendiedod del if anterior 
               # si se descarta compo primo se sigue con el sigueinte numero y s evuevle la variable primo como en el inicio
        print(n)
    else:
        primo = True
    n += 1

# encuanto al sigueinte codigo es casi lo mimso que el anterior solo que se le agrega un break apra que a la hora de ingresa al 
# condicional que lo cataloga como no primo , de una vez salte al sigueinte numero

# 10) ¿Se puede mejorar el proceso del punto 9? Utilizar las sentencias break y/ó continue para tal fin
n = 0
primo = True
while (n < tope_rango):
    for div in range(2, n):
        if (n % div == 0):
            primo = False
            break #este break hace que el numero que se analizo y se decarto como primo no se siga analsiando y se salte de unavez al siguiente numero
    if (primo):
        print(n)
    else:
        primo = True
    n += 1
#los siguente dos codigos entre los dos codigos anteriores cual tiene mejro rendimiento, esto mediante el conteo de los ciclos que hagan cada uno , 
# el resultado del primeorm dividira al resultado del segundo para observar la optimizacion que se halla tenido

# 11) En los puntos 9 y 10, se diseño un código que encuentra números primos y además se lo optimizó. ¿Es posible saber en qué medida se optimizó?

ciclos_sin_break = 0
n = 0
primo = True
while (n < tope_rango):
    for div in range(2, n):
        ciclos_sin_break += 1# realiza el aumento del conteo da cada ciclo
        if (n % div == 0):
            primo = False
    if (primo):
        print(n)
    else:
        primo = True
    n += 1
print('Cantidad de ciclos: ' + str(ciclos_sin_break))


ciclos_con_break = 0
n = 0
primo = True
while (n < tope_rango):
    for div in range(2, n):
        ciclos_con_break += 1# realiza el aumento del conteo da cada ciclo
        if (n % div == 0):
            primo = False
            break
    if (primo):
        print(n)
    else:
        primo = True
    n += 1
print('Cantidad de ciclos: ' + str(ciclos_con_break))
print('Se optimizó a un ' + str(ciclos_con_break/ciclos_sin_break) + '% de ciclos aplicando break') # realiza la division para ver la optimizacion

# 12) Si la cantidad de números que se evalúa es mayor a treinta, esa optimización crece?
tope_rango=100
ciclos_sin_break = 0
n = 0
primo = True
while (n < tope_rango):
    for div in range(2, n):
        ciclos_sin_break += 1
        if (n % div == 0):
            primo = False
    if (primo):
        print(n)
    else:
        primo = True
    n += 1
print('Cantidad de ciclos: ' + str(ciclos_sin_break))

ciclos_con_break = 0
n = 0
primo = True
while (n < tope_rango):
    for div in range(2, n):
        ciclos_con_break += 1
        if (n % div == 0):
            primo = False
            break
    if (primo):
        print(n)
    else:
        primo = True
    n += 1
print('Cantidad de ciclos: ' + str(ciclos_con_break))
print('Se optimizó a un ' + str(ciclos_con_break/ciclos_sin_break) + '% de ciclos aplicando break')