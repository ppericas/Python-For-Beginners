class Rectangulo:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base*self.altura
    
rectangulo = Rectangulo(10, 20)
print(rectangulo.calcular_area())