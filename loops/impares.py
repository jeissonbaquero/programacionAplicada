#el siguete codigo determina que numero son paraes e impares  en un rango de numero
#for i in range(1,21):
    #con el modulo puede determinar si es impar o par el numero 
    #dando un residuo de 0 si es par y de 1 si es impar 
#    residuo=i%2
    #con el sigueinte condicional imprime si es par o es impar depedniedeeo del residuo obtenido
#    if residuo == 0:
#        print(f'{i} es par')
#    else:
#        print(str(i)+'es impar')

#este codigo de adelante reliza otra tarea a diferencia que el anteriro 
#for i in range(0,6):
#    result = i**3
#    print(result)


# por ultimo este codigo se puede evidecnia como una variable puede cambiar
#encuanto al tipo, pasaod de float a int
times = input("Enter a number of times: ")
times = float(times)
times = int(times)
print(type(times))
print(times)

if times == 0:
    print("Don't do anything")
else:
    for i in range(1,times+1):
        print("i = ", i)