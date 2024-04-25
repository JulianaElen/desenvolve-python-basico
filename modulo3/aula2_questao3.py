# Solicita os dados de entrada
idade = int(input("Digite sua idade: "))
jogou = input("Já jogou pelo menos 3 jogos de tabuleiro (resposta deve ser True ou False)? ")
ganhou = int(input("Quantos jogos já venceu? "))


# Verifica a validade dos dados e indica se pode ou não entrar
print(f"Apto para ingressar no clube de jogos de tabuleiro: {(idade >= 16 and idade <= 18) and (jogou == "True") and (ganhou >= 1)}")
   
