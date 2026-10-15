
# Fazer um programa para ler os três coeficientes de uma equação do segundo grau. Usando a fórmula de Bhaskara, calcular e mostrar os valores das raízes x1 e x2
# Se a equação não possuir raízes reais, mostrar uma mensagem  
# Delta não pode ser negativo e o Coeficente "a" não poder ser zero(0)

#usuario insere os valores dos coeficientes
a = float(input("Digite o coeficiente A: "))
while(a==0):
    a = float(input("\nO coeficiente A deve ser diferente de zero: "))
b = float(input("\nDigite o coeficiente B: "))
c = float(input("\nDigite o coeficiente C: "))

#descobrir o Delta (Discriminante)
delta = (b**2)-4*a*c

if (delta<0): 
    print ("\nO delta é um valor negativo, portanto esta equação não possui raízes.\nOperação Finalizada")
else:
    raiz_delta = delta ** (1/2) #método para calcular raíz sem utilizar funções ou módulos

    #achar as raízes aplicando a fórmula
    x1 =(-b + raiz_delta)/(2*a) #x1 é igual -b + Raiz de Delta, sobre o total da multipicação de 2*conficiente "a"
    x2 =(-b - raiz_delta)/(2*a) #x2 é igual -b - Raiz de Delta, sobre o total da multipicação de 2*conficiente "a"

    print(f"\n x1 = {x1:.1f}, x2 = {x2:.1f}\n")

    #Tirando a Prova real utilizando a Equação do 2ºgrau
    prova_real1 = abs((a*(x1**2))+(b*x1)+c) < 0.00001
    if (prova_real1==True):
        print(f"Prova real X1: \n {(a):.1f}*{x1:.1f}²+{b}*{x1:.1f}+{c:.1f} = 0") #utilizando formatação para imprimir apenas uma casa decimal

    prova_real2 = abs((a*(x2**2))+(b*x2)+c) < 0.00001 # abs serve apenas para ignora o sinal de negativo caso o resultado seja algo como -0.00001
    if(prova_real2==True):
        print(f"\nProva real X2: \n {(a):.1f}*{x2:.1f}²+{b}*{x2:.1f}+{c:.1f} = 0")
'''
Em computação, operações com números decimais podem gerar pequenas imprecisões de arredondamento nas últimas casas decimais.
qnd isso acontece, o Python vai entender que não é igual a zero, portanto em vez de usarmos o operador == 0 (igual a 0) na equação,
o pardão na programação é testar se o resultado está muito próximo de zero
'''
