from Cliente import Cliente
from Produto import Produto
from Venda import Venda


class SistemaVendas: 
    def __init__(self):
        self.Produto = Produto
        self.Cliente = Cliente
        self.Venda = Venda
    
    def cadastrarProduto(self):
        nomeProduto = input("Digite o nome do produto: ")
        quantidade = int(input("Digite a quantidade de estoque: "))
        preco = float(input("Digite o preço do produto: "))

        with open("produtos_estoque/produtos_estoque.txt", "a") as arquivo:
            arquivo.write(f"{nomeProduto}, {quantidade}, {preco}\n")
            arquivo.close()
            print("Produto Adicionado!")

    def listarProdutos(self):
        with open("produtos_estoque/produtos_estoque.txt", "r") as arquivo:
            print("\n---Lista de Produtos---")
            print(arquivo.read())

    def editarProduto(self):
            nome_antigo = input("Digite o nome do produto a ser editado: ")
            encontrado = False
            produtos_atualizados = []

            with open("produtos_estoque/produtos_estoque.txt", "r") as arquivo:
                produtos = arquivo.readlines()
                
            for linha in produtos:
                nome, quantidade, preco = linha.strip().split(",")
                if nome == nome_antigo:
                    print("\nProduto encontrado!")
                    novo_nome = input("\nDigite o novo nome do produto: ")
                    nova_quantidade = int(input("Digite a nova quantidade do produto: "))
                    novo_preco = float(input("Digite o novo preço do produto: "))
                    produtos_atualizados.append(f"{novo_nome},{nova_quantidade},{novo_preco}\n")
                    encontrado = True
                else:
                    produtos_atualizados.append(linha)

            if encontrado:
                with open("produtos_estoque/produtos_estoque.txt", "w") as arquivo:
                    arquivo.writelines(produtos_atualizados)
                print("Produto atualizado com sucesso!")
            else:
                print("Produto não encontrado!")

    def excluirProduto(self):
            nome_remover = input("Digite o nome do produto a ser excluído: ")
            produtos_atualizados = []
            encontrado = False

            with open("produtos_estoque/produtos_estoque.txt", "r") as arquivo:
                produtos = arquivo.readlines()

            for linha in produtos:
                linhas = linha.strip().split(",")
                if linhas[0] != nome_remover:
                    produtos_atualizados.append(linha)
                else:
                    encontrado = True

            if encontrado:
                with open("produtos_estoque/produtos_estoque.txt", "w") as arquivo:
                    arquivo.writelines(produtos_atualizados)
                print("Produto removido com sucesso!")
            else:
                print("Produto não encontrado!")


    def CadastrarCliente(self):
        nomeCliente = input("Digite o Nome do cliente: ")
        cpf = input("Digite o CPF do cliente: ").strip()

        with open("Clientes/Clientes.txt", "r") as arquivo:
            for linha in arquivo:
                dados = linha.strip().split(",")
                if dados[1].strip() == cpf:  
                    print("\nCPF já cadastrado!")
                    return
        with open("Clientes/Clientes.txt", "a") as arquivo:
            arquivo.write(f"{nomeCliente}, {cpf}\n")
            arquivo.close()
        
        print("Cliente cadastrado com sucesso!")

    def ListarCliente(self):
        with open("Clientes/Clientes.txt", "r") as arquivo:
            print("\n---Lista de Clientes---")
            print(arquivo.read())

    def excluirCliente(self):
            nomeCliente_remover = input("Digite o nome do cliente a ser excluído: ")
            clientes_atualizados = []
            encontrado = False

            with open("Clientes/Clientes.txt", "r") as arquivo:
                Clientes = arquivo.readlines()

            for linha in Clientes:
                linhas = linha.strip().split(",")
                if linhas[0] != nomeCliente_remover:
                    clientes_atualizados.append(linha)
                else:
                    encontrado = True

            if encontrado:
                with open("Clientes/Clientes.txt", "w") as arquivo:
                    arquivo.writelines(clientes_atualizados)
                print("Cliente removido com sucesso!")
            else:
                print("Cliente não encontrado!")

    def registrarVenda(self):
        nomeinput = input("Nome do Cliente: ")

        with open("Clientes/Clientes.txt", "r") as arquivo:
            Clientes = arquivo.readlines()
            for linha in Clientes:
                nomeCliente, cpf = linha.strip().split(",")
                if nomeinput == nomeCliente:
                    cliente = Cliente(nomeCliente, cpf) 
                    break
            else:
                print("Cliente Não encontrado!")
                return 

        nome_produtoInput = input("Nome do Produto: ")

        with open("produtos_estoque/produtos_estoque.txt", "r") as arquivo:
            produtos = arquivo.readlines()
            for linha in produtos:
                nomeProduto, quantidade, preco = linha.strip().split(",")
                if nome_produtoInput == nomeProduto:
                    produto = Produto(nomeProduto, int(quantidade), float(preco))  
                    break
            else:
                print("Produto Não encontrado!")
                return  

        quantidade_comprada = int(input("Quantidade: "))
        if produto.AtualizarQuantidade(quantidade_comprada):
            total = produto.preco * quantidade_comprada

            with open("produtos_estoque/produtos_estoque.txt", "w") as arquivo:
                for linha in produtos:
                    nomeProduto, quantidade, preco = linha.strip().split(",")
                    if nomeProduto == nome_produtoInput:
                        quantidade = str(int(quantidade) - quantidade_comprada)
                    arquivo.write(f"{nomeProduto}, {quantidade}, {preco}\n")

            with open("Vendas/vendas.txt", "a") as arquivo: 
                arquivo.write(f"{cliente.nomeCliente}, {cliente.cpf}, {produto.nomeProduto}, {quantidade_comprada}, R${total}\n")
            print("Venda Registrada!")


    def exibir_menu(self):
        while True:
            print("\n========= MENU =========")
            print("1 - Cadastrar Cliente")
            print("2 - Listar Clientes")
            print("3 - Excluir Cliente")
            print("4 - Cadastrar Produto")
            print("5 - Listar Produtos")
            print("6 - Editar Produto")
            print("7 - Excluir Produto")
            print("8 - Registrar Venda")
            print("9 - Listar Vendas")
            print("10 - Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.CadastrarCliente()
            elif opcao == "2":
                self.ListarCliente()
            elif opcao == "3":
                self.excluirCliente()
            elif opcao == "4":
                self.cadastrarProduto()
            elif opcao == "5":
                self.listarProdutos()
            elif opcao == "6":
                self.editarProduto()
            elif opcao == "7":
                self.excluirProduto()
            elif opcao == "8":
                self.registrarVenda()
            elif opcao == "9":
                self.listar_vendas()
            elif opcao == "10":
                break
            else:
                print("Opção inválida! Tente novamente.")

    def listar_vendas(self):
        with open("vendas/vendas.txt", "r") as arquivo:
            print(arquivo.read())

if __name__ == "__main__":
    sistema = SistemaVendas()
    sistema.exibir_menu()
