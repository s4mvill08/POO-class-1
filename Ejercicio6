class Dispositivos:
    def __init__(self, nombre):
        self.nombre = nombre
        self.estado = False

    def encender(self):
        self.estado = True
        print(self.nombre, "Encendido")
        
    def apagar(self):
        self.estado = False
        print(self.nombre, "Apagado")

class Lugar_casa:
    def __init__(self, nombre):
        self.nombre = nombre
        self.__dispositivos = []

    def agregarDis(self, dispositivo):
        self.__dispositivos.append(dispositivo)
        print('dispositivo agregado')

    def mostrarDis(self):
        for dispositivo in self.dispositivos:
            print(dispositivo.nombre)

class Casa:
    def __init__(self, direccion):
        self.direccion = direccion
        self.__espacios = []

    def agregarES(self, nombre):
        self.__espacios.append(Lugar_casa(nombre))
        print("Espacio0 agregado")

    def buscar_espacio(self, nombre):
        for espacio in self.__espacios:
            if espacio.nombre == nombre:
                return espacio 
        return None


    def mostrarES(self):
        for espacio in self.__espacios:
            print(espacio.nombre)

mi_casa = Casa("Calle 122")
mi_casa.agregarES("cocina")
mi_casa.agregarES("Habitacion")
mi_casa.agregarES("bano")
television = Dispositivos("Television")
mi_casa.buscar_espacio("habitacion").agregarDis(television)
mi_casa.buscar_espacio("habitacion").mostrarDis()
