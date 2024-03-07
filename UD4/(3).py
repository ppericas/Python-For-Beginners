class Circulo:

    def __init__(self, radio, pi):
        self.radio = radio
        self.pi = pi

    def calcular_area(self):
        return self.pi*self.radio**2

    def calcular_longitud(self):
        return 2*self.pi*self.radio

circulo = Circulo(3, 3.14)
print(circulo.calcular_area(), circulo.calcular_longitud())