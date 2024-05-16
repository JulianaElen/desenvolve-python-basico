# Mostra a data e hora atuais

from datetime import  datetime

data = datetime.now()

print(data.strftime("Data: %d/%m/%Y \nHora: %H:%M"))
