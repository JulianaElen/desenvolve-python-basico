import csv
import os

#Primeira parte que tem as funções de usuarios

# funcao que criar um usuario novo e adiciona ao arquivo de usuarios
def criarUsuario():

    # abre o arquivo de usuarios para leitura e pega o proximo id
    with open('usuarios.csv', mode='r') as arquivo:
        reader = csv.reader(arquivo)
        next(reader)
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
                    print(f"ID: {linha[0]}, Nome: {linha[1]}, Senha: {linha[2]}, permissão: {linha[3]}")
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

    idEditar = input("Digite o id do usuário que deseja modificar: ")
    

    # cria a lista de usuarios
    with open('usuarios.csv', mode='r', newline='') as arquivo:
        reader = csv.reader(arquivo)

        with open(arquivoTemporario, mode='w', newline='') as arquivoAux:
            writer = csv.writer(arquivoAux)

            for linha in reader:
                if linha[0] == idEditar:
                    encontrado = True
                    print(f"Usuário encontrado: ID: {linha[0]}, Nome: {linha[1]}, Senha: {linha[2]}, Permissão: {linha[3]}")
                    
                    # Editar o nome
                    resp1 = int(input("Deseja editar o nome? (1 para sim, 2 para não): "))
                    if resp1 == 1:
                        novoNome = input("Digite o novo nome: ")
                        linha[1] = novoNome

                    # Editar a senha
                    resp2 = int(input("Deseja editar a senha? (1 para sim, 2 para não): "))
                    if resp2 == 1:
                        novaSenha = input("Digite a nova senha: ")
                        linha[2] = novaSenha

                    # ediitar a permissão
                    resp3 = int(input("Deseja editar a permissão? (1 para sim, 2 para não): "))
                    if resp3 == 1:
                        novaPermissao = input("Digite a nova permissão (1 para funcionário, 2 para gerente): ")
                        linha[3] = novaPermissao

                writer.writerow(linha)

    # foi criado um arquivo auxiliar para armazenar os dados, aq os dados volatm para o original e ele é apagado
    if encontrado:
        os.remove('usuarios.csv')
        os.rename(arquivoTemporario, 'usuarios.csv')
        print("Usuário atualizado com sucesso.")

    else:
        os.remove(arquivoTemporario)
        print("Usuário não encontrado.")
                    
# função para apagar o usuario
def apagarUsuario():

    encontrado = False
    arquivoTemporario = 'usuariosAux.csv' # usa o arquivo temporario, como na função de cima

    idApagar = input("Digite o id do usuario que você quer apagar: ")

    with open('usuarios.csv', mode='r', newline='') as arquivo:
        reader = csv.reader(arquivo)

        with open(arquivoTemporario, mode='w', newline='') as arquivoAux:
            writer = csv.writer(arquivoAux)

            for linha in reader:
                if linha[0] != idApagar: # escreve todas as linhas, menos a que eu quero apagar
                    writer.writerow(linha)
                else:
                    encontrado = True

    if encontrado:
        os.remove('usuarios.csv')
        os.rename(arquivoTemporario, 'usuarios.csv')
        print("Usuário removido com sucesso.")
    else:
        os.remove(arquivoTemporario)
        print("Usuário não encontrado.")

#Segunda Parte que faz as funções de gerenciar os produtos

# função de criar produto
def criarProduto():

    with open('produtos.csv', mode='r', newline='') as arquivo:
        reader = csv.reader(arquivo)
        next(reader)
        idDisponivel = max([int(row[0]) for row in reader], default=0) + 1 #pegando o id para o novo produto

    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    descricao = input("Digite a deacricao do produto: ")

    with open('produtos.csv', mode='a', newline='') as arquivo: #escreve no arquivo de produtos, no final (modo a)
        writer = csv.writer(arquivo)
        writer.writerow([idDisponivel, nome, preco, descricao])

    print("Produto criado com sucesso.")

# funcao de leitura dos produtos
def lerProdutos():
    tipoLeitura = int(input('Escolha uma opção: \n 1 - Todos os produtos \n 2 - Buscar por id \n 3 - Imprimir ordenados por nome \n 4 - Imprimir ordenados por preço \n 5 - Cancelar\n'))

    # imprime todos os produtps sem ordenação
    if tipoLeitura == 1:
        print('Todos os produtos:')

        with open('produtos.csv', mode='r', newline='') as arquivo:
            reader = csv.reader(arquivo)
            next(reader)

            for linha in reader:
                print(f"ID: {linha[0]}, Nome: {linha[1]}, Preco: {linha[2]}, Descrição: {linha[3]}")

    # Imprime apenas o produto do id desejado
    elif tipoLeitura == 2:
        idBusca = input("Digite o id do produto que deseja buscar: ")
        encontrado = False

        with open('produtos.csv', mode='r', newline='') as arquivo:
            reader = csv.reader(arquivo)

            for linha in reader:
                if linha[0] == idBusca: # busca id e imprime
                    print('Produto encontrado:')
                    print(f"ID: {linha[0]}, Nome: {linha[1]}, Preço: {linha[2]}, Descricao: {linha[3]}")
                    encontrado = True
                    break

        if not encontrado:
            print("Produto não encontrado.")
            
    # imprime os produtos ordenados por nome
    elif tipoLeitura == 3:
        print('Produtos ordenados por nome:')

        with open('produtos.csv', mode='r', newline='') as arquivo:
            reader = csv.reader(arquivo)
            next(reader)

            produtos = list(reader)
            produtos.sort(key=lambda x: x[1])  # ordena pelo nome

            for linha in produtos:
                print(f"ID: {linha[0]}, Nome: {linha[1]}, Preço: {linha[2]}, Descrição: {linha[3]}")
                
    # imprime os produtos ordenados pelo preco
    elif tipoLeitura == 4:
        print('Produtos ordenados por preço:')

        with open('produtos.csv', mode='r', newline='') as arquivo:
            reader = csv.reader(arquivo)
            next(reader)

            produtos = list(reader)
            produtos.sort(key=lambda x: float(x[2]))  # Ordena pelo preço
            for linha in produtos:
                print(f"ID: {linha[0]}, Nome: {linha[1]}, Preço: {linha[2]}, Descriço: {linha[3]}")

    elif tipoLeitura == 5:
        print("Operação cancelada.")
        return

    else:
        print("Opção inválida. Escolha uma opção válida.")

#Função para editar um produto existente
def editarProduto():
    encontrado = False
    arquivoTemporario = 'produtosAux.csv' #cria arquivo auxiliar

    idEditar = input("Digite o ID do produto que deseja modificar: ")

    with open('produtos.csv', mode='r', newline='') as arquivo:
        reader = csv.reader(arquivo)

        with open(arquivoTemporario, mode='w', newline='') as arquivoAux:
            writer = csv.writer(arquivoAux)

            for linha in reader:
                if linha[0] == idEditar:
                    encontrado = True
                    print(f"Produto encontrado: ID: {linha[0]}, Nome: {linha[1]}, Preço: {linha[2]}, Descrição: {linha[3]}")

                    # Editar o nome
                    resp1 = int(input("Deseja editar o nome? (1 para sim, 2 para não): "))
                    if resp1 == 1:
                        novoNome = input("Digite o novo nome: ")
                        linha[1] = novoNome

                    # Editar o preço
                    resp2 = int(input("Deseja editar o preço? (1 para sim, 2 para não): "))
                    if resp2 == 1:
                        novoPreco = float(input("Digite o novo preço: "))
                        linha[2] = novoPreco

                    # Editar a Descrição
                    resp3 = int(input("Deseja editar a Descrição? (1 para sim, 2 para não): "))
                    if resp3 == 1:
                        novaDescricao = input("Digite a nova Descrição: ")
                        linha[3] = novaDescricao

                writer.writerow(linha)

    if encontrado: # salva no arquivo
        os.remove('produtos.csv')
        os.rename(arquivoTemporario, 'produtos.csv')
        print("Produto atualizado com sucesso.")
    else:
        os.remove(arquivoTemporario)
        print("Produto não encontrado.")

# função para apagar o produto
def apagarProduto():
    encontrado = False
    arquivoTemporario = 'produtosAux.csv'

    idApagar = input("Digite o ID do produto que deseja apagar: ")

    with open('produtos.csv', mode='r', newline='') as arquivo:
        reader = csv.reader(arquivo)

        with open(arquivoTemporario, mode='w', newline='') as arquivoAux:
            writer = csv.writer(arquivoAux)

            for linha in reader:
                if linha[0] == idApagar:
                    encontrado = True
                    print(f"Produto removido: ID: {linha[0]}, Nome: {linha[1]}, Preço: {linha[2]}, DEscrição: {linha[3]}")
                else:
                    writer.writerow(linha)

    if encontrado:
        os.remove('produtos.csv')
        os.rename(arquivoTemporario, 'produtos.csv')
        print("Produto removido com sucesso.")
    else:
        os.remove(arquivoTemporario)
        print("Produto não encontrado.")

#Terceira parte, que cuida da autentificação

#função do login do usuario
def login():

    usuarios = []

    with open('usuarios.csv', mode='r', newline='') as arquivo:
        reader = csv.reader(arquivo)

        for linha in reader:
            usuarios.append({'id': linha[0], 'nome': linha[1], 'senha': linha[2], 'permissao': linha[3]})

    nome = input("Digite seu nome de usuário: ")
    senha = input("Digite sua senha: ")

    for usuario in usuarios: #valida se o usuario existe e os dados está corretos
        if usuario['nome'] == nome and usuario['senha'] == senha:
            print(f"Bem-vindo(a), {nome}!")
            return usuario['permissao'] #retorna o nivel de permissao dele

    print("Usuário ou senha incorretos.")
    return None

#controla a permissão de cada usuarios
def controlePermissao(permissao):

    while True:
        if permissao == 1: #funcionario
            opcao = int(input("Escolha a opção desejada: \n 1 - Listar usuários \n 2 - Listar produtos \n 3 - Sair\n"))

            if opcao == 1:
                lerUsuarios()
            elif opcao == 2:
                lerProdutos()
            elif opcao == 3:
                print("Programa cancelado!")
                break
            else:
                print("Opção inválida. Por favor, escolha uma opção válida.")

        elif permissao == 2: #gerente
            opcao = int(input("Escolha a opção desejada: \n 1 - Criar novo usuário \n 2 - Listar usuários \n 3 - Editar usuário \n 4 - Apagar usuário \n 5 - Criar novo produto \n 6 - Listar produtos \n 7 - Editar produto \n 8 - Apagar produto \n 9 - Sair\n"))

            if opcao == 1:
                criarUsuario()
            elif opcao == 2:
                lerUsuarios()
            elif opcao == 3:
                editarUsuario()
            elif opcao == 4:
                apagarUsuario()
            elif opcao == 5:
                criarProduto()
            elif opcao == 6:
                lerProdutos()
            elif opcao == 7:
                editarProduto()
            elif opcao == 8:
                apagarProduto()
            elif opcao == 9:
                print("Programa cancelado!")
                break
            else:
                print("Opção inválida. Por favor, escolha uma opção válida.")

        else:
            print("Permissão inválida.")
            break


def main():
    permissao = login()
    if permissao:
        controlePermissao(int(permissao))
        main()  # chamada recursiva do menu

if __name__ == "__main__":
    main()