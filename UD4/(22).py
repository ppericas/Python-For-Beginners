from abc import ABC, abstractmethod
import math

# Clase abstracta Color
class Color(ABC):
    @abstractmethod
    def obtener_color(self):
        pass

    def cambiar_color(self, nuevo_color):
        print(f"Cambiando color a {nuevo_color}")

    def comparar_colores(self, otro_color):
        return self.obtener_color() == otro_color.obtener_color()


class Forma(ABC):
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def obtener_informacion(self):
        pass

    @abstractmethod
    def calcular_area(self):
        pass

    @abstractmethod
    def calcular_perimetro(self):
        pass


class Rojo(Color):
    def obtener_color(self):
        return "Rojo"

class Azul(Color):
    def obtener_color(self):
        return "Azul"


class Cuadrado(Forma):
    def __init__(self, lado, color):
        super().__init__(color)
        self.lado = lado

    def obtener_informacion(self):
        print(f"Cuadrado de lado {self.lado}, Color: {self.color.obtener_color()}")

    def calcular_area(self):
        return self.lado**2

    def calcular_perimetro(self):
        return 4 * self.lado

    def cambiar_lado(self, nuevo_lado):
        print(f"Cambiando lado a {nuevo_lado}")
        self.lado = nuevo_lado


class Circulo(Forma):
    def __init__(self, radio, color):
        super().__init__(color)
        self.radio = radio

    def obtener_informacion(self):
        print(f"Círculo de radio {self.radio}, Color: {self.color.obtener_color()}")

    def calcular_area(self):
        return math.pi * self.radio**2

    def calcular_perimetro(self):
        return 2 * math.pi * self.radio

    def cambiar_radio(self, nuevo_radio):
        print(f"Cambiando radio a {nuevo_radio}")
        self.radio = nuevo_radio


rojo = Rojo()
azul = Azul()

cuadrado = Cuadrado(5, rojo)
circulo = Circulo(3, azul)

cuadrado.obtener_informacion()
print(f"Área del cuadrado: {cuadrado.calcular_area()}")
print(f"Perímetro del cuadrado: {cuadrado.calcular_perimetro()}")
cuadrado.cambiar_lado(8)

circulo.obtener_informacion()
print(f"Área del círculo: {circulo.calcular_area()}")
print(f"Perímetro del círculo: {circulo.calcular_perimetro()}")
circulo.cambiar_radio(5)

print(rojo.comparar_colores(azul))