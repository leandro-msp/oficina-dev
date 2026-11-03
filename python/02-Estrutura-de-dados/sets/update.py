# MODIFICANDO CONJUNTOS (CRUD)

'''Como nn há índices, a adição e remoção são feitas diretamente pelo valor'''

cidades = {"Sao Paulo","Rio de Janeiro"}

# add (create)
cidades.add("Curitiba")
print(cidades)

# remover (delete)
cidades.remove("Rio de Janeiro") # gera erro se "Rio de Janeiro" não existir
cidades.discard("Rio de Janeiro") # mais seguro -> remove se existir, ignora se não existir