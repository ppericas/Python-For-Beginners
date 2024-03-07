class Vehiculos:
    def __init__(self):
        pass

    def arrancar(self):
        return ""


class Coche:
    def __init__(self):
        super().__init__()

    def arrancar(self):
        return "Coche arrancado"


class Moto:
    def __init__(self):
        super().__init__()

    def arrancar(self):
        return "Moto arrancado"        

coche = Coche()
moto = Moto()

print(coche.arrancar())
print(moto.arrancar())