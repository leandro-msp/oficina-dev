# existem 3 tipos núermos em Python
#   int -> inteiro
#   float -> flutuante (número com casas decimais)    
#   complex

'''Td em Python é um objeto, sendo assim, tipos de dados são clases e variáveis são instâncias(objetos) dessas classes'''

a = 10 # tipo int
b = 10.5  # float
c = 5j # complex

print(type(a))
print(type(b))
print(type(c))

# INT 
'''São números inteiros positivos, negativos, que nn apresentam casas decimais, seu tamanhp é limitado apenas pela capacidade de memória disponível'''

e = 5
f = 1239873487812
g = -8

print('Inteiros: ')
print(type(e))
print(type(f))
print(type(g))

#FLOAT  
'''são números de ponto flutuante, são positivos ou negativos que podem conter uma ou mais casas decimais'''

h = 10.2
i = 2.0
j = -15.23

print('Float: ')
print(type(h))
print(type(i))
print(type(j))

'''
Podemos acrescentar o caracter e ou E seguido por um número inteiro positivo ou negativo para especificar a notação científica.
'''
# notação científica
e = 35e4
print(type(e)) # <class 'float'>
print(e) # 350000.0
E = 3.8e-2
print(type(E)) # <class 'float'>
print(E) # 0.038

#Complex

'''Número complexos são escritos com j representando a parte imaginária.
Eles podem se escritos complex(3,4) ou 3,4j. Um numero complexo 'c' é armzaenado internamente usando coordenadas Cartesianas ou Retangulares'''

a = 2+4j
b = -3j
c = complex(3,4)

print('Complex: ')
print(type(a))
print(type(b))
print(type(c))


# CONVERSÃO DE TIPOS NUMÉRICOS
print("\n")
k = 5
i = 8.6
z = 5j


print ("Conversão de Números")
print(type(k))
print(type(i))
print(type(z))

print(float(k))
print(int(i))
print(complex(k))

#NÚMEROS ALEATÓRIOS
'''
Embora Python não tenha uma função random() para gerar um número aleatório, existe um módulo construído em Python chamado random que nos permite criar números aleatórios:
'''

import random

print (random.randrange(1,10)) #função gera números entre 1 e 9

numero_aleatorio = random.randint(1,50) # gera um número inteiro entre 1 e 10

print(numero_aleatorio)


