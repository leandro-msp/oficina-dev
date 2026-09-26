numero = int(input("Digite um número de 1 a 10: "))
while(numero<1 or numero>10):
    numero = int(input("Digite um númetro de 1 a 10: "))

multiplicador = 1
print(f"Taboada do {numero}")
while multiplicador<=10:
    resultado = numero*multiplicador
    print(f"{numero}x{multiplicador}={resultado}")
    multiplicador+=1

