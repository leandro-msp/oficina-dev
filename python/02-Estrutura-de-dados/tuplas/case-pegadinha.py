t = (1, [2, 3])
try:
    t[1] += [4]
except TypeError as erro: # para nn quebrar a execução, o erro é atribuido a uma variavel
    print("TypeError:", erro)
print(t)

'''Deu erro e alterou a lista. O += faz duas coisas: primeiro estende a lista no lugar (isso funciona) e depois tenta atribuir o resultado de volta em t[1] (isso falha). 

Como Evitar:
Nunca usar operadores de atribuiç~çao ( = , +=). Em vez disso, utilizar métodos que alteram o objeto sem tentar reatribuí-lo:

t[1].append(4) — Adiciona um elemento ao final da lista.
• t[1].extend([4]) — Adiciona múltiplos elementos ao final da lista.

'''

dados = ("Nome",["Leandro","João"])

dados[1].append('Mateus')
print(dados)

dados[1].extend(["Leticia","Julia"]) # usa-se extend para add múltiplos valores
print(dados)
