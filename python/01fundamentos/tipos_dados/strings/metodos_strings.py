# manipulando strings com métodos (funções especiais)



nome = " Meu nome é Leandro Marc "

print(len(nome)) # 25 retorna o comprimento da string

print(len(nome.strip())) # 23 -> remove os espaços extras nas extremidas da string para

print(nome.lower()) # meu nome é leandro marc

print(nome.upper()) # MEU NOME É LEANDRO MARC

print(nome.swapcase()) #mEU NOME É lEANDRO mARC -> inverte maiuscula para minuscula e vice-versa

print(nome.title()) # Meu Nome É Leandro Marc -> primeira letra de cada palavra se torna Uppercase

print(nome.replace("Marc","MARC")) # Meu nome é Leandro MARC -> substitiu a string que desejamos por outra q especificarmos
                                   # primeiro argumento qual string a ser substituida
                                   # segundo argumento, o que será colocado

print (nome.split(" ")) # separa a string em sbstrings caso haja um separador
#['', 'Meu', 'nome', 'é', 'Leandro', 'Marc', '']
'''
lista = nome.split(" ")
print(lista[1])*
'''

# método JOIN
print ("join():")
esportes = ['Futebol','Tênis','Vôlei','Automobilismo','Basquete']

print(', '.join(esportes)) # Futebol, Tênis, Vôlei, Automobilismo, Basquete
# o método join() retorna a string que resulta da concatenação dos objetos em um iterável separados por delimitador. O delimitador é o primeiro argumento .
print(' - '.join(esportes)) # Futebol - Tênis - Vôlei - Automobilismo - Basquete
print('-'.join('abcdefghi')) # a-b-c-d-e-f-g-h-i


print(list('abcdefghi')) # ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'] transforma em uma lista

#método count() -> retorna o núermo de ocorrências não sobrepostas da substring informada
print("count:")
print ("BANANANANA".count("ANA")) #2 


# métodos startwith() e endswith() retorna valores booleanos, caso uma string determinada inicia ou termina com um prefixo especificado
print ("startwith:")
print("Python".startswith("Py")) #true
print("Python".startswith("thon")) #false 
print("Python".startswith("py")) #false (é case sensitive)

print ("endswith:")
print("Desenvolvimento".endswith("mento")) #true
print("Desenvolvimento".endswith("desen")) #false


# find() -> pode ser usado para vermos se uma string conté uma sbstring informada e retornar o menor índice na string onde esta substring é encontrada:
print ("find:")
print('Bom dia, hoje está um dia chuvoso'.find('dia')) #4
print('Bom dia, hoje está um dia chuvoso'.find('om')) #1

# isalnum() -> retorna True e a string for não-vazia E todos os seus caracateres forem alfanuméricos(ou uma letra ou um numero), caso contrario, retorna false
print ("ISALNUM:")
print('abc123'.isalnum()) #true
print('a@bc'.isalnum()) #false
print(' '.isalnum()) #false

#isalpha() -> retorna True se a string for não-vazia e tds os caracteres forem alfabéticos(letras), caso contrário, retorna False

print ("ISALPHA:")
print('abcd'.isalpha()) # true
print('abc 123'.isalpha()) # false

# isditig() -> verifica se possui apenas dítigos(números) e é não-vazia

print ("ISDIGIT:")

print('10'.isdigit()) #true
print('10z'.isdigit()) #false

# isidentifier() -> retorna True se uma determina sring é um identificador(nome símbolico dado para referenciar objeto(variavel)) válido de acordo
# com a definição da linguagem Python, caso contrário, retorna False

print("Isidentifier:")
print ('nome'.isidentifier()) # true              '------------------------------------------'
print('nome2'.isidentifier()) # true              '                                          '
print('2nome'.isidentifier()) # false             ' dessa forma podemos saber como definir   '
print('nome#'.isidentifier()) # false             '           uma variável corretamente      '
print('nomeComposto'.isidentifier()) # true       '                                          '
print('nome_Composto'.isidentifier()) # true      '------------------------------------------'

# iskeyword() -> método que é capaz de testar se uma determinada string corresponde à uma palavra-chave do Pyhton, para utilizá-lo devemos importar, 
# este método é contido no módulo keyword, sendo então necessário importá-lo

from keyword import iskeyword


print("iskeyword:")
print(iskeyword('or'))      #true
print(iskeyword('if'))      #true 
print(iskeyword('else'))    #true
print(iskeyword('for'))     #true
print(iskeyword('switch'))  #false
print(iskeyword('const'))   #false


# método isprintable()
'''
O método isprintable() determina se uma string consiste inteiramente de caracteres imprimíveis. 
Ele retorna True se a string for vazia ou se todos os caracteres alfabéticos que ela conter forem imprimíveis, 
retorna False se ela conter pelo menos um caracter não-imprimível. Caracteres não-alfabéticos são ignorados.
'''

print("isprintable:")

print('Leandro\nMarc'.isprintable()) # false
print('Leandro Marc'.isprintable()) # true
print(''.isprintable()) # true
print('x\na'.isprintable()) # false


# insspace() -> determina se uma string consiste de caracteres de espaço em brano, retornará True se a string for não-vazia E tds os caracteres forem de espaço em branco 
# caso contrário retorna FALSE

print("isspace:")
print(''.isspace())  #false
print ('x'.isspace())  #false
print (' '.isspace())  #true
print ('\t\n'.isspace()) #true

# isupper() -> verifica se todos os caracteres de uma string são uppercase

print("isupper:")
print('STRING'.isupper()) #true
print('String'.isupper()) #false

#islower() -> verifica se todos os caracteres de uma sintr são lowercase

print("islower:")
print('string'.islower()) # true
print('strinG'.islower()) # false

