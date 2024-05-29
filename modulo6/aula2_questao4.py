lista1 = []
lista2 = []
listaIntercalada = []

quat1 = int(input("Digite a quantidade de elementos da lista 1: "))
print(f"Digite os {quat1} elementos da lista 1:")
for i in range(quat1):
    lista1.append(int(input()))

quat2 = int(input("Digite a quantidade de elementos da lista 2: "))
print(f"Digite os {quat2} elementos da lista 2:")
for i in range(quat2):
    lista2.append(int(input()))

# combine essas duas listas de forma alternada para formar uma terceira lista
tam = min(len(lista1), len(lista2))

for i in range(tam):
    listaIntercalada.append(lista1[i])
    listaIntercalada.append(lista2[i])
if len(lista1) > len(lista2):
    listaIntercalada.extend(lista1[tam:])
else:
    listaIntercalada.extend(lista2[tam:])

print(f"Lista intercalada: {listaIntercalada}")