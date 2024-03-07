print("Sumas: ")
def suma_acumulativa(n):
    return sum(range(1, n+1))
suma_acumulativa = [suma_acumulativa(i) for i in range(1, 11)]
print(suma_acumulativa)

print("Restas: ")
def resta_acumulativa(n):
    return sum(range(10, n - 1, -1))
resta_acumulativa = [resta_acumulativa(i) for i in range(1, 11)]
print(resta_acumulativa)

print("Producto: ")
def producto_acumulativo(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
producto_acumulativo = [producto_acumulativo(i) for i in range(1, 11)]
print(producto_acumulativo)

print("División: ")
def division_acumulativa(n):
    result = 1
    for i in range(1, n + 1):
        result /= i
    return result
division_acumulativa = [division_acumulativa(i) for i in range(1, 11)]
print(division_acumulativa)