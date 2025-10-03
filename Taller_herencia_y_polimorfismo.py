class Persona:
    def __init__(self, nombre, correo):
        self.nombre = nombre
        self.correo = correo
    
    def presentarse(self):
        return f"{self.nombre} - {self.correo}"

class Empleado(Persona):
    def __init__(self, nombre, correo, salario):
        super().__init__(nombre, correo)
        self.salario = salario
        self.tareas = 0
    
    def calcular_bono(self):
        return 0

class Desarrollador(Empleado):
    def __init__(self, nombre, correo, salario, lenguaje):
        super().__init__(nombre, correo, salario)
        self.lenguaje = lenguaje
    
    def calcular_bono(self):
        bono = self.salario * 0.10
        if self.tareas > 5:
            bono += self.salario * 0.01
        return bono

class Analista(Empleado):
    def __init__(self, nombre, correo, salario, seniority):
        super().__init__(nombre, correo, salario)
        self.seniority = seniority
    
    def calcular_bono(self):
        bono = self.salario * 0.08
        if self.seniority == "senior":
            bono += self.salario * 0.03
        return bono

class Gerente(Empleado):
    def __init__(self, nombre, correo, salario):
        super().__init__(nombre, correo, salario)
        self.equipo = []
    
    def agregar_empleado(self, empleado):
        if empleado == self:
            print("El gerente no puede agregarse a sí mismo")
            return False
        if empleado in self.equipo:
            print("El empleado ya está en el equipo")
            return False
        self.equipo.append(empleado)
        return True
    
    def calcular_bono(self):
        return self.salario * 0.15 + (self.salario * 0.02 * len(self.equipo))

class Tarea:
    id_contador = 1
    def __init__(self, descripcion, horas):
        self.id = Tarea.id_contador
        Tarea.id_contador += 1
        self.descripcion = descripcion
        self.horas = horas
        self.asignado = None

class Proyecto:
    def __init__(self, nombre, presupuesto):
        self.nombre = nombre
        self.presupuesto = presupuesto
        self.tareas = []
    
    def agregar_tarea(self, descripcion, horas):
        t = Tarea(descripcion, horas)
        self.tareas.append(t)
        return t.id
    
    def asignar(self, tarea_id, empleado):
        for t in self.tareas:
            if t.id == tarea_id:
                t.asignado = empleado
                empleado.tareas += 1

class Empresa:
    def __init__(self, nombre):
        self.nombre = nombre
        self.empleados = []
        self.proyectos = []

empresa = Empresa("Tecnosoft")

while True:
    print("---Bienvenido, escoge una opcion---")
    print("1. Desarollador")
    print("2. Analista")
    print("3. Gerente")
    print("4. Proyecto")
    print("5. Tarea")
    print("6. Asignar")
    print("7. Equipo")
    print("8. Ver")
    print("9. Bonos")
    print("0. Salir")
    opcion = input("Seleccione una opcion: ")
    
    if opcion == "1":
        nombre = input("Nombre: ")
        correo = input("Correo: ")
        salario = float(input("Salario: "))
        lenguaje = input("Lenguaje: ")
        des = Desarrollador(nombre, correo, salario, lenguaje)
        empresa.empleados.append(des)
    
    elif opcion == "2":
        nombre = input("Nombre: ")
        correo = input("Correo: ")
        salario = float(input("Salario: "))
        seniority = input("Seniority: ")
        analista = Analista(nombre, correo, salario, seniority)
        empresa.empleados.append(analista)
    
    elif opcion == "3":
        nombre = input("Nombre: ")
        correo = input("Correo: ")
        salario = float(input("Salario: "))
        gerente = Gerente(nombre, correo, salario)
        empresa.empleados.append(gerente)
    
    elif opcion == "4":
        nombre = input("Nombre: ")
        presupuesto = float(input("Presupuesto: "))
        proyecto = Proyecto(nombre, presupuesto)
        empresa.proyectos.append(proyecto)
    
    elif opcion == "5":
        print("Proyectos:")
        for p in empresa.proyectos:
            print(f"{empresa.proyectos.index(p)}. {p.nombre}")
        id_P = int(input("Proyecto: "))
        descripcion = input("Descripcion: ")
        h = int(input("Horas: "))
        if h < 0:
            print("Horas no pueden ser negativas")
        else:
            empresa.proyectos[id_P].agregar_tarea(descripcion, h)
    
    elif opcion == "6":
        print("Proyectos:")
        for p in empresa.proyectos:
            print(f"{empresa.proyectos.index(p)}. {p.nombre}")
        i_p = int(input("Proyecto: "))
        print("Tareas:")
        for t in empresa.proyectos[i_p].tareas:
            print(f"{t.id}. {t.descripcion}")
        t_id = int(input("Tarea: "))
        print("Empleados:")
        for e in empresa.empleados:
            print(f"{empresa.empleados.index(e)}. {e.nombre}")
        i_e = int(input("Empleado: "))
        empresa.proyectos[i_p].asignar(t_id, empresa.empleados[i_e])
        
    elif opcion == "7":
        gerentes = [e for e in empresa.empleados if isinstance(e, Gerente)]
        print("Gerentes:")
        for g in gerentes:
            print(f"{gerentes.index(g)}. {g.nombre}")
        i_g = int(input("Gerente: "))
        print("Empleados:")
        for e in empresa.empleados:
            print(f"{empresa.empleados.index(e)}. {e.nombre}")
        ie = int(input("Empleado: "))
        gerentes[i_g].agregar_empleado(empresa.empleados[ie])
    
    elif opcion == "8":
        print("Empleados:")
        for e in empresa.empleados: print(f"  {e.nombre} - {e.__class__.__name__}")
        print("Proyectos:")
        for p in empresa.proyectos:
            print(f"  {p.nombre}:")
            for t in p.tareas: 
                print(f"    {t.descripcion} - {t.asignado.nombre if t.asignado else 'Sin asignar'}")
    
    elif opcion == "9":
        for e in empresa.empleados: print(f"{e.nombre}: ${e.calcular_bono():,.2f}")
    
    elif opcion == "0":
        print("Saliendo")
        break