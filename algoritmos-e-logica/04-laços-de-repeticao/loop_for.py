#laço_for

for x in range(2,17,3): #primiero parâmetro é onde inicia , segundo parâmetro onde ele para, e terceiro o intervalo entre os números
    print(x)
    

print("Exemplo 2 :")
for x in range(5): # por padrão começa em zero, e intervalo de um. Onde para sempre será obrigatório
    print(x)
    

print("Exemplo 3 :")

for x in range(1,6):
    print(x)
    
    
print("Exemplo 4 :")
for x in range(0,10,2):
    print(x)
    
print("Exemplo 5 :")
for x in range(5,0,-1): #passo negativo/ contagem regressiva
    print(x)
      
'''O laço for é recomendado quando você já tem um valor fixo, ou seja, sabe a quantidade de vezes que o código vai rodar'''


#Uso do Laço for para calcular média de mais de um aluno.

qtde = int(input("Digite a quantidade de alunos: ")) # usuário já possui um valor fixo(definido) 
for(x) in range(0,qtde,1):  # o loop começa em zero | termina na quantidade o usuario inseriu | avança de um em um
    # o bloco inteiro abaixo será percorrido(irá se repetir) com base na qtdd que usuário
    aluno = input("Digite o nome do Aluno: ")
    av1 = float(input("Digite AV1: "))
    av2 = float(input("Digite AV2: "))
    média = (av1+av2) / 2
    print("A média do aluno ",aluno," foi: ", média)
print("Operação finalizada!")