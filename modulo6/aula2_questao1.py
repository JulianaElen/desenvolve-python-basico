import random

listaNum = []

# Cria a lista com valores aleatorios
for i in range(20):
    listaNum.append(random.randint(-100, 100))

# A lista ordenada, sem modificar a lista original
print(sorted(listaNum))

# A lista original
print(listaNum)

# O índice do maior valor da lista
print(listaNum.index(max(listaNum)))

# O índice do menor valor da lista
print(listaNum.index(min(listaNum)))