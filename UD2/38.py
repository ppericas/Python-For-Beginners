altura = int(input("Ingrese la altura: "))
a = 1
espacio = " "
asterisco = "*"

if altura >= 2:
    for _ in range(altura):
        print((espacio * altura) + (asterisco) * a)
        altura -= 1
        a += 2

else:
    print("Debe ser mayor o igual que 2")