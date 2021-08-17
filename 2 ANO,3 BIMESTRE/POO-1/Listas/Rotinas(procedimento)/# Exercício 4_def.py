# Exercício 4 da lista de procedimentos do 3° Bimestre
# Laurent Chaves Assis Feliciano
# Kaiky Augusto Bedim
# Renato Minoru Nishikawa
# Alberson Wander de Sá
# 2°F - Informática
# 4) Fazer um programa em python que calcule a área total de uma casa. Para isso, o programa deve possuir uma rotina
# que receba como parâmetro USANDO RECURSO DE EMPACOTAMENTO os nomes de cada cômodo e as suas medidas dos
# comprimentos e larguras. Dentro da rotina, desempacote a tupla recebida e faça o cálculo mostrando o nome e a área
# de cada cômodo, bem como a soma de todas as áreas calculadas e exiba o resultado da área total do imóvel.
def calculo_da_area(*parametro_usando_empacotamento):
    soma_largura=soma_comprimento=soma_areas=0
    area = parametro_usando_empacotamento[1] * parametro_usando_empacotamento[2]
    soma_largura+=parametro_usando_empacotamento[1]
    soma_comprimento+=parametro_usando_empacotamento[2]
    area_da_casa=soma_comprimento*soma_largura
    soma_areas+= area
    print(f'Comodo:{parametro_usando_empacotamento[0]}\nÁrea:{area}\nSoma das areas:{soma_areas}\nÁrea da casa:{area_da_casa}')

    
while True:
    nome_dos_comodos_e_suas_medidas = (input('\n\033[0;33mDigite o nome do cômodo:\033[m'),float(input('\n\033[0;33mDigite a largura do cômodo:\033[m')),float(input('\n\033[0;33mDigite o comprimento do cômodo:\033[m')))
    calculo_da_area(nome_dos_comodos_e_suas_medidas)
    r = input('\n\033[0;33mDeseja continuar o cálculo de área da casa?Digite "nao" para encerrar:\033[m')
    if r=='nao':break