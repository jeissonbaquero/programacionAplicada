#el programa indica los numero primos que hay en una rango de numeros ,ademas de contarnos el tiempo en que se tarda en hacer testo en valores de milisegundos
import time
inicio= time.time()#toma el valor del tiempo en que inicia
time.sleep(1)
for i in range (0,3):
    conta=0
    for n in range(1,i+1):
        residuo=i%n
        if residuo == 0:
            conta= conta+1
    if conta==2: 
        print(f'{i} es un primo')
fin= time.time()#toma el timepo en el que finaliza
print("t = ",(fin-inicio)*1000)#impreme la diferencia entra el teimpo de entrada y el tiempo de salida, dando el tiempo de ejecucion del programa
