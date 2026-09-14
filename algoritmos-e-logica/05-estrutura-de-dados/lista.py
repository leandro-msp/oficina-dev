nomes = ['Lucas','Luana','Raquel','Marcelo']
idades = [25,18,27,32]
cidades = []

# recuperar valor específico        
print(nomes[2])
print (idades[1])

# recuperar lista completa
print (nomes)

#matriz

matriz = [
    ['Rockstar','Ubisoft','Actvision'],
    ["GTA VI","Assassin'S Creed","Call of Duty"],
    ['PC','PS5','XBOX Series-X']
] 

# recuperar dado de uma matriz

print("A Empresa Responsável pelo desenvolvimento do game",matriz[1][1],"é a",matriz[0][1])
print ("No dia 19 de Novembro de 2026 será a data em que a",matriz[0][0],"lançará o game",matriz[1][0],". A princípio somente para os consoles:",matriz[2][1],"e",matriz[2][2])


# impressão por item da lista

for linha in matriz:
    for item in linha:
        print (item)
       


