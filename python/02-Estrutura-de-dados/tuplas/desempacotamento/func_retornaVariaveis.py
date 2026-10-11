def minMax (dado):
    return min(dado), max (dado)

resultado = minMax([8,16,2,18])
print (resultado) # (2, 18)
print(type(resultado)) # <class 'tuple'>

menor, maior  = minMax([8,16,2,18]) 
print(menor,maior) # 2 18