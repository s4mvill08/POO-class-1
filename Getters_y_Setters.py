class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    # Getter para el nombre
    @property
    def nombre(self):
        return self._nombre

    # Setter para el nombre
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    # Getter para la edad
    @property
    def edad(self):
        return self._edad

    # Setter para la edad
    @edad.setter
    def edad(self, nueva_edad):
        if nueva_edad > 0:
            self._edad = nueva_edad
        else:
            raise ValueError("La edad debe ser un número positivo.")

# Ejemplo de uso
persona = Persona("Juan", 25)
print(persona.nombre)  # Juan
persona.nombre = "Carlos"
print(persona.nombre)  # Carlos

print(persona.edad)  # 25
persona.edad = 30
print(persona.edad)  # 30