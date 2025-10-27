#Ejercicio 2
class productos:
    def __init__(self, nombre, precio, cantidad, código):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.código = código
         
    def mostrar_datos(self):
        print("Nombre del producto: ", self.nombre)
        print("Precio del producto: ", self.precio)
        print("Cantidad del producto: ", self.cantidad)

    def vender(self, cantidad_vender):
        if self.cantidad >= cantidad_vender:
            self.cantidad = self.cantidad - cantidad_vender
            print("vendido")
        else:
            print("No hay producto suficiente")

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
        código = int(input("Código: "))

        producto = productos(nombre, precio, cantidad, código)
        lista_productos.append(producto)
        print("Producto guardado")
    
    elif opcion == 2:
        for producto in lista_productos:
            if producto.código == código:
                print("Nombre: ", producto.nombre)
                print("Cantidad disponible:", producto.cantidad)
                print("/n")
    
    elif opcion == 3:
        código_n = int(input("Código del producto: "))

        existe = True    
        for producto in lista_productos:
            if producto.código == código_n:
                cantidad_vender = int(input("Cantidad a vender: "))
                producto.vender(cantidad_vender)
                break
        
        
        if existe == False:
            print("Este producto no esta disponible")
    
    elif opcion == 0:
        print("Fin del proceso")
        break

    else:
        print("opcion incorrecta")

