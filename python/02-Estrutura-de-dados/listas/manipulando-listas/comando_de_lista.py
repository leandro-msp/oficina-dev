''' As listas têm métodos próprios para adicionar, remover, buscar e reordenar elementos.
    Metodos retornam valores e podem ou não alterar a lista original
'''


l = 'a b c'.split() #['a', 'b', 'c']

# append(x) -> Add valor ao final da lista, retorna None, e altera a lista original 
l.append('d') #  ['a', 'b', 'c', 'd']

# extend(iteravel) -> Add cada item de outor iterável no final , Retorna None, e altera a lista original
l.extend(['e','f']) # ['a', 'b', 'c', 'd', 'e', 'f']

# insert(i,x) -> insere x na posição i, empurrando os itens seguintes para direita, retorna None, e altera a lista original
l.insert(0,'A') # ['A','a', 'b', 'c', 'd', 'e', 'f']

# remove(x) - > remove a primeira ocorrência do valor x (ValueError se não existir), retorna None, e altera a lista original
l.remove('b') # ['A','a', 'c', 'd', 'e', 'f']

# pop(i) -> remove o item do índice 'i' e devolve esse item; sem argumento, remove e devolve o último , retorna o item removido, altera a lista orginal
sem_argumento = l.pop() # f < - s/argumento remove ultimo item
print(sem_argumento) 

com_argumento = l.pop(0) # A <- c/argumento remove o item do índice informado
print(com_argumento)

# index() procura a posição da primeira ocorrência 'x' (ValueErro se o mesmo não existir), Retorna valor Inteiro, não altera a lista 
posicao = l.index('c') # 1
print(posicao)

# count() Conta quantas vezes o elemento informado aparece na llista , retorna Número inteiro, não altera a lista original
quantidade = l.count('b') # 0
print (quantidade) 

# sort() Ordena a lista (aceita 'key' e reverse), retorna None, e altera a lista original
num =[5,8,3,7,4,2]
num.sort() # [2, 3, 4, 5, 7, 8] <- altera diramente na lista original
print(num)

# reverse() inverte a ordem , retorna none, e altera a lista original
lista = 'a b c' .split() # ['a','b','c']
lista.reverse() # ['c', 'b', 'a']






