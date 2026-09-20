# Função de Pesquisa Binária

'''
Esta função pega um array ordenado e um item. Se o item está no array, a função retorna a sua posição. Dessa maneira, é capaz de saber por qual
ponto do array deve continuar procurando.
'''
def pesquisa_binaria(lista,item):
    baixo = 0 # primeiro item(índice)da lista

    alto = len(lista) -1 # último item(índice) da lista
    ''' pelo fator da contagem dos itens de um array começar por 0, logo o valor mais alto deve ser o tamanho da lista -1.
    Exemplo, se uma lista possui 20 itens, a recuperação dos valores seriam dadas através
    dos índices 0 a 19, logo a posição(índice) 20 não existe, que resultaria em erro.
    '''

    while baixo <= alto: # enquanto não chegar a um único elemento (sobrar só um item na lista e ainda nn foi encontrado o item desejado)
        meio = (baixo+alto) // 2 # soma a quantidade de elementos e divide por dois, o mesmo que do exemplo teórico, começar pela metade
        chute = lista[meio] # a metade se torna o chute
        if chute == item: # se o chute("número falado") for igual ao item procurado(número escolhido)
            return meio # acertou
        if chute > item: # caso o número falado for maior que o número escolhido 
            alto = meio -1 # "dizer muito alto", logo o novo valor mais alto passa ser o valor chutado menos 1, exemplo chute foi 50, o alto passa ser 49
        else:
            baixo = meio +1 # "dizer muito baixo", logo os elementos anteriores são descartados e começa contar do próximo, exemplo chute goi 50, próximos elementos válidos serão de 51 a 75
    return None # se lista for percorrida completamente e não for encontrado, o elemento nn pertence a lista


minha_lista = [1,3,5,7,9]

print (pesquisa_binaria(minha_lista,3)) # lista contendo valores, e o valor a ser procurado
print (pesquisa_binaria(minha_lista,-1))


# LINHA 17 =  uso da duas barras pois o resultao de uma divisão é um número float, dessa forma se torna inteiro