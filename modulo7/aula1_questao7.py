import random

def criptogra(nomes):
    n = random.randint(1, 10)
    
    listaNomesCript = []
    
    for i in nomes:
        nomesCript = ""
        for j in i:
            if 33 <= ord(j) <= 126:
                codigo = ord(j) + n
                if codigo > 126:
                    codigo = 33 + (codigo - 127)
                nomesCript += chr(codigo)
            else:
                nomesCript += j
        listaNomesCript.append(nomesCript)
    
    return listaNomesCript, n

nomes = ["Luana", "Ju", "Davi"]
nomesCript, chave = criptogra(nomes)
print(f"nomes cript = {nomesCript}")
print(f"chave aleatoria = {chave}")
