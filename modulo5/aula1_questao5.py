#Reconhece emojis

import emoji

emojis_disponiveis = [':rosto_confuso:', ':coração_rosa:', ':foguete:', ':sol:', ':pizza:', ':polegar_para_cima:', ':fogo:', ':sino:', ':osso:', ':rosto_preocupado:']

print("Emojis disponíveis:")
for i in emojis_disponiveis:
    print(emoji.emojize(i, language='pt'), ' -', i)

frase = input("\nDigite uma frase e ela será emojizada:")
print("Frase emojizada:")
print(emoji.emojize(frase, language='pt'))
