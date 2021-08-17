# Exercício 1 da lista de Banco de dados SQL x Python do 3°Bimestre
# Laurent Chaves Assis Feliciano
# Kaiky Augusto Bedim
# Renato Minoru Nishikawa
# Alberson Wander de Sá
# 2°F - Informática
from prettytable import PrettyTable

import mysql.connector

def abrir_banco():

    try:

        global BancoDeDados

        BancoDeDados = mysql.connector.Connect(host='localhost',database='univap',user='root', password='')

        if BancoDeDados.is_connected():

            InformacaoBanco = BancoDeDados.get_server_info()

            print(f'Conectado ao servidor banco de dados - Versão {InformacaoBanco}')

            print('Conexão estabelecida')

            global Comandosql

            Comandosql = BancoDeDados.cursor()

            Comandosql.execute('select database();')

            NomeBanco = Comandosql.fetchone()

            print(f'Banco de dados acessado = {NomeBanco}')

            print('='*80)

            return 1

        else:

            print(f'Conexão não realizada com banco {NomeBanco}.')

            return 0

    except Exception as Erro:

        print(f'Ocorreu um erro : {Erro}')

        return 0

def mostrar_disciplinas():

    Grid = PrettyTable(['Códigos das Disciplinas', "Nomes de Disciplinas"])

    try:
        Comandosql = BancoDeDados.cursor()

        Comandosql.execute(f'select * from disciplinas;')

        Tabela = Comandosql.fetchall()

        if Comandosql.rowcount > 0:

            for Registro in Tabela: Grid.add_row([Registro[0],Registro[1]])

            print(Grid)

        else:   print('Não existem disciplinas cadastrados no banco de dados da escola.')

    except Exception as Erro:   print(f'Ocorreu um erro: {Erro}')

def consultardisciplina(cd=0):

    try:

        Comandosql = BancoDeDados.cursor()

        Comandosql.execute(f'select * from disciplinas where codigodisc = {cd};')

        Tabela = Comandosql.fetchall()

        if Comandosql.rowcount > 0:

            for Registro in Tabela:

                print(f'Nome da Disciplina: {Registro[1]}')

                return 'Contém'

        else:   return 'Não Contém'

    except Exception as Erro:   return (f'Ocorreu erro ao tentar consultar esta disciplina: Erro -> {Erro}')

def cadastrardisciplina(cd=0,nd=''):

    try:

        Comandosql = BancoDeDados.cursor()

        Comandosql.execute(f'insert into disciplinas(codigodisc, nomedisc)values({cd},"{nd}") ;')

        BancoDeDados.commit()

        return 'Cadastro da disciplina realizado com sucesso.'

    except Exception as Erro:

        print(f'Ocorreu um erro: {Erro}')

        return 'Não foi possível cadastrar esta disciplina.'

def alterardisciplina(cd=0, nomedisciplina=''):

    try:

        Comandosql = BancoDeDados.cursor()

        #criando comando update para atulizar o nome da disciplina em questão

        Comandosql.execute(f'Update disciplinas SET nomedisc="{nomedisciplina}" where codigodisc = {cd};')

        #método commit é responsável por REGRAVAR de fato o novo NOME DA DISCIPLINA disciplina na tabela

        BancoDeDados.commit()

        return 'Disciplina alterada com sucesso.'

    except Exception as Erro :

        print(f'Ocorreu um erro: {Erro}')

        return 'Não foi possível alterada esta disciplina'

def excluirdisciplina(cd=0):

    try:

        Comandosql = BancoDeDados.cursor()

        Comandosql.execute(f'select * from disciplinasxprofessores where coddisciplina={cd};')

        if Comandosql.rowcount==0:

            Comandosql.execute(f'delete from disciplinas where codigodisc = {cd};')

            BancoDeDados.commit()

            return 'Disciplina excluída com sucesso.'

        else:   print('Não é Possível excluir a Disciplina pois ela está atribuida à algum professor')
    except Exception as Erro:

        print(f'Ocorreu um erro: {Erro}')

        return 'Não foi possível excluir esta disciplina.'
'''
========================================= MÓDULO PRINCIPAL DO PROGRAMA===============================================
'''
if abrir_banco() == 1:

    Resposta = input('Deseja entrar no módulo de Disciplinas?"sim" para entrar e qualquer coisa para sair:')

    while Resposta =='sim':

        print('='*80)

        print('{:^80}'.format('Banco de Dados UNIVAP - Disciplinas'))

        print('='*80)

        while True:

            try:
                CodigoDisc = input('Código da Disciplina (0- Mostra Todas):')

                if CodigoDisc.isnumeric():

                    CodigoDisc = int(CodigoDisc)

                    break

            except Exception as Erro:   print(f'Ocorreu um erro: {Erro}')

        if CodigoDisc == 0:

            mostrar_disciplinas()

            continue

        if consultardisciplina(CodigoDisc) == 'Não Contém':

            NomeDisciplina = input('Nome da Disciplina:')
            
            print(cadastrardisciplina(CodigoDisc,NomeDisciplina))

        else:

            Opcoes = input("Escolha: [A]-Alterar [E]-Excluir [C]-Cancelar Operações ==>")

            while Opcoes!='A' and Opcoes !='E' and Opcoes !='C':    Opcoes = input("Escolha Entre: [A]-Alterar [E]-Excluir [C]-Cancelar Operações ->")

            if Opcoes=='A':

                print('Atenção: Código da disciplina não pode ser alterado:')

                NomeDisciplina = input('Informe novo nome da disciplina:')

                print(alterardisciplina(CodigoDisc, NomeDisciplina))
                
            elif Opcoes == 'E':

                Confirmar = input('Confirme a exclusão do professor: SIM caso tenha certeza ou NAO caso deseje cancelar:')

                while Confirmar != 'S' and Confirmar != 'N':    Confirmar = input('Digite novamente caso queira excluir o professor: SIM caso tenha certeza ou NAO caso deseje cancelar:')

                print([excluirdisciplina(CodigoDisc)])

        print('\n\n')

        print('='*80)

        if input('Deseja continuar utilizando o programa?"sim" para continuar e qualquer tecla para sair ->') == 'sim':    continue
        else:
            break

            Comandosql.close()
        
            BancoDeDados.close()

else:   print('Programa encerrado, Há algum problema na conexão com banco de dados.')