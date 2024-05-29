urls = ["www.google.com", "www.gmail.com", "www.github.com", "www.reddit.com;", "www.yahoo.com"]
dominios = []

for i in range(len(urls)):
    aux = urls[i]
    aux = aux.replace('www.', '')
    aux = aux.replace('.com', '')
    dominios.append(aux)

print(urls)
print(dominios)