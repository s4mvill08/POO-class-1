class persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.cuentas = []
        
    def agregar_cuenta(self, cuenta):
        self.cuentas.append(cuenta)
        
class cuenta:
    def __init__(self, numero, oficina):
        self.numero = numero   
        self.oficina = oficina     
    
    def depositar(self, cantidad):
        self.saldo += cantidad

#Crear una instancia(objeto) de la clase persona
persona1 = persona("Juan", 30)
print("el nombre de la persona", persona1.nombre)
print(f"La edad de la persona es {persona1.edad}")

#Crear una instancia(objeto) de la clase cuenta
cuenta1 = cuenta("123456", "Oficina 1")
print("El número de cuenta es:", cuenta1.numero)
print(f"La oficina es {cuenta1.oficina}")

#Asociar la cuenta a la persona
persona1.agregar_cuenta(cuenta1)

cuenta2 = cuenta("234567", "Oficina 2")

persona1.agregar_cuenta(cuenta2)

persona1.cuentas[0].depositar(1000)
print(persona1.cuentas[0].saldo)
print(persona1.cuentas[1].saldo)

print(persona1.cuentas[1].numero)
