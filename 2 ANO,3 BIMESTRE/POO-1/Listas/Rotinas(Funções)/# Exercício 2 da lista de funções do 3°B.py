# Exercício 2 da lista de funções do 3°Bimestre
# Laurent Chaves Assis Feliciano
# Kaiky Augusto Bedim
# Renato Minoru Nishikawa
# Alberson Wander de Sá
# 2°F - Informática
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
