'''o computador escolhe um número secreto de forma aleatória, e você tenta adivinhar qual é. 
O programa vai te dando dicas se o seu palpite foi alto demais ou baixo demais até você acertar.
'''

import random

print ("::: JOGO DA ADIVINHAÇÃO :::")
print("Informe um número de 1 a 100, e direi se está abaixo ou acima do número escolhido, até que descubra qual é")

numero_escolhido= random.randint(1,100) # máquina escolhe um número aleatório de 1 a 100, pode aumentar o range, consequentemente isso aumentará o número de tentativas ()
                                        # Se o jogador for bom, certamente vai utilizar a estratégia da busca binária para descobrir em poucas tentativas :)
tentativas = 0
palpite = int(input("\nDiga um número: "))
tentativas+=1 # a partir do momento que o usuário da o primeiro número, já é uma tentativa
while palpite != numero_escolhido: # início do laço, se o número for diferente do escolhido, começa a verificação se é menor ou maior que num secreto
    if palpite < numero_escolhido:
        print("Muito baixo, tente um número maior!") # da a dica se está a cima ou abaixo
        palpite = int(input("\nDiga um número: "))
        tentativas +=1 # usuario errou. Logo o programa solicita novo palpite e soma mais uma tentativa

    # ocorre mesmo processo do bloco anterior, só muda a verificação
    else:
        print("Muito alto, tente um número menor!")
        palpite = int(input("\nDiga um número: "))
        tentativas +=1 
#a partir do momento que o palpite se torna igual ao número escolhe, o programa cai fora do laço, ou seja o usuário acertou, e exibe a mensagem
print(f"Parabéns, você acertou, eu escolhi exatamente o número {numero_escolhido}\n")
print(f"Você acertou em {tentativas} tentativas")


#CORREÇÃO / ADAPTAÇÃO

'''Para eveitar de repetir o input do palpite e tentativas 3 vezes dentro do código, é utilizado uma estrutura de Loop Infinito com Saída (While True)

...

tentativas = 0

while True : # o laço roda infinitamente até encontrar um "break"
    palpite = int(input("Diga um número:"))
    tentativas += 1 # conta a tentativa atula de forma única no topo

    if palpite < numero_escolhido:
        print ("Muito baixo, tente um número maior!")
    elif palpite > numero_escolhido:
        print ("Muito alto, tente um número menor!")
    else:
        # se nn for menor nem maior, o usuário acertou!
        print (f"Parabéns, você acertou! Eu escolhi exatamente o número {numero_escolhido}")
        print (f"Você acertou em {tentativas} tentativas!")

        break # o 'break' quebra o 'While True' e encerra o programa(game)

'''