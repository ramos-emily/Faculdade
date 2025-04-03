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
        print("escreveu errado burro :( ")

total = 0

for i in carrinho:
    valor_total = i['preco'] * i['quantidade']
    total += valor_total
    print(f"{i['quantidade']} unidades de {i['item']} - R${valor_total:.2f}")


print(f"Valor total das compras foi de: R${total:.2f}")
