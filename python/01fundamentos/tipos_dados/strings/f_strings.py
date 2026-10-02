# F-STRINGS

'''f-strings são strings formatadas que são prefixada com a letra 'f'  e é similiar à formatação de strings aceita por format()'''

primeiro_nome = "João"
sobrenome = "Silva"

resultado = f'Meu nome é {primeiro_nome} {sobrenome}'
print(resultado)

# é possível utilizar métodos

resultado = f'Meu nome é {primeiro_nome.upper()} {sobrenome.lower()}'
print(resultado)


# dados de dicionário

pessoa = {'nome':'Letícia','profissão':'Engenheira'}

resultado = f'Meu nome é {pessoa["nome"]} e sou {pessoa["profissão"]}'

print(resultado)

# operações matemáticas

calculo = f'5x2 = {5*2}'
print(calculo)

for x in range(1,11):
    valor = f'O Valor é {x:02}'
    print(valor)

''' n: É a variável que está mudando a cada volta do laço (1, 2, 3...)
    :: Indica o início das regras de formatação.
    0: Define o caractere de preenchimento (neste caso, o número zero).
    2: Define a largura mínima total que o número deve ocupar na tela.

    Isso significa: "Se o número não tiver pelo menos 2 dígitos, coloque um zero na frente para preencher a lacuna."
'''

# formatação de datas

from datetime import datetime

dt_nascimento = datetime(2000,7,13) # y/m/d

resultado = f'Data: {dt_nascimento:%d, %B, %Y}'

print(resultado) # Data: 13, July, 2000

''' Cada letra com o símbolo % extrai uma informação específica:
    %B: Retorna o nome completo do mês por extenso (neste caso, por padrão do sistema, "July"
    %d: Retorna o dia do mês preenchido com zero à esquerda, se necessário
    %Y: Retorna o ano completo com 4 dígitos ("2000").

'''

# convertendo para string

y = 5
z = [4,5,6.8,12]

print(type(str(y))) # <class 'str'>
print(type(repr(z))) # <class 'str'>
