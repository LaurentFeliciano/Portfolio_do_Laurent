# Exercício 5 da lista de Strings do 2°Bimestre
# Laurent Chaves Assis Feliciano
# Kaiky Augusto Bedim
# Renato Minoru Nishikawa
# Alberson Wander de Sá
# 2°F - Informática
nome= str(input('Digite um nome:'))
new_var = nome.count('A')
print(f'{ new_var };')
new_var = nome.count('a')
print(f'{ new_var };')
new_var= nome.find('A')
print(f'Posição {new_var };')
new_var= nome[::-1].find('A')
print(f'Posição {new_var };')
