# Exercício 1 da lista de listas de listas do 2°Bimestre
# Laurent Chaves Assis Feliciano
# Kaiky Augusto Bedim
# Renato Minoru Nishikawa
# Alberson Wander de Sá
# 2°F - Informática
# 1) Fazer um programa para solicitar ao usuário a digitação de 5 números e armazená-los numa lista. Após armazená-los
# mostre o Maior e o Menor valores e os seus índices na lista. Caso tenha valores iguais e estes forem o maior e/ou menor
# números, mostre todas as posições destes na lista criada. 
Lista=[]
for Contador in range(0,5): 
    Lista.append(input('Digite um número:'))
    if Contador==0: 
        Maior=Lista[0]
        Menor=Lista[0] 
    if Lista[Contador]>Maior:
        Maior=Lista[Contador]
    elif Lista[Contador]<Menor:
        Menor=Lista[Contador]
print(f'Maior valor:{Maior}, posição:{Lista.index(Maior)+1}')
print(f'Menor valor:{Menor}, posição:{Lista.index(Menor)+1}')
if Maior==Menor: 
    print(f'Maior e Menor:{Maior}, posição: 1 a 5')