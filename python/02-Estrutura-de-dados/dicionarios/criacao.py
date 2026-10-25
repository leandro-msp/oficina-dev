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
MODELO DE MAPEAMENTO
Paralelo a lista que o valor é recuperado pelos índices, no dicinonário criamos o próprio "índices" utilizando rótulos que fazem sentido para o contexto.
A estrutura é beseadas em pares: Uma chave(o identificador, no qual é a referência do objeto) e Valor(dado armazenado)

Se procurar pela chave "nome", será recuperado o valor que está associado a ela: '''

print(usuario["nome"])
s
print (usuario)
'''
RESTRIÇÃO DAS CHAVES (UNICIDADE E IMUTABILIDADE) :

Unicidade: Não pode existir duas chave idênticas, se um novo valor for inserido a uma chave já existente, o anterior será sobrescrito

Imutabilidade:  o tipo de dado de uma chave(referencia) não pode ser alterado depois de criado (string e tipos numéricos por exemplo): '''

# Unicidade

cores = {
    "cor1":"azul",
    "cor2":"vermelho",  
    "cor1":"amarelo"
}

print(cores["cor1"])

# dicionarios internos

