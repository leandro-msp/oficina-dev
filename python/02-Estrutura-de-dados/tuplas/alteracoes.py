'''
Tuplas possuem a características de Imutável, ou seja, significa que as posições sempre apontam para os mesmos objetos. Qualquer tentativa de trocar, adicionar ou remover gera erro:
'''

marcas = ("Nike","Adidas","Pulman")

'''
marcas[0] = "Gucci" <<<- gera erro ->>> TypeError: 'tuple' object does not support item assignment
marcas.append("Gucci") <<<-- gera erro ->>> AttributeError: 'tuple' object has no attribute 'append' | este atributo nn existe para tupals
'''

# para add valores, cria-se nova tupla

marcas = marcas +("Gucci",) # concatena e reatribui

print(marcas)

# remover valor

temporaria = list(marcas) # converte para lista
temporaria.remove("Pulman") # remove o valor
marcas = tuple(temporaria) # volta a ser tupla
print(marcas)

# Obs.: Se há a troca frequente de tupla pra lista e volta a ser tupla, certamente a estrutura a ser usada é a própria lista.

# IMUTABILIDADE É RASA

''' Pegadinha da lista dentro da tupla:
Em uma tupla a posição sempre aponta para o mesmo objeto, mas isso nn impede que esse objeto, se for mutável, seja alterador por dentro
'''

registro = ("São Paulo",['Zona Sul','Capital'])
registro[1].append('Interior')  #altera a lista, e não a tupla

print(registro)