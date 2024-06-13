meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

data = input("Digite a sua data de nascimento no formato dd/mm/aaaa: ")

mes = int(data[3:5])-1

print(f"Você nasceu em {data[:2]} de {meses[mes]} de {data[6:]}.")