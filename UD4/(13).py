class Animal:
    def __init__(self):
        pass

    def mover(self):
        return "El animal se mueve de alguna manera."


class Pajaro(Animal):
    def __init__(self):
        super().__init__()

    def volar(self):
        return "El pájaro vuela por el cielo."


class Pez(Animal):
    def __init__(self):
        super().__init__()

    def nadar(self):
        return "El pez nada por el agua."

pajaro = Pajaro()
pez = Pez()

print(pajaro.mover())
print(pajaro.volar())
print(pez.mover())
print(pez.nadar())