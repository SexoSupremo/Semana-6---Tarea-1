class Producto:
    def __init__(self, nombre, precio):
        self._nombre = nombre
        self._precio = precio
    
    @property
    def nombre(self):
        return self._nombre
    
    @property
    def precio(self):
        return self._precio
    
    def mostrar_info(self):
        return f"Nombre: {self._nombre}\nPrecio: ${self._precio:.2f}"

class Ropa(Producto):
    def __init__(self, nombre, talla, precio):
        super().__init__(nombre, precio)
        self._talla = talla
    
    @property
    def talla(self):
        return self._talla
    
    def mostrar_info(self):
        return f"{super().mostrar_info()}\nTalla: {self._talla}"

class Pantalon(Ropa):
    def __init__(self, talla, precio, estilo):
        super().__init__("Pantalon", talla, precio)
        self._estilo = estilo
    
    def mostrar_info(self):
        return f"{super().mostrar_info()}\nEstilo: {self._estilo}"

class Camisa(Ropa):
    def __init__(self, talla, precio, tipo_manga):
        super().__init__("Camisa", talla, precio)
        self._tipo_manga = tipo_manga
    
    def mostrar_info(self):
        return f"{super().mostrar_info()}\nTipo de manga: {self._tipo_manga}"

class Zapatos(Ropa):
    def __init__(self, talla, precio, tipo):
        super().__init__("Zapatos", talla, precio)
        self._tipo = tipo
    
    def mostrar_info(self):
        return f"{super().mostrar_info()}\nTipo: {self._tipo}"

class Carrito:
    def __init__(self):
        self._productos = []
    
    def agregar_producto(self, producto):
        self._productos.append(producto)
    
    def obtener_total(self):
        return sum(producto.precio for producto in self._productos)
    
    def mostrar_carrito(self):
        if not self._productos:
            return "El carrito está vacío"
        
        resumen = "\n=== Carrito de Compras ===\n"
        for i, producto in enumerate(self._productos, 1):
            resumen += f"\nProducto {i}:\n{producto.mostrar_info()}\n---------------"
        resumen += f"\nTotal a pagar: ${self.obtener_total():.2f}"
        return resumen

class Tienda:
    def __init__(self):
        self._inventario = []
        self._carrito = Carrito()
    
    def agregar_producto(self, producto):
        self._inventario.append(producto)
    
    def mostrar_inventario(self):
        if not self._inventario:
            return "No hay productos en el inventario"
        
        inventario = "\n----- Inventario ----------\n"
        for i, producto in enumerate(self._inventario, 1):
            inventario += f"\nProducto {i}:\n{producto.mostrar_info()}\n---------------"
        return inventario
    
    def comprar_producto(self, indice):
        try:
            producto = self._inventario[indice]
            self._carrito.agregar_producto(producto)
            return f"\nProducto agregado al carrito:\n{producto.mostrar_info()}"
        except IndexError:
            return "El producto no se encuentra"
    
    def mostrar_carrito(self):
        return self._carrito.mostrar_carrito()

def main():
    # Crear la tienda
    tienda = Tienda()
    
    # Agregar productos al inventario
    productos = [
        Pantalon("32", 45.99, "Casual"),
        Pantalon("34", 49.99, "Formal"),
        Camisa("M", 35.99, "Corta"),
        Camisa("L", 39.99, "Larga"),
        Zapatos("42", 89.99, "Deportivo"),
        Zapatos("40", 99.99, "Formal")
    ]
    
    for producto in productos:
        tienda.agregar_producto(producto)
    
    while True:
        print("\n=== Tienda de Ropa ===")
        print("1. Ver inventario")
        print("2. Comprar producto")
        print("3. Ver carrito")
        print("4. Salir")
        
        opcion = input("\nElija una opción: ")
        
        if opcion == "1":
            print(tienda.mostrar_inventario())
        elif opcion == "2":
            print(tienda.mostrar_inventario())
            try:
                indice = int(input("\nIngrese el número de producto que quiere comprar: ")) - 1
                print(tienda.comprar_producto(indice))
            except ValueError:
                print("Por favor ingrese un número válido")
        elif opcion == "3":
            print(tienda.mostrar_carrito())
        elif opcion == "4":
            print("¡Gracias por su compra!")
            break
        else:
            print("La opción elegida no es válida")

if __name__ == "__main__":
    main()