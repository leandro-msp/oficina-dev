#projeto 3 - verificar se o resultado da soma é ímpar ou par, e qual dos valores digitados é maior


numero1 = int(input("Digite um número:"))
numero2 = int(input("Digite outro número:"))

if ((numero1+numero2)%2==0):
    print ("O resultado é um número par.")
else: 
    print("O resultado é um número ímpar.")
if (numero1>numero2):
    print("O primeiro valor digitado é maior")
elif(numero2>numero1):
    print("O segundo valor digitado é maior")
else:
    print("Os valores digitados são iguais.")

