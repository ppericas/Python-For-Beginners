altura = int(input("Ingrese la altura del cuadrado:"))
espacio = " "
asterisco = "*"
if altura >= 2:
    primera_ultima_fila = (asterisco + espacio)*altura
    print(primera_ultima_fila)

    for _ in range(altura - 2):
        print(asterisco + espacio * (altura - 2) + espacio * (altura - 1) + asterisco)
    print(primera_ultima_fila)

else:
    print("La altura debe ser mayor o igual que 2")