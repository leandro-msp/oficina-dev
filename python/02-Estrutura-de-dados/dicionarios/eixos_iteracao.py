'''
Os Três Eixos de Navegação (Iteração):

1.Iterar apenas pelas Chaves (para saber quais categorias ou identificadores existem).
2.Iterar apenas pelos Valores (para processar os dados finais, ignorando como foram rotulados).
3.Iterar pelos Pares (Itens) (para analisar a relação direta entre a chave e o valor simultaneamente).
'''

usuario = {
    "nome": "Ana",
    "idade": 28,
    "ativo": True

}

usuario['cidade'] = "Sao Paulo"
print ( usuario )


# 1. Iterar apenas pelas CHAVES

for chave in usuario.keys():
    print(chave) # nome idade ativo cidade

# 2. Iterar apenas pelos VALORES

for valor in usuario.values():
    print(valor) # Ana 28 True São Paulo

# 3. Iterar por CHAVE e Valor simultanteamento ( Pares, mais útil)

for chave, valor in usuario.items():
    print(f'A chave {chave} guarda o valor {valor}')

