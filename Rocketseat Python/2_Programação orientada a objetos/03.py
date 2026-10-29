
#Encapsulamento
class ContaBancaria:
    def __init__(self, saldo):
        self.__saldo = saldo #Atrubuto privado

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor

    def sacar(self, valor):
        if valor > 0 and valor <= self.__saldo:
            self.__saldo -= valor

    def consultar_saldo(self):
        return self.__saldo

conta1 = ContaBancaria(1000)
print(f"Saldo da conta: {conta1.consultar_saldo()}")
conta1.sacar(100)
conta1.depositar(400)

