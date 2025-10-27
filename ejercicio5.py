class Persona:
    def __init__(self, cedula, nombre, ti):
        self.nombre = nombre
        self.cedula = cedula
        self.ti = ti

    def obtener_documento(self):
        if self.cedula is not None:
            return self.cedula
        else:
            return self.ti 

persona1 = Persona("Juan", 111, None)
persona2 = Persona("Maria", 2222, None)
persona3 = Persona("Isaac", None, 3333)
