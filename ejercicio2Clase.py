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
        
    elif opcion == 2:
        print("Cantidad de productos disponibles: ")
        if len(lista_productos) == 0:
            print("No hay productos disponibles")
        else:
            for producto in lista_productos:
                producto.mostrar_datos()
        
    elif opcion == 3:
        #Producto a vender
        print("Producto a vender: ") 
        contador = 1
        for producto in lista_productos:
            print(contador, producto.nombre, " - Cantidad: ", producto.cantidad)
            contador = contador + 1
    
        numero_de_producto = int(input()) - 1
    
        if 0 <= numero_de_producto < len(lista_productos):
            producto_elegido = lista_productos(numero_de_producto)
            cantidad_vender = int(input())
        
        if cantidad_vender <= producto_elegido.cantidad:
            producto_elegido.cantidad = producto_elegido.cantidad - cantidad_vender
            print("Vendido")
            print("Cantidad restante: ", producto_elegido.cantidad)
            
    elif opcion == 0:
        print("Fin del proceso")
        break
    else: 
        print("Error, intente de nuevo")
