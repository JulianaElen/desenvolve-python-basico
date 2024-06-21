import csv

# funcao que criar um usuario novo e adiciona ao arquivo de usuarios
def criarUsuario():
    # abre o arquivo de usuarios para leitura e pega o proximo id
    with open('usuarios.csv', mode='r') as arquivo:
        reader = csv.reader(arquivo)
        idDisponivel = max([int(row[0]) for row in reader], default=0) + 1

    nome = input("Digite o nome do usuário: ")
    senha = input("Digite a senha do usuário: ")
    permissao = int(input("Qual o tipo de permissão? Digite 1 para funcionário e 2 para gerente: "))

    if permissao not in [1, 2]:
        print("Digite um valor válido (1 para Funcionário ou 2 para Gerente).")
        return

    # abre o csv no modo 'a' para adicionar a informação no final dele
    with open('usuarios.csv', mode='a', newline='') as arquivo:

        writer = csv.writer(arquivo)
        writer.writerow([idDisponivel, nome, senha, permissao])

    print("Usuário criado com sucesso.")

# Funcao para ler os usuarios 
def lerUsuarios():

    # pede o tipo de leitura
    tipoLeitura = int(input('Escolha uma opção: \n 1 - Todos os usúarios \n 2 - Gerentes \n 3 - Funcionários \n 4 - Busca por id \n 5 - Cancelar\n'))

    # mostra todos os usuarios
    if tipoLeitura == 1:
        print('Todos os usuários:')
        with open('usuarios.csv', mode='r', newline='') as arquivo:
            reader = csv.reader(arquivo)
            next(reader)  # pula o cabeçalho
            for linha in reader:
                print(f"ID: {linha[0]}, Nome: {linha[1]}, Senha: {linha[2]}, Permissão: {linha[3]}")

    # mostra apenas o gerente
    elif tipoLeitura == 2:
        print('Gerentes:')
        with open('usuarios.csv', mode='r', newline='') as arquivo:
            reader = csv.reader(arquivo)
            next(reader) 
            for linha in reader:
                if linha[3] == '2':
                    print(f"ID: {linha[0]}, Nome: {linha[1]}, Senha: {linha[2]}, Permissão: {linha[3]}")

    # mostra apenas os funcionarios
    elif tipoLeitura == 3:
        print('Funcionários:')
        with open('usuarios.csv', mode='r', newline='') as arquivo:
            reader = csv.reader(arquivo)
            next(reader)  
            for linha in reader:
                if linha[3] == '1':  
                    print(f"ID: {linha[0]}, Nome: {linha[1]}, Senha: {linha[2]}, Permissão: {linha[3]}")

    # mostra o usuario pelo id
    elif tipoLeitura == 4:
        idBusca = input("Digite o ID do usuário que deseja buscar: ")
        encontrado = False
        with open('usuarios.csv', mode='r', newline='') as arquivo:
            reader = csv.reader(arquivo)
            next(reader)  
            for linha in reader:
                if linha[0] == idBusca:
                    print('Usuário encontrado:')
                    print(f"ID: {linha[0]}, Nome: {linha[1]}, Senha: {linha[2]}, Permissão: {linha[3]}")
                    encontrado = True
                    break
        if not encontrado:
            print("Usuário não encontrado.")

    elif tipoLeitura == 5:
        print("Operação cancelada.")
        return

    else:
        print("Opção inválida. Escolha uma opção válida.")

# funcao para editar um usuario
def editarUsuario():

    encontrado = False
    arquivoTemporario = 'usuariosAux.csv'

    idEditar = int(input("Digite o id do usuário que deseja modificar: "))
    

    # cria a lista de usuarios
    with open('usuarios.csv', mode='r', newline='') as arquivo:
        reader = csv.reader(arquivo)
        with open(arquivoTemporario, mode='w', newline='') as arquivoAux:
            writer = csv.writer(arquivoAux)
            for linha in reader:
                if linha[0] == idEditar:
                    encontrado = True
                    


        



def delete_user():
    pass

# Funções de Produtos/Serviços (CRUD)
def create_product():
    pass

def read_products():
    pass

def update_product():
    pass

def delete_product():
    pass

# Funções adicionais
def login():
    pass

def access_control():
    pass

def search_product():
    pass

def print_products_sorted_by_name():
    pass

def print_products_sorted_by_price():
    pass

# Funções de Gerência de Arquivos
def load_users_from_file():
    pass

def save_users_to_file():
    pass

def load_products_from_file():
    pass

def save_products_to_file():
    pass

opcao1 = int(input("Escolha a opção desejada: \n 1 - Criar novo usuário \n 2 - Listar usuários \n 3 - Editar usuário"))

if opcao1 == 1:
    criarUsuario()
elif opcao1 == 2:
    lerUsuarios()
elif opcao1 == 3:
    editarUsuario()
