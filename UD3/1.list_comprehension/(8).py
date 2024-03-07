def primo(numero):
    contador=0
    for i in range(1,numero+1):
        if numero==1:
            contador=2
            break
        if numero%i==0:
            contador+=1
    if contador==2:
        return numero
    else:
        return
primos= [primo(numero) for numero in range(1,101) if primo(numero)!=None]
print("Numeros 1-100:", primos)

primos = [num for num in range(2, 1000) if primo(num)]
primeros_100_primos = [num for num in primos if num][:100]

print("Numeros 1-100:", primeros_100_primos)