import re

while True:
    frase = input("Digite uma frase (digite \"fim\" para encerrar): ")
    fraseAux = frase.lower()
    fraseInvertida = ""

    if fraseAux == "fim":
        break

    fraseAux = re.sub('[^a-zA-Z0-9]', '', fraseAux)
    
    fraseInvertida = fraseAux[::-1]

    if fraseAux == fraseInvertida:
        print(f"{frase} é palíndromo!")
    else:
        print(f"{frase} não é palíndromo!")

