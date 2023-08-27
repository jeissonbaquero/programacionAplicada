#este codigo realiza el deletreo de una palabra quitando una letra, como la t de la palabra python,
#teniendo un tiempo de espera entre el deletro de cada letra
import time as tiempo # se importa la libreria time la cual proporciona varias funciones relacionadas con el tiempo

cadena='python'
#el ciclo for lo realizamos para recorrer la cadena anteriormente dicha sinedo la variable letra la que  va
# utilizado cada uno de las letra que conforman la palabra python 
for letra in cadena:
    #se realiza el condicional if para que cuando llege a la letra 't' esta no la imprima y siga con la siguiente letra
    if letra == 't':
        continue
    print(letra)
    tiempo.sleep(1)#metodo de la libreria tiem la cual realiza una pausa de 1 segunda para seguir el codigo