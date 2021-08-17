# Exercício 1 da lista de tratamento de erros(try) do 3°Bimestre
# Laurent Chaves Assis Feliciano
# Kaiky Augusto Bedim
# Renato Minoru Nishikawa
# Alberson Wander de Sá
# 2°F - Informática
# a) Faça um programa que solicite a digitação de um número inteiro e outro real. Usando tratamentos de erros,
# quando o usuário digitar números de tipos diferentes dos que foram pedidos o programa o programa deve ficar
# pedindo até que ele digite o dado do tipo correto.
while True:
    try:
        n=int(input('Digite um numero inteiro:'))
        r=float(input('Digite um número real:'))
    except:
        print('Digite novamente...:')
    else: 
        print('boa mlk')
        break