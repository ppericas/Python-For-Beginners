tabla_multiplicar = {}

for i in range(1, 6):
    tabla_multiplicar[i] = {}
    for j in range(11):
        tabla_multiplicar[i][j] = i * j

print(tabla_multiplicar)