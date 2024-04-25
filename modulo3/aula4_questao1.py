# Leitura de dois números:
x = int(input("Qual o primeiro número? "))
y = int(input("Qual o segundo número? "))

# Soma os dois números e pega seu resto na divisão por 2
resto = (x+y) % 2

# Verifica se o resto é 0 ou não
if resto == 0:
    print(f"A soma de {x} e {y} é par.")
else:
    print(f"A soma de {x} e {y} é ímpar.")