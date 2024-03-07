class Libros:
    def __init__(self, titulo, autor, genero, paginas):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.paginas = paginas

    def get_titulo(self):
        return self.titulo

    def get_autor(self):
        return self.autor

    def get_genero(self):
        return self.genero

    def get_paginas(self):
        return self.paginas

    def set_titulo(self, titulo):
        self.titulo = titulo

    def set_autor(self, autor):
        self.autor = autor

    def set_genero(self, genero):
        self.genero = genero

    def set_paginas(self, paginas):
        self.paginas = paginas

mi_libro = Libros("Fight Club", "Chuck Palahiuk", "Novela Negra", 218)

print("Título:", mi_libro.get_titulo())
print("Autor:", mi_libro.get_autor())
print("Género:", mi_libro.get_genero())
print("Páginas:", mi_libro.get_paginas())

# Using the set methods to change values
mi_libro.set_titulo("Fight Club")
mi_libro.set_autor("Chuck Palahniuk")
mi_libro.set_genero("Novela/Sátira/Ciencia ficción")
mi_libro.set_paginas(218)

print(mi_libro.get_titulo(), mi_libro.get_autor(), mi_libro.get_genero(), mi_libro.get_paginas())