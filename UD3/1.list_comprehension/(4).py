print("Mètode 1")
letras = [chr(i).lower() for i in range(65, 91)]
print(letras)

print("Mètode 2")
import string
alfabeto = [string.ascii_letters[i] for i in range(int(len(string.ascii_letters)/2))]
print(alfabeto)