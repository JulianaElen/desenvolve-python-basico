import random

lista = []

for i in range(20):
    lista.append(random.randint(-10, 10))
print(lista)

inicioMaior, tamMaior = 0, 0
inicioAtual, tamAtual = 0, 0

for i in range(len(lista)):
    if lista[i] < 0:
        tamAtual +=1
        if tamAtual == 1:
            inicioAtual = i
    else:
        if tamAtual > tamMaior:
            tamMaior = tamAtual
            inicioMaior = inicioAtual
        tamAtual = 0

del lista[inicioMaior:inicioMaior+tamMaior:]
print(lista)