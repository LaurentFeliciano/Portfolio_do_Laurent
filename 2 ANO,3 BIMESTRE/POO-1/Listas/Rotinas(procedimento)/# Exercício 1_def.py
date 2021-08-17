# Exercício 1 da lista de procedimentos do 3° Bimestre
# Laurent Chaves Assis Feliciano
# Kaiky Augusto Bedim
# Renato Minoru Nishikawa
# Alberson Wander de Sá
# 2°F - Informática
# 1) Fazer um programa em python para que o usuário digite um número decimal inteiro qualquer e armazene tal número
# em uma variável global qualquer. Em seguida, chame uma rotina SEM PASSAGEM DE PARÂMETRO, para convertê-lo este
# número em binário. A a conversão de decimal para binário deve usar estrutura de repetição que você quiser. Dentro da
# rotina imprima o resultado da conversão.
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
