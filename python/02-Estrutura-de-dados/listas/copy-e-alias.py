# Cópia x Referência (Alias)

''' Atribuir uma lista a outra variável não a copia, mas sim cria um 'alias'. 
    os dois nomes apontam para o mesmo objeto na memória, logo, uma alteração em uma, afeta diretamente o outro
    lista2 = lista1
'''

lista1 = [1,2,3]
lista2 = lista1 # alias -> é o mesmo objeto, NÃO uma cópia

lista2.append(4)

print(f'Lista 1:{lista1}') # [1, 2, 3, 4]
print(f'Lista 2:{lista2}') # [1, 2, 3, 4]

print ("Ambas as listas são o mesmo objeto? -> ", lista1 is lista2) # confrima que o mesmo objeto

# Para se obter uma cópia independente (rasa) , há os métodos .copy(), list(nome_lista) ou o próprio Slicing, lista [:]

lista3 = list(range(1,6))
print (f'Lista 3: {lista3}')

copia =  lista3.copy()
copia.append(6)
print(f"Cópia: {copia}")

# ou 

copia2 = list(copia)
copia2.append(7)
print(f"Cópia 2: {copia2}")

# ou

copia3 = copia2[:] # vai seguir o padão, do primeiro elemento, ao último elemento
copia3.append(8)
print(f"Cópia 3: {copia3}")

print ("Lista 3 e Cópia, tratam-se do Mesmo Objeto? -> ", lista3 is copia)

# CÓPIA DE LISTAS ANINHADAS

''' Uma cópia rasa cria uma cópia somente do nível externo, as sublistas conitnuam compartilhadas, ou seja ocorre o mesmo quando duas variaveia apontaram para mesmo objeto.
    para um cópia totalmente independente utiliza-se copy.deepcopy()
'''

import copy

original = [[1, 2], [3, 4]]

rasa = original.copy()        # cópia rasa: sublistas compartilhadas
rasa[0].append(99)
print('apos copy() rasa:', original) # [[1, 2, 99], [3, 4]] -> copia original também é agetada

original = [[1, 2], [3, 4]]
profunda = copy.deepcopy(original)   # cópia profunda: tudo independente
profunda[0].append(99)
print('apos deepcopy():', original) # [[1, 2], [3, 4]] -
