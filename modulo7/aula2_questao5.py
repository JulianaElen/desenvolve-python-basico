import random

def embaralhar_palavras(frase):
    palavras = frase.split() 
    resultado = []
    
    for i in palavras:
        if len(i) > 2:
            primeiraLetra = i[0]
            ultimaLetra = i[-1]
            letrasInternas = list(i[1:-1])
            random.shuffle(letrasInternas)
            palavraEmbaralhada = primeiraLetra + ''.join(letrasInternas) + ultimaLetra
        else:
            palavraEmbaralhada = i  
        resultado.append(palavraEmbaralhada)
    
    return ' '.join(resultado)

# Exemplo de uso:
frase = "Python é uma linguagem de programação"
resultado = embaralhar_palavras(frase)
print(resultado)
