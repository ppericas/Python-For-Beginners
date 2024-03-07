frase = input("Ingrese una frase: ")

print("1 : Contar el número de palabras que tiene la frase.")
print("2 : Convertir este texto en mayúsculas.")
accion = int(input("Ingrese la acción que desea realizar: "))

def contar_palabras(frase):
    palabras = frase.split()
    return len(palabras)

def convertir_mayuscula(frase):
    mayusculas = frase.upper()
    return mayusculas

while accion not in (1, 2):
    print("Ingrese una opción correcta.")
    accion = int(input("Ingrese la acción que desea realizar: "))

if accion == 1:
    numero_de_palabras = contar_palabras(frase)
    print(f"El número de palabras en la frase es: {numero_de_palabras}")
else:
    mayusculas = convertir_mayuscula(frase)
    print(f"La frase en mayuscula és: {mayusculas}")