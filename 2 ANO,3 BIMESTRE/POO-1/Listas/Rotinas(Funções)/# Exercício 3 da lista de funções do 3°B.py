# Exercício 3 da lista de funções do 3°Bimestre
# Laurent Chaves Assis Feliciano
# Kaiky Augusto Bedim
# Renato Minoru Nishikawa
# Alberson Wander de Sá
# 2°F - Informática
# 3) Criar um programa python com uma função que receba parâmetros opcionais do nome e idade de uma pessoa.
# O programa deve informar mostrar o nome da pessoa e se ela é, ou não, maior de idade. ATENÇÃO: O NOME
# E/OU A IDADE DA PESSOA PODEM NÃO TEREM SIDO INFORMADOS E A FUNÇÃO DEVE CUIDAR DESTE CASO, VISTO
# QUE ESTAMOS USANDO UMA FUNÇÃO COM PARÂMETROS OPCIONAIS. 
def teste(n='ninguem',i='0'):
    if i.isnumeric()==True: i = int(i)
    if i>=18:   
        print(f'Nome:{n},Maior de idade')
    elif i<18 and idade>0:   
        print(f'Nome:{n},Menor de idade')
    elif i==0:  
        print(f'Nome:{n},O usuário preferiu não inserir sua idade')


nome=input('Digite seu nome:')
idade=input('Digite sua idade:')
teste(nome,idade)