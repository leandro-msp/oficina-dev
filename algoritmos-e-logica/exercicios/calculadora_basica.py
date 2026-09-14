#projeto 5 - calculadora 2 (match-case):

print (">>>> CALCULADORA SIMPLES <<<<")

#inserir primeiro valor
valor1 = int(input("Digite o número: "))

#selecionar o tipo de operação(adição,subtração,multiplicação...)
operação = input("Digite a operação desejada (+, -, *, /, %, ^):")

#certifica o usuário escolher somente as operações disponíveis
while operação not in ["+", "-", "*", "/", "%", "^"]: # método mais limpo para detectar se o usuário digitou elementos fora do requisitado
    operação = input("Operação inválida, escolha entre as disponíveis (+, -, *, /, %, ^): ")

#inserir segundo valor 
valor2 = int(input("Digite outro número: "))

#o match case é mesmo processo do (switch-case de outras linguagens)
match operação:
    case "+":
        resultado = valor1+valor2
        print("Resultado: ",resultado)

    case "-":
        resultado = valor1-valor2
        print ("Resultado: ",resultado)

    case "*":
        resultado = valor1*valor2
        print ("Resultado: ",resultado)
    case "/":
        try:
            resultado = valor1/valor2
            print ("Resultado: ",resultado)
        except ZeroDivisionError:  # caso o usuario digite zero, em vez do script travar, ele captura o erro de divisão por zero, converte em aviso, aí sim finaliza o código em segurança.
            print ("Erro: Não é possível dividir por zero!")
    case "%":
        try:
            resultado = valor1%valor2
            print ("Resultado: ",resultado)
        except ZeroDivisionError:
            print("Erro: Não é possível calcular o resto de uma divisão por zero!")
    case _: # default
        resultado = valor1**valor2
        print ("Resultado: ",resultado)
print("Operação Finalizada")