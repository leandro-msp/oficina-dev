'''Ao utilizar os índices e o nome da tupla, o usuário necessariamente precisa saber/lembrar o que é cada posição. Com o módulo collections, podemos utilizar
o 'namedtuple', que dá nomes aos campos
'''

from collections import namedtuple

pontos = namedtuple ("Coordenadas",["x","y"])

coordenadas = pontos(5,10)

print(coordenadas)

print(coordenadas.x, coordenadas.y) # resgatando por nome

print(coordenadas[0],coordenadas[1]) # resgatando por índice


#  unpacking

a,b = coordenadas

print(a+b)

coordenadas2 = coordenadas._replace(x=20)  # alterando valor criando uma nova tupla
print(coordenadas2, coordenadas)

print(coordenadas2._asdict()) # imprime como dicionário, transformando campos em chaves

