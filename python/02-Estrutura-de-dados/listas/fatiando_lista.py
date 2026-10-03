# Fatiando uma Lista (Slicing)

'''Slicing: é a extração de um conjunto de elementos contidos numa lista, sintaxe:

    lista[incio:fim:passo]

    inicio -> se refre ao índice de início do fatiamento
    fim -> se refere ao índice final do fatiamento (a lista final não vai conter esse elemento).
    passo -> parâmetro opcional, e é utilizado para se pular elementos da lista original
'''

lista = list(range(10,70,10)) # [10, 20, 30, 40, 50, 60] -> usando range para criar lista com elementos q começa do 10, vai até 60, com intervalo de 10
print(lista)

print(lista[2:5]) # [30,40,50]

numeros = list(range(1,11))
print(numeros) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numerosFatiados = numeros[1:5] 

print(numerosFatiados) # [ 2, 3, 4, 5]

# Fatiando com índices Negativos

dias_semana = 'segunda terça quarta quinta sexta sábado domingo'.split()
print (dias_semana) # ['segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sábado', 'domingo']

ultimos_tres_dias = dias_semana[-3:] # -3 corresponde ao sábado e -1 domingo
'''nesse caso não precisamos especificar o “fim”, pois queremos todos os elementos até o final da lista.'''

print(ultimos_tres_dias) # ['sexta', 'sábado', 'domingo']


# FATIANDO COM PASSO (step)

'''O passo indica de quantos elementos em quantos elementos queremos selecionar da lista. Se não especificado, o passo é considerado como 1.'''

pares = list(range(0,22,2))
print (pares) # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# fatiar essa lista de forma a obter apenas os números pares em posições ímpares

pares_fatiados = pares[1::2]
print(pares_fatiados) # [2, 6, 10, 14, 18]

''' utilizamos o 1 como valor do início para pular o primeiro elemento.
    O 2 como passo, para selecionar apenas os elementos de posição ímpar e o omitimos o fim, 
    para incluir todos os elementos até o final da lista.'''


# FATIANDO STRINGS

mensagem = 'Olá, Mundo!'

fatiar_mensagem = mensagem[5:10] # Mundo
print(fatiar_mensagem)

'''o método nn funciona somente em listas, pode ser aplicado tbm em strings, onde cada caractere é tratado como um "índice" elemento '''

