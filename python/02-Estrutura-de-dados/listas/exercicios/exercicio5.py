'''Exercício 5. Usando for, range() e append(), monte uma lista com os números pares de 1 a 10.'''

numeros = []

for n in range(1,11):
    if n%2==0:
        numeros.append(n)

print(numeros)