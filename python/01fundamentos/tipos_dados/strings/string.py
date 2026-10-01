# Tipo String

'''Uma string é tradicionalmente um tipo de dados que representa uma sequência de caracteres.
Caracateres podem ser letras, dígitos, símbolos ($, !, #, @), etc.

Computadores originalmente nn lidam com cacteres, mas com números(binários). Mesmo que vejamos caracteres em nossa tela, internamente ele são
armazenados e manipulados como uma combinação de 0's e 1's.

a conversão de caracteres en números é chamada de codificação e o processo reverso é decodificação

ASCII e Unicode , são algumas das codificações polulares usadas. Em Python a string é uma sequência de caracteres Unicode. Unicode foi introduzido
para incluir todos os caracateres em todos os idiomas e trazer uniformidade na codificação.
'''

# ASCII | Unicode

# função ord()
print(
ord('A'), # 65
ord('X'), # 88
ord('<')  # 60
)

# função chr() -> faz o processo inverso do ord(). Ao fornecer valor numérico ele retorna uma string representando este valor
print(
chr(65),
chr(88),
chr(60)
)

''' as strings podem ser expressas de diveras maneiras, podemos encapsular elas com aspas simples ('texto'), aspas duplas("texto") ou múltiplas("""texto""")

na função print, um string já caracterizada por aspas, caso queiramos usar palavras  com aspas dentro da string é feito da seguinte forma:
'''

print('usando aspas dentros das \'strings\'') # uso da contabarra
print("usando aspas dentros das \"strings\"") # uso da contabarra

# ou inventer os tipos

print ('usando aspas dentro das "strings"')
print ("usando aspas dentro das 'strings'")

# INDICES De Strings

nome = "Leandro"
print(nome[0]) # imprime a primeira letra do nome
print(nome[-7]) # imprime a primeira letra do nome

print(nome[6]) # imprime a última letra do nome
print(nome[-1]) # imprime a última letra do nome

'''
o primeiro caracter começa na posição 0, isso é muito comum nas linguagens de programação e estruturas de dados. 
Cada caracter na string é associado com um índice numérico, que é um inteiro representando a localização do caracter em uma determinada string.
'''

# formando substring a partir de uma string

nome = "Ayrton Senna"

# selecionando o caracter da posição 3 até o 9(nn incluindo 10)

print(nome[3:10]) # ton Sen
print(nome[::-1]) # inverte a string -> anneS ontryA