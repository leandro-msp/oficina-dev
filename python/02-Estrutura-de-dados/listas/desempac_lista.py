# lista com vários dados atribuidos a variáveis

nome, idade, cidade, profissao, linguagem, status = ["Bia", 25, "Recife", "Desenvolvedora", "Python", "Ativa"]

print(nome, idade, cidade, profissao, linguagem, status)

# removendo "valor que não interessa" com underline (_)

func, _, _, departamento, linguagem, status = ["Bia", 25, "Recife", "Desenvolvedora", "Python", "Ativa"]

print(func, departamento, linguagem, status)

# capturando tudo que está no meio e "joga fora" 

funcionario, *_, status = ["João", 36, "São Paulo", "Tec.Redes", "N/D", "Ativo"] # João Ativo
'aterisco (*), captura vários valors de uma só vez que não nos interssam, sempre precisar colocar um underline(_) para cada um deles.'
print(funcionario, status)

# ou 

dados = ["João", 36, "São Paulo", "Tec.Redes", "N/D", "Ativo"]

nome, *_, status = dados 

print(nome, status)