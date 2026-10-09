'''Exercício 7. Remova os itens repetidos de ['python', 'java', 'python', 'go', 'java'], mantendo a ordem da primeira aparição. '''

linguagens = 'python java python go java'.split()
print(linguagens)
unicas = []

for item in linguagens:
    if item not in unicas: 
        unicas.append(item)
    # caso item ainda não esteja presente na lista "unicas", ele será adicionado

print(unicas)