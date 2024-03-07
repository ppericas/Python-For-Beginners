texto = "Hello World".lower()

conteo_vocales = {vocal: texto.count(vocal) for vocal in 'aeiou'}

print(conteo_vocales)
