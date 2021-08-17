# Exercício 2 da lista de procedimentos do 3° Bimestre
# Laurent Chaves Assis Feliciano
# Kaiky Augusto Bedim
# Renato Minoru Nishikawa
# Alberson Wander de Sá
# 2°F - Informática
# 2) Refaça o programa 1, de tal forma que o usuário possa passar o número decimal digitado como parâmetro para rotina.
# Depois de passar este número como parâmetro e imprimir o resultado da conversão para binário, chame a rotina
# novamente no módulo principal do programa, porém desta vez, passando como parâmetro o número 59. Com isso, o
# programa dever exibir também o resultado desta conversão.
def conversão_para_binario(parametro):
    resultado=''
    while True:
        resto= parametro%2
        parametro=parametro//2
        if resto ==1:
            resultado='1'+ resultado
        else:
            resultado='0'+ resultado
        if parametro<=1:
            resultado='1'+ resultado
            break
    print(f'\033[0;33mResultado:{resultado}\033[m')

    
variavel_global_qualquer = int(input('\n\033[0;33mDigite um valor inteiro que será convertido em binário:\033[m'))
conversão_para_binario(variavel_global_qualquer)
conversão_para_binario(59)
