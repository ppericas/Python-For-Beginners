from abc import ABC, abstractmethod
import math

class Figura(ABC):
    @abstractmethod
    def area(self):
        pass

    def informacion(self):
        print(f"Tipo de figura: {self.__class__.__name__}, Área: {self.area()}")

class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * self.radio**2

# Crear instancias de las clases
rectangulo = Rectangulo(5, 8)
circulo = Circulo(3)

# Llamar a los métodos informacion y area con polimorfismo
figuras = [rectangulo, circulo]
for figura in figuras:
    figura.informacion()
    print(f"Área: {figura.area()}\n")
