class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.__titular = titular
        self.__saldo = saldo_inicial
    
    # Getters
    def get_titular(self):
        return self.__titular
    
    def get_saldo(self):
        return self.__saldo
    
    # Métodos protegidos
    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto
            print(f"Depósito exitoso. Nuevo saldo: ${self.__saldo}")
        else:
            print("Monto inválido")
    
    def retirar(self, monto):
        if 0 < monto <= self.__saldo:
            self.__saldo -= monto
            print(f"Retiro exitoso. Nuevo saldo: ${self.__saldo}")
        else:
            print("Fondos insuficientes o monto inválido")
    
    def transferir(self, otra_cuenta, monto):
        if monto <= self.__saldo:
            self.__saldo -= monto
            otra_cuenta.depositar(monto)
            print(f"Transferencia a {otra_cuenta.get_titular()} realizada")
        else:
            print("Fondos insuficientes")

# Uso
cuenta1 = CuentaBancaria("Juan Pérez", 1000)
cuenta2 = CuentaBancaria("María Gómez", 500)

print(f"Saldo inicial de {cuenta1.get_titular()}: ${cuenta1.get_saldo()}")
cuenta1.depositar(300)
cuenta1.retirar(200)
cuenta1.transferir(cuenta2, 150)

print(f"\nSaldo final de {cuenta2.get_titular()}: ${cuenta2.get_saldo()}")