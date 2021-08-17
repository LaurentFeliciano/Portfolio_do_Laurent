# Exercício 1 da lista de módulos do 3°Bimestre
# Laurent Chaves Assis Feliciano
# Kaiky Augusto Bedim
# Renato Minoru Nishikawa
# Alberson Wander de Sá
# 2°F - Informática
# 1) Crie um módulo CHAMADO TESTE.PY que possua as seguintes funções:
# a. Valida_CPF: Esta função deverá receber um parâmetro UM CPF EMPACOTADO. Em seguida,
# desempacote-o; verifique se é CPF recebido é ou não válido e retorne uma mensagem “CPF VÁLIDO” OU
# “CPF INVÁLIDO” para o programa que o chamou.
# b. CRIE UM PROGRAMA QUALQUER QUE IMPORTE O MÓDULO TESTE.PY e use a função Valida_CPF,
# passando como parâmetro uma lista com os números de um cpf informado pelo usuário. Este programa
# irá receber e exibir a mensagem retornada pela função Valida_CPF.
# c. Este programa deve terminar quando o usuário desejar.
from teste import valida_cpf 
while True:
    cpf=input('Digite um cpf:')
    print(f'O CPF é {valida_cpf(cpf)}!')
    r=input('Deseja continuar?"n" para nao:') 
    if r == 'n':
        break


