from random import randint

class Personaje:
    def __init__(self, nombre, salud, ataque=0):
        self.nombre = nombre
        self.salud = salud
        self.ataque = ataque

    def atacar(self):
        while enemigo.salud > 0:
            self.ataque = randint(1, 10)
            jugador.salud -= self.ataque
            print(f"{jugador.nombre} ha recibido {self.ataque} puntos de daño. Ahora tiene {jugador.salud} puntos de salud")

            self.ataque = randint(1, 10)
            enemigo.salud -= self.ataque 
            if enemigo.salud <= 0:
                print(f"{enemigo.nombre} ha recibido {self.ataque} puntos de daño. Ahora tiene 0 puntos de salud")
            else:
                print(f"{enemigo.nombre} ha recibido {self.ataque} puntos de daño. Ahora tiene {enemigo.salud} puntos de salud")

            if enemigo.salud <= 0:
                print(f"{enemigo.nombre} ha sido derrotado")
                break

# Create instances of Personaje
jugador = Personaje(nombre="Jugador", salud=100)
enemigo = Personaje(nombre="Enemigo", salud=50)

# Call the atacar method on the jugador object
jugador.atacar()
