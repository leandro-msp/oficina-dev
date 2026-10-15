nome, idade, cidade = ("Leandro", 26, "Carapicuíba") # cada variável recebe um valor presente dentro da tupla, seguindo a mesma sequência da posição dos valores

print(nome, idade,  cidade)

a, b = 5, 10
print(a,b )

a, b = b , a # faz a troca sem a necessiade uma variável auxiliar
print(a, b)


''' Em muitas linguagens de programação, se você fizer a = b diretamente, o valor original de a é perdido. 
Por isso, usa-se uma variável temporária (geralmente chamada de temp ou aux):
exemplo:   '''

# uso da variável temporária em outras linguagens ( no python nn é necessário,)
d =  20
e = 30
print(f"d={d}")
print(f"e={e}")

aux = d # temporária -> salva o valor de 'd' na variável auxiliar
d = e   # 'd' recebe o valor de 'e'
e = aux   # 'e' recebe o valor que estava salvo em 'aux'

print(f"d={d}")
print(f"e={e}")

nome, _, cidade = ("Leandro", 26, "Carapicuíba") # _ = valor que não interessa
print(nome,cidade)

'''Quando o número de itens varia, utiliza-se o asterisco para capturar "o resto" '''


primeiro, *resto = (10,20,30,40) # 'primeiro' recebe o primeiro valor da dupla, os demais valores são salvos na variável resto
print(primeiro,resto) # 10 [20, 30, 40]

*inicio, ultimo = (10,20,30,40) # processo inverso
(print(inicio, ultimo)) # [10, 20, 30] 40

start, *middle, end = (1,2,3,4,5)
print (start, middle, end) # 1 [2, 3, 4] 5

x, *limbo = (5,)
print(x, limbo) # 5 []

'''Obs.: A variável com * recebe sempre uma lista(mesmo que seja vazia), e só pode haver um asterisco por atribuição'''

