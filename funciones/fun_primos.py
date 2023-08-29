def buscar_pr(a,b):
    for i in range (a,b+1):
        contador=0
        for n in range(1,i+1):
            residuo=i%n
            if residuo == 0:
                contador= contador+1
            if contador>2:
                break
        if contador ==2: 
            print(f'{i} es un primo')
a=int(input('digite el numero inferior del rango '))
b=int(input('digite el numero superior del rango '))
buscar_pr(a,b)
