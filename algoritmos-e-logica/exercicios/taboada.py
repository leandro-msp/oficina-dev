#taboada usando FOR -> o usuário deve digitar um número de 1 a 10, e a saída deve ser a tabuada da multiplicação daquele número.

numero = int(input("Digite um númetro de 1 a 10: "))
while(numero<1 or numero>10):
    numero = int(input("Digite um númetro de 1 a 10: ")) #apenas para manter o controle do enunciado (de 1 a 10)
print (f"\nTaboada do {numero}")
for multiplicador in range(1,11): # 1 onde inicia, 11 onde para
    resultado = numero * multiplicador
    print(f"{numero}x{multiplicador}={resultado}")
print("\n")
