# VARIÁVEIS 

'''
Variáveis são usadas para armazenar informações a serem referenciadas e manipuladas em um programa de computador. 
Elas também fornecem uma maneira de rotular dados com um nome descritivo, para que nossos programas possam ser entendidos mais claramente pelo leitor e por nós mesmos.

'''

# Atribuindo Valores às Variáveis

'''As variáveis em Python não precisam declaração explícita para reservar espaço em memória, a declaração ocorre automaticamente quando você atribui um valor à variável.'''

nome = "Leandro" 
idade = 26 
altura = 1.80 

print (nome) ; print(idade) ; print(altura)

#ou add multiplos valores para multiplas variaves

a, b, c = 10, 8.5, "Olá"
print(a)
print(b)
print(c)

'''para declarar constantes, usa-se letras totalmente maiúsculas. Já que não existe uma regra propria do motor para criação de constantes, é adotado este "bom senso",
ao ver que o identificador está com letras full uppercase, já se identifica que é um valor q nn pode ser variado.'''

PI = 3.14
GRAVIDADE = 9.8


# TIPOS DE VARIÁVEIS         
''' Em outras linguagens de programação uma variável é inicialmente declarada como tendo um tipo de dado específico, e qualquer valor atribuido a ela durante sua vida útil
deve sempre ter esse tipo. O Python não segue essa restrição, uuma variável pode ser atribuida a um valor de um tipo e , posteriormente, re-atribuida a um a valor de tipo diferente
'''

d = 10
print (d)

d = "fundamentos Python"
print(d)  # passou a ser string

# REFERÊNCIA A OBJETOS
'''Por ser uma linguagem orientada objetos, o Python, sendo assim praticamento todos os itens de dados em programa Python são objetos de um tipo ou classe específica'''

 
# 1-> cria um objeto do tipo inteiro
# 2-> dará o valor 33 
# 3-> aprensenta no console

type(33) # <class 'int'>

''' Uma variável é o nome simbólico que é uma referênci ou ponteiro para um objeto. Uma vez que um objeto é atribuído a uma variavel, podemos nos referir ao objeto com esse nome.
Mas os dados em si ainda estão contidos no objeto.
'''
 
x = 50
# essa atribuição ciria um objeto integer com valor '50' e atribui a variável 'x' para apontar esse objeto

y = x 
# ao executarmos, o python nn cria outro objeto, ele criará um nome simbólico/referencia 'y', no qual aponta para o mesmo objeto que aponta pra 'x'

y = 25

# dessa vez, um novo  objeto integer será criado com valor '25' e 'y' se torna sua referencia

x = 'e'

# o objeto com valor 'e' será criado e fará de 'x' uma referencia a ele

'''INICIALMENTE TINHAMOS:
x = 50
y = x

agora temos:    x = e 
                y = 25

Agora não temos mais referência ao objeto integer '50'. Quando numero de referência a um objeto cai para zero, ele não está mais acessível.
Logo, sua vida acabou. o Python eventualmente perceberá que é incacessível e recuperará a memória alocada para que possa ser usada para outra coisa.
Este processo chama-se : GARBAGE COLLECTION
'''

# IDENTIDADE DOS OBJETOS
'''No Python, todo objeto criado recebe um número que o identifica exclusivamente. 
É garantido que dois objetos não terão o mesmo identificador durante qualquer período em que sua vida útil se sobreponha.'''

# função id() retorna o identificador inteiro de um objeto. Dessa forma podemos verificar se duas variaveis realmente apontam para o mesmo objeto.

k = 100
j = k

print (id(k))
print (id(j))
#ambas apontam mesmo obejto, caso haja alteração no 'j' apontará para outro objeto
j = 70
print (id(j))

# Deletando uma variável

numero = 123
del numero
# ao tentar imprimir com print apontará que o variavel nn foi definida
