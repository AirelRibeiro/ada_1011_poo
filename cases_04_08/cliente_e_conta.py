import random


class NumeroContaGenerator:
    def __init__(self):
        self.contas_utilizadas = set()

    def gerar_numero_conta(self):
        while True:
            numero_conta = str(random.randint(10000000, 99999999))
            if numero_conta not in self.contas_utilizadas:
                self.contas_utilizadas.add(numero_conta)
                return numero_conta


class Cliente:
    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf
        self.__conta = None

    def vincular_conta(self, conta):
        self.__conta = conta

    def __str__(self):
        return f"Cliente: {self.__nome}\nCPF: {self.__cpf}"


class ContaBancaria:
    numero_conta_generator = NumeroContaGenerator()

    def __init__(self, cliente=None, saldo=0):
        self.__numero = (
            ContaBancaria.numero_conta_generator.gerar_numero_conta()
        )
        self.__saldo = saldo
        self.__cliente = cliente

    def vincular_cliente(self, cliente):
        if self.__cliente is None:
            self.__cliente = cliente
        else:
            raise Exception(
                "Essa conta já pertence possui um  cliente registrado!"
            )

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        if valor <= self.__saldo:
            self.__saldo -= valor
            return True
        else:
            return False

    def __str__(self):
        return f"\nConta: {self.__numero}\nSaldo: {self.__saldo}"


cliente1 = Cliente("João da Silva", "123.456.789-10")
cliente2 = Cliente("Antônia Nunes", "321.654.987-01")
conta1 = ContaBancaria(cliente1)
cliente1.vincular_conta(conta1)
# conta1.vincular_cliente(cliente2)
conta1.depositar(1000)
conta1.sacar(500)
print(cliente1)
print(conta1)
