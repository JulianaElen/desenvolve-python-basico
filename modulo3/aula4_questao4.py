# Solicita os dados
km = float(input("Digite a distância em km: "))
peso = float(input("Digite o peso do pacote em kg: "))

# Calculo do frete condicional
if km <= 100:
    frete = peso
elif km <= 300:
    frete = peso * 1.5
elif km > 300:
    frete = peso * 2

# Imprime o valor do frete, junto com a taxa adicional se kg > 10
print(f"O valor do frete é R${frete+10:.2f}" if peso > 10 else f"O valor do frete é R${frete:.2f}")
