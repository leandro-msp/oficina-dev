# Credenciais fixas do banco
bd = ('MySQL','root','0000','Teste','localhost')

# Unpacking (descompactação)
type_bd, user, password, name_bd, host_bd = bd

# simulação de inserção de dados pelo usuário
tipo =  input("Tipo de conexão: ").strip()
usuario = input("Usuário: ").strip()
senha = input("Senha: ").strip()
nome_banco = input("Nome da base de dados: ").strip()
host = input("HOST: ").strip()

# Validação -> comparação dos valores

if (tipo == type_bd and
    usuario == user and
    senha == password and
    nome_banco == name_bd and
    host == host_bd):
    print(" Conexão Realizada com Sucesso !!")
else:
    print("Falha na conexão, verifique se os dados estão corretos!")