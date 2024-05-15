n = int(input("Digite n: "))
cont = 0

# Seguinto o fluxograma temos:
# while n < cont: 
#     cont = cont + 1
#     print(cont)
# print("Fim")

# Mas acho que tem algo errado, pois cont = 0, e para ser menor que 0 tem que ser um número negativo. Então, se n for negativo o loop nunca vai acabar, já que sempre somamos 1 ao cont

while n > cont: 
    cont = cont + 1
    print(cont)
print("Fim")