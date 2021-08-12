# Exercício 3 da lista de funções do 3°Bimestre
# Laurent Chaves Assis Feliciano
# Kaiky Augusto Bedim
# Renato Minoru Nishikawa
# Alberson Wander de Sá
# 2°F - Informática
def teste(n='ninguem',i=0):
    if i.isdigit(): i = int(i)
    if i>=18:   
        print(f'Nome:{n},Maior de idade')
    elif i<18 and idade>0:   
        print(f'Nome:{n},Menor de idade')
    elif i==0:  
        print(f'Nome:{n},O usuário preferiu não inserir sua idade')


nome=input('Digite seu nome:')
idade=input('Digite sua idade:')
teste(nome,idade)