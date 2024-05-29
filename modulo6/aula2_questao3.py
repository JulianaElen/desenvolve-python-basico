import random

lista1 = []
lista2 = []
interseccao = []

# Cria as listas com valores aleatorios
for i in range(20):
    lista1.append(random.randint(0, 50))
for i in range(20):
    lista2.append(random.randint(0, 50))

for i in range(20):
    aux = lista1[i]
    if aux in lista2 and aux not in interseccao:
        interseccao.append(lista1[i])

# Ambas as listas
print(lista1)
print(lista2)
print(interseccao)

# A lista intersecção ordenada
print(interseccao.sort())

# A quantidade de vezes que cada elemento aparece em cada lista
print("Contagem:")
for i in range(len(interseccao)):
    print(f"{interseccao[i]}: (lista1 = {lista1.count(interseccao[i])}, lista2 = {lista2.count(interseccao[i])})")