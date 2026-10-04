# COMO REMOVER UM ITEM DE UMA LISTA

'''Há quatro formas de remover itens, e a escolha depende do que temos em mãos(valor ou posição(indice)) e se o item removido será utilizado'''

lista = 'vermelho azul verde branco preto'.split()
print(lista) # ['vermelho', 'azul', 'verde', 'branco', 'preto']

#remover pelo valor
lista.remove('azul')
print(lista) # ['vermelho', 'verde', 'branco', 'preto']

# remover pelo índice e usar o item
primeira_cor = lista.pop(0)
print(primeira_cor) # vermelho

# remover pelo índice(ou fatia)
del lista[1]
print (lista) # ['verde', 'preto']

# esvaziar a lista inteira 
carrinho = 'tênis blusa meia óculos'.split()
print(carrinho)
carrinho.clear()
print('Carrinho: ',carrinho)