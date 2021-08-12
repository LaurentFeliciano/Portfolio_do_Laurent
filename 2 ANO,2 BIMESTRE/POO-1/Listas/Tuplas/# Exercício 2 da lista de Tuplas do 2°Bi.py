# Exercício 2 da lista de Tuplas do 2°Bimestre
# Laurent Chaves Assis Feliciano
# Kaiky Augusto Bedim
# Renato Minoru Nishikawa
# Alberson Wander de Sá
# 2°F - Informática
# 2) Crie uma tupla com classificação de um campeonato de futebol com 10 times. Em seguida mostre:
# a. Os 5 primeiros colocados
# b. Os 4 últimos da colocados
# c. A listagem dos times em ordem alfabética
# d. Em que posição está um time informado pelo usuário
 
classificacao=('time A','time C','time B','time D','time E','time F','time G','time H','time I','time J')
print(f'{classificacao[0:5]}')
print(f'{classificacao[-1:-5:-1]}')
print(f'{sorted(classificacao)}')
time=input('Digite o nome de um time:')
print(f'posição:{classificacao.index(time)+1}')