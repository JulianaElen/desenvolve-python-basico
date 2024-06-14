import csv
from collections import defaultdict

arquivoMusicas = 'spotify-2023.csv'

with open(arquivoMusicas, 'r', encoding='latin-1') as arquivo:
    texto = csv.reader(arquivo)
    cabecalho = next(texto) 
    top = defaultdict(lambda: ["", "", 0, 0])

    for col in texto:
        try:
            nome = col[0]
            artista = col[1]
            cont = int(col[2])
            ano = int(col[3])
            streams = int(col[8])
        except ValueError:
            continue

        if '"' in nome or '"' in artista:
            continue
        
        if 2012 <= ano <= 2022:
            if streams > top[ano][3]:
                top[ano] = [nome, artista, ano, streams]

topMusicas = [top[topAno] for topAno in range(2012, 2023)]

print("Músicas mais tocadas de cada ano entre 2012 e 2022:")
for i in topMusicas:
    print(i)
