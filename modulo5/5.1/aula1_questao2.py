# Raiz da soma de valores aleatorios
import random
import math

soma = 0

n = int(input("Digite o valor de n: "))

for i in range(n):
    soma += random.randint(0,100)

print(f"Resultado: {soma**2}")

