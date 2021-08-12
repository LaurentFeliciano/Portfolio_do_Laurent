# Exercício 6 da lista de Tuplas do 2°Bimestre
# Laurent Chaves Assis Feliciano
# Kaiky Augusto Bedim
# Renato Minoru Nishikawa
# Alberson Wander de Sá
# 2°F - Informática
palavras=('Laurent','Chaves','Assis','Feliciano','Programador','Em','Python','CSS','HTML','Csharp')
# Crie uma tupla contendo 10 palavras quaisquer. Em seguida, mostre somente as vogais de cada palavra
# armazenada.
for palavra in palavras:
    print(f'\nNa palavra {palavra.upper()} temos: ', end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra, end=',')