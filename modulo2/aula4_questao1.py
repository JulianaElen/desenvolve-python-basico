# Questão 1

# Recebe o valor da largura e do comprimento
comp = int(input("Qual o comprimento? "))
larg = int(input("Qual a largura? "))

# Recebe o preco por m2
preco_m2 = float(input("Qual o preço do metro quadrado em ponto flutuante? "))

# calcula a area total do terreno
area = comp * larg

# calcula o preco total do terreno
preco_total = area * preco_m2

# imprime o resultado
print(f"O terreno possui {area}m2 e custa R${preco_total}")
