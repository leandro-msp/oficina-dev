# Criação de um dicionário vazio 

dicionario = {} 

# ou 

dicionario1 = dict()


# Criando com dados iniciais

usuario = {
    "nome":"Leandro",           
    "idade": 26,
    "status":"estudante",
}

'''
Modelo de mapemanto:
Parelelo a lista que o valor é recuperado pelos índices, no dicinonário criamos o próprio "índices" utilizando rótulos que fazem sentido para o contexto.
A estrutura é beseadas em pares: Uma chave(o identificador, no qual é a referência do objeto) e Valor(dado armazenado)

Se procurar pela chave "nome", será recuperado o valor que está associado a ela: '''

print(usuario["nome"])

