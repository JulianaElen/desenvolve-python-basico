frase = input("Didite a frase: ")
objetivo = input("Digite a palavra objetivo: ")
anagramas = []

objetivo = sorted(objetivo)
listaPalavras = frase.lower().split(" ")

for i in listaPalavras:
    aux = sorted(i)
    if aux == objetivo:
        anagramas.append(i)

print(anagramas)