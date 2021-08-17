# Exercício 6 da lista de Strings do 2°Bimestre
# Laurent Chaves Assis Feliciano
# Kaiky Augusto Bedim
# Renato Minoru Nishikawa
# Alberson Wander de Sá
# 2°F - Informática
# 6) Fazer um programa em python para mostrar o primeiro e o último nome de pessoa digitado pelo usuário,
# independente da quantidade de palavras do nome digitado. 
Nome=input('Digite um nome completo')
NomeCortado= Nome.split()
print(f'Primeiro nome:{NomeCortado[0]}\nSegundo nome:{NomeCortado[-1]}')