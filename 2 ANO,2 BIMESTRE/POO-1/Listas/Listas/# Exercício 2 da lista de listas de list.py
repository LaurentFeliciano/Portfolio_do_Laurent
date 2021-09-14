# Exercício 2 da lista de listas de listas do 2°Bimestre
# Laurent Chaves Assis Feliciano
# Kaiky Augusto Bedim
# Renato Minoru Nishikawa
# Alberson Wander de Sá
# 2°F - Informática
# 2)Fazer um programa que solicite ao usuário a criação de uma lista com VÁRIOS números DIFERENTES, ou seja, caso o
# usuário digite um valor já existente peça outro número e não insira este número repetido na lista. Quando o usuário
# digitar 0, deve ser finalizada a criação da lista
Lista=[]
while True:
    Num=int(input('Digite um número (0 para encerrar):'))
    if Num== 0: break
    if Num not in Lista:    Lista.append(Num)
    else:   print('Não foi possível adicioná-lo a lista pois ele já está presente')
print(Lista)
