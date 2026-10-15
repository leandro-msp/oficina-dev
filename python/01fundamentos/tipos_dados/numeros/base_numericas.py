'''Normalmente escrevemos inteiros na base 10. No entando, Python nos permite escrever interios nos formatos:
Hexadecimal (base16) , Octal (base 8) e Binário (base 2)

Isso pode ser feito adicionando prefixos ao número inteiro:

0b ou 0B = Binário
0o ou 0O = Octal
0x ou 0X
'''

print (0b1000) # 8
print (0o10)   # 8
print (0x8)    # 8

#Métdo bin()
'''Converte e retorna a string binária equivalente de um determinado inteiro'''

print(bin(12345))

a = 255
print(a)

print(bin(a)) # '0b11111111'

#converter de volara para inteiro, usa-se função int e passa a base 2 como argumento
int('0b11111111',2)


#MÉTODO OCT()
'converte e retorna a strinf octal equivalente de um determinado numero inteiro'

oct(8) #'0o10'

#conversão

int('0o10',8) #8

#MÉTODO HEX()
'Converte e retorna a strinf hexadecima equivalente de um determinado inteiro'

hex(255) #'0xff'

#conversão

int('0xff',16) # 255

