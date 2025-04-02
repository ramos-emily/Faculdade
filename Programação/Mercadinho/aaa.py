tabela = {"Alface": 5.00,
          "Batata": 4.55,
          "Tomate": 9.80,
          "Feijão": 7.30}
valor_total = 0
while True:
    produto = input("Qual o produto? ").capitalize()
   
    if produto == "Sair":
        print("Bye!")
        break
       
    quantidade = int(input("Quantidade: "))
    valor_produto = tabela[produto] * quantidade
    valor_total = valor_total + valor_produto
print(f"Valor total das compras foi de: R${valor_total:.2f}")
