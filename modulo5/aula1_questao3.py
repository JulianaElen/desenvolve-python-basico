# Adivinhe o numero

import random

num = random.randint(1,10)
aux = 0

while True:
    aux = int(input("Adivinhe o numero entre 1 e 10: "))
    if aux == num:
        print(f"Correto! o número é {num}")
        break
    elif aux > num:
        print("Muito alto, tente novamente!")
        continue
    elif aux < num:
        print("Muito baixo, tente novamente!")
        continue