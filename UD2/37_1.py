altura = int(input("Ingrese la altura del cuadrado:"))
asterisco = "*"
espacio = " "

if altura >= 2:

    for _ in range(altura):
        print((asterisco + espacio) * altura)

else:
    print("La altura debe ser mayor o igual que 2")