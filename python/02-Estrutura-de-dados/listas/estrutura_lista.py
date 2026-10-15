# Listas é uma coleção ordenada e mutável de itens, elas permite guardar múltiplos valores dentro de uma única variável

# exemplo
frutas = ['Maçã','Banana','Uva'] # a ordem padrão é a no qual foi criada, sendo possível alterar utilizando métodos

print (frutas) # ['Maçã','Banana','Uva']
print (type(frutas)) # <class 'list'>

# CRIAÇÃO DE LISTAS

#lista com apensum elemento
lista1 = ["Caderno"]

# lista vazia
lista2 = []

# múltiplos itens
lista3 = ['Python','Programação',2026]

# utilizando função range()
lista4 = list(range(10)) # lista de 0 a 9  -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(lista4)

# repetindo valor
zeros = [0] *5
print(zeros) # [0, 0, 0, 0, 0]

# com quebra de string
palavras ='Python é uma linguagem de programação'.split()
print(palavras) # ['Python', 'é', 'uma', 'linguagem', 'de', 'programação']
print(type(palavras)) # <class 'list'>
palavras.append("teste")
print(palavras)


# ACESSANDO DADOS DA LISTA

'''Todos os itens da umalista são indexados, ou seja para ca item da lista um índice é atribuído da seguinte forma:
    lista[indice], sendo que começa em 0 (zero)
'''
#          0       1       2       3
nomes = ['João','Marcos','Silva','Maria']

#recuperando valor Marcos:

print(nomes[1])

''' O primeiro índice é 0, o último válido sempre será o tamanho da lista menos um -> len(lista) -1.
    exemplo desta lista, são 4 nomes, os índices vão de 0 a 3, logo nomes[4] gera o erro IndexError -> tentar acessar valores de um índex fora de intervalo
'''

#INDEXAÇÃO NEGATIVA

'''Indexação negatica significa começar do fim'''

# -1 se refere ao último item

#          -4      -3      -2      -1
nomes = ['João','Marcos','Silva','Maria']

print(nomes[-1]) # Maria
print(nomes[-4]) # João -> primeiro item

# Sublistas ( Lista dentro de Lista)

lista5 = ['Mateus',['Júlia','Kauan','Letícia'],'Marcos']

# como acessar o valor Letícia
sublista = lista5[1] # recupera o índice um que é a sublista
print(sublista[2]) # Leticia

# método direto

print(lista5[1][2]) # Leticia
