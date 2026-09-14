#ESTRUTURA CONDICIONAL SIMPLES

a = 5
b = 5
c = 2 
d = 0
if (a==b): #se A for igual a B // true
    c = a+b # o valor de C passa ser a soma de A e B (5+5)
    c = c+5 # C passa a valer seu novo valor + 5 (10 + 5)
d = c + 10 # D tem o valor de C + 10 (15+10)
print(d) # logo a saída será 25


a = 5
b = 3
c = 2
d = 0
if (a==b): #false
    c = a+b # não será executado
    c = c+5 # não será executado
d = c + 10 # D vai valer C + 10 ( 2 + 10)
print(d) # 12


subTotal= float(input("Digite o sub-Total da compra:"))
desconto = 0
if (subTotal>=100):
    desconto = subTotal*0.02
totalCompra = (subTotal-desconto)
    # ou totalCompra  = subTotal*0.2 || < - -  já aplica o desconto direto no total sem precisar criar varíavel desconto, já que o valor ja está definido como 0.2

print("Total Compra: R$", totalCompra)

#COMPOSTA
emailCadastrado = "jose@email.com"
senhaCadastrada = "123"
emailDigitado = input("Digite seu email: ").lower()
senhaDigitada = input("Digite sua senha: ")

if ((emailDigitado == emailCadastrado) and (senhaDigitada==senhaCadastrada)): # autenticação -- > tipo de lógica aplicada em verificação de dados salvos no banco de Dados;
    print("Login Efetuado com sucesso!")
else:
    print("O e-mail ou senha inseridos estão incorretos, ou o usário não está cadastrado.")


#ENCADEADO:
subTotal = float(input("Digite o sub-Total da compra:"))
desconto = 0
if (subTotal>180):
    desconto = subTotal*0.05    # ou - > totalCompra = subTotal*0.05 (neste cenário não existe variável desconto)
elif(subTotal>140 and subTotal<180):
    desconto = subTotal*0.2     # ou - > totalCompra = subTotal*0.02 (neste cenário não existe variável desconto)
else:
   totalCompra = (subTotal-desconto)   # case "não tem desconto" - > totalCompra = subTotal (neste cenário não existe variável desconto)
print("Total da Compra: R$",totalCompra)


