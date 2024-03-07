class CalculadoraRecursiva:
    def __init__(self, n):
        self.n = n

class Fibonacci(CalculadoraRecursiva):
    def __init__(self, n):
        super().__init__(n)

    def fibonacci(self, n):
        if n <= 1:
            return n
        else:
            return self.fibonacci(n-1) + self.fibonacci(n-2)
        
class Factorial(CalculadoraRecursiva):
    def __init__(self, n):
        super().__init__(n)

    def factorial(self, n):
        if n == 0:
            return 1
        else:
            return n * self.factorial(n-1)

# Calcular el n término de Fibonacci
n_fibonacci = 5
calculadora_fibonacci = Fibonacci(n_fibonacci)
resultado_fibonacci = calculadora_fibonacci.fibonacci(n_fibonacci)

# Calcular el factorial de n
n_factorial = 6
calculadora_factorial = Factorial(n_factorial)
resultado_factorial = calculadora_factorial.factorial(n_factorial)

print(f"El término {n_fibonacci} de la sucesión de Fibonacci es: {resultado_fibonacci}")
print(f"El factorial de {n_factorial} es: {resultado_factorial}")
