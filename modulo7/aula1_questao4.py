num = input("Digite o número: ")

if len(num) == 8:
    num = "9" + num

print(f"Número compreto: {num[:5]}-{num[5:]}")