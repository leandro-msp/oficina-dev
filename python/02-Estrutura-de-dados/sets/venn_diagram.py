time_a = {"Ana", "Carlos", "João"}
time_b = {"Carlos", "Maria", "Pedro"}

# 1. União (|): Junta tudo, sem repetir quem está nos dois
todos = time_a | time_b
print (f'Uniao: {todos}') # {'Ana', 'Carlos', 'João', 'Maria', 'Pedro'}

# 2. Interseção (&): Quem está em AMBOS os conjuntos?
comuns = time_a & time_b
print(f'Intersecao: {comuns}') # {'Carlos'}

# 3. Diferença (-): Quem está em um, mas NÃO está no outro?
exclusivos_a = time_a - time_b 
print (f'Diferenca A: {exclusivos_a}') # {'Ana', 'João'}

exclusivos_b = time_b - time_a
print (f'Diferenca B: {exclusivos_b}') # {'Maria', 'Pedro'}

# 4. Diferença Simétrica (^): Quem está em apenas um dos times (exclui os comuns)?
diferentes = time_a ^ time_b
print (f'Difenreca Simetrica {diferentes}') # {'Ana', 'Jo�o', 'Pedro', 'Maria'}