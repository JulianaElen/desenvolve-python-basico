# Todos os números pares entre 20 e 50, ou seja, [20, 22, 24, …, 48, 50]
lista1 = [n for n in range(20, 51) if n % 2 == 0]
print(lista1)

# Os quadrados de todos os valores da lista [1,2,3,4,5,6,7,8,9]
lista2 = [n**2 for n in range(1, 10)]
print(lista2)

# Todos os números entre 1 e 100 que sejam divisíveis por 7
lista3 = [n for n in range(1, 101) if n % 7 == 0]
print(lista3)

# Para todos os valores em range(0,30,3), escreva "par" ou "ímpar" dependendo da paridade do elemento (ex: ['par', 'impar',… , 'impar']) 
lista4 = ["Par" if n % 2 == 0 else "Ímpar" for n in range(0,30,3)]
print(lista4)
