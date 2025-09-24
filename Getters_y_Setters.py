
class Usuario:
     def _init_(self, nombre, correo):
         self.__nombre = nombre
         self.__correo = correo

     def get_correo(self):
         return "El correo es " + self.__correo

     def get_nombre(self):
         return self.__nombre
    
     def set_nombre(self, nombre):
        if nombre != "Camilo" and nombre != "Samuel":
            return "No puedes cambiar el nombre"
        else:
            self.__nombre = nombre
            return "Nombre cambiando correctamente"

usuario = Usuario("Samuel", "sm@gmail.com")
print(usuario.get_nombre())
print(usuario.get_correo())
usuario.get_nombre = "Camilo"
print(usuario.get_nombre)

"""class Usuario:
    def _init_(self, nombre="sin nombre", correo="sin correo", *gustos):
        self.__nombre = nombre
        self.__correo = correo
        self.gustos = gustos

    def presentar(self, **datos):
        print("Hola, soy", self.__nombre)
        print("Mis gustos son", self.gustos)
        print("Datos adicionales: ", datos)
        print("Correo: ",self.__correo)

usuario = Usuario("Samuel", "Samuel@gmail.com", "leer", "nadar", "ir al cine")
usuario.presentar()"""