'''Em Python, uma variável delcarada fora da unção ou num escopo global é conhecida como variável global.
Isso significa que uma variável global pode ser acessada dentro ou fora de uma função:'''

x = 'global'

def imprimir():
    print (f"{x} na função imprimir()")

imprimir()

print (f"{x} fora da função")

'''Se desejarmos alterar o valox de x dentro de uma função devemos usar palavra-chave "global", caso contrário resultado em erro

'''

# errado :
'''
x =  3 
def add():
    x = x + 5
    print(x)

add() '''

#correto:

x = 5
def add():
    global x
    x = x + 5
    print(x)

add()