# Exercício 4 da lista de Tuplas do 2°Bimestre
# Laurent Chaves Assis Feliciano
# Kaiky Augusto Bedim
# Renato Minoru Nishikawa
# Alberson Wander de Sá
# 2°F - Informática
# 4) Crie uma tupla com 5 números digitados pelo usuário um a um. Depois mostre:
# a. Quantas vezes aparece o número 10.
# b. Em que posição tem o número 3. Pode ser que não apareça, cuide disso!
# c. Quais são os pares armazenados na tupla 
numeros=(int(input('Digite um numero:')),int(input('Digite um numero:')),int(input('Digite um numero:')),int(input('Digite um numero:')),int(input('Digite um numero:')))

print(f'Quantas vezes apareceram o numero 10:{numeros.count(10)}')
if 3 in numeros:    print(f'Em que posição tem o número 3:{numeros.index(3)+1}° posição')
else:   print('O número 3 não foi digitado')
print(f'Quais são os pares armazenados na tupla:',end='')
for pares in numeros:   
    if pares%2==0: print(pares,end=',')