# Exercício 5 da lista de funções do 3°Bimestre
# Laurent Chaves Assis Feliciano
# Kaiky Augusto Bedim
# Renato Minoru Nishikawa
# Alberson Wander de Sá
# 2°F - Informática
# 5) Fazer um programa em python que solicite ao usuário a digitação de vários faturamentos diários de um comércio.
# Passe estes N faturamentos para a função, a qual deverá retornar um DICIONÁRIO com os seguintes dados:
# • Total faturamento
# • Maior faturamento
# • Menor faturamento
# • Faturamento médio
def faturamentos(valores):
    dic=dict()
    total=0
    valores.sort()
    maior= valores[len(valores)-1]
    menor= valores[0]
    for contador in valores:
        total+=contador
    medio=total/len(valores)
    dic['total faturamento']= total
    dic['maior faturamento']= maior
    dic['menor faturamento']= menor
    dic['faturamento médio']= medio
    return dic

lista=[]
while True:
    n=int(input('Digite um faturamento:'))
    lista.append(n)
    if input('Deseja continuar inserindo?"n" para nao')=='n':
        break
for contador,faturamento in faturamentos(lista).items():
    print(f'{contador}={faturamento}')