class Motor:
    def __init__(self):
        self.estado = "apagado"
    
    def encender(self):
        self.estado = "encendido"
    
    def apagar(self):
        self.estado = "apagado"

class Vehiculo:
    def __init__(self, placa, marca):
        self.placa = placa
        self.marca = marca
        self.motor = None
        self.servicio = "no esta en servicio"
    
    def instalar_motor(self):
        self.motor = Motor()
        print("Motor instalado")
    
    def encender(self):
        if self.motor == None:
            print("Sin motor")
            return
        self.motor.encender()
        print("Encendido")
    
    def poner_servicio(self):
        if self.motor == None or self.motor.estado == "apagado":
            print("Necesita motor encendido")
            return
        self.servicio = "si"
        print("En servicio")

class Flota:
    def __init__(self):
        self.vehiculos = []
    
    def agregar(self, vehiculo):
        self.vehiculos.append(vehiculo)
    
    def buscar(self, placa):
        for vehiculo in self.vehiculos:
            if vehiculo.placa == placa:
                return vehiculo
        return None
    
    def mostrar(self):
        for vehiculo in self.vehiculos:
            motor = "Sin motor" if vehiculo.motor == None else vehiculo.motor.estado
            print(f"{vehiculo.placa} - {vehiculo.marca} - Servicio:{vehiculo.servicio} - Motor:{motor}")

flota = Flota()

while True:
    print("1.Agregar vehiculo")
    print("2.Motor")
    print("3.Encender")
    print("4.Servicio")
    print("5.Ver")
    print("6.Salir")
    
    opcion = input("Opcion: ")
    
    if opcion == "1":
        placa = input("Placa: ")
        marca = input("Marca: ")
        flota.agregar(Vehiculo(placa, marca))
        print("Agregado")
    
    elif opcion == "2":
        placa = input("Placa: ")
        vehiculo = flota.buscar(placa)
        if vehiculo:
            vehiculo.instalar_motor()
        else:
            print("No existe")
    
    elif opcion == "3":
        placa = input("Placa: ")
        vehiculo = flota.buscar(placa)
        if vehiculo:
            vehiculo.encender()
        else:
            print("No existe")
    
    elif opcion == "4":
        placa = input("Placa: ")
        vehiculo = flota.buscar(placa)
        if vehiculo:
            vehiculo.poner_servicio()
        else:
            print("No existe")
    
    elif opcion == "5":
        flota.mostrar()
    
    elif opcion == "6":
        break
