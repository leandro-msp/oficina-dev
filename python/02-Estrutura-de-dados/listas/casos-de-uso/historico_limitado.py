# Histórico de comandso digitados 

#Onde será armazenado os comandos
historico = []

#Constante que limita a quantidade de elementos
MAX_COMANDOS = 5

def addComando(cmd):
    historico.append(cmd)
    if len(historico) > MAX_COMANDOS:
        historico.pop(0) # irá remover o item mais antigo(índice 0)

addComando ('ls')
addComando ('rm')
addComando ('mkdir')
addComando ('touch')
addComando ('code .')

print (historico)

addComando('cd') # nesta etapa o 'ls' é deletado

print (historico)
    



