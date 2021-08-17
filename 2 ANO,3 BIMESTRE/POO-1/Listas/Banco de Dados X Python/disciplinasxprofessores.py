# Exercício 2 da lista de Banco de dados SQL x Python do 3°Bimestre
# Laurent Chaves Assis Feliciano
# Kaiky Augusto Bedim
# Renato Minoru Nishikawa
# Alberson Wander de Sá
# 2°F - Informática
# 2) Criar um programa Python que cadastre, altere, exclua e consulte registros na tabela “disciplinasxprofessores”.
# Lembrem-se de criar a tabela para receber os registros dentro do banco de dados “univap”. Esta tabela deve ter
# a seguinte estrutura e deve estar relacionada com as tabelas “disciplinas” e “professores”, criadas até então. 
# Este programa deve prever os testes de possiblidades de erros comuns ao acessarmos o banco de dados.
# Também deve ser previsto teste de integridade de dados, ou seja, ao tentarmos incluir um professor, ou
# disciplina que não tenham sido previamente cadastrados, o programa deve informar ao usuário que não foi
# possível realizar o processo.
# Crie possiblidades de consultas para o usuário visualizar quais as disciplinas e professores foram
# previamente cadastrados e que podem ser usados na relação de cadastro e alteração nesta tela.
# Logicamente preveja todos os tipos de erros comuns e trate-os nesta tela. 
from prettytable import PrettyTable

import mysql.connector

def abrir_banco():

    try:

        global BancoDeDados

        BancoDeDados = mysql.connector.Connect(host='localhost',database='univap',user='root', password='')

        if BancoDeDados.is_connected():

            InformacaoBanco = BancoDeDados.get_server_info()

            print(f'Conectado ao servidor banco de dados - Versão {InformacaoBanco}')

            print('Conexão ok')

            global Comandosql

            Comandosql = BancoDeDados.cursor()

            Comandosql.execute('select database();')

            NomeBanco = Comandosql.fetchone()

            print(f'Banco de dados "{NomeBanco}" acessado.')

            print('-'*80)

            return 1

        else:

            print(f'Conexão não realizada com banco {NomeBanco}.')

            return 0

    except Exception as Erro:

        print(f'Ocorreu um erro : {Erro}')

        return 0

def mostrar_disciplinasxprofessores():

    Grid = PrettyTable(['Código da Discipina no Curso','Código da Disciplina', 'Código do Professor' , 'Curso' , 'Carga Horária' , 'Ano Letivo'])

    try:
        Comandosql = BancoDeDados.cursor()

        Comandosql.execute(f'select * from disciplinasxprofessores;')

        Tabela = Comandosql.fetchall()

        if Comandosql.rowcount > 0:

            for Registro in Tabela: Grid.add_row([Registro[0],Registro[1],Registro[2],Registro[3],Registro[4],Registro[5]])

            print(Grid)

        else:   print('Não existe nenhum cadastro no banco de dados da escola.')

    except Exception as Erro:   print(f'Ocorreu um erro: {Erro}')

def consultar_disciplinasxprofessores(cdnc=0):

    try:

        Comandosql = BancoDeDados.cursor()

        Comandosql.execute(f'select * from disciplinasxprofessores where codigodisciplinanocurso = {cdnc};')

        Tabela = Comandosql.fetchall()

        if Comandosql.rowcount > 0:

            for Registro in Tabela:

                print(f'Código da Disciplina: {Registro[1]}, Código do Professor:{Registro[2]}, Curso:{Registro[3]}, Carga Horária:{Registro[4]}, Ano letivo:{Registro[5]}')

                return 'Contém'

        else:   return 'Não Contém'

    except Exception as Erro:   return (f'Ocorreu um erro ao tentar consultar este cadastro: {Erro}')

def cadastrar_disciplinasxprofessores(cdnc=0,cd=0,cp=0,c=0,ch=0,al=0):

    try:

        Comandosql = BancoDeDados.cursor()

        Comandosql.execute(f'insert into disciplinasxprofessores(codigodisciplinanocurso,coddisciplina,codprofessor,curso,cargahoraria,anoletivo)values({cdnc},{cd},{cp},{c},{ch},{al}) ;')

        BancoDeDados.commit()

        return 'Cadastro realizado com sucesso!'

    except Exception as Erro :

        print(f'Ocorreu um erro: {Erro}')

        return 'Não foi possível cadastrar os dados.'

def alterar_disciplinasxprofessores(cdnc=0,cd=0,cp=0,c=0,ch=0,al=0):

    try:

        Comandosql = BancoDeDados.cursor()

        Comandosql.execute(f'Update disciplinasxprofessores SET coddisciplina ={cd}, codprofessor={cp}, curso={c} , cargahoraria={ch} ,anoletivo={al} where codigodisciplinanocurso  = {cdnc};')

        BancoDeDados.commit()

        return 'Disciplinasxprofessores alterado com sucesso.'

    except Exception as Erro:

        print(f'Ocorreu um erro: {Erro}')

        return 'Não foi possível alterar este professor'

def excluir_disciplinasxprofessores(cdnc=0):

    try:

        Comandosql = BancoDeDados.cursor()

        Comandosql.execute(f'delete from disciplinasxprofessores where codigodisciplinanocurso = {cdnc};')

        BancoDeDados.commit()

        return 'Cadastro Excluido com sucesso.'

    except Exception as Erro :

        print(f'Ocorreu um erro: {Erro}')

        return 'Não foi possível excluir este cadastro.'
'''
========================================= MÓDULO PRINCIPAL DO PROGRAMA===============================================
'''
if abrir_banco() == 1:

    Resposta = input('Deseja entrar no módulo de DisciplinasXProfessores?"sim" para entrar e qualquer coisa para sair:')

    while Resposta =='sim':

        print('-'*80)

        print('{:^80}'.format('Banco de Dados UNIVAP - disciplinasxprofessores'))

        print('-'*80)

        while True:

            CodigoDaDisciplinaNoCurso = input('Código da disciplina no curso: (0- Mostra Todas) ')

            if CodigoDaDisciplinaNoCurso.isnumeric():

                CodigoDaDisciplinaNoCurso = int(CodigoDaDisciplinaNoCurso)

                break

        if CodigoDaDisciplinaNoCurso == 0:

            mostrar_disciplinasxprofessores()

            continue

        if consultar_disciplinasxprofessores(CodigoDaDisciplinaNoCurso) == 'Não Contém':
            try:
                CodProfessor= int(input('Digite um Código de Professor válido:'))

                Comandosql= BancoDeDados.cursor()

                Comandosql.execute(f'select * from professores where registro={CodProfessor};')

                Tabela= Comandosql.fetchall()

                if Comandosql.rowcount > 0:

                    CodDisciplina=input('Digite o Código de Disciplina Cadastrado Anteriormente na Tabela Disciplinas:') 

                    Comandosql= BancoDeDados.cursor()

                    Comandosql.execute(f'select * from disciplinas where codigodisc={CodDisciplina};')

                    Tabela= Comandosql.fetchall()

                    if Comandosql.rowcount > 0:

                        Curso = int(input('Informe o Curso do Professor:'))

                        CargaHoraria= int(input('Informe a Carga Horária do(a) Professor(a):'))
                    
                        AnoLetivo= int(input('Informe o Ano Letivo:'))

                        print(cadastrar_disciplinasxprofessores(CodigoDaDisciplinaNoCurso,CodProfessor,CodDisciplina,Curso,CargaHoraria,AnoLetivo))

            except Exception as Erro:   print(f'Ocorreu um erro:{Erro}')
        else:

            Opcoes = input("Escolha: [A]-Alterar [E]-Excluir [C]-Cancelar Operações -> ")

            while Opcoes!='A' and Opcoes!='E' and Opcoes!='C':  Opcoes = input("Escolha entre A , E ou C: [A]-Alterar [E]-Excluir [C]-Cancelar Operações -> ")

            if Opcoes=='A':

                try:
                    print('Atenção: o Código da Disciplina não pode ser alterado: ')
                    
                    CodProfessor= int(input('Digite um Novo Código de Professor válido:'))

                    Comandosql= BancoDeDados.cursor()

                    Comandosql.execute(f'select * from professores where registro={CodProfessor};')

                    Tabela= Comandosql.fetchall()

                    if Comandosql.rowcount > 0:

                        CodDisciplina=input('Digite o Novo Código de Disciplina Cadastrado Anteriormente na Tabela Disciplinas:') 

                        Comandosql= BancoDeDados.cursor()

                        Comandosql.execute(f'select * from disciplinas where codigodisc={CodDisciplina};')

                        Tabela= Comandosql.fetchall()

                        if Comandosql.rowcount > 0:

                            Curso = int(input('Informe o Novo Curso do Professor:'))

                            CargaHoraria= int(input('Informe a Nova Carga Horária do(a) Professor(a):'))
                    
                            AnoLetivo= int(input('Informe o Novo Ano Letivo:'))

                            print(alterar_disciplinasxprofessores(CodigoDaDisciplinaNoCurso,CodProfessor,CodDisciplina,Curso,CargaHoraria,AnoLetivo))

                except Exception as Erro:   print(f'Ocorreu um erro: {Erro}')

            elif Opcoes == 'E':

                Confirmar = input('Confirme a exclusão do professor: SIM caso tenha certeza ou NAO caso deseje cancelar:')

                while Confirmar != 'SIM' and Confirmar != 'NAO':    Confirmar = input('Digite novamente caso queira excluir o professor: SIM caso tenha certeza ou NAO caso deseje cancelar:')

                print (excluir_disciplinasxprofessores(CodigoDaDisciplinaNoCurso))

        print('\n\n')

        print('-'*80)

        if input('Deseja continuar utilizando o programa?"sim" para continuar e qualquer tecla para sair ->') == 'sim': continue

        else:

            break

            Comandosql.close()
        
            BancoDeDados.close()

else:   print('Programa encerrado, Há algum problema na conexão com banco de dados.')