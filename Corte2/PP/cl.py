class Circulo:
    pi=3.14

    def __init__(self,diametro):#este es el contructor de la case se debe nombrar __init__
        print('nuevo circulo con diametro:{}'.format (diametro))
        self.radio= diametro/2
    def circuferencias(self):
        return 2*self.pi*self.radio
cir=Circulo(2)
mediaPizza=Circulo(12)
habitacionredond=Circulo(6)
print(cir.circuferencias())
print(mediaPizza.circuferencias())