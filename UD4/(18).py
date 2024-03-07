class Tienda:
    productos = 0
    
    @staticmethod
    def agregar_producto():
        Tienda.productos += 1
        print("Se ha añadido un producto al inventario.")

    def obtener_productos():
        return Tienda.productos

Tienda.agregar_producto()
Tienda.agregar_producto()

total = Tienda.obtener_productos()
print(f"Total de productos en la tienda: {total}")