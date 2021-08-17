# Exercício 6 da lista de Tuplas do 2°Bimestre
# Laurent Chaves Assis Feliciano
# Kaiky Augusto Bedim
# Renato Minoru Nishikawa
# Alberson Wander de Sá
# 2°F - Informática
Palavras=('Laurent','Chaves','Assis','Feliciano','Programador','Em','Python','CSS','HTML','Csharp')
# 6)Crie uma tupla contendo 10 palavras quaisquer. Em seguida, mostre somente as vogais de cada palavra
# armazenada.
for P in Palavras:
    print(f'\nNa palavra {P.upper()} temos: ', end='')
    for Letra in P:
        if Letra.lower() in 'aeiou':
            print(Letra, end=',')