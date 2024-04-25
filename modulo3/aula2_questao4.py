# Solicita a classe e demais dados 
classe = input("Escolha a classe (guerreiro, mago ou arqueiro): ")
forca = int(input("Digite os pontos de força (de 1 a 20): "))
magia = int(input("Digite os pontos de magia (de 1 a 20): "))

# Verifica a validade dos dados se a classe é guerreiro
g = (classe == "guerreiro") and (forca >= 15) and (magia <= 10)
# Verifica a validade dos dados se a classe é mago
m = (classe == "mago") and (forca <= 10) and (magia >= 15)
# Verifica a validade dos dados se a classe é arqueiro
a = (classe == "arqueiro") and (forca > 5 and forca <= 15) and (magia > 5 and magia <= 15) 

# Imprime se os atributos estão corretos
print(f"Pontos de atributo consistentes com a classe escolhida: {g or m or a}")

