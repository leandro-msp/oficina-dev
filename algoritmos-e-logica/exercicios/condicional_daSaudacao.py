hora = int(input("Digite a hora: \n"))

if (hora<12):
    print("Bom Dia!!")
elif(hora<=18): # não há a necessidade de inserir operador  "E" (hora>=12 and hora<=18), pois se o valor for menor que 12, ja cai na primerica condição, sendo assim qlqr valor a partir de 12 até 18 já cai na segunda condição
    print("Boa Tarde!!")
elif(hora>=19 and hora<=23):
    print("Boa noite")
else:
    print("Hora Inválida")