'''Exercício 4. Dada a lista de notas [7.5, 8.0, 6.5, 9.0], calcule a média e conte quantas notas ficaram acima dela. '''

notas = [7.5,8.0,6.5,9.0]
media  = sum(notas) / len(notas)

acima = 0
for nota in notas:
    if nota > media:
        acima += 1

print(f'Média: {media:.2f}') 
print(f'Acima da média: {acima}')
