''' Peça ao usuário digitar números repetidamente. O Programa deve parar quando o usuário digitar o número 0 (zero).
    No final , mostre a soma total de todos os números que foram digitados.
'''

numero= int(input("Digite um número: "))
soma = 0

while numero!=0:
    soma=soma+numero # ou soma+=numero
    numero = int(input("Digite outro número: "))
print(f"A soma dos valores digitados é: {soma}")