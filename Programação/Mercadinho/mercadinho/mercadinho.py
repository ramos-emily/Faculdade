tabela = {"Alface": {"preco": 4.00, "estoque": 10},
          "Batata": {"preco": 4.55, "estoque": 10},
          "Tomate": {"preco": 9.80, "estoque": 10},
          "Feijão": {"preco": 7.30, "estoque": 10}
}

carrinho = []

while True:
    print("==============================================\n") 
    print("            MERCADINHO EMILY\n             ")
    print("    DIGITE 'sair' PARA ENCERRAR A COMPRA\n ")
    print("==============================================\n")
    print("Opções de produtos:\n")
    for produto, info in tabela.items():
        print(f"{produto.capitalize()} - R${info['preco']:.2f} (Estoque: {info['estoque']})")
    print("==============================================\n")


    produto = input("Qual o produto? ").capitalize()
   
    if produto == "Sair":
        print("Bye!")
        break

    if produto in tabela:
        quantidade = int(input("Quantidade: "))

        if quantidade > tabela[produto]['estoque']:
            print(f"\n\ncabou {produto}, disponivel: {tabela[produto]['estoque']}")
        else:
            preco = tabela[produto]['preco']
            novoItem = {
                'item': produto.capitalize(),
                'quantidade': quantidade,
                'preco': preco
            }

        carrinho.append(novoItem)
        tabela[produto]['estoque'] -= quantidade
        print(f"\n\n{quantidade} unidades de {produto} adicionados ao carrinho")
    
    else: 
        print("acho que voce escreveu errado :( nao tem esse produto!")

total = 0

for i in carrinho:
    valor_total = i['preco'] * i['quantidade']
    total += valor_total
    print(f"{i['quantidade']} unidades de {i['item']} - R${valor_total:.2f}")


print(f"Valor total das compras foi de: R${total:.2f}")



#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#SELECIONA O CODIGO INTEIRO DE CIMA E APERTA CTRL ; (VAI COMENTAR O CODIGO INTEIRO)
#AI FAZ A MESMA COISA COM ESSE DEBAIXO PARA REMOVER O COMENTARIO
#ESSE DEBAIXO EU FIZ PORQUE GOSTEI DA IDEIA, VE AI
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!






# import tkinter as tk 
# from tkinter import messagebox 
# import subprocess 

# class Mercadinho:
#     opcoes = {
#         "arroz": {"preco": 4.00, "estoque": 10},
#         "feijao": {"preco": 7.99, "estoque": 10},
#         "morango": {"preco": 8.98, "estoque": 10},
#         "batata": {"preco": 7.89, "estoque": 10},
#         "toddynho": {"preco": 3.49, "estoque": 10},
#         "doritos": {"preco": 9.99, "estoque": 10},
#         "pao de forma": {"preco": 22.08, "estoque": 10},
#         "yakult": {"preco": 13.99, "estoque": 10},
#         "alface": {"preco": 7.45, "estoque": 10},
#         "kit kat": {"preco": 4.00, "estoque": 10}
#     } 
#     carrinho = []
#     total = 0.0
#     cpf = None  

#     def __init__(self):
#         self.root = tk.Tk()
#         self.root.withdraw() 

#     def comprar(self): 
#         while True: 
#             print("Opções de produtos:")
#             for produto, info in self.opcoes.items():
#                 print(f"{produto.capitalize()} - R${info['preco']:.2f} (Estoque: {info['estoque']})") 

#             escolha = input("Digite o nome do produto que deseja comprar (ou 'sair' para encerrar a compra): ").strip().lower()
#             if escolha == 'sair':
#                 break

#             if escolha in self.opcoes:
#                 quantidade = int(input("Digite a quantidade desejada: "))

#                 if quantidade > self.opcoes[escolha]['estoque']:
#                     self.exibir_aviso(f"Estoque insuficiente para {escolha}. Disponível: {self.opcoes[escolha]['estoque']}")
#                 else:
#                     preco = self.opcoes[escolha]['preco']
#                     novoItem = {
#                         'item': escolha.capitalize(),
#                         'quantidade': quantidade,
#                         'preco': preco
#                     }

#                     self.carrinho.append(novoItem)
#                     self.opcoes[escolha]['estoque'] -= quantidade  
#                     self.exibir_aviso(f"{quantidade} unidades de {escolha} adicionadas ao carrinho.")
#             else:
#                 print("Produto não encontrado. Tente novamente.")

#         self.resumo_compra()
#         self.pagar()

#     def exibir_aviso(self, mensagem):
    
#         aviso = tk.Toplevel(self.root)
#         aviso.title("Aviso")
#         aviso.geometry("300x100")
        
#         tk.Label(aviso, text=mensagem, padx=20, pady=20).pack()
        
#         tk.Button(aviso, text="OK", command=aviso.destroy).pack()
        
#         aviso.attributes("-topmost", True)
#         aviso.wait_window()
#     def resumo_compra(self):
#         print("\nResumo da compra")
#         for produto in self.carrinho:
#             preco_total = produto['preco'] * produto['quantidade']
#             print(f"{produto['quantidade']} unidades de {produto['item']} - R${preco_total:.2f}")
#             self.total += preco_total

#         print(f"Total da compra: R${self.total:.2f}")

#     def pagar(self):
#         pagamento = input("Insira o valor a pagar (ou 'cancelar' para cancelar a compra): ").strip().lower()
#         if pagamento == "cancelar":
#             print("Compra cancelada :(")
#             return 

#         try:
#             valor_pago = float(pagamento)

#         except ValueError: 
#             print("Valor inválido. Tente novamente.")
#             self.pagar()
#             return

#         troco = valor_pago - self.total 

#         if troco < 0:
#             print(f"Valor insuficiente. Faltam R${-troco:.2f}")
#             self.pagar()
#         else:
#             if troco > 0:
#                 print(f"Troco: R${troco:.2f}")
            
#             cpf_nota = input("CPF na nota? (sim/não): ").strip().lower()
            
#             if cpf_nota in {"sim", "s", "sim", "s", "SIM", "Sim", "ss", "SS"}:
#                 self.cpf = input("Digite o CPF: ")
#                 print(f"Nota fiscal: Total da compra - R${self.total:.2f} | CPF - {self.cpf} Obrigado pela compra, volte sempre! :)")
#             else:
#                 print(f"Nota fiscal: Total da compra - R${self.total:.2f} Obrigado pela compra, volte sempre! :)")

#             self.gerar_nota_fiscal()

#     def gerar_nota_fiscal(self):
#         nome_arquivo = 'nota_fiscal.txt'

#         conteudo = "==============================================\n"
#         conteudo += "            MERCADINHO FAISQUINHA\n"
#         conteudo += "                 NOTA FISCAL\n"
#         conteudo += "==============================================\n"
#         conteudo += f"{'ID':<5} {'Nome':<9} {'Preço':>9} {'Quantidade':>9}\n"
#         conteudo += "-" * 40 + "\n"

#         for i, produto in enumerate(self.carrinho, start=1): 
#             conteudo += (f"{i:<5} "
#                          f"{produto['item']:<12} "
#                          f"R${produto['preco']:>5.2f} "
#                          f"{produto['quantidade']:>10}\n")


#         conteudo += (
#             "-" * 45 + "\n"
#             f"Total da compra: R${self.total:.2f}\n"
#         )
#         if self.cpf:
#             conteudo += f"CPF: {self.cpf}\n"
#         conteudo += (
#             "Obrigado pela compra, volte sempre :)\n"
#             "==============================================\n"
#         )


#         with open(nome_arquivo, 'w') as f:
#             f.write(conteudo)

#         subprocess.run(['notepad.exe', nome_arquivo])

# mercado = Mercadinho()
# mercado.comprar()
