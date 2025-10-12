import random
class cuentas:
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
        cuenta = random.randint(100, 999)
        cuenta_nueva = 0
        for cuenta in lista_cuenta:
            for a in cuenta:
                if cuenta == cuenta:
                    cuenta_nueva != cuenta
                    print("Nueva cuenta")
                    
        print("La cuenta creada es: ", cuenta)
        titular = input("Titular: ")
        saldo = 0
        print("El saldo inicial es 0 ")
        nueva_cuenta = cuentas(cuenta, titular, saldo)
        lista_cuenta.append(nueva_cuenta)
        print("Cuenta creada")
        
    elif opcion == 2:
        for cuenta in lista_cuenta:
            cantidad = float(input("Cantidad a depositar: "))
            cuenta.saldo += cantidad
            print("Depósito realizado")
            break
        else:
            print("Cuenta no encontrada")
            
    elif opcion == 3:
        for cuenta in lista_cuenta:
            cantidad = float(input("Cantidad a retirar: "))
            if cantidad <= cuenta.saldo:
                cuenta.saldo -= cantidad
                print("Retiro realizado")
            else:
                print("Fondos insuficientes")
            break
        else:
            print("Cuenta no encontrada")
            
    elif opcion == 4:
        for cuenta in lista_cuenta:
            cuenta.mostrar_datos()
            break
        else:
            print("Cuenta no encontrada")
            
    elif opcion == 0:
        break
