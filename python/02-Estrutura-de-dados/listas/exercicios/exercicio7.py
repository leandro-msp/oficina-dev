valores = [12, 45, 7, 45, 30]
maior = valores[0]
posicao = 0

for i, v in enumerate(valores): # indice e valor
    print(f'{i}:{v}')
    if v > maior: # verifica se o valor na lista é maior que o valor armazenado em 'maior' (ex.: 1º loop v= 12.. no segundo v=45) , logo 45>12.. maior passa valer 45
        maior = v       # 1ºvolta - > v= 12 , 12 > 12 (false), posição = 0
        posicao = i     # 2ºvolta - > v= 45 , 45 > 12 (true) , posição = 1
                        # 3ºvolta - > v= 45 , 7 > 45 (false) , posição = 1 <<-- condição é falsa, então não entra a instrução do IF
                        # 4ºvolta - > v= 45 , 45 > 45 (false), posição = 1 <<-- condição é falsa, então não entra a instrução do IF
                        # 5ºvolta - > v= 45 , 30 > 45 (false), posição = 1 <<-- condição é falsa, então não entra a instrução do IF
        
print(f'Maior: {maior} na posição {posicao}')
