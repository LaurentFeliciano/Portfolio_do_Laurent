# Exercício 1 da lista de listas de listas do 2°Bimestre
# Laurent Chaves Assis Feliciano
# Kaiky Augusto Bedim
# Renato Minoru Nishikawa
# Alberson Wander de Sá
# 2°F - Informática
# 1) Fazer um programa para solicitar ao usuário a digitação de 5 números e armazená-los numa lista. Após armazená-los
# mostre o Maior e o Menor valores e os seus índices na lista. Caso tenha valores iguais e estes forem o maior e/ou menor
# números, mostre todas as posições destes na lista criada. 
lista=list()
for contador in range(0,5): 
    lista[contador]=int(input('Digite um número:'))
    if contador==0: maior=lista[contador],menor=lista[contador] 
    if lista[contador]>maior:
        maior=lista[contador]
    elif lista[contador]<menor:
        menor=lista[contador]