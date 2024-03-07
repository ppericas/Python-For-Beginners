from itertools import permutations

[print(permutacion) for permutacion in list(permutations([1,2,3]))]

palabra = input("Ingrese una palabra")

[print(permutacion) for permutacion in list(permutations(palabra))]