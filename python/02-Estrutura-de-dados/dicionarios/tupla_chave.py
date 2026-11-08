'''
Como chave de dicionário: A tupla brilha quando você precisa mapear malhas, tabuleiros ou coordenadas, usando dois ou mais eixos para apontar para um único valor:
'''
# O dicionário usa a tupla (linha, coluna) como chave de identificação

componentes = {
    (0,0) : "CPU",
    (0,1) : "RAM",
    (0,2) : "SSD",
    (1,0) : "GPU",
    (1,1) : "MotherBoard"
}

# buscando exatamente o que tem na linha 0, coluna 2

busca = componentes[(0,2)]
print(busca)

busca = componentes[(0,0)]
print(busca)

for key, value in componentes.items():
    print (f"{key}:{value}")