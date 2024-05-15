n1 = int(input("Digite n1: "))
n2 = int(input("Digite n2: "))
n3 = int(input("Digite n3: "))

m = (n1+n2+n3)/3

# Eu realmente não entendi qual o sentido de fazer essa atividade usando while pois não tem loop, pra mim faz muito mais sentido usar if

if m >= 60:
    print("Aprovado")
elif m >= 40:
    print("Recuperação")
else:
    print("Reprovado")
print("Fim")
