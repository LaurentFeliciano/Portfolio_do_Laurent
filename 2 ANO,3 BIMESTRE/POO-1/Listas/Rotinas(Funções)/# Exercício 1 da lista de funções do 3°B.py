# Exercício 1 da lista de funções do 3°Bimestre
# Laurent Chaves Assis Feliciano
# Kaiky Augusto Bedim
# Renato Minoru Nishikawa
# Alberson Wander de Sá
# 2°F - Informática
# 1) Desenvolver um programa python que tenha uma rotina para retornar uma MENSAGEM ao usuário informando
# se ALUNOS estão APROVADOS, REPROVADOS ou EM EXAMES.
# REGRAS:
# a) para ser APROVADO o aluno deve ter tirado média mínima 6;
# b) para estar EM EXAME o aluno deve ter tirado média entre 3.5 e menor que 6;
# c) para ser REPROVADO a média do aluno deve ser menor que 3.5; Neste programa peça ao usuário para digitar
# diretamente a média do aluno. 

def teste():
    global media
    if media>=6:    return 'Aprovado'
    elif media>=3.5 and media<6:    return 'Em Exame'
    elif media<3.5: return 'Reprovado'
media=float(input('Digite a média de um aluno:'))
print(f'O aluno está {teste()}')