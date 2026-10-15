#Uso do While para calcular de média de mais de um aluno


repetir = "s"               # valor inicial da variável repetir
while(repetir=="s"):        # enquanto a varíavel permanecer com este valor irá rodar o bloco abaixo
    print("Cálculo de Média:")
    aluno = input("Digite o nome do Aluno: ")
    av1 = float(input("Insira sua nota da av1: "))
    av2 = float(input("Insira sua nota da av2: "))
    média = (av1+av2) / 2
    print ("A média do Aluno", aluno, "foi: ", média)
    
    # aqui que "decide" se o código vai rodar novamente, pois será atribuído um valor para a varíavel do início do código, e se ele for "s", instrução irá rodar novamente
    repetir = input("Caso queira calcular nova média, digite 's', caso contrário digite: 'n' : ")
    while (repetir!="s" and repetir!="n"):
        repetir = input("Comando não aceito, digite somente 's' ou 'n'!:")
print("Fim da operação!!")