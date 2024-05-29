frase = input("Digite uma frase: ")

vogais = [n for n in frase if n.lower() in 'aeiou']

consoantes = [n for n in frase if n.lower() not in 'aeiou ']

print(vogais)
print(consoantes)