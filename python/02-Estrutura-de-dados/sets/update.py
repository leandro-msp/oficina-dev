# MODIFICANDO CONJUNTOS (CRUD)

'''Como nn há índices, a adição e remoção são feitas diretamente pelo valor'''

cidades = {"Sao Paulo","Rio de Janeiro"}

# add (create)
cidades.add("Curitiba")
print(cidades)

# remover (delete)
cidades.remove("Rio de Janeiro") # gera erro se "Rio de Janeiro" não existir
cidades.discard("Rio de Janeiro") # mais seguro -> remove se existir, ignora se não existir

'''A regra é que não existe uma posição fixa para os elementos, logo não é possível acessar valores específicos, para tanto é possível utilizar alguns métodos comuns'''

# Verificar se o valor existe no conjunto -> Operação rápida de O(1)  <-  Notação Big O

print ("Bahia" in cidades) # False

if "Sao Paulo" in cidades:
    print("A cidade informada existe no conjunto")
else:
    print('A cidade informada não existe no conjunto')

'''
pesquisa = input("Digite o nome de uma cidade: ")

if pesquisa in cidades:
    print("A cidade informada existe no conjunto")
else:
    print('A cidade informada não existe no conjunto') '''



# percorrer elementos
for cidade in cidades:
    print(cidade)

''' Pesquisar elementos específicos é a principal ra~zao para usar um Set! 
O processo de procurar um elemento usando o operador IN é a maior força dos conjuntos em python
Considerando também sua performance, já que sua busca é O(1)
 '''

# exemplo prático de bom uso

#IDs usuários banidos ( armazenaods em um set para busca rápida)
usuarios_banidos = {1024, 8892, 3451, 9912}

usuario_atual = input("Digite o número de usuário que deseja pesquisar: ")

if usuario_atual in usuarios_banidos:
    print("Acesso deste usuário está negado!")
else:
    print("Usuário Liberado")
