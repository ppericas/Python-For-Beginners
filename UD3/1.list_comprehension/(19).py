words = ['apple', 'banana', 'cherry', 'cucumber', 'elderberry', 'apricot', 'avocado']

palabras = {word[0]: [w for w in words if w.startswith(word[0])] for word in words}

print(palabras)
