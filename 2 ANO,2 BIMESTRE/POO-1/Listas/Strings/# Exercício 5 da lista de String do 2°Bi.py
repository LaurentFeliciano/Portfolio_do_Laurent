# Exercício 5 da lista de Strings do 2°Bimestre
# Laurent Chaves Assis Feliciano
# Kaiky Augusto Bedim
# Renato Minoru Nishikawa
# Alberson Wander de Sá
# 2°F - Informática
#
# 5) Fazer um programa em python que solicite a digitação de um nome qualquer. Pede-se:
# a. Mostrar quantas vezes a letra “A” ou “a” aparece
# b. Em que posição a letra “A” aparece a primeira vez
# c. Em que posição a letra “A” aparece a última vez 

Nome= str(input('Digite um nome:'))
# a. Mostrar quantas vezes a letra “A” ou “a” aparece:
X = Nome.count('A')
print(f'{X};')
X = Nome.count('a')
print(f'{X};')
# b. Em que posição a letra “A” aparece a primeira vez:
X= Nome.find('A')
print(f'Posição {X};')
# c. Em que posição a letra “A” aparece a última vez: 
X= Nome[::-1].find('A')
print(f'Posição {X};')
