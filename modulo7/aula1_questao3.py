frase = input("Didite a frase: ")
cont = 0

for i in range(len(frase)):
    if frase[i] == " ":
        cont += 1

print(f"Espaços em branco: {cont}")
