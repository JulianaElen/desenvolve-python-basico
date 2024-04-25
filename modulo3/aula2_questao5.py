# Solicita as informações
genero = input("Qual o seu gênero (F ou M)? ")
idade = int(input("Qual a sua idade? "))
tempo = int(input("Quantos anos de serviço você tem? "))

# Verifica a validade de cada caso
a = (genero == "F" and idade > 60) or (genero == "M" and idade > 65)
b = (tempo >= 30)
c = (idade >= 60 and tempo >= 25)

# Se um deles for verdadeio retorna true
print(a or b or c)
