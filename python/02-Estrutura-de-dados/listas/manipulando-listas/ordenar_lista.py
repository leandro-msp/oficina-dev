# lista.sort()  -> altera a própria lista
#               -> Retornar None
#               -> só funciona com listas              

# sorted(lista) -> Não altera a lista original
#               -> Retorna uma nova lista ordenada
#               -> funciona com qualquer iterável: lista, tupla, string, dicionário

'''Ambas aceitam Reverse=True (ordem decresente) e key(critério de ordenação)'''

numbers = [7,4,9,0,3,1]

#sorted(lista) 

ordenada = sorted(numbers)          # nova lista
print(ordenada)                     # [0, 1, 3, 4, 7, 9]
print(numbers)                      # [7, 4, 9, 0, 3, 1] <- manteve a original

ordenada2 = sorted(numbers,reverse=True) # [9, 7, 4, 3, 1, 0] <- nova lista em ordem decrescente
print(ordenada2)


numbers.sort(reverse=True) # decrescente 
print(numbers) # [9, 7, 4, 3, 1, 0]

nomes = 'Mateus Lucas Teo Natalia Rute'.split()
nomes.sort(key=len) # ordendar pelo tamanho do nome -> len conta a qtdd de caracteres de cada elemento

print (nomes)  # ['Teo', 'Rute', 'Lucas', 'Mateus', 'Natalia']

