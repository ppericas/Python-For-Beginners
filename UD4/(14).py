class Vehiculos:
    def __init__(self, ruedas, velocidad=0):
        self.ruedas = ruedas
        self.velocidad = velocidad

    def acelerar(self, velocidad):
        return f"Acelerando el vehiculo a {velocidad} K/H"


class Coche(Vehiculos):
    def __init__(self, ruedas, puertas):
        super().__init__(ruedas)
        self.puertas = puertas

    def acelerar(self, velocidad):
        return f"Velocidad actual del coche: {velocidad} K/H"


class Bicicleta(Vehiculos):
    def __init__(self, ruedas, tipo):
        super().__init__(ruedas)
        self.tipo = tipo
    
    def acelerar(self, velocidad):
        return f"Velocidad actual de la bicicleta: {velocidad} K/H"

vehiculo = Vehiculos(ruedas=0)
coche = Coche(ruedas=4, puertas=4)
bicicleta = Bicicleta(ruedas=2, tipo="Montaña")

print(vehiculo.acelerar(0))
print(coche.acelerar(120))
print(bicicleta.acelerar(60))