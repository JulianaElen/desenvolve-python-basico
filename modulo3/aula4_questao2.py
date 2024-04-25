# Solicita a nota
nota = int(input("Qual a sua avaliação para o filme? "))

# Verifica o valor da nota e exibe a mensagem
if nota == 1:
    print("Ruim.")
elif nota == 2:
    print("Regular.")
elif nota == 3:
    print("Bom!")
elif nota == 4:
    print("Muito Bom!")
elif nota == 5:
    print("Excelente!")
else:
    print("Nota invalida. Digite um valor entre 1 e 5.")
    