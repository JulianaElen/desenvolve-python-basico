import  os, sys
from random import randint

# Abra o arquivo "gabarito_forca.txt" e escolha aleatoriamente uma palavra;
arquivo = open("gabarito_forca.txt", "r")
arquivoPalavras = arquivo.read()  
palavras = arquivoPalavras.splitlines()

lugarPalavra = randint(0,9)
palavra = palavras[lugarPalavra]

# Com o arquivo "gabarito_enforcado.txt", crie uma lista de strings com os estágios do enforcado;
arquivo2 = open("gabarito_enforcado.txt", "r")
arquivoForca = arquivo2.read()
enforcado = []
estagios = arquivoForca.strip().split("\n\n")
for linha in estagios:
        enforcado.append(linha.strip())

# No início exiba o número de letras da palavra sorteada como underscores;
forca = "_" * len(palavra)
print(forca)

# Permita que o jogador insira letras para adivinhar a palavra;
# Em caso de acerto, mostre o progresso do jogador substituindo os underscores correspondentes à letra digitada;
# Em caso de erro, crie a função "imprime_enforcado()" que recebe um inteiro indicando o número de erros do jogador e imprime o enforcado correspondente;
# Limite o número de tentativas para 6 (as partes do enforcado).
erros = 0
print(enforcado[0])
while erros < 6:
    letra = input("Digite uma letra: ")

    if letra in palavra:
        for i in range(len(palavra)):
            if palavra[i] == letra:
                forca = forca[:i] + letra + forca[i+1:]
        print(forca)

        if "_" not in forca:
            print("Parabéns, você venceu!")
            break
    else:
        erros += 1
        print(enforcado[erros])
else:
    print("Você perdeu! A palavra correta era:", palavra)

arquivo2.close()
arquivo.close()