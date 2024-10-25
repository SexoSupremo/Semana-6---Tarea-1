
class Ropa:
    def __init__(self, tipo, talla, precio):
        self.tipo = tipo
        self.talla = talla
        self.precio = precio
    
    def mostrar_info(self):
        print(f"Tipo: {self.tipo}")
        print(f"Talla: {self.talla}")
        print(f"Precio: ${self.precio}")


class Pantalon(Ropa):
    def __init__(self, talla, precio, estilo):
        super().__init__("Pantalon", talla, precio)
        self.estilo = estilo
    
    def mostrar_info(self):
        super().mostrar_info()
        print(f"Estilo: {self.estilo}")

class Camisa(Ropa):
    def __init__(self, talla, precio, tipo_manga):
        super().__init__("Camisa", talla, precio)
        self.tipo_manga = tipo_manga
    
    def mostrar_info(self):
        super().mostrar_info()
        print(f"Tipo de manga: {self.tipo_manga}")

class Zapatos(Ropa):
    def __init__(self, talla, precio, tipo):
        super().__init__("Zapatos", talla, precio)
        self.tipo = tipo
    
    def mostrar_info(self):
        super().mostrar_info()
        print(f"Tipo: {self.tipo}")

class Corbata(Ropa):
    def __init__(self, talla, precio, diseño):
        super().__init__("Corbata", talla, precio)
        self.diseño = diseño
    
    def mostrar_info(self):
        super().mostrar_info()
        print(f"Diseño: {self.diseño}")

class Boxer(Ropa):
    def __init__(self, talla, precio, material):
        super().__init__("Boxer", talla, precio)
        self.material = material
    
    def mostrar_info(self):
        super().mostrar_info()
        print(f"Material: {self.material}")

class Bombacha(Ropa):
    def __init__(self, talla, precio, tipo):
        super().__init__("Bombacha", talla, precio)
        self.tipo = tipo
    
    def mostrar_info(self):
        super().mostrar_info()
        print(f"Tipo: {self.tipo}")

class Remera(Ropa):
    def __init__(self, talla, precio, diseño):
        super().__init__("Remera", talla, precio)
        self.diseño = diseño
    
    def mostrar_info(self):
        super().mostrar_info()
        print(f"Diseño: {self.diseño}")


class Tienda:
    def __init__(self):
        self.inventario = []
        self.carrito = []
    
    def agregar_producto(self, producto):
        self.inventario.append(producto)
    
    def mostrar_inventario(self):
        print("\n-----Inventario ----------")
        for i, producto in enumerate(self.inventario, 1):
            print(f"\nProducto {i}:")
            producto.mostrar_info()
            print("---------------")
    
    def comprar_producto(self, indice):
        if 0 <= indice < len(self.inventario):
            producto = self.inventario[indice]
            self.carrito.append(producto)
            print(f"\nProducto agregado al carrito:")
            producto.mostrar_info()
        else:
            print("El producto no se encuentra")
    
    def mostrar_carrito(self):
        if not self.carrito:
            print("\nEl carrito está vacío")
            return
            
        print("\n=== Carrito de Compras ===")
        total = 0
        for producto in self.carrito:
            producto.mostrar_info()
            print("---------------")
            total += producto.precio
        print(f"Total a pagar: ${total}")

def main():
    tienda = Tienda()
    
 
    tienda.agregar_producto(Pantalon("32", 45.99, "Casual"))
    tienda.agregar_producto(Pantalon("34", 49.99, "Formal"))
    tienda.agregar_producto(Camisa("M", 35.99, "Corta"))
    tienda.agregar_producto(Camisa("L", 39.99, "Larga"))
    tienda.agregar_producto(Zapatos("42", 89.99, "Deportivo"))
    tienda.agregar_producto(Zapatos("40", 99.99, "Formal"))
    tienda.agregar_producto(Corbata("Única", 25.99, "Rayada"))
    tienda.agregar_producto(Corbata("Única", 29.99, "Lisa"))
    tienda.agregar_producto(Boxer("M", 15.99, "Algodón"))
    tienda.agregar_producto(Boxer("L", 15.99, "Lycra"))
    tienda.agregar_producto(Bombacha("M", 12.99, "Clásica"))
    tienda.agregar_producto(Bombacha("L", 12.99, "Cola less"))
    tienda.agregar_producto(Remera("S", 19.99, "Lisa"))
    tienda.agregar_producto(Remera("M", 24.99, "Estampada"))
    
    while True:
        print("\n=== Tienda de Ropa ===")
        print("1. Ver inventario")
        print("2. Comprar producto")
        print("3. Ver carrito")
        print("4. Salir")
        
        opcion = input("\nElija una opción: ")
        
        if opcion == "1":
            tienda.mostrar_inventario()
        elif opcion == "2":
            tienda.mostrar_inventario()
            try:
                indice = int(input("\nIngrese el número de producto a comprar: ")) - 1
                tienda.comprar_producto(indice)
            except ValueError:
                print("Por favor ingrese un número válido")
        elif opcion == "3":
            tienda.mostrar_carrito()
        elif opcion == "4":
            print("¡Gracias por su compra!")
            break
        else:
            print("La opcion elegida no es valida")

if __name__ == "__main__":
    main()