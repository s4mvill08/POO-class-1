class productos:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
         
    def mostrar_datos(self):
        print("Nombre del producto: ", self.nombre)
        print("Precio del producto: ", self.precio)
        print("Cantidad del producto: ", self.cantidad)

print("Control de los productos que se venden")
lista_productos = []

while True:
    print(" 1. Guardar producto")
    print(" 2. Cantidad de unidades disponibles")
    print(" 3. Cantidad a vender")
    print(" 0. Salir")
    opcion = int(input())
    
    if opcion == 1:
        nombre = input("Nombre: ")
        precio = float(input("Precio: "))
        cantidad = int(input("Cantidad: "))
        producto = productos(nombre, precio, cantidad)
        lista_productos.append(producto)
        print("Producto guardado")
    
    elif opcion == 2:
        nombre = input("Nombre del producto: ")
        for producto in lista_productos:
            if producto.nombre == nombre:
                print("Cantidad disponible:", producto.cantidad)
    
    elif opcion == 3:
        nombre = input("Nombre del producto: ")
        for producto in lista_productos:
            if producto.nombre == nombre:
                vender = int(input("Cantidad a vender: "))
                if vender > producto.cantidad:
                    print("No hay suficientes unidades")
                else:
                    producto.cantidad = producto.cantidad - vender
                    print("Venta realizada")
                    print("Quedan:", producto.cantidad)
                break
    
    else:
        print("Fin del proceso")
        break