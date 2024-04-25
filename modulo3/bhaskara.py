import math

a, b, c = int(input("Qual o valor de a? ")), int(input("Qual o valor de b? ")), int(input("Qual o valor de c? "))

if (b**2 - (4 * a * c)) < 0:
    print("As raízes tem parte imaginaria diferente de 0.")
elif (b**2 - (4 * a * c)) == 0:
    print(f"A raiz é {-b / (2 * a)}.")
else:
    print(f"A primera raiz é {((-b - math.sqrt(b**2 - (4 * a * c))) / (2 * a)):.3f} e a segunda raíz é {((-b + math.sqrt(b**2 - (4 * a * c))) / (2 * a)):.3f}.")