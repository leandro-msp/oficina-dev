alunos = [
    {'nome':'Gustavo','nota':9.5},
    {'nome':'Lucia','nota':7.5},
    {'nome':'Carlos','nota':5},
    {'nome':'Julia','nota':4},
    {'nome':'Kauan','nota':6}
]


# método simples de acesso aos dados
print(alunos[0]['nome']) # Gustavo
# -> toda linha  se torna parte do índice , e para acessar os dados informasse as chaves

print (alunos[1]['nota']) # 7.5

for aluno in alunos:
    print (f'{aluno['nome']}: {aluno['nota']}') 


# Utilizando list comprehensions

aprovados = [a['nome'] for a in alunos if a['nota']>=6] # ['Gustavo', 'Lucia', 'Kauan']
print(aprovados)
