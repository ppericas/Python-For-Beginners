numero = int(input("Inserte un número: "))
j = numero
def es_primo(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

while j > 1:
    if es_primo(j):
        print(j)
    j -= 1