# operadores em strings

'''
+  -> concatenação, adiciona valores
*  -> repetição, concatena múltiplas cópias da mesma string
in -> verifica se determinado caracter existe na string
not in -> verifica se determinado caracter não existe na string
'''

estado = "São Paulo"
pais = "Brasil"

print(estado +" - "+pais) # São Paulo - Brasil
print (pais*5) #BrasilBrasilBrasilBrasilBrasil
print('P' in estado) # True
print ('B' not in pais) # False