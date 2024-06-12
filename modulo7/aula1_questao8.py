def validaCPF(cpf):
    cpf = cpf.replace('.', '').replace('-', '')

    if len(cpf) != 11 or not cpf.isdigit():
        print("Inválido")
        return

    def calcular_digito_verificador(cpf, multiplicadores):
        soma = sum(int(cpf[i]) * multiplicadores[i] for i in range(len(multiplicadores)))
        resto = soma % 11
        return 0 if resto < 2 else 11 - resto

    multiplicadores1 = list(range(10, 1, -1))
    primeiro_digito = calcular_digito_verificador(cpf[:9], multiplicadores1)

    multiplicadores2 = list(range(11, 1, -1))
    segundo_digito = calcular_digito_verificador(cpf[:9] + str(primeiro_digito), multiplicadores2)

    if int(cpf[9]) == primeiro_digito and int(cpf[10]) == segundo_digito:
        print("Válido")
    else:
        print("Inválido")

cpf = input("Digite o CPF na forma XXX.XXX.XXX-XX: ")
validaCPF(cpf)