# Fila: "Primeiro entra, Primeiro sai"

fila_atendimento = []

#adicionar pessoas na fila
fila_atendimento.append('Ederman')
fila_atendimento.append('Piglin')
fila_atendimento.append('Steve') 

print(fila_atendimento) # ['Ederman', 'Piglin', 'Steve']


# atender (após atender remover da fila (início), assim o próximo assume o primeiro lugar)
atendido = fila_atendimento.pop(0) # 'Enderman' -> o primeiro é removido ,  e usado
print (f"Em atendimento: {atendido}")
print (f'Fila atual: {fila_atendimento}') # ['Piglin', 'Steve']


# método automatizado
print('Método 2'.center(20,'-'))

# add pessoas á fila
fila_atendimento = []
fila_atendimento.append('Ederman') ; fila_atendimento.append('Piglin') ; fila_atendimento.append('Steve') 
print (fila_atendimento)

# analizar qtdd de presentes na fila e realizar o loop enquanto não zerar
while len(fila_atendimento) > 0: 
    atendido = fila_atendimento.pop(0)
    print (f"Em atendimento: {atendido}")
    if len(fila_atendimento) >0:
        print (f'Fila atual: {fila_atendimento}')
print("Não há mais pessoas aguardando atendimento")

    
