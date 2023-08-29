def suma(a,b):
    #print(a+b)
    return a+b
a=(input('ingrese el primer valor')) #sin el int() se toma el valor de la variable como str
b=(input('ingrese el segundo valor'))
#a=int(a)
#b=int(b)
resultado = suma(a,b)
print(resultado)
print(type(resultado))
resultado=int(resultado)
print(type(resultado))
valor=resultado**3
print(valor)