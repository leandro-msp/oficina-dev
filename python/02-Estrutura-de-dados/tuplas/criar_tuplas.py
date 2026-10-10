vazia = ()
cores = ("vermelho","azul","amrelo")
mista = (2,"quatro",6.0, True)
sem_parenteses = 1,2,3 # (1, 2, 3) <class 'tuple'>
de_lista = tuple([10,20,30]) # (10, 20, 30)
de_string = tuple("python") # ('p', 'y', 't', 'h', 'o', 'n')

print(vazia,cores,mista)
print(sem_parenteses,type(sem_parenteses))
print(de_lista, de_string)


# TUPLA DE UM ÚNICO ELEMENTO (vírgula obrigatória)

tupla1 =("Python",) # é tupla
tupla2 = "Python",  # é tupla

nao_e_tupla = ("Phyton") # não é tupla , tipo string

print (type(tupla1), type(tupla2), type(nao_e_tupla))
print(len(tupla1))

print((5) * 2, (5,) * 2) # 10 (5, 5) -> 1º operação , 2º "replica o valor da tupla"


