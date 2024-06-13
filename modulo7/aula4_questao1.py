import os, sys

frase = open("frase.txt", "w")
aux = input("Digite uma frase: ")
frase.write(aux)
print(f"Frase salva em {os.path.abspath("frase.txt")}")
frase.close()
