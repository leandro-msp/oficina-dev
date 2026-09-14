#projeto 4 - Simução de autenticação de login

usuario_cadastrado = "user000"
senha_cadastrada = "1234"

user_digitado = input("Digite o usuário: ").lower()
senha_digitada = input("Digite a senha: ")

if (user_digitado==usuario_cadastrado and senha_digitada==senha_cadastrada):
    print ("Login Efetuado com sucesso!")
else: 
    print ("Falha no login!\nUsário ou Senha foram digitados incorretamente.")

