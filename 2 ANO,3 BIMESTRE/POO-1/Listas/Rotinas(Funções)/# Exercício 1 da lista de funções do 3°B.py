# Exercício 1 da lista de funções do 3°Bimestre
# Laurent Chaves Assis Feliciano
# Kaiky Augusto Bedim
# Renato Minoru Nishikawa
# Alberson Wander de Sá
# 2°F - Informática
def teste():
    global media
    if media>=6:    return 'Aprovado'
    elif media>=3.5 and media<6:    return 'Em Exame'
    elif media<3.5: return 'Reprovado'
media=float(input('Digite a média de um aluno:'))
print(f'O aluno está {teste()}')