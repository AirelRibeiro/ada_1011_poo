class Cliente:
    dados_clientes = []

    @classmethod
    def adiciona_cliente(cls, cliente):
        cls.dados_clientes.append(cliente)

    def __init__(self, nome, telefone, agencia, conta):
        self.__nome = nome
        self.__telefone = telefone
        self.__agencia = agencia
        self.__conta = conta
        self.adiciona_cliente(self)

    def __repr__(self) -> str:
        return f"{self.__nome} - Tel.: {self.__telefone} -Ag.: {self.__agencia} - CC: {self.__conta}"

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    @classmethod
    def busca_cliente(cls, nome):
        [cliente] = [
            clt for clt in cls.dados_clientes if clt.get_nome() == nome
        ]

        if cliente is None:
            return "Cliente não localizado."
        else:
            return cliente


cliente1 = Cliente("João da Silva", "81995925479", 123, 456)
cliente2 = Cliente("Antônia Nunes", "81995925479", 231, 436)

print(Cliente.dados_clientes)
print(Cliente.busca_cliente(cliente1.get_nome()))
