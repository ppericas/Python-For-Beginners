inicio = int(input("Valor inicio: "))
n = int(input("n: "))

cubos = {numero: numero ** 2 for numero in range(inicio + 1, inicio + n + 1)}
print(cubos)