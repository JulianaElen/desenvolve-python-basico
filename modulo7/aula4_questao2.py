import os, sys, re

arquivoFrase = open("frase.txt", "r")
frase = arquivoFrase.read()
arquivoFrase.close()

frase = re.sub('[^a-zA-Z0-9áéíóúÁÉÍÓÚâêîôÂÊÎÔãõÃÕçÇ: ]', '', frase)
frase = frase.split()

arquivoPalavras = open("palavras.txt", "w")

for i in frase:
    arquivoPalavras.write(f"{i} \n")

arquivoPalavras.close()

# 2) Escreva um script que leia o arquivo salvo no exercício anterior e salva em um novo arquivo "palavras.txt", removendo todos os espaços em branco e caracteres não alfabéticos, e separando cada palavra em uma linha. Ao final, imprima o conteúdo do arquivo "palavras.txt".
# Ex:
# Bom
# dia
# meu
# nome
# é
# Davi

