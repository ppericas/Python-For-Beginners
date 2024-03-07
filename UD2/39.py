altura = int(input("Ingrese la altura: "))
i = 1
j = 1
k = 0
l = altura

m = altura
n = 1
o = altura

e = "."
a = "*"
if altura > 2:
    if altura % 2 == 0:
        for _ in range(altura // 2):
            print((e * ((altura // 2) - i)) + (a * j))
            i += 1
            j += 2
        
        for _ in range(altura // 2):
            print((e * k) + (a * (l - 1)))
            k += 1
            l -=2

    else:

        for _ in range(altura // 2 + 1):
            print((e * (m - 2)) + (a * n))
            m -= 1
            n += 2
        
        for _ in range(altura // 2):
            print((e * m)+(a * (o - 2)))
            m += 1
            o -= 2





else:
    print("La altura debe ser mayor que 2")