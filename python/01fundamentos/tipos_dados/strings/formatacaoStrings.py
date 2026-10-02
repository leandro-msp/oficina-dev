# método center() -> retorna uma strinf centralizada em um determinado comprimeiro especificado por nós via argumento
# por padr~doa, o preenchimento consiste no cactere de espaço ASCII

print('python'.center(20)) # '       python       '
print('python'.center(20,'.')) # '..........python.........'

# método expandtabs() -> substituiu cada cacter tab (\t)com espaços

print ("expandtabs: ")     
print('a\tb'.expandtabs()) # 'a       b'

# método ljust() ->
'''O método ljust() retorna uma string justificada à esquerda em um campo de comprimento especifica por nós via argumento, 
por padrão, o preenchimento consiste no caractere de espaço ASCII'''

print ("ljust: ")    
print('C++'.ljust(10)) # 'C++       '
print('C++'.ljust(10,'.')) # 'C++........'

# rjust() -> inverso o ljust

print ("rjust: ") 
print('JavaScript'.rjust(20)) # '          Javascript'
print('JavaScript'.rjust(20,'-')) # '----------Javascript'

print ("zfill: ") 
# método zfill() -> retorna uma cópia da sintr com preenchumento à esquerda com caracteres '0' , o comprimento é especificado no argumento
print('10'.zfill(5)) #00010
print ('a'.zfill(5)) #0000a 


# format() -> nos permite construir strings de uma forma mais fexível:
print ("format: ") 
nome = "Luan"
idade = 35
profissao = "Gerente"

print("{0} tem {1} anos de idade, e é {2}".format(nome,idade,profissao)) # Luan tem 35 anos de idade, e é Gerente
# os valores são os índices, e a sequencia de distribuição dentro do format define qual valor vai para qual índice


# CRIANDO ELEMENTO HTML

print("HTML com format:")
tag = 'p'
texto = 'Este é um parágrafo'

elemento = '<{0}>{1}</{0}>'.format(tag,texto)
print(elemento)

# cálculo de valor
print("Calculo de valor")
valor = '1 GB é igual a {:,} bytes'.format(10**9)
print(valor) # 1 GB é igual a 1,000,000,000 bytes

#CÓDIGOS DE FORMATAÇÃO

print("Códigos de Formatação")

# inteiro:
print("inteiro:")
print("{:d}".format(4)) #4 -> base decimal (base10)

#binário
print("binário:")
print("{:b}".format(25)) #11001 -> base binária (base2)

# hexadecimal
print("Hexadecimal:")
print("{:X}".format(15)) #F -> base hexadecimal (base16)

#lista

print("lista:")
print("{:}".format([15,30])) # [15,30]

'Representando Strings de forma similar ao estilo da linguagem C'

print("Similiar Linguagem C:")

# String

print("String:")
nome = "Alan"
amigo = "Jones"
print("%s é amigo de %s" %(nome,amigo)) # Alan é amigo de Jones 

''' s-> signifca string
    Cada %s dentro do texto funciona como um reservatório (ou uma lacuna) esperando para receber um texto.
    O símbolo % posicionado logo após a string serve para conectar o texto aos dados que serão inseridos nele.
    Logo em seguida, os valores são passados dentro de parênteses (nome, amigo) como uma tupla.
    O Python substitui os marcadores exatamente na ordem em que as variáveis aparecem
'''
print("inteiro:")
# Inteiro

print("Inteiro:")
print("%d" %(2020))  # 2020  

#float
print("float:")
print("%3.5f" % (3.123456789)) # 3.12346  | 
print("%2.4f" % (3.123456789)) # 3.1235
''' f -> significa que o valor é um número ponto flutuante (float)
    .5: Instrui o Python a exibir exatamente 5 casas decimais após o ponto. (ocorre arredondamento)
    3: Representa a largura mínima total que o texto deve ter (incluindo o ponto e todas as casas decimais). 
    Como o resultado final 3.12346 já possui 7 caracteres no total (o que é maior que 3), 
    o Python ignora essa largura mínima e exibe o número normalmente.
    caso o tamanho da largura mínima for maior que a quantidade de caracteres, o Python add espaços em branco à esquerda para preencher
    até que o texto complete 10 caracteres.
'''