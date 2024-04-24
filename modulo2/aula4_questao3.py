# Questão 3

# cria um array de produtos
produtos = []
# cria a variavel do total de compra
valor_total = 0

# estrutura de repetição que pede para que o usuario digite as informações de 3 produtos e as armazena do array
for i in range(3):
    nome = input(f"Digite o nome do produto {i+1}: ")
    valor_unidade = float(input(f"Digite o preço unitário do produto {i+1}: "))
    quantidade = int(input(f"Digite a quantidade do produto {i+1}: "))
    # soma o valor do produto a variavel do total da compra
    valor_total += (valor_unidade*quantidade)
    # armazena os dados dos produtos
    produtos.append((nome, valor_unidade, quantidade))

print("A sua lista de compras foi:")
# imprime os dados dos produtos
for produto in produtos:
     print(f"Nome: {produto[0]}. Valor unitário: R${produto[1]:.2f}. Quatidade: {produto[2]}.")

# imprime o total da compra
print(f"Total: RS{valor_total:,.2f}")