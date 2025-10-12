class Registro:
    def __init__(self, tipo, cantidad, valor_unitario):
        self.tipo = tipo
        self.cantidad = cantidad
        self.valor_unitario = valor_unitario


class Factura:
    def __init__(self, codigo):
        self.codigo = codigo
        self.registros = []
        self.total = 0
        
    def agregar_registro(self, tipo, cantidad, valor_unitario):
        nuevo_registro = Registro(self, tipo, cantidad, valor_unitario)
        self.registros.append(nuevo_registro)
        self.total = self.total + (cantidad * valor_unitario)
        
        
mi_factura = Factura(12345)
mi_factura.agregar_registro("Gaseosa", 5, 2500)
mi_factura.agregar_registro("Arepa", 3, 2000)

print("Mi factura es: ", mi_factura.total)
