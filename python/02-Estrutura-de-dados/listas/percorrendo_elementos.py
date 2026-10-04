# PERCORRENDO LISTAS

'''A forma mais comum de percorrer os elementos em uma lista é com o loop "for elemento in lista"'''

lista = list(range(10,70,10))

                        
for numero in lista:    # cada elemento da lista será armazenado numa variável "temporária" e será imprimido cada vez q o loop rodar 
    print(numero)     


'''Utilizando a função enumerate() podemos recuperar o valor, mas também o índice referente aquele valor na lista'''

lista = 'Leandro João Carlos Luana Katia'.split()  # ['Leandro', 'João', 'Carlos', 'Luana', 'Katia']

for indice,valor in enumerate(lista): # cria duas variaveis "temporarias" para armazenar os valores dos índices e dos valores
    print(f'índice:{indice}, valor:{valor}')


'''Uma outa forma também é utilizando o loop While, geralmente esse método é quando não temos um valor fixo de elementos na lista
ou seja, quando não sabemos quantos itens vamos consultar, dessa forma o loop só para qnd a condição se torna falsa
'''
numeros = list(range(1,11)) # lista de 1 a 10
quantidade = 0 # variavel global que será verificada e alterada durante o looping
# -> é mais comum se utilizar a referência  "i",  i=0
while quantidade < len(numeros): 
    print(f'índice {quantidade}: {numeros[quantidade]}')
    quantidade +=1 

'''A principio a quantidade inicia em zero que será a varíavel que será verificada e tabalhar em cima da condição, sendo:
    "Enquanto 'quantidade" for menor que o numero de elementos da lista" imprima cada valor da lista correspondente ao índice
    que está sendo representando com o próprio valor 'quantidade' logo ele começa por zero, o primiero índice será 0,
    dps que imprimir será atribuido +1 ao valor da quantidade, logo o proximo indice será o 1, e assim por diante até que
    a condição se torne falsa (quantiade não ser menor q qntd de elementos)
'''

