print ("Olá Mundo") # print -> saída/impressão

#Palvras Chaves

import keyword 
print(keyword.kwlist) # lista de palavras chaves

'''
Identificadores: Os identificadores são nomes dados às entidades como variáveis,funções,classes, etc, eles nos ajudam a diferenciar uma entidade da outra

Regras: podem ser escritos combinando letras lowercase,(a-z) ou uppercase (A-Z) ou dígitos (0-9) ou unerline(_).
    ex.: minhaClasse, variavel_1 e minha_variavel.

    são case sensitive (idade,Idade e IDADE são três variáveis diferentes). Não podem começar com digitos, "13variavel" por exemplo, porém variavel13 é aceito.

    palavras chaves jamais podem ser usadas como identificadores. (ex.: if, else, def, true)
'''

'''Identação:
No Python a identação não é utilizada como questão de legibilidade, mas sim é um ponto importantíssimo, ela indica blocos de códigos:
'''

hp = 100

if hp> 0:
    print ("Saúde Máxima")

'''Statements:
As instruções em Python geralmente terminam com uma nova linha, entretanto a linguagem permite o uso do caractere de continuação de linha (\ - contra-barra) para indicar
que a linha deve continuar:
'''

valor = 10 +\
    8 + \
    8

print(valor)

'''Ponto e vírgula (;) permite várias instruções em uma única linha, visto que nenhuma instrução inicia um novo bloco de código:'''

a,b = 10,2 ; c = a * b ; print (f"{a} x {b} = {c}")


