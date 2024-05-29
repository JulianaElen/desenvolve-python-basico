horas_trabalhadas = [40, 37, 45, 40, 40, 48]
pagamentos = [20*min(n, 40) + 25*max(0, n-40) for n in horas_trabalhadas] 

print(pagamentos)