class Departamento:
    def __init__(self):
        self.empleados = []
    
    def mostrar_datos(self, empleados):
        for empleado in empleados:
            print(f"nombre: {empleado.nombre}, id: {empleado.id}, salario: {empleado.salarioP}")
            
    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)
        
    def eliminar_empleado(self, empleado):
        self.empleados.remove(empleado)
        
    def calcular_salario_departamento(self, empleados):
        total = 0
        for empleado in empleados:
            total += empleado.salarioP
            return total
    
class Empleado:
    def __init__(self, nombre, id, salarioP):
        self.nombre = nombre
        self.id = id
        self.salarioP = salarioP
        
class Desarrollador(Empleado):
    def __init__(self, nombre, id, salarioP):
        super().__init__(nombre, id, salarioP)
    
class Gerente(Empleado):
    def __init__(self, nombre, id, salarioP):
        super().__init__(nombre, id, salarioP)