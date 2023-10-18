class Facade:
    pass
edad= int()
sueldo= int()
reacionalidad= str()


facade_1= Facade()## se declaro un objeto
facade_1_type =type(facade_1)
print(facade_1_type)##medice de que tipo de clase viene
class Grade:
    numero_minimio=65#es un atributo que se le asigno
    pass

class Rules:
    def washing_brushes(self):#se ponene sel siempre en  los parentesis , si se tinei mas parametros para este, este parametro va de primero
        return 'hola'

class circle:
    pi= 3.14
    def area(self, readio):
        return circle.pi*readio**2 # para poner un paramewtro en una funcion se llama a la calse si, el parametro ya esta en los necesario de la funcion no se llama creo

circulo=circle()
pizza_area=circulo.area(12/2)
print(pizza_area)
teaching_table_area= circulo.area(36/2)
print(teaching_table_area)
round_room_area= circulo.area(11460/2)
print(round_room_area)


class Circulo:
    pi=3.14
    radio =0
    def __init__(self,diametro):#este es el contructor de la case se debe nombrar __init__
        print('nuevo circulo con diametro:{}'.format (diametro))
    self.radio= diametro/2
    def circuferencias(self):
        return 2*self.pi*self.radio
cir=Circulo(2)
mediaPizza=Circulo(12)
habitacionredond=Circulo()
print(cir.circuferencias())
print(mediaPizza.circuferencias())
