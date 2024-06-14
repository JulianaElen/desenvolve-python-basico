# Selecione pelo menos 10 livros que você leu ou gostaria de ler. Você deve reunir as seguintes informações: título, autor, ano de publicação e número de páginas.
livros = [
    {'Título': 'Dália Azul', 'Autor': 'Nora Roberts', 'Ano de publicação': 2004, 'Número de páginas': 375},
    {'Título': 'Orgulho e Preconceito', 'Autor': 'Jane Austen', 'Ano de publicação': 1813, 'Número de páginas': 240},
    {'Título': 'Memórias Póstumas de Brás Cubas', 'Autor': 'Machado de Assis', 'Ano de publicação': 1881, 'Número de páginas': 192},
    {'Título': 'Graal - O cavaleiro sem nome', 'Autor': 'Christian de Montella', 'Ano de publicação': 1957, 'Número de páginas': 320},
    {'Título': 'Noite na Taverna', 'Autor': 'Álvares de Azevedo', 'Ano de publicação': 1855, 'Número de páginas': 98},
    {'Título': 'A Sociedade Cinderela', 'Autor': 'Kay Cassidy', 'Ano de publicação': 2010, 'Número de páginas': 306},
    {'Título': 'O Mapa de Vidro', 'Autor': 'S. E. Grove', 'Ano de publicação': 2015, 'Número de páginas': 396},
    {'Título': 'Arsène Lupin: Ladrão de Casaca', 'Autor': 'Maurice Leblanc', 'Ano de publicação': 1907, 'Número de páginas': 212},
    {'Título': 'Vidas Secas', 'Autor': 'Graciliano Ramos', 'Ano de publicação': 1938, 'Número de páginas': 100},
    {'Título': 'Ensaio sobre a cegueira', 'Autor': 'Saramago', 'Ano de publicação': 1955, 'Número de páginas': 241}
]

# No Python, crie um arquivo chamado "meus_livros.csv", aberto para escrita.
nome_arquivo = 'meus_livros.csv'
with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as arquivo_csv: 
    # Na primeira linha escreva os títulos da planilha separados por vírgula (sem espaço em branco). Os títulos são: "Título", "Autor", "Ano de publicação" e "Número de páginas". Lembre de finalizar a linha com uma quebra de linha.
    arquivo_csv.write("Título,Autor,Ano de publicação,Número de páginas\n")
    # A partir da segunda linha escreva as informações de cada livro que você levantou, separando cada informação por uma vírgula (sem espaço em branco). Lembre de finalizar cada linha com uma quebra de linha.
    for livro in livros:
        linha = f"{livro['Título']},{livro['Autor']},{livro['Ano de publicação']},{livro['Número de páginas']}\n"
        arquivo_csv.write(linha)
    print(f'Arquivo {nome_arquivo} criado com sucesso!')


