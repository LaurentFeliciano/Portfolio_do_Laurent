# Exercício 4 da lista de funções do 3°Bimestre
# Laurent Chaves Assis Feliciano
# Kaiky Augusto Bedim
# Renato Minoru Nishikawa
# Alberson Wander de Sá
# 2°F - Informática
# 4) Criar um programa que solicite ao usuário a digitação de um número. O dado digitado deverá ser um número
# INTEIRO. Caso não tenha sido digitado um número inteiro, o programa deve solicitar novo número. ATENÇÃO:
# NO MÓDULO PRINCIPAL DO PROGRAMA DEVE TER SOMENTE AS DUAS LINHAS DE COMANDO ABAIXO:
# n = digitenumero(“Digite um numero:”)
# print(f“O número inteiro digitado foi {n}”)
#  observações:
# a. Repare que a função se chama “digitenumero”
# b. A função envia a mensagem como parâmetro

def digitenumero(n):
    while True:
        if isinstance(n,int)==False:
            n=input('Digite novamente:')
            if n.isnumeric()==True: n = int(n)
        else:
            print(n)


n = digitenumero('Digite um numero:')
print(f'O número inteiro digitado foi {n}') 