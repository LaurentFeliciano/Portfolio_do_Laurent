# Exercício 1 da lista de listas de listas do 2°Bimestre
# Laurent Chaves Assis Feliciano
# Kaiky Augusto Bedim
# Renato Minoru Nishikawa
# Alberson Wander de Sá
# 2°F - Informática
lista=list()
for contador in range(0,5): 
    lista[contador]=int(input('Digite um número:'))
    if contador==0: maior=lista[contador],menor=lista[contador] 
    if lista[contador]>maior:
        maior=lista[contador]
    elif lista[contador]<menor:
        menor=lista[contador]