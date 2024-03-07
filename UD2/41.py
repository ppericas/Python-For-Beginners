from sympy import isprime

def es_primo(numero):
    return isprime(numero)

def calcular_fatorial(numero):
    fatorial = 1
    for i in range(1, numero + 1):
        fatorial *= i
    return fatorial

resultado = int(input("Ingrese un número: "))

print("1 : Saber si el número es primo.")
print("2 : Calcular el factorial.")
accion = int(input("Ingrese la acción que desea realizar: "))

while accion not in (1, 2):
    print("Ingrese una opción correcta.")
    accion = int(input("Ingrese la acción que desea realizar: "))

if accion == 1:
    if es_primo(resultado):
        print(f"{resultado} es un número primo.")
    else:
        print(f"{resultado} no es un número primo.")
else:
    print(f"El factorial de {resultado} es: {calcular_fatorial(resultado)}")
