class Personaje:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def mover_derecha(self):
        self.x += 1

    def mover_izquierda(self):
        self.x -= 1

    def mover_arriba(self):
        self.y += 1

    def mover_abajo(self):
        self.y -= 1


class Enemigo(Personaje):
    def __init__(self, x=-20, y=10, boss="Clyde"):
        super().__init__(x, y)
        self.boss = boss


class Jugador(Personaje):
    def __init__(self, x=0, y=0, personaje="Pepper"):
        super().__init__(x, y)
        self.personaje = personaje


class Jugar:
    def encontrar_enemigo(self, jugador, enemigo):
        while jugador.x != enemigo.x or jugador.y != enemigo.y:
            if jugador.x != enemigo.x:
                jugador.mover_derecha() if jugador.x < enemigo.x else jugador.mover_izquierda()

            if jugador.y != enemigo.y:
                jugador.mover_arriba() if jugador.y < enemigo.y else jugador.mover_abajo()
            print(jugador.x, jugador.y)



jugador = Jugador()
enemigo = Enemigo()

jugar = Jugar()
jugar.encontrar_enemigo(jugador, enemigo)

print(f"Posición del jugador: ({jugador.x}, {jugador.y})")
