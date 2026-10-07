# vers. intereção com terminal

history = [] # lista vazia
MAX_COMMANDS = 5 # const com limits de qntidade

def addCommand(cmd):
    history.append(cmd)
    if len(history) > MAX_COMMANDS:
         history.pop(0) # deletando semore o primeiro item ao atingir o limite de 5



continuar = 'yes'
while continuar == 'yes':
    new_command = input("Digite um comando: \n")
    addCommand(new_command) # o valor digitado é adicionado no parâmetro 
    continuar = input("Se desejar continuar digite 'yes', para sair digite 'no': ") # ao continuar os items vão sendo adicionado na lista, seguindo a regra de manter os 5 mais recentes
if continuar=='no':
    print("\nHistórico Salvo!")
    print(history)
    