import random

elementos = []

# Cria um valor aleatorio
num_elementos = random.randint(5, 20)

# Cria a lista com valores aleatorios
for i in range(num_elementos):
    elementos.append(random.randint(1, 10))

# A lista elementos
print(elementos)

# A soma dos valores da lista
print(sum(elementos))

# A média dos valores da lista
print(sum(elementos) / num_elementos)