n = int(input("Digite a quantidade de pessoas: "))
cont = 0
soma_idades = 0

while cont < n:
    idade = int(input(f"Digite a idade {cont+1}: "))
    soma_idades += idade
    cont += 1
print(soma_idades/n)