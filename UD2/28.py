import random

numero_random = random.randint(1, 100)
print(numero_random)
numero = ""
count = 0

while (count < 10) and (numero_random != numero):
    numero = int(input("Ingrese un número del 1 al 100: "))
    count += 1
if (numero == numero_random):
    print("Enhorabuena, has acertado el número!")
else:
    print("Mala suerte, otra vez sera")