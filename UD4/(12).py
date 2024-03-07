class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


class Empleado(Persona):
    def __init__(self, nombre, edad, salario):
        super().__init__(nombre, edad)
        self.salario = salario

empleado = Empleado("Juan", 39, 30000)

print(f"Nombre: {empleado.nombre}. Edad: {empleado.edad}. Salario: {empleado.salario}.")