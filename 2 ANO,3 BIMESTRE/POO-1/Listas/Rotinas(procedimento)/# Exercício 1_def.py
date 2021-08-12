# Exercício 1 da lista de procedimentos do 3° Bimestre
# Laurent Chaves Assis Feliciano
# Kaiky Augusto Bedim
# Renato Minoru Nishikawa
# Alberson Wander de Sá
# 2°F - Informática
def conversão_para_binario():
    resultado=''
    global variavel_global_qualquer
    while True:
        resto= variavel_global_qualquer%2
        variavel_global_qualquer=variavel_global_qualquer//2
        if resto ==1:
            resultado='1'+ resultado
        else:
            resultado='0'+ resultado
        if variavel_global_qualquer<=1:
            resultado='1'+ resultado
            break
    print(f'Resultado:{resultado}')

    
variavel_global_qualquer = int(input('\nDigite um valor inteiro que será convertido em binário:'))
conversão_para_binario()
