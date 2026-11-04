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

'''ao fazer uma laço "for" no idcionário principal, a variável que guarda o "valor" receberá o dicionário intero inteiro.'''

for id_user, dados_internos in sistema.items():
    print (f"O {dados_internos['nome']} tem as permissões: {dados_internos['permissoes']}")