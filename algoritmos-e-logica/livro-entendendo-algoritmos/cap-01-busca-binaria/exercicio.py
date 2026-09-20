# UTILIZANDO PESQUISA BINÁRIA PRA ENCONTRAR ITEM NA LISTA DE NOMES
nomes = [
    "Ana", "Bruno", "Camila", "Daniel", "Eduarda", 
    "Felipe", "Gabriela", "Gustavo", "Helena", "Igor", 
    "Juliana", "Leonardo", "Mariana", "Matheus", "Natália", 
    "Otávio", "Patrícia", "Rafael", "Sabrina", "Thiago", 
    "Vanessa", "Vinícius", "Beatriz", "Caio", "Larissa", 
    "Lucas", "Letícia", "Rodrigo", "Amanda", "Diego"
]

def pesquisaBinaria(lista,nome):
    lista.sort() # vai deixar a lista em ordem alfabética
    começo = 0
    final = len(lista) -1

    while começo <= final:
        meio = (começo+final)//2
        chute = lista[meio]

        if chute == nome:
            return meio
        if chute > nome: # os operadores identificam também a ordem alfabética pra determinar se uma letra é maior que a outra, exemplo A < B
            final = meio -1
        else:
            começo = meio +1
    return None

procurarNome = input("Digite um nome que deseja procurar na lista: \n").capitalize() # usuário digita o elemento que deseja procurar , e tratamento de primeira letra maíscula, caso o escreva tudo minúsculo
elemento = pesquisaBinaria(nomes,procurarNome) # o valor final retorna será um número que é o indice, ou None, e será armazenado na variável "elemento"

if elemento != None: # caso o resultado da variável for diferente de None, obviamente será um número, pois localizou na lista, e vai exbir que foi encontrado
    print (f"o nome {procurarNome} existe na lista e está no índice:",elemento,"\n")
else:
    print("O Nome procurado não existe na lista\n") # caso não haja o nome, elemento é igual a None , ou seja a condição já cai no falso ( elemento nn é diferente de None), ou seja nome não encontrado
