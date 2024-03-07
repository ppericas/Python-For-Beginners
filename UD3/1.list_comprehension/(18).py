def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

primeros_10_numeros = {num: es_primo(num) for num in range(1, 11)}
print(primeros_10_numeros)