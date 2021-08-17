# Exercício 3 da lista de procedimentos do 3° Bimestre
# Laurent Chaves Assis Feliciano
# Kaiky Augusto Bedim
# Renato Minoru Nishikawa
# Alberson Wander de Sá
# 2°F - Informática
# 3) Fazer um programa com uma rotina que verifique se um número passado como parâmetro é ou não primo. 
def e_primo_ou_nao(parametro):
    total_de_divisões=0
    for contador in range (1,parametro+1):
        if parametro%contador ==0:
            print(f'\033[0;32m{contador}', end=' ')
            total_de_divisões+=1
        else:
            print(f'\033[0;31m{contador}', end =' ')
    if total_de_divisões>2:
        print(f'\033[0;33m\n{parametro} não é um numero primo\033[m')
    else:
        print(f'\033[0;33m\n{parametro} é um numero primo\033[m')


numero = int(input('\n\033[0;33mDigite um valor inteiro para verificar se ele é primo ou não:\033[m'))
e_primo_ou_nao(numero)
