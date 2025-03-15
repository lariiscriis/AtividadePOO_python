class Produto:
    def __init__(self, nomeProduto, preco, quantidade):
        self.nomeProduto = nomeProduto
        self.preco = preco
        self.quantidade = quantidade

    def AtualizarQuantidade(self, quantidade_comprada):
       if self.quantidade >= quantidade_comprada:
            self.quantidade -= quantidade_comprada
            return True
       else:
            print("Estoque insuficiente!")
            return False
        
    def __str__(self):
        return f"{self.nomeProduto} - Estoque: {self.quantidade} - R${self.preco}"