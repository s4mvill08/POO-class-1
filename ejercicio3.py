class Banco:
    def __init__(self, cuenta, titular, saldo):
        self.cuenta = cuenta
        self.titular = titular
        self.saldo = saldo
        
    def mostrar_datos(self):
        print("Cuenta: ", self.cuenta)
        print("Titular: ", self.titular)
        print("Saldo: ", self.saldo)

print("Control de cuentas bancarias")
lista_cuenta = []

while True:
    print(" 1. Ingresar cuenta")
    print(" 2. Depositar")
    print(" 3. Retirar")
    print(" 4. Ver cuenta")
    print(" 0. Salir")
    opcion = int(input("Opción: "))
    
    if opcion == 1:
        cuenta = input("Número de cuenta: ")
        titular = input("Titular: ")
        saldo = float(input("Saldo inicial: "))
        nueva_cuenta = Banco(cuenta, titular, saldo)
        lista_cuenta.append(nueva_cuenta)
        print("Cuenta creada")
        
    elif opcion == 2:
        num = input("Número de cuenta: ")
        for cuenta in lista_cuenta:
            if cuenta.cuenta == num:
                cantidad = float(input("Cantidad a depositar: "))
                cuenta.saldo += cantidad
                print("Depósito realizado. Nuevo saldo:", cuenta.saldo)
                break
        else:
            print("Cuenta no encontrada")
            
    elif opcion == 3:
        num = input("Número de cuenta: ")
        for cuenta in lista_cuenta:
            if cuenta.cuenta == num:
                cantidad = float(input("Cantidad a retirar: "))
                if cantidad <= cuenta.saldo:
                    cuenta.saldo -= cantidad
                    print("Retiro realizado. Nuevo saldo:", cuenta.saldo)
                else:
                    print("Fondos insuficientes")
                break
        else:
            print("Cuenta no encontrada")
            
    elif opcion == 4:
        num = input("Número de cuenta: ")
        for cuenta in lista_cuenta:
            if cuenta.cuenta == num:
                cuenta.mostrar_datos()
                break
        else:
            print("Cuenta no encontrada")
            
    elif opcion == 0:
        break