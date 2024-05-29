tam = int(input("Qual o tamanho da lista (a partir de 4)? "))

lista = []

print("Digite os elementos da lista: ")

for i in range(tam):
    lista.append(int(input()))

# A lista original
print(lista)

# Os 3 primeiros elementos
print(lista[:3:])

# Os 2 últimos elementos
print(lista[tam-2::])

# A lista invertida (do fim para o começo)
print(lista[::-1])

# Os elementos de índice par (0, 2, 4 … )
print(lista[0::2])

# Os elementos de índice ímpar (1, 3, 5, … )
print(lista[1::2])