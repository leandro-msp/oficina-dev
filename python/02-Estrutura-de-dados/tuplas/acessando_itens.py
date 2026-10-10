estados = "BA","SP","RJ","MG","RS"

# print(type(estados))

print(estados[0]) # BA
print(estados[-1]) # RS

#slicing
print(estados[1:3]) # ('SP', 'RJ')
print(estados[::-1]) # ('RS', 'MG', 'RJ', 'SP', 'BA')
# [início:fim:passo] -> inicio vazio, fim vazio, passo -1 , a leitura é feita de trás para frente, recuando de 1 em 1 elemento
'''O fatiamento funciona igual ao das listas(o fim é exclusivo) e devolve uma nova tupla'''
estados2 = estados[::-2] # ('RS', 'RJ', 'BA')
print(estados2)

print(len(estados)) # 5 


print("SP" in estados) # True
print(estados.index("RJ")) # 2 -> index devolve a posição da primeira ocorrência


numbers = (1,2,1,1)
print(numbers.count(1)) # 3
print((1,2) + (3,)) #  (1, 2, 3) <- concatenação
print (("hello",) * 3) # ('hello', 'hello', 'hello')

print(min(4,1,9)) # 1
print(max(4,1,9)) # 9
print(sum((4,1,9))) # 14
print(sorted((4,1,9))) # [1, 4, 9]

'''
tuplas tem apenas dois métodos: index() e o count()
sorted() aceita tupla, mas devolve uma lista - > exemplo da linha 27 a saída é [1, 4, 9]
'''


departamentos = ("RH","DIRETORIA","MANUTENÇÃO","LIMPEZA","SAC")

for item in departamentos:
    print(item)