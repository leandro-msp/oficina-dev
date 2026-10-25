usuario = dict({"nome":"Maria","idade":"32"}) 
print (usuario)


# -> criação de campos
usuario['ativo'] = True
print(usuario)

# se o campo aj existir o valor é sobrescrito
usuario['nome'] = "João"
print(usuario)

# atualizando mútilpos itens de uma vez
usuario.update({'nome':"Carla",'idade':18,'ativo':False}) 
print(usuario)

# REMOÇÃO

# -> remover e recuperar/salvar dado
idade_removida = usuario.pop('idade')
print(idade_removida)

# -> remover diretamente da memória

del usuario['ativo']
print(usuario)


dados = {
    "cidade" : "Carapicuiba",
    "estado" : "Sao Paulo",
    "regiao" : "Sudeste",
    "metropole" : False
}

# verificação se chave existe  

if "cidade" in dados:
    print ("Chave 'cidade' existe!")
