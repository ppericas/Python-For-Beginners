class CalculadoraRecursiva:
    def __init__(self, n):
        self.n = n
        self.resultado = None

    def reiniciar_resultado(self):
        self.resultado = None

    def fibonacci(self, n):
        if n <= 1:
            return n
        else:
            return self.fibonacci(n-1) + self.fibonacci(n-2)

# Calcular el n término de Fibonacci
n = 8
calculador_fibonacci = CalculadoraRecursiva(n)
resultado = calculador_fibonacci.fibonacci(n)
print(f"El término {n} de la sucesión de Fibonacci es: {resultado}")

reiniciar = calculador_fibonacci.reiniciar_resultado()
m = 9
calculador_fibonacci = CalculadoraRecursiva(n)
resultado = calculador_fibonacci.fibonacci(m)
print(f"El término {m} de la sucesión de Fibonacci es: {resultado}")