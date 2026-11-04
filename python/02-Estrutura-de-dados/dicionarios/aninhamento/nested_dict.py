''' O valor associado a uma chave pode ser qualquer tipode de daod, inclusive outro dicionário ou uma lista.
    É exatamente dessa forma que sistema reais e a internet organizam dados (como o formato JSON)

    Para acessar ou modifcar dados aninhados, a busca deve ser feita com múltiplos colchetes, ledno da esquerda para a direita, mergulhando um nível por vez.
'''

sistema = {
    "usuario_1" :{
        "nome" : "ana",
        "permissoes" : ["ler","escrever"],
        "ativo": True
    },
    "usuario_2":{
        "nome":"Carlos",
        "permissoes": ["ler"],
        "ativo": False
    }
}

# ACESSANDO DADOS PROFUNDO

''' O primeiro colchete resolve o primeiro nível
    O que ele deve retonar servurá de vase para o segundo colchete, e assim por diante.
'''

# mergulhando dois níveis para recuperar um texto

nome = sistema["usuario_1"]["nome"]
print(nome)

# mergulhando no dicionário e depois acessando o índice zero da lista

primeira_permisao = sistema["usuario_2"]["permissoes"][0]
print(primeira_permisao)

# ATUALIZANDO E ADICIONANDO EM NÍVEIS INTERNOS

''' A regra é idêntica à de uma dicionário simples, mas devemos especificar o caminho completo até a chave de destino'''

# atualizando um valor que está no seungo nível
sistema["usuario_1"]["ativo"] = False

# criando uma chave nova dentro do dicionário do usuário_2
sistema["usuario_2"]["departamento"] = "Vendas"

print(sistema)
