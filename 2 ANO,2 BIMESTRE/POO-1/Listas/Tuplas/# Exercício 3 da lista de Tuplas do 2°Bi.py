# Exercício 3 da lista de Tuplas do 2°Bimestre
# Laurent Chaves Assis Feliciano
# Kaiky Augusto Bedim
# Renato Minoru Nishikawa
# Alberson Wander de Sá
# 2°F - Informática
# 3) Crie uma tupla com 5 números aleatórios. Logo depois mostre qual o maior e o menor número armazenado.
# Mostre também a tupla com os números que foram sorteados 
import random
NumerosAleatórios=((random.randint(0,100)),(random.randint(0,100)),(random.randint(0,100)),(random.randint(0,100)),(random.randint(0,100)))
NumerosOrganizados=sorted(NumerosAleatórios)
print(NumerosOrganizados[0])
print(NumerosOrganizados[4])
print(NumerosOrganizados)