#el codigo compara dos numero los cuales sonde de diferente tipo de variable numerico, ademas de eso realia la suma de estos numero dado com resultado un tipo
a=input("ingresar un numero a: ")
a=int(a)
b=input("ingresar un numero b: ")
b=float(b)
c=a+b

if a==b:
    print("iguales")
else:
    print("diferentes")
print("a es de tipo: ", type(a))
print("b es de tipo: ", type(b))
print("c = ",c)
print("c es de tipo: ", type(c))

if type(a) == type(b):
    print("a y b son del mismo tipo")
else:
    print("a y b son de diferentes tipo")