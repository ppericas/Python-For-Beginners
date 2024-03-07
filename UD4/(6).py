class Coche:
    def __init__(self, marca, modelo, potencia, color, matriculacion):
        self.marca = marca
        self.modelo = modelo
        self.potencia = potencia
        self.color = color
        self.matriculacion = matriculacion
        self.siguiente_revision = None

    def mostrar(self):
        return self.marca, self.modelo, self.potencia, self.color, self.matriculacion

    def acelerar(self):
        return self.potencia + 10
    
    def frenar(self):
        return self.potencia - 10

    def itv(self):
        año_actual = 2024
        if not self.siguiente_revision:
            if (año_actual - self.matriculacion) <= 4:
                self.siguiente_revision = self.matriculacion + 4
            elif (año_actual - self.matriculacion) <= 6:
                self.siguiente_revision = self.matriculacion + 6
            elif (año_actual - self.matriculacion) <= 8:
                self.siguiente_revision = self.matriculacion + 8
            else:
                self.siguiente_revision = año_actual + 1
        else:
            self.siguiente_revision += 1

        return self.siguiente_revision

marca = input("Inserte la marca del coche")
modelo = input("Inserte el modelo del coche")
potencia = int(input("Inserte la potencia del coche"))
color = input("Inserte el color del coche")
matriculacion = int(input("Inserte el año de matriculacion del coche"))

coche = Coche(marca, modelo, potencia, color, matriculacion)
print(coche.mostrar(), coche.acelerar(), coche.frenar(), coche.itv())