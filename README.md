# Sistema de una tienda de ropa utilizando POO ## 

## Proposito

 Este sistema se diseñó para gestionar una tienda de ropa, permitiendo lo requerido dentro de la Tarea: Administrar el inventario de distintos tipos de prendas, Simular una compra y mostrar la aplicacion de los principios de POO

 Este proyecto es un ejemplo educativo simple de como podriamos implementar un sistema comercial usando POO en Python

## Estructura

 El proyecto no dispone de una jerarquía visual de clases para representar los tipos de productos de ropa ya que se sigue los pasos de la tarea de forma especifica, sin embargo, esta es su disposición dentro del codigo:

 Producto
 #### -Ropa
 #### --Pantalón
 #### --Camisa
 #### --Zapatos

## Clases Princiaples

Producto: La clase base que contiene los atributos básicos determinados dentro de la tarea (nombre y precio)
Ropa: Hereda del Producto y se añade el atributo talla
Pantalon,Camisa, Zapatos: Clases especficias dispuestas en la tarea que heredan de Ropa y añaden atributos solicitadas en la misma
Carrito: Manipula la lista de productos elegidos y calcula el total a pagar
Tienda: Gestiona el inventario y las operaciones de la compra


## Ejecución:

1. Python 3.11 o superior instalado
2. Clonar el repositorio : git clone https://github.com/tu-usuario/Tienda_Ropa_POOBootcamp.git
3. Dependiendo del sistema operativo navegar hacia la ruta del proyecto
 - Windows : cd C://user/carpeta/tarea1.py
 - Linux : ~/user/carpeta/tarea1.py
4. Ejecuta : py tarea1.py