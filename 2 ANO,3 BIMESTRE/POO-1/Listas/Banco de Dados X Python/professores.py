# Exercício 1 da lista de Banco de dados SQL x Python do 3°Bimestre
# Laurent Chaves Assis Feliciano
# Kaiky Augusto Bedim
# Renato Minoru Nishikawa
# Alberson Wander de Sá
# 2°F - Informática

# 1) Criar um programa completo em Python para cadastro, alteração, exclusão e consulta a registros da tabela
# professores. Lembrem-se de criar a tabela no mesmo banco de dados “univap”, usado para os exemplos desta apostila:

# O princípio de funcionamento desta tela deve ser o mesmo do programa completo apresentado para
# tela de Dados de Disciplinas, desenvolvida e apresentada em aulas.
# Este programa deve prever testes de consistências gerais, ou seja, exigir do usuário digitação correta do
# nome, telefone, idade e salário do professor.
# Seu programa deve tratar os erros comuns, voltados principalmente a integridade dos dados, ou seja, só
# podemos alterar ou excluir algum professor caso não existam registros de disciplinas ligadas a ele na tabela
# “disciplinasxprofessores”
# Também cuide de tratar os erros comuns de conexão com banco de dados, exemplificados em aula.
# Podem melhorar a aparência das telas de acordo que tenha boa aparência para o usuário final 
# Exercício 1 da lista de Banco de dados SQL x Python do 3°Bimestre
# Laurent Chaves Assis Feliciano
# Kaiky Augusto Bedim
# Renato Minoru Nishikawa
# Alberson Wander de Sá
# 2°F - Informática
def abrir_professores():
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

                print(f'Banco de dados "{NomeBanco}" acessado.')

                print('-'*80)

                return 1

            else:

                print(f'Conexão não realizada com banco {NomeBanco}.')

                return 0

        except Exception as Erro:

            print(f'\033[0;31mOcorreu um erro : {Erro}\033[m')

            return 0

    def mostrar_professores():

        Grid = PrettyTable(['Registro','Nome','Telefone','Idade','Salário'])

        try:
            Comandosql = BancoDeDados.cursor()

            Comandosql.execute(f'select * from professores;')

            Tabela = Comandosql.fetchall()

            if Comandosql.rowcount > 0:

                for Registro in Tabela: Grid.add_row([Registro[0],Registro[1],Registro[2],Registro[3],Registro[4]])

                print(Grid)

            else:   print('Não existem professores cadastrados no banco de dados da escola.')

        except Exception as Erro:   print(f'\033[0;31mOcorreu um erro: {Erro}\033[m')

    def consultar_professor(rp=0):

        try:

            Comandosql = BancoDeDados.cursor()

            Comandosql.execute(f'select * from professores where registro = {rp};')

            Tabela = Comandosql.fetchall()

            if Comandosql.rowcount > 0:

                for Registro in Tabela:

                    print(f'Nome do professor: {Registro[1]}, Telefone do professor:{Registro[2]}, Idade do professor:{Registro[3]}, Salário do professor:{Registro[4]}')

                    return 'Contém'
            
            else:   return 'Não Contém'

        except Exception as Erro:   return (f'\033[0;31mOcorreu um erro ao tentar consultar esta disciplina: {Erro}\033[m')

    def cadastrar_professor(rp=0,np='',tp='',ip=0,sp=0):

        try:

            Comandosql = BancoDeDados.cursor()

            Comandosql.execute(f'insert into professores(registro,nomeprof,telefoneprof,idadeprof,salarioprof)values({rp},"{np}","{tp}",{ip},{sp}) ;')

            BancoDeDados.commit()

            return 'Cadastro do professor realizado com sucesso.'

        except Exception as Erro :

            print(f'\033[0;31mOcorreu um erro: {Erro}\033[m')

            return 'Não foi possível cadastrar o professor.'

    def alterar_professor(rp=0,np='',tp='',ip=0,sp=0):

        try:

            Comandosql = BancoDeDados.cursor()

            Comandosql.execute(f'Update professores SET nomeprof="{np}",telefoneprof="{tp}",idadeprof={ip},salarioprof={sp} where registro = {rp};')

            BancoDeDados.commit()

            return 'Professor alterado com sucesso.'

        except Exception as Erro :

            print(f'\033[0;31mOcorreu um erro: {Erro}\033[m')

            return 'Não foi possível alterar este professor'

    def excluir_professor(rp=0):

        try:
            Comandosql = BancoDeDados.cursor()

            Comandosql.execute(f'select * from disciplinasxprofessores where codprofessor={rp};')

            Comandosql.fetchall()
            
            if Comandosql.rowcount==0:

                Comandosql.execute(f'delete from professores where codprofessor = {rp};')

                BancoDeDados.commit()

                return 'Professor excluído com sucesso.'
                
            else:   print('Não é Possível excluir a Disciplina pois ela está atribuida à algum professor')

            return 'Professor excluído com sucesso.'

        except Exception as Erro :

            print(f'\033[0;31mOcorreu um erro: {Erro}\033[m')

            return 'Não foi possível excluir este professor.'
    '''
    ========================================= MÓDULO PRINCIPAL DO PROGRAMA ===============================================
    '''

    if abrir_banco() == 1:

        Resposta = input('Deseja entrar no módulo de Professores?"sim" para entrar e qualquer coisa para sair:')

        while Resposta =='sim':

            print('-'*80)

            print('{:^80}'.format('Banco de Dados UNIVAP - Professores'))

            print('-'*80)

            while True:

                Registro = input('Registro do professores (0- Mostra Todas):')

                if Registro.isnumeric():

                    Registro = int(Registro)

                    break

            if Registro == 0:

                mostrar_professores()

                continue

            if consultar_professor(Registro) == 'Não Contém':
                try:
                    NomeProfessor = input('Nome do professor:')

                    TelefoneProfessor = input('Telefone do professor(formato:(##)#####-#### ):')

                    while len(TelefoneProfessor) != 14:

                        TelefoneProfessor = input('Digite um Telefone do professor válido(formato:(##)#####-#### ):')

                    IdadeProfessor = int(input('Idade de professor:'))

                    while IdadeProfessor>=150 and IdadeProfessor<=13:

                        IdadeProfessor = int(input('Digite uma Idade do Professor válida:'))

                    SalarioProfessor = float(input('Salário de professor(Somente Dígitos):'))

                    print(cadastrar_professor(Registro,NomeProfessor,TelefoneProfessor,IdadeProfessor,SalarioProfessor))

                except Exception as Erro:   print(f'\033[0;31mOcorreu um erro:{Erro}\033[m')
            else:

                Opcoes = input("Escolha: [A]-Alterar [E]-Excluir [C]-Cancelar Operações -> ")

                while Opcoes!='A' and Opcoes!='E' and Opcoes!='C':  Opcoes = input("Escolha entre A , E ou C: [A]-Alterar [E]-Excluir [C]-Cancelar Operações -> ")

                if Opcoes=='A':

                    try:
                        NomeProfessor = input('Nome do novo professor:')

                        TelefoneProfessor = input('Telefone do novo professor(formato:(##)#####-#### ):')

                        while len(TelefoneProfessor) != 14:

                            TelefoneProfessor = input('Digite um Telefone do novo professor (formato:(##)#####-#### ):')

                        IdadeProfessor = int(input('Idade do novo professor:'))

                        while IdadeProfessor>=150 and IdadeProfessor<=13:

                            IdadeProfessor = int(input('Digite uma Idade de Professor válida:'))

                        SalarioProfessor = float(input('Salário de professor(Somente Dígitos):'))

                        print(alterar_professor(Registro,NomeProfessor,TelefoneProfessor,IdadeProfessor,SalarioProfessor))

                    except Exception as Erro:   print(f'\033[0;31mOcorreu um erro: {Erro}\033[m')

                elif Opcoes == 'E':

                    Confirmar = input('Confirme a exclusão do professor: SIM caso tenha certeza ou NAO caso deseje cancelar:')

                    while Confirmar != 'SIM' and Confirmar != 'NAO':    Confirmar = input('Digite novamente caso queira excluir o professor: SIM caso tenha certeza ou NAO caso deseje cancelar:')

                    print(excluir_professor(Registro))

            print('\n\n')

            print('-'*80)

            if input('Deseja continuar utilizando o programa?"sim" para continuar e qualquer tecla para sair ->') == 'sim': continue

            else:

                break

                Comandosql.close()
            
                BancoDeDados.close()

    else:   print('Programa encerrado, Há algum problema na conexão com banco de dados.')