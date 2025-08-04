class productos: #La clase en la que esta guardada la informaciòn basica de los productos
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
    #Ciclo en el que se muestra que quiere hacer el usuario
    print(" 1. Guardar producto")
    print(" 2. Cantidad de unidades disponibles")
    print(" 3. Cantidad a vender")
    print(" 0. Salir")
    opcion = int(input())
    
    if opcion == 1:
        
        #Datos del producto
        print("Ingrese el nombre del producto: ")
        nombre = input()
        print("Ingrese el precio del producto: ")
        precio = int(input())
        print("Ingrese la cantidad de productos disponibles: ")
        cantidad = int(input())
        
        # Se crea un objeto nuevo y se agrega a la lista vacia
        producto = productos(nombre, precio, cantidad)
        lista_productos.append(producto)
        print("El producto ha sido guardado correctamente.")
        
        #Se muestra la lista de productos
    elif opcion == 2:
        print("Cantidad de productos disponibles: ")
        if len(lista_productos) == 0:
            print("No hay productos disponibles")
        else:
            for producto in lista_productos:
                producto.mostrar_datos()
        
        # Se crea una lista de productos para vender
    elif opcion == 3:
        print("productos a vender")
        
        if len(productos) == 0:
            print("No hay productos para vender")
        else:
            numero = 1
            for p in productos:
                print(f"{numero}. {producto.nombre} ({producto.cantidad} disponibles)")
                numero = numero + 1
            
            numero = int(input()) - 1
            producto_seleccionado = productos[numero]
            
            cantidad_vender = int(input("¿Cuántas unidades quieres vender? "))
            
            if cantidad_vender <= producto_seleccionado.cantidad:
                producto_seleccionado.cantidad = producto_seleccionado.cantidad - cantidad_vender
                print(f"✓ Venta realizada")
                print(f"Quedan {producto_seleccionado.cantidad} unidades de {producto_seleccionado.nombre}")
            else:
                print("⚠️ No hay suficientes unidades disponibles")
            
        # Si el usuario quiere salir del programa    
    elif opcion == 0:
        print("Fin del proceso")
        break
    else: 
        print("Error, intente de nuevo")