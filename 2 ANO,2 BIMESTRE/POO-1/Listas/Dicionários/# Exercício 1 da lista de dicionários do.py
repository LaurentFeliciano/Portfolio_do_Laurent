# Exercício 1 da lista de dicionários do 2°Bimestre
# Laurent Chaves Assis Feliciano
# Kaiky Augusto Bedim
# Renato Minoru Nishikawa
# Alberson Wander de Sá
# 2°F - Informática
# 1) Crie um programa para inserir num dicionário o nome e a média de um aluno. Diante da média, insira também
# no dicionário o resultado do aluno, a saber:
# a. Média de 0 até 5.9 – “aluno em recuperação”
# b. Média maior ou igual a 6.0 – “Aluno na média”
# Após armazenar a situação no dicionário imprima o nome, a média e a situação armazenadas no dicionário
Dict={}
Dict['Nome']=input('Digite seu nome:')
Dict['Media']=int(input('Digite a sua média:'))
if Dict['Media']>=0 and Dict['Media']<=5.9: Dict['Resultado']='aluno em recuperação'
elif  Dict['Media']>=6: Dict['Resultado']='aluno na média'
print(Dict)