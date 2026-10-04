pilha_pratos = [] # pilha vazia

#empilhando pratos
pilha_pratos.append('Prato 1'); pilha_pratos.append('Prato 2'); pilha_pratos.append('Prato 3'); pilha_pratos.append('Prato 4');

# desempilhar(remover pratos do final)
prato = pilha_pratos.pop() # sempre o último
print (f'Prato retirado: {prato}')
print (f'Quais pratos ainda estão na pilha: {pilha_pratos}')


# Método automático
print('Pilha de Prados'.center(24,':'))
print(pilha_pratos)

while len(pilha_pratos) > 0:
    prato = pilha_pratos.pop()
    print (f'Prato retirado: {prato}')
    if len(pilha_pratos) > 0: 
        print (f'Quais pratos ainda estão na pilha: {pilha_pratos}')
print('Não há mais pratos!')

    





