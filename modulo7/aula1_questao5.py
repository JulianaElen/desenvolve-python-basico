frase = input("Didite a frase: ")
cont = 0
indices = []

for i in range(len(frase)):
    if frase[i] in "aeiou":
        cont += 1
        indices.append(i)
print(f"{cont} vogais \n indices: {indices}")