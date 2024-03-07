i = int(input("Ingrese un número:"))
factorial = 1

for num in range(1, i + 1):
    factorial *= num

print(factorial)