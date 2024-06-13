frase = input("Digite sua frase: ")
vogais = "aeiouAEIOU"
fraseAux = frase

for i in vogais:
    fraseAux = fraseAux.replace(i, '*')  

print("Frase modificada:",fraseAux)