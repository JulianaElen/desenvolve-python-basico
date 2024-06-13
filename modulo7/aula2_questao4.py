import re

def validadorSenha(senha):

    if len(senha) < 8:
        return False

    if not (any(c.isupper() for c in senha) and any(c.islower() for c in senha)):
        return False
    if not any(c.isdigit() for c in senha):
        return False
    if not re.search(r'[!@#$%^&*()_+{}\[\]:;<>,.?\/\\~-]', senha):
        return False
    return True


senha1 = "Senha123@"
senha2 = "senhafraca"
senha3 = "Senha_fraca"
senha4 = "Sen)a12aaaa"
senha5 = "SenhaDe34$"
print(validadorSenha(senha1))  # Saída esperada: True
print(validadorSenha(senha2))  # Saída esperada: False
print(validadorSenha(senha3))  # Saída esperada: False
print(validadorSenha(senha4))  # Saída esperada: True
print(validadorSenha(senha5))  # Saída esperada: True

