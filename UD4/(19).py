class Producto:
    total_productos = 0  # Atributo estático para el contador global de productos en la tienda

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
        Producto.total_productos += 1

    def mostrar_informacion(self):
        print(f"Producto: {self.nombre}, Precio: {self.precio:.2f}€")

    @staticmethod
    def obtener_total_productos():
        return Producto.total_productos


producto1 = Producto("Pantalón", 20.99)
producto2 = Producto("Xilofono", 49.99)


producto1.mostrar_informacion()
producto2.mostrar_informacion()


total = Producto.obtener_total_productos()
print(f"Total de productos en la tienda: {total}")