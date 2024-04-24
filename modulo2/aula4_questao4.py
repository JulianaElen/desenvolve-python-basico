# Questão 4

# Solicita o valor em reais
valor = int(input("Digite o valor em reais: "))

# Imprime o valor inteiro da divisão por cada valor de nota e depois pega o resto dessa divisão.
print(f"{valor//100} notas(s) de R$100,00")
valor %= 100
print(f"{valor//50} notas(s) de R$50,00")
valor %= 50
print(f"{valor//20} notas(s) de R$20,00")
valor %= 20
print(f"{valor//10} notas(s) de R$10,00")
valor %= 10
print(f"{valor//5} notas(s) de R$5,00")
valor %= 5
print(f"{valor//2} notas(s) de R$2,00")
valor %= 2
print(f"{valor//1} notas(s) de R$1,00")
valor %= 1
