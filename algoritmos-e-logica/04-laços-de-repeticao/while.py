# loop usando while

#while = enquanto -> esse método de loop trabalha verificando uma condição, e equanto ela for verdadeira a instrução designada no bloco será realizada
print ("\nExemplo 1: \n")

quantidade = 0 
while(quantidade<5): 
    print (quantidade)
    quantidade+=1

# 1º a variável "quantidade" começa com zero,
# 2º O loop verifica a condição: a variável quantidade é menor que 5? SIM ! 0 é menor que cinco
# 3º Então enquanto for menor que 5, exiba o valor atual de "quantidade" e adicione 1 no seu valor 
# 4º o último valor gerado é 4, pq? Pois a partir do próximo passo a condição se torna falsa, 5 não é menor que 5, e a instrução é finalizada

print ("\nExemplo 2: \n")
qtd = 0
while(qtd<=5):
    print (qtd)
    qtd+=1

# Neste exemplo segue o mesmo processo, porém a condição muda, se o valor atual de "qtd" for menor ou igual a 5, realiza a instrução
# por isto neste método o valor 5 será impresso, pois a condição se torna falsa quando chega no 6

print ("\nExemplo 3: \n")

continuar = "sim"
while (continuar=="sim"):
    nome = input("Digite seu nome:\n")
    continuar=input("se deseja digitar novamente? responda 'sim' \n")
print("Operação Finalizada")

# 1º o programa incia com a variavel "continuar" com seu valor "sim", o enquanto analisa se ve que é verdadeira
# 2º sendo verdadeira a instrução é dada ao usuário, "digite seu nome", apois digitar a variável "continuar" entra em cena novamente
# 3º se o usuário digitar sim, o a condição do while cai no verdadeiro de novo, e solicita pra digitar o nome novamente 
# 4º caso o usuário digite qualquer outra coisa, a variável "continuar" terá seu valor mudado, sendo assim a condição do while cai no falso e encerra a operação

# o método de looping WHILE é utilizado quando não temos uma quantidade fixa/exata definada para que o código repita tal instrução.



