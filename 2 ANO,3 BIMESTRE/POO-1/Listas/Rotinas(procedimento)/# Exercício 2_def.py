# Exercício 2 da lista de procedimentos do 3° Bimestre
# Laurent Chaves Assis Feliciano
# Kaiky Augusto Bedim
# Renato Minoru Nishikawa
# Alberson Wander de Sá
# 2°F - Informática
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
