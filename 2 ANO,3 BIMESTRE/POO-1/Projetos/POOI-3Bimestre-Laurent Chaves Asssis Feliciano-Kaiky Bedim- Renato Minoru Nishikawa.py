# Projeto de Python do 3°Bimestre
# Laurent Chaves Assis Feliciano
# Kaiky Augusto Bedim
# Renato Minoru Nishikawa
# Alberson Wander de Sá
# 2°F - Informática

# PROJETO 3º BIMESTRE – POOI – PROFESSOR ALBERSON WANDER
# Regras gerais:
# Este projeto deve ser feito em grupo de 3 alunos
# Entrega na semana segunda semana g2 do 3º bimestre
# Cópias de projetos serão zerados


# 1)	Criar um programa completo em Python para cadastro, alteração, exclusão e consulta a registros da tabela professores. Lembrem-se de criar a tabela no mesmo banco de dados “univap”, usado para os exemplos DADOS EM AULA DO 3º BIMESTRE: 
 
# O princípio de funcionamento desta tela deve ser o mesmo do programa completo apresentado para tela de Dados de Disciplinas, desenvolvida e apresentada em aulas.
# Este programa deve prever testes de consistências gerais, ou seja, exigir do usuário digitação correta do nome, telefone, idade e salário do professor. 
# Seu programa deve tratar os erros comuns, voltados principalmente a integridade dos dados, ou seja, só podemos alterar ou excluir algum professor caso NÃO EXISTAM registros de disciplinas ligadas a ele na tabela “disciplinasxprofessores”
# Também cuide de tratar os erros comuns de conexão com banco de dados, exemplificados em aula.
# Podem melhorar a aparência das telas de acordo que tenha boa aparência para o usuário final
# 2)	Criar um programa Python que cadastre, altere, exclua e consulte registros na tabela “disciplinasxprofessores”. Lembrem-se de criar a tabela para receber os registros dentro do banco de dados “univap”. Esta tabela deve ter a seguinte estrutura e deve estar relacionada com as tabelas “disciplinas” e “professores”, criadas até então.

 
# 		Este programa deve prever os testes de possiblidades de erros comuns ao acessarmos o banco de dados. 
# Também deve ser previsto teste de integridade de dados, ou seja, ao tentarmos incluir um professor, ou disciplina que não tenham sido previamente cadastrados, o programa deve informar ao usuário que não foi possível realizar o processo.
# Crie possiblidades de consultas para o usuário visualizar quais as disciplinas e professores foram previamente cadastrados e que podem ser usados na relação de cadastro e alteração nesta tela.
#  Logicamente preveja todos os tipos de erros comuns e trate-os nesta tela. 


# Observação final:
# - Caso o usuário tente excluir algum professor, ou disciplina, que estejam relacionados na tabela disciplinasxprofessores este NÃO PODERÁ SER EXCLUÍDO. AVISE AO USUÁRIO. ESTE PROCESSO PODE SER TRATADO COM TRY, ou então através de consulta. 
import disciplinasxprofessores
import disciplinas
import professores

print('-'*80)

print('\033[1;35mPrograma de Manipulação de um Banco de Dados utilizando Python e MySQL\033[m\n')

while True:
    try:
        print('''\033[0;32m
        Tabelas Possíveis de serem acessadas:

        [1]-Disciplinas
        [2]-Professores
        [3]-Disciplinasxprofessores
        [4]-Nenhuma
        \033[m
        ''')
        Resposta = int(input('\033[34mDeseja acessar qual tabela?Caso não queira acessar nenhuma, digite 4:\033[m'))

        while Resposta !=1 and Resposta !=2 and Resposta !=3 and Resposta !=4: Resposta = int(input('Resposta inválida, digite novamente:'))

    except Exception as Erro:   print(f'\033[0;31mOcorreu um erro: {Erro}\033[m]')

    if Resposta == 1:   disciplinas.abrir_disciplinas()

    if Resposta == 2:   professores.abrir_professores()

    if Resposta == 3:   disciplinasxprofessores.abrir_disciplinasxprofessores()

    if Resposta == 4: break

print('\033[1;35mObrigado por utilizar nosso programa!\033[m\n\033[0;33mCriadores:\nLaurent Chaves Assis Feliciano\nKaiky Augusto Bedim\nRenato Minoru Nishikawa\033[m\n\033[0;35m2°F- Informática\033[m')
