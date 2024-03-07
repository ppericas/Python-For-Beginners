class Productos:
    def __init__(self, nombre, precio, descripcion):
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion

    def crear_producto(self, nombre, precio, descripcion):
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion

    def get_nombre(self):
        return self.nombre

    def get_precio(self):
        return self.precio

    def get_descripcion(self):
        return self.descripcion

    def set_nombre(self):
        nuevo_nombre = input("Nuevo nombre: ")
        self.nombre = nuevo_nombre
        return nuevo_nombre

    def set_precio(self):
        nuevo_precio = float(input("Nuevo precio: "))
        self.precio = nuevo_precio
        return nuevo_precio        

    def set_descripcion(self):
        nueva_descripcion = input("Nueva descripción: ")
        self.descripcion = nueva_descripcion
        return nueva_descripcion

productos = Productos("Pepsicola", 1.33, "Bebida isotónica")
print(productos.get_nombre(), productos.get_precio(), productos.get_descripcion())
productos.set_nombre()
productos.set_precio()
productos.set_descripcion()
print(productos.get_nombre(), productos.get_precio(), productos.get_descripcion())
