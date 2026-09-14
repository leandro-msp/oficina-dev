#OPERADORES ARITMÉTICOS
print ("Operadores Aritiméticos: ")

#unários: 
unário = 25
unário2 = -unário
print("Unário:",unário2) 


#binários:
a = 10
b = 20
c = 30 
d = 40
e = 2

soma = a + b  # 10+20 = 30
subtração = d - c # 40-30 = 10
multiplicação = a * b # 10*20 = 200
divisão = d / a  # 40/10 =  4
resto = b % e # resto da divisão de 20/2 = 0
print ("Soma: ",soma)
print ("Subtração: ",subtração)
print ("Multiplicação: ",multiplicação)
print ("Divisão: ",int(divisão)) # transformando resultado em número inteiro
print ("Resto: ",resto)


#OPERADORES RELACIONAIS:
print ("Operadores Relacionais: ")

f = "10"

igual = (a == f) # == --> confere se os valores e tipos são iguais | a=10, porém f="10", A é tipo inteiro e F tipo String
maiorQue = b > a # b(20) é maior que a(10) ? True
menorQue = c < d # c(30) é menor que d(40) ? True
maiorIgual = (b + c) >= d # a soma de b(20) + c(30) --> 50 é manior ou igual a d(40) ? True
menorIgual = a <= e # a(10) menor ou igual a e(2) ? False
diferenteDe = b != a+a #b(20) é diferente de a(10) + a(10) ? False

print (igual)
print (maiorQue)
print (menorQue)
print (maiorIgual)
print (menorIgual)
print (diferenteDe)


# OPERADORES LÓGICOS
print ("Operadores Lógicos: ")

opNot = not(a<b) # inverte o resultado a operação True para False, e False para True
        # 10 é menor que 20 ? True , passar a ser False. | Seria o mesmo que afirmar "10 não é menor que 20", que é uma afirmação falsa

opAnd = (a<b and d>c) # AND = Ambas comparações ou condições devem ser verdadeiras para que retorne o valor True
# 10 é menor que 20 ? True, E 40 é maior que 30? True  --> logo resultado da operação é True

opOr = (c<d or a>b) # Basta uma comparação/condição ser verdadeira que já atende.
# 30 é menor que 40? True | ou 10 é maior que 20? False | porém uma já foi atendida

print("Operador Not:",opNot)
print("Operador And:",opAnd)
print("Operador Or:",opOr)


# código do APPA
print ("CÓDIGOS DO APPA: ")

x = 100
y = 300
z = 500
w = 200
 
k = x+y+z # 100+300+500 = 900

print("k=",k)

k = z+w/x #500+200/100 --> como não estão parênteses, a operação segue a ordem de prioridade, primeiro a divisão depois a soma
                # 200/100 =  2   ---> 500+2 = 502
print("Novo valor de k=",int(k))

#Operação direto no Print
print(z>w) 
print(w>z)
print(y+w==z)
print(z>w and w>y)
print(z>w or w>y)
print(not y+w==z)


