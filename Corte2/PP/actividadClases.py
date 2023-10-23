import math
class Circulo:
    pi=3.1416
    def __init__(self,diametro):
        print('nuevo circulo con diametro:{}'.format (diametro))
        self.radio= diametro/2
    def circuferencias(self):
        perimetro= 2*self.pi*self.radio
        print("el periemtro del circuto es {}".format(perimetro))
        return perimetro
    def Area (self):
        A=self.pi*(self.radio)**2
        print("el Area del circulo es {}".format(A))
        return A

class Rectangulo:
    def __init__(self,alto,ancho):
        print('se creo un nuevo rectangulo de ancho :{}'.format (ancho) +"y alturas:{}".format(alto))
        self.A=alto
        self.B=ancho
    def per(self):
        perimetro=(self.A *2)+(self.B*2) 
        print("el periemtro del rectangulo es {}".format(perimetro))
        return perimetro
    def Area (self):
        Area=self.A*self.B
        print("el Area del rectangulo es {}".format(Area))
        return Area

class  Cuadrado:
    def __init__(self,lado):
        print('se creo un nuevo cuadrado de lado:{}'.format (lado))
        self.lado=lado
    def per(self):
        perimetro=self.lado*4 
        print("el periemtro del cuadrado es {}".format(perimetro))
        return perimetro
    def Ar (self):
        A=self.lado**2
        print("el Area del cuadrado es {}".format(A))
        return A
class triangulo:
    def __init__ (self,l1,l2,l3):
        print('se creo un nuevo triangulos de lados:{}'.format (l1)+' {}'.format(l2)+' {}'.format(l3))
        self.A=l1
        self.B=l2
        self.C=l3
    def perimetro (self):
        perimetro=self.A+self.B+self.C
        print("el periemtro del triangulo es {}".format(perimetro))
        return perimetro
    def area(self):
        s=(self.A+self.B+self.C)/2
        area=math.sqrt(s*(s-self.A)*(s-self.B)*(s-self.C))
        print("el area del triangulo es {}".format(area))
        return area
    

C=Circulo(2)
C.Area()
C.circuferencias()

Cu=Cuadrado(3)
Cu.Ar()
Cu.per()


re= Rectangulo(2,3)
re.Area()
re.per()


tri=triangulo(3,5,4)
tri.area()
tri.perimetro()
        