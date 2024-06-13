import re

caminhoArquivo = 'estomago.txt'
with open(caminhoArquivo, 'r', encoding='latin-1') as arquivo:
    texto = arquivo.read()  

linhas = texto.splitlines()

# O texto das primeiras 25 linhas
print("As primeiras 25 linhas do arquivo:")
for i in range(min(25, len(linhas))):
    print(linhas[i])

# O número de linhas do arquivo
print(f"Quantidade de linhas do arquivo: {len(linhas)}")

# A linha com maior número de caracteres
maiorLinha = ''
cont = 0
for linha in linhas:
    if len(linha) > cont:
        maiorLinha = linha
        cont = len(linha)
print(f"A maior linha é: {maiorLinha}")

# Contar menções aos nomes
def contarMencoes(nome, texto):
    padrao = rf'\b{re.escape(nome)}\b'
    return len(re.findall(padrao, texto, re.IGNORECASE))

contNonato = contarMencoes('nonato', texto)
contIria = contarMencoes('íria', texto)
print(f'Menções ao nome "Nonato": {contNonato}')
print(f'Menções ao nome "Íria": {contIria}')
