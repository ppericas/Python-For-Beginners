def calcular_cuadrado(numero):
    return numero ** 2

resultados = {num: calcular_cuadrado(num) for num in range(1, 11)}
print(resultados)