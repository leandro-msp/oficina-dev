cidade = {
    "nome":"Carapicuiba",
    "estado":"Sao Paulo",
    "regiao":"oeste",
    "tipo":"metropole"
}

print (cidade)

nome_cidade = cidade.get("nome")
qtd_habitantes = cidade.get("habitantes","Não informado")

print(nome_cidade) ;  print (qtd_habitantes)

cidade["habitantes"] = 398.236

qtd_habitantes = cidade.get("habitantes")
print(f'Segundo estimativas do IBGE a cidade de {nome_cidade} possui {qtd_habitantes} habitantes')

localizacao = cidade.pop("regiao")
print(localizacao)

# método seguro para tentativa de remoção de chave caso ela não exista, utilizando o método Del que por padrão gera erro qnd a chave não existe.
try:
    del cidade['area']
except KeyError:
    print("Erro: A chave informada não existe")

tipo_removido = cidade.pop("tipo")
print(tipo_removido)

if "estado" in cidade:
    print("a chave informada existe")


for chave in cidade.keys():
    print(chave)

for valor in cidade.values():
    print(valor)

for chave,valor in cidade.items():
    print(f'a chave "{chave}" armazena o valor "{valor}"')


