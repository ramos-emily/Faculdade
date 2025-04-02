import tkinter as tk #tinker é uma bibilhoteca que vai dar vida a minha nota fiscal
from tkinter import messagebox #messagebox é a janela de aviso que eu coloquei 
import subprocess #conjunto do bloco do notas, so dara continuidade quando o bloco de notas for fechado

class Mercadinho:
    opcoes = {
        "arroz": {"preco": 4.00, "estoque": 10},
        "feijao": {"preco": 7.99, "estoque": 10},
        "morango": {"preco": 8.98, "estoque": 10},
        "batata": {"preco": 7.89, "estoque": 10},
        "toddynho": {"preco": 3.49, "estoque": 10},
        "doritos": {"preco": 9.99, "estoque": 10},
        "pao de forma": {"preco": 22.08, "estoque": 10},
        "yakult": {"preco": 13.99, "estoque": 10},
        "alface": {"preco": 7.45, "estoque": 10},
        "kit kat": {"preco": 4.00, "estoque": 10}
    } #Esse dicionário é usado para consultar o preço e a quantidade disponível de cada produto ao realizar uma compra.
    carrinho = []
    total = 0.0
    cpf = None  # None é um objeto especial que ultilizado na ausencia de um valor ou falta de informaçao.

    def __init__(self):
        self.root = tk.Tk() #base da interface da minha nota fiscal, tk é a janela onde contem os widgets
        self.root.withdraw()  # Oculta a janela principal

    def comprar(self): 
        while True: #cria um ciclo infinito ate a apariçao do break
            print("Opções de produtos:")
            for produto, info in self.opcoes.items(): #aqui e onde puxa (opcoes) que é a minha lista de compras
                print(f"{produto.capitalize()} - R${info['preco']:.2f} (Estoque: {info['estoque']})") #aqui ele formata como eu quero e exibe o nome do produto, seu preço e estoque disponivel.

            escolha = input("Digite o nome do produto que deseja comprar (ou 'sair' para encerrar a compra): ").strip().lower() #esse .strip().lower()Remove espaços em branco das extremidades e converte a entrada para minúsculas.
            if escolha == 'sair':
                break

            if escolha in self.opcoes:#aqui ele ve se o produto existe na minha lista de compra
                quantidade = int(input("Digite a quantidade desejada: "))

                # Verificar se há estoque suficiente
                if quantidade > self.opcoes[escolha]['estoque']:#confere se tem o produto no estoque
                    self.exibir_aviso(f"Estoque insuficiente para {escolha}. Disponível: {self.opcoes[escolha]['estoque']}")
                else:
                    preco = self.opcoes[escolha]['preco']#obtem o preço
                    novoItem = {
                        'item': escolha.capitalize(),
                        'quantidade': quantidade,
                        'preco': preco
                    }#dicionario que representa o item adicionado no carrinho.

                    self.carrinho.append(novoItem) #adiciona ao carrinho
                    self.opcoes[escolha]['estoque'] -= quantidade  # Atualizar o estoque
                    self.exibir_aviso(f"{quantidade} unidades de {escolha} adicionadas ao carrinho.")#exibe aviso
            else:
                print("Produto não encontrado. Tente novamente.")

        self.resumo_compra()
        self.pagar()

    def exibir_aviso(self, mensagem):
        # Usa uma nova janela para a notificação
        aviso = tk.Toplevel(self.root)#cria uma janela filha, onde vai aconetecr as interaçoes com o usuario
        aviso.title("Aviso")#aviso e a referncia da janela de aviso
        aviso.geometry("300x100")  # Tamanho da janela de aviso
        
        # Adiciona o texto de aviso na janela
        tk.Label(aviso, text=mensagem, padx=20, pady=20).pack()#.pack() e uma funçao do tinker que serve para gerenciar o layout dos widgets da minha nota fiscal.
        
        # Botão para fechar a janela de aviso
        tk.Button(aviso, text="OK", command=aviso.destroy).pack()
        
        # Força a janela de aviso a ficar no topo
        aviso.attributes("-topmost", True)
        aviso.wait_window()  # Aguarda o fechamento da janela de aviso

    def resumo_compra(self):
        print("\nResumo da compra")
        for produto in self.carrinho: #percorre os itens do meu carrinho.
            preco_total = produto['preco'] * produto['quantidade']
            print(f"{produto['quantidade']} unidades de {produto['item']} - R${preco_total:.2f}")
            self.total += preco_total #conta necessaria para exiber valor da minha compra

        print(f"Total da compra: R${self.total:.2f}")

    def pagar(self):
        pagamento = input("Insira o valor a pagar (ou 'cancelar' para cancelar a compra): ").strip().lower()
        if pagamento == "cancelar":
            print("Compra cancelada :(")
            return #se o usuario optar por compra cancelada, exibira a mensagem acima e encerrará a compra.

        try:
            valor_pago = float(pagamento)#Tenta converter o valor inserido pelo usuário para um número de ponto flutuante (float).

        except ValueError: #se o usuario tentar formas diferentes de pagamento, nao sera aceito
            print("Valor inválido. Tente novamente.")
            self.pagar()
            return

        troco = valor_pago - self.total #calcula o troco

        if troco < 0:
            print(f"Valor insuficiente. Faltam R${-troco:.2f}")
            self.pagar()
        else:
            if troco > 0:
                print(f"Troco: R${troco:.2f}")
            
            cpf_nota = input("CPF na nota? (sim/não): ").strip().lower()
            
            # Verificar se cpf_nota é uma das opções válidas
            if cpf_nota in {"sim", "s", "sim", "s", "SIM", "Sim", "ss", "SS"}:
                self.cpf = input("Digite o CPF: ")
                print(f"Nota fiscal: Total da compra - R${self.total:.2f} | CPF - {self.cpf} Obrigado pela compra, volte sempre! :)")
            else:
                print(f"Nota fiscal: Total da compra - R${self.total:.2f} Obrigado pela compra, volte sempre! :)")

            # Gerar a nota fiscal
            self.gerar_nota_fiscal()

    def gerar_nota_fiscal(self):
        nome_arquivo = 'nota_fiscal.txt' #nome do arquivo onde a nota fiscal será salva.

        # Conteúdo da nota fiscal
        conteudo = "==============================================\n"
        conteudo += "            MERCADINHO FAISQUINHA\n"
        conteudo += "                 NOTA FISCAL\n"
        conteudo += "==============================================\n"
        conteudo += f"{'ID':<5} {'Nome':<9} {'Preço':>9} {'Quantidade':>9}\n"
        conteudo += "-" * 40 + "\n" #Adiciona uma linha de separação de 40 caracteres.

        # Adicionar os dados dos produtos no carrinho
        for i, produto in enumerate(self.carrinho, start=1): #Itera sobre o carrinho de compras, fornecendo um índice i começando de 1.
            conteudo += (f"{i:<5} "
                         f"{produto['item']:<12} "
                         f"R${produto['preco']:>5.2f} "
                         f"{produto['quantidade']:>10}\n")

        # Rodapé onde adiciona o total da compra e o CPF (se fornecido) ao final da nota fiscal.

        conteudo += (
            "-" * 45 + "\n"
            f"Total da compra: R${self.total:.2f}\n"
        )
        if self.cpf:
            conteudo += f"CPF: {self.cpf}\n"
        conteudo += (
            "Obrigado pela compra, volte sempre :)\n"
            "==============================================\n"
        )

        # Salvar o conteúdo no arquivo de texto
        with open(nome_arquivo, 'w') as f: #'w' é uma funçao juntamente com o open(). Este modo abre o arquivo para escrita. Se o arquivo já existe, ele será truncado (ou seja, seu conteúdo anterior será apagado). Se o arquivo não existir, ele será criado.
            f.write(conteudo)

        # Abrir o Bloco de Notas
        subprocess.run(['notepad.exe', nome_arquivo])

# Cria uma instância da classe Mercadinho e inicia a compra
mercado = Mercadinho()#e criada no final para dar inicio a compra, tudo feito antes foi um preparo do ambiente para usar os metodos e atributos da classe
mercado.comprar()#contém a lógica de interação com o usuário, permitindo que o cliente faça uma compra é colocado no final tmb para garantir que todos os componentes e metodos necessarios ja estejam definidos e disponiveis.
