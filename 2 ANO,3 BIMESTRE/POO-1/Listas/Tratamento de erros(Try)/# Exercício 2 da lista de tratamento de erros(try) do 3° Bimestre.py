# Exercício 2 da lista de tratamento de erros(try) do 3°Bimestre
# Laurent Chaves Assis Feliciano
# Kaiky Augusto Bedim
# Renato Minoru Nishikawa
# Alberson Wander de Sá
# 2°F - Informática
# b) Desenvolver um programa que mostre para o usuário o seguinte menu:
# 1- QUADRADO DE UM NÚMERO
# 2- RAIZ CÚBICA DE UM NÚMERO
# 3- FATORIAL DE UM NÚMERO
# Após a exibição do menu acima, o programa deve solicitar que o usuário escolha uma destas opções.
# Crie rotina de tratamento de erro (try) para que o usuário seja obrigado a digitar sempre um número de uma
# opção existente. Se por exemplo ele digitar “um”, ou uma palavra qualquer ao invés do número da opção, o
# programa deve insistir na digitação correta e avisá-lo do motivo do erro. Outras rotinas try devem ser criadas para
# quando o usuário informar um número para cálculos escolhidos. Imagine se ele não digitar número algum e até
# mesmo digitar palavras. Isto não pode acontecer porque o python irá travar.
from math import factorial
while True:
    n=0
    raiz=0
    p=0
    f=1

    try:
        print('''
    1- QUADRADO DE UM NÚMERO
    2- RAIZ CÚBICA DE UM NÚMERO
    3- FATORIAL DE UM NÚMERO
'''
)
        r=int(input('Digite 1, 2 ou 3:'))
        if r==1:
            try:
                n=float(input('Digite um numero:'))
                p=n**2
            except Exception as erro:
                print(f'Ocorreu o erro:{erro}')
            else:
                print(f'Quadrado de {n}={p}')
        if r==2:
            try:
                n=float(input('Digite um numero:'))
                raiz=n**(1/3)
            except Exception as erro:
                print(f'Ocorreu o erro:{erro}')
            else:
                print(f'Raiz cúbica de {n}={raiz}')
        if r==3:
            try:
                n=int(input('Digite um numero:'))
                for c in range(-1,-n-1,-1):
                    f*=c
            except Exception as erro:
                print(f'Ocorreu o erro:{erro}')
            else:
                print(f'Fatorial de {n}={f}')
    except Exception as erro:
        print(f'Digite um valor entre 1 e 3 para não ocorrer o erro {erro}')
    else:
        r=input('Deseja continuar?"n" para nao:')
        if r=='n':   break