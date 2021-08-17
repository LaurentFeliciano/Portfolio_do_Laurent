# Exercício 5 da lista de procedimentos do 3° Bimestre
# Laurent Chaves Assis Feliciano
# Kaiky Augusto Bedim
# Renato Minoru Nishikawa
# Alberson Wander de Sá
# 2°F - Informática
# 5) Fazer um programa em python que contenha uma rotina para verificar qual o maior e menor números contidos numa
# lista. O usuário deve digitar vários números e armazená-los na referida lista que será passada como parâmetro. Imprima
# qual número maior e o menor e qual a posição destes números dentro da referida lista. ATENÇÃO, NÃO PERMITA A
# DIGITAÇÃO DE NÚMEROS IGUAIS DENTRO DA LISTA.
lista=list()
def maior_menor(numeros):
    print(numeros)
    for contador in range(0,len(numeros)):
        if contador==0: 
            maior=0 
            menor=numeros[contador]
        if numeros[contador]>maior: maior=numeros[contador]
        elif numeros[contador]<menor: menor=numeros[contador]
    print(f'Maior número é {maior} e está na posição {numeros.index(maior,0)},Menor número é {menor} e está na posição {numeros.index(menor,0)}')

    
while True:
    numero=float(input('Digite um número:'))
    if numero in lista:
        print('Não foi possível inserir este número')
    else: 
        lista.append(numero)
    r=input('Deseja inserir mais um número? Digite qualquer coisa para sim e "nao" para encerrar:')
    if r=='nao':   break
maior_menor(lista)

