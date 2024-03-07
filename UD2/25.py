num1 = int(input("Ingrese un valor: "))
num2 = int(input("Ingrese un valor: "))

if num1 == num2:
    print("No pueden ser iguales.")
else:
    num3 = int(input("Ingrese un valor: "))

    if num1 == num3:
        print("No pueden ser iguales.")

    if num2 == num3:
        print("No pueden ser iguales.")

if num1 > num2:
    if num1 > num3:
        print(num1)
    else:
        print(num3)
elif num2 > num1:
    if num2 > num3:
        print(num2)
    else:
        print(num3)