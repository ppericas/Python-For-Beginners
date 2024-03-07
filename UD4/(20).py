class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def informacion(self):
        print(f"Vehículo: {self.marca} {self.modelo}")

class Automovil(Vehiculo):
    def __init__(self, marca, modelo, num_puertas, tipo_carroceria):
        super().__init__(marca, modelo)
        self.num_puertas = num_puertas
        self.tipo_carroceria = tipo_carroceria

    def informacion(self):
        super().informacion()
        print(f"Tipo: Automóvil, Puertas: {self.num_puertas}, Carrocería: {self.tipo_carroceria}")

class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, cilindrada, tipo_moto):
        super().__init__(marca, modelo)
        self.cilindrada = cilindrada
        self.tipo_moto = tipo_moto

    def informacion(self):
        super().informacion()
        print(f"Tipo: Motocicleta, Cilindrada: {self.cilindrada}, Tipo: {self.tipo_moto}")


def mostrar_informacion_vehiculo(vehiculo):
    vehiculo.informacion()


auto = Automovil("Toyota", "Land Cruiser", 4, "Todoterreno")
moto = Motocicleta("Honda", "VT Shadow", "750cc", "Cruiser")


vehiculos = [auto, moto]
for vehiculo in vehiculos:
    mostrar_informacion_vehiculo(vehiculo)