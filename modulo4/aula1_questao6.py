n = int(input("Digite a quantidade de experimentos: "))
cont = 0

sapo = 0
rato = 0
coelho = 0

while cont < n:
    quantia = int(input())
    tipo = input()

    if tipo == "S":
        sapo += quantia
    elif tipo == "R":
        rato += quantia
    elif tipo == "C":
        coelho += quantia
    
    cont += 1

total = sapo+coelho+rato
print(f"Total: {total}")
print(f"Total de coelhos: {coelho}")
print(f"Total de ratos: {rato}")
print(f"Total de sapos: {sapo}")
print(f"Percentual de coelhos: {(coelho*100)/total:.2f}%")
print(f"Percentual de ratos: {((rato*100)/total):.2f}%")
print(f"Percentual de sapos: {((sapo*100)/total):.2f}%")
