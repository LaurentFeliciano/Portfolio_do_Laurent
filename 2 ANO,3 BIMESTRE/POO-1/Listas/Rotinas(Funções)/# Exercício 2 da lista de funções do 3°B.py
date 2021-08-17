# Exercício 2 da lista de funções do 3°Bimestre
# Laurent Chaves Assis Feliciano
# Kaiky Augusto Bedim
# Renato Minoru Nishikawa
# Alberson Wander de Sá
# 2°F - Informática
# 2) Criar um programa python para solicitar ao usuário a digitação de vários números. A cada número digitado,
# chame uma função para realizar a soma dos seus antecessores até o número digitado. Entretanto, o usuário
# deve informar também para cada número digitado ele deseja ver o cálculo que está sendo feito. Assim sendo, a
# função recebe o número digitado e a resposta se deseja ou não ver o processo da soma. VALE INFORMAR O
# PADRÃO DA VISUALIZAÇÃO DO PROCESSO DA SOMA DEVERÁ SER FALSO. Veja os exemplos:
# a. Exemplo se usuário desejar visualizar o processo da soma sendo feito:
# Digite um número: 4
# Deseja visualizar o processo da soma? s: s
# Soma = 1+2+3+4 = 10
# b. Exemplo se usuário NÃO DESEJAR visualizar o processo da soma sendo feito:
# Digite um número: 5
# Deseja visualizar o processo da soma? s: (neste caso se o usuário não informar, por padrão será exibido
# resultado abaixo)
# Soma= 15
#  ATENÇÃO: CRIE O RECURSO PARA ENSINAR O PROGRAMADOR A USAR A FUNÇÃO DA SOMA CASO SEJA USADO
# O COMANDO help() DO PYTHON

def somaAntecessores(n):
    '''
    Esta função retorna a soma dos antecessores do número digitado pelo usuário
    '''
    somaAntecessores=0
    resultado=''
    global r
    for c in range(1,n+1):
        somaAntecessores+=c
        if c==n:
            resultado+=str(c)+'='+str(somaAntecessores)
            return resultado
        if r=='sim':
            resultado+=str(c)+'+'
        else:
            resultado=somaAntecessores
    return resultado


while True:
    num=int(input('Digite um número:'))
    r=input('Deseja visualizar o processo da soma? Digite "sim" caso deseje:')
    print(f'Soma={somaAntecessores(num)}')
    r=input('Deseja continuar inserindo números?"nao" para continuar:')
    if r=='nao':
        break
