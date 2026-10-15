#Função da fórmula de báscara

'''Seguindo mesmo conceito do exercício "Fórmula de Bhaskara, porém aplicando a operçao em modo de função'''

def formulaBhaskara(a,b,c):
    while(a==0):
        a = float(input("Coeficente 'a' não pode ser igual a zero: "))
    delta = (b**2)-4*a*c
    if (delta<0):
        print("\nO delta é um valor negativo, portanto esta equação não possui raízes.\nOperação Finalizada")
    else:
        raiz_delta = delta **(1/2)
        x1 = (-b + raiz_delta)/(2*a)
        x2 = (-b - raiz_delta)/(2*a)
        return f"\nAs raízes são:\nx1= {x1:.2f} e x1={x2:.2f}\n" #duas casas decimais
        

coeficiente_a = float(input("Digite o coeficiente 'a': "))
coeficiente_b = float(input("Digite o coeficiente 'b': "))
coeficiente_c = float(input("Digite o coeficiente 'c': "))

resultado=formulaBhaskara(coeficiente_a,coeficiente_b,coeficiente_c)

if resultado!=None: #caso operação não ouver raízes não precisa aprenstar o resultado, ja que o return é None
    print(resultado)
