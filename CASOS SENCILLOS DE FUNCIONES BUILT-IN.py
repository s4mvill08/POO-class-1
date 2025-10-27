# CASOS SENCILLOS DE FUNCIONES BUILT-IN DE PYTHON

print("=== FUNCIONES BUILT-IN CON CASOS SENCILLOS ===\n")

# abs() - Obtener valor absoluto de temperatura
temperatura = -15
temperatura_absoluta = abs(temperatura)
print(f"La temperatura es {temperatura}°C, su valor absoluto es {temperatura_absoluta}°C")

# all() - Verificar si todos los estudiantes pasaron el examen
notas_pasaron = [True, True, True, True]
todos_pasaron = all(notas_pasaron)
print(f"¿Todos los estudiantes pasaron? {todos_pasaron}")

# any() - Verificar si algún estudiante pasó el examen
algunas_notas = [False, False, True, False]
alguien_paso = any(algunas_notas)
print(f"¿Alguien pasó el examen? {alguien_paso}")

# ascii() - Convertir texto con caracteres especiales
nombre = "José"
nombre_ascii = ascii(nombre)
print(f"El nombre '{nombre}' en ASCII es: {nombre_ascii}")

# bin() - Convertir número a binario
numero = 10
numero_binario = bin(numero)
print(f"El número {numero} en binario es: {numero_binario}")

# bool() - Verificar si una lista tiene elementos
lista_vacia = []
lista_con_elementos = [1, 2, 3]
tiene_elementos1 = bool(lista_vacia)
tiene_elementos2 = bool(lista_con_elementos)
print(f"¿Lista vacía tiene elementos? {tiene_elementos1}")
print(f"¿Lista con datos tiene elementos? {tiene_elementos2}")

# breakpoint() - Pausar programa para debug (comentado)
# print("Antes del breakpoint")
# breakpoint()  # Aquí se pausaría el programa
# print("Después del breakpoint")

# bytearray() - Crear array de bytes modificable
texto = "Hola"
bytes_modificables = bytearray(texto, 'utf-8')
print(f"'{texto}' como bytearray: {bytes_modificables}")

# bytes() - Crear bytes inmutables
bytes_inmutables = bytes(texto, 'utf-8')
print(f"'{texto}' como bytes: {bytes_inmutables}")

# callable() - Verificar si algo se puede llamar como función
def mi_funcion():
    return "¡Hola!"

variable = 42
es_funcion = callable(mi_funcion)
es_numero = callable(variable)
print(f"¿mi_funcion es callable? {es_funcion}")
print(f"¿42 es callable? {es_numero}")

# chr() - Obtener carácter de código ASCII
codigo = 65
caracter = chr(codigo)
print(f"El código ASCII {codigo} corresponde al carácter: '{caracter}'")

# classmethod() - Se usa como decorador en clases
class Contador:
    total = 0
    
    @classmethod
    def obtener_total(cls):
        return cls.total

total_actual = Contador.obtener_total()
print(f"Total del contador: {total_actual}")

# compile() - Compilar código para ejecutar después
# Crear un namespace personalizado
print("=== Solución 2: Diccionario como namespace ===")
codigo = "resultado = 5 + 3"
codigo_compilado = compile(codigo, '<string>', 'exec')

mi_namespace = {}
exec(codigo_compilado, mi_namespace)
print(f"Resultado del código compilado: {mi_namespace['resultado']}")

print("\n" + "="*50 + "\n")

# complex() - Crear número complejo
numero_complejo = complex(3, 4)
print(f"Número complejo: {numero_complejo}")

# delattr() - Eliminar atributo de objeto
class Persona:
    def __init__(self):
        self.nombre = "Juan"

persona = Persona()
print(f"Antes: persona.nombre = {persona.nombre}")
delattr(persona, 'nombre')
tiene_nombre = hasattr(persona, 'nombre')
print(f"Después de delattr: ¿tiene nombre? {tiene_nombre}")

# dict() - Crear diccionario
pares = [('a', 1), ('b', 2), ('c', 3)]
diccionario = dict(pares)
print(f"Diccionario creado: {diccionario}")

# dir() - Ver métodos y atributos de un objeto
texto_ejemplo = "hola"
metodos = dir(texto_ejemplo)
print(f"Primeros 5 métodos de string: {metodos[:5]}")

# divmod() - Obtener división y resto
dividendo = 17
divisor = 5
cociente, resto = divmod(dividendo, divisor)
print(f"{dividendo} ÷ {divisor} = {cociente} con resto {resto}")

# enumerate() - Numerar elementos de una lista
frutas = ['manzana', 'banana', 'naranja']
print("Lista numerada:")
for indice, fruta in enumerate(frutas):
    print(f"  {indice}: {fruta}")

# eval() - Evaluar expresión matemática
expresion = "10 + 5 * 2"
resultado_eval = eval(expresion)
print(f"Resultado de '{expresion}' = {resultado_eval}")

# exec() - Ejecutar código Python
codigo_python = "x = 10; y = x * 2; print(f'x={x}, y={y}')"
exec(codigo_python)

# filter() - Filtrar números pares
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(f"Números pares de {numeros}: {pares}")

# float() - Convertir texto a decimal
precio_texto = "19.99"
precio_numero = float(precio_texto)
print(f"Precio como texto: '{precio_texto}', como número: {precio_numero}")

# format() - Formatear número con decimales
precio = 123.456
precio_formateado = format(precio, '.2f')
print(f"Precio formateado: ${precio_formateado}")

# frozenset() - Crear conjunto inmutable
numeros_repetidos = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
conjunto_unico = frozenset(numeros_repetidos)
print(f"Números únicos: {conjunto_unico}")

# getattr() - Obtener atributo de objeto
cadena = "python"
metodo_upper = getattr(cadena, 'upper')
resultado_upper = metodo_upper()
print(f"'{cadena}' en mayúsculas: '{resultado_upper}'")

# globals() - Ver variables globales (solo algunas)
variables_globales = globals()
print(f"Cantidad de variables globales: {len(variables_globales)}")

# hasattr() - Verificar si objeto tiene atributo
lista_ejemplo = [1, 2, 3]
tiene_append = hasattr(lista_ejemplo, 'append')
tiene_volar = hasattr(lista_ejemplo, 'volar')
print(f"¿Lista tiene método 'append'? {tiene_append}")
print(f"¿Lista tiene método 'volar'? {tiene_volar}")

# hash() - Obtener código hash de objeto inmutable
palabra = "python"
codigo_hash = hash(palabra)
print(f"Hash de '{palabra}': {codigo_hash}")

# help() - Obtener ayuda (comentado para no interrumpir)
# help(len)  # Mostraría la documentación de len()

# hex() - Convertir a hexadecimal
numero_decimal = 255
numero_hex = hex(numero_decimal)
print(f"El número {numero_decimal} en hexadecimal es: {numero_hex}")

# id() - Obtener identificador único del objeto
lista1 = [1, 2, 3]
lista2 = [1, 2, 3]
lista3 = lista1
id1 = id(lista1)
id2 = id(lista2)
id3 = id(lista3)
print(f"ID de lista1: {id1}")
print(f"ID de lista2: {id2} (diferente objeto)")
print(f"ID de lista3: {id3} (mismo objeto que lista1)")

# input() - Obtener entrada del usuario (comentado)
# nombre = input("¿Cuál es tu nombre? ")
# print(f"Hola, {nombre}!")

# int() - Convertir texto a número entero
edad_texto = "25"
edad_numero = int(edad_texto)
print(f"Edad como texto: '{edad_texto}', como número: {edad_numero}")

# isinstance() - Verificar tipo de objeto
valor = 42
es_entero = isinstance(valor, int)
es_texto = isinstance(valor, str)
print(f"¿{valor} es entero? {es_entero}")
print(f"¿{valor} es texto? {es_texto}")

# issubclass() - Verificar si es subclase
class Animal:
    pass

class Perro(Animal):
    pass

es_subclase = issubclass(Perro, Animal)
print(f"¿Perro es subclase de Animal? {es_subclase}")

# iter() - Crear iterador
colores = ['rojo', 'verde', 'azul']
iterador = iter(colores)
primer_color = next(iterador)
segundo_color = next(iterador)
print(f"Primer color: {primer_color}")
print(f"Segundo color: {segundo_color}")

# len() - Obtener longitud
mi_nombre = "Carlos"
longitud_nombre = len(mi_nombre)
print(f"El nombre '{mi_nombre}' tiene {longitud_nombre} letras")

# list() - Convertir a lista
palabra = "casa"
letras = list(palabra)
print(f"La palabra '{palabra}' como lista: {letras}")

# locals() - Ver variables locales
def ejemplo_locals():
    variable_local = "soy local"
    variables = locals()
    return len(variables)

cantidad_vars = ejemplo_locals()
print(f"Cantidad de variables locales en la función: {cantidad_vars}")

# map() - Aplicar función a cada elemento
precios = [10, 20, 30, 40]
precios_con_iva = list(map(lambda x: x * 1.21, precios))
print(f"Precios originales: {precios}")
print(f"Precios con IVA (21%): {precios_con_iva}")

# max() - Encontrar valor máximo
temperaturas = [18, 25, 30, 22, 28]
temp_maxima = max(temperaturas)
print(f"Temperaturas: {temperaturas}")
print(f"Temperatura máxima: {temp_maxima}°C")

# memoryview() - Vista de memoria de bytes
datos = b"Hola Mundo"
vista = memoryview(datos)
primer_byte = vista[0]
print(f"Primer byte de '{datos.decode()}': {primer_byte}")

# min() - Encontrar valor mínimo
calificaciones = [85, 92, 78, 96, 88]
nota_minima = min(calificaciones)
print(f"Calificaciones: {calificaciones}")
print(f"Nota más baja: {nota_minima}")

# next() - Obtener siguiente elemento del iterador
numeros_iter = iter([10, 20, 30])
siguiente = next(numeros_iter)
print(f"Siguiente número del iterador: {siguiente}")

# object() - Crear objeto base
objeto_base = object()
tipo_objeto = type(objeto_base)
print(f"Tipo de object(): {tipo_objeto}")

# oct() - Convertir a octal
numero_oct = 64
octal = oct(numero_oct)
print(f"El número {numero_oct} en octal es: {octal}")

# open() - Abrir archivo (ejemplo conceptual)
# archivo = open('mi_archivo.txt', 'w')
# archivo.write('Hola mundo')
# archivo.close()
print("open() se usa para abrir archivos (ejemplo comentado)")

# ord() - Obtener código ASCII de carácter
letra = 'A'
codigo_ascii = ord(letra)
print(f"El carácter '{letra}' tiene código ASCII: {codigo_ascii}")

# pow() - Calcular potencia
base = 2
exponente = 8
potencia = pow(base, exponente)
print(f"{base} elevado a {exponente} = {potencia}")

# print() - Mostrar información
mensaje = "¡Python es genial!"
print(f"Mensaje: {mensaje}")

# property() - Se usa como decorador para propiedades
class Circulo:
    def __init__(self, radio):
        self._radio = radio
    
    @property
    def area(self):
        return 3.14159 * self._radio ** 2

circulo = Circulo(5)
area_circulo = circulo.area
print(f"Área de círculo con radio 5: {area_circulo:.2f}")

# range() - Crear secuencia de números
numeros_del_1_al_5 = list(range(1, 6))
print(f"Números del 1 al 5: {numeros_del_1_al_5}")

# repr() - Representación de objeto
mi_lista = [1, 2, 3]
representacion = repr(mi_lista)
print(f"Representación de {mi_lista}: {representacion}")

# reversed() - Invertir secuencia
palabra_original = "Python"
palabra_invertida = ''.join(reversed(palabra_original))
print(f"'{palabra_original}' invertida es: '{palabra_invertida}'")

# round() - Redondear número
precio_exacto = 15.6789
precio_redondeado = round(precio_exacto, 2)
print(f"Precio exacto: ${precio_exacto}, redondeado: ${precio_redondeado}")

# set() - Crear conjunto (elimina duplicados)
numeros_con_repetidos = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
numeros_unicos = set(numeros_con_repetidos)
print(f"Números con repetidos: {numeros_con_repetidos}")
print(f"Números únicos: {numeros_unicos}")

# setattr() - Establecer atributo en objeto
class Producto:
    pass

producto = Producto()
setattr(producto, 'nombre', 'Laptop')
setattr(producto, 'precio', 999.99)
print(f"Producto: {producto.nombre}, Precio: ${producto.precio}")

# slice() - Crear rebanada
texto_largo = "Python es increíble"
trozo = slice(0, 6)
resultado_slice = texto_largo[trozo]
print(f"Texto completo: '{texto_largo}'")
print(f"Primeros 6 caracteres: '{resultado_slice}'")

# sorted() - Ordenar elementos
estudiantes = ['Ana', 'Carlos', 'Beatriz', 'David']
estudiantes_ordenados = sorted(estudiantes)
print(f"Estudiantes desordenados: {estudiantes}")
print(f"Estudiantes ordenados: {estudiantes_ordenados}")

# staticmethod() - Método estático en clase
class Matematicas:
    @staticmethod
    def sumar(a, b):
        return a + b

resultado_suma = Matematicas.sumar(5, 3)
print(f"Suma usando método estático: 5 + 3 = {resultado_suma}")

# str() - Convertir a texto
numero_entero = 42
numero_como_texto = str(numero_entero)
print(f"Número {numero_entero} como texto: '{numero_como_texto}'")

# sum() - Sumar elementos
gastos_mensuales = [800, 200, 150, 300, 100]
total_gastos = sum(gastos_mensuales)
print(f"Gastos mensuales: {gastos_mensuales}")
print(f"Total de gastos: ${total_gastos}")

# super() - Acceder a clase padre
class Vehiculo:
    def __init__(self, marca):
        self.marca = marca

class Auto(Vehiculo):
    def __init__(self, marca, modelo):
        super().__init__(marca)  # Llama al __init__ de Vehiculo
        self.modelo = modelo

mi_auto = Auto("Toyota", "Corolla")
print(f"Mi auto: {mi_auto.marca} {mi_auto.modelo}")

# tuple() - Convertir a tupla
coordenadas_lista = [10, 20]
coordenadas_tupla = tuple(coordenadas_lista)
print(f"Lista: {coordenadas_lista}, Tupla: {coordenadas_tupla}")

# type() - Obtener tipo de objeto
elementos = [42, "hola", [1, 2, 3], True]
for elemento in elementos:
    tipo = type(elemento)
    print(f"Tipo de {elemento}: {tipo}")

# vars() - Variables de objeto
class Estudiante:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

estudiante = Estudiante("María", 20)
atributos = vars(estudiante)
print(f"Atributos del estudiante: {atributos}")

# zip() - Combinar listas
nombres = ['Juan', 'Ana', 'Luis']
edades = [25, 30, 28]
ciudades = ['Madrid', 'Barcelona', 'Valencia']

print("Información combinada:")
for nombre, edad, ciudad in zip(nombres, edades, ciudades):
    print(f"  {nombre}, {edad} años, vive en {ciudad}")

print("\n=== ¡TODOS LOS EJEMPLOS COMPLETADOS! ===")
print("Cada función built-in con un caso práctico y sencillo de usar.")