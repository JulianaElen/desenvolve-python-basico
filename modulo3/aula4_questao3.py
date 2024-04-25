# Solicita o ano
ano = int(input("Digite o ano: "))

# Resto da divisão por 4
resto4 = ano % 4

# Resto da divisão por 100
resto100 = ano % 100

# Resto da divisão por 400
resto400 = ano % 400

# Verifica se é bissexto:
print("Bissexto" if (resto4 == 0 and resto100 != 0) or (resto400 == 0) else "Não Bissexto")