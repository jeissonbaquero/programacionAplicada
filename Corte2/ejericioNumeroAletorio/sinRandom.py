#intenteo de generar un numero seudoaleatorio sin el metodo ramndom, utilizador el metodo tiempara que ala horar acutal se generea cierto numero 
import time

def generar_numero_azar():
    # se Utiliza el tiempo actual en segundos para generar un número aparentemente aleatorio
    numero = int((time.time() * 1000) % 100)
    return numero


numero_aleatorio = generar_numero_azar()
print("Número aleatorio:", numero_aleatorio)
