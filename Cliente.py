class Cliente:
    def __init__(self, nomeCliente, cpf):
        self.nomeCliente = nomeCliente
        self.cpf = cpf

    def __str__(self):
        return f"Cliente: {self.nomeCliente}, CPF: {self.__cpf}"