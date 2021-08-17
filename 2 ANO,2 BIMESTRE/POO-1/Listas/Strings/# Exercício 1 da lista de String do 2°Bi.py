# Exercício 1 da lista de Strings do 2°Bimestre
# Laurent Chaves Assis Feliciano
# Kaiky Augusto Bedim
# Renato Minoru Nishikawa
# Alberson Wander de Sá
# 2°F - Informática
# 1) Fazer um programa em python para:
# a. Mostrar todas as letras de uma frase em letras maiúsculas
# b. Todas as letras da frase em letras minúsculas
# c. Informar quantas letras tem na frase
# d. quantas letras tem na primeira palavra da frase
Frase= 'minha mãe é doida gente socorro'
# a. Mostrar todas as letras de uma frase em letras maiúsculas:
print(f'{Frase.upper()}')
# b. Todas as letras da frase em letras minúsculas:
print(f'{Frase.lower()}')
# c. Informar quantas letras tem na frase:
print(f'{len(Frase)}')
# d. quantas letras tem na primeira palavra da frase:
x=Frase.split()
print(f'{len(x[0])+1}')
