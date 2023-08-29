def factorial(num):
    a = isinstance(num,int)
    if a == True and num >= 0:
        fact=1
        if a > 0:
            for i in range(1, num+1):
                fact=fact*i
        print(f'the factorial de {num} es: ', fact)
        
    else:
        print("por favor, ingresar un numero positivo")
        fact='no existe'
    return fact
while 1==1:
    numero=int(input("introducion un numero positivo: "))
    guardar=str(factorial(numero))
    print('el factorial : '+ guardar)