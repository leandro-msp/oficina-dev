# Processar IDs de usuários em lotes de 100
ids_usuarios = list(range(1,1001)) # 1000 usuários

#define o tamanho de cada lote
tamanho_lote = 100

for i in range(0,len(ids_usuarios),tamanho_lote): # range(0,1000,100) 
    lote = ids_usuarios[i:i+tamanho_lote] # pegar 100 usuários a partir da posição da volta atual(i)
    # ex.: 1ªvolta  ->  0:0+100   -> lote = id_usuarios[índice 0 ao índice 100]
    # ex.: 2ªvolta  ->  100:100+100   -> lote = id_usuarios[índice 100 ao índice 200]

    #informa o lote atual e quantos usuários há nele
    print (f'Processando lote {i//tamanho_lote+1}: {len(lote)} usuários') # // -> divisão inteira (descarta casa decimal)
    # ex.: 1ªvolta       ->    i = 0 // 100 + 1     
    #                    ->    0 + 1 = 1

    # ex.: 2ª volta      -> i= 100 // 100 + 1
    #                             1 + 1 = 2