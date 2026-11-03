# criando um conjunto de dados

meu_set = {1,2,3,4,4,4,5}
print(meu_set) # {1, 2, 3, 4, 5} -> duplicatas sumiram

# criando set(conjunto) vazio

set_vazioErrado = {} # método errado -> cria um dicionário vazio

set_vazio = set() # método correto

print(set_vazio)


'''O uso prático mais comum de um Set na programação rotineira é a eliminação instantânea de duplicatas em uma lista'''

emails_recebidos = ["ana@gmail.com", "joao@gmail.com", "ana@gmail.com"]

# Converte para Set (limpa duplicatas) e volta para Lista

emails_unicos = list(set(emails_recebidos))
print(emails_unicos)