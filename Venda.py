from Cliente import Cliente
from Produto import Produto

class Venda:
    def __init__(self, Cliente, Produto, quantidade_comprada):
        self.Cliente = Cliente 
        self.Produto = Produto  
        self.quantidade_comprada = quantidade_comprada
        self.total = self.Produto.preco * self.quantidade_comprada 

    def registrar_venda(self):
        if self.Produto.AtualizarQuantidade(self.quantidade_comprada):
            with open("produtos_estoque/produtos_estoque.txt", "a") as arquivo:
                arquivo.write(f"{Cliente.nomeCliente}, {Cliente.cpf}, {Produto.nomeProduto}, {self.quantidade_comprada}, R${self.total}\n")
            print(f"Venda registrada! Total: R${self.total:.2f}")
        else:
            print("Erro: Estoque insuficiente!")

    def listar_vendas():
            with open("produtos_estoque/produtos_estoque.txt", "r") as arquivo:
                vendas = arquivo.readlines()
                if not vendas:
                    print("Nenhuma venda registrada ainda.")
                else:
                    print("\n--- Histórico de Vendas ---")
                    for venda in vendas:
                        print(venda.strip())
        