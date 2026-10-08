'''
Exercício 2 

(questão de prova). Pensando na manipulação de listas, observe os comandos da coluna A e associe-os às funções da coluna B.

Coluna A	Coluna B
1. append()	(4) Remove e retorna o elemento de uma posição (por padrão, o último).
2. remove()	(1) Adiciona um elemento ao final da lista.
3. insert()	(2) Remove a primeira ocorrência de um valor da lista.
4. pop()	(3) Insere um elemento em uma posição específica da lista.
Assinale a alternativa que apresenta a sequência correta da coluna B, de cima para baixo:
'''

lista = 'a b c '.split()

lista.append('d')       # add elemento no final
lista.insert(1,'X')     # insere elemento na posição específica
lista.remove('b')       # remove o valor(primeira ocorrência) 'b'
item = lista.pop()              # remove e retorna o valor(neste caso o último)

print(f'{lista} \n{item}')

