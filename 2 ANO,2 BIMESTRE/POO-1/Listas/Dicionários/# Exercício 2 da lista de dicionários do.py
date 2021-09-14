# Exercício 2 da lista de dicionários do 2°Bimestre
# Laurent Chaves Assis Feliciano
# Kaiky Augusto Bedim
# Renato Minoru Nishikawa
# Alberson Wander de Sá
# 2°F - Informática
# 2) Fazer um programa para inserir num dicionário o nome de 4 jogadores e um número sorteado entre 1 e 6, que
# simulará que o determinado jogador atirou um dado. Após armazenados os 4 nomes e os números dos dados de
# cada jogador, classifique os jogadores, sabendo que o vencedor foi o que tirou maior número no dado.
import random
Dict={}
for C in range(0,4):
    Nome= input('Digite seu nome:')
    Dict[Nome]= random.randint(1,6)
    if C==0:    
        Dict['Vencedor']= Nome
        Dict['PtsVencedor']= Dict[Nome]
    if Dict[Nome]> Dict['PtsVencedor']:  
        Dict['Vencedor']= Nome
        Dict['PtsVencedor']= Dict[Nome]
print(Dict['Vencedor'])
print(Dict['PtsVencedor'])