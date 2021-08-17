def valida_cpf(cpf):
    # Laurent Chaves Assis Feliciano
    # Kaiky Bedim
    # Renato Minoru Nishikawa
    # 2°F Informática
    # 25/05/2021
    # POOI 2° Bimestre
    # Alberson Wander

    # --------------------------------------------------------------------------------------------------------------------------#

    # Variáveis Percentuais e Estatísticas:

    qnt_cpf_testados=0
    qnt_cpf_validos=0
    qnt_cpf_invalidos=0
    porcent_invalidos=0
    porcent_validos=0


    # Variáveis Usuais durante o Código:

    dicionario={}
    lista = []
    aux_verificador1 = (10, 9, 8, 7, 6, 5, 4, 3, 2)
    aux_verificador2 = (11, 10, 9, 8, 7, 6, 5, 4, 3, 2)
    soma = 0
    aux = 0
    tabela_cpf = []
    CPF = ""


    # Início do Código:

    # Início do Teste de CPF:

    dicionario['cpf'] = cpf

        # Teste de dimensão do CPF:
    while len(dicionario['cpf']) != 11:
            dicionario['cpf'] = (input('\033[4;31mCPF com proporções inválidas, digite novamente:\033[m '))


    # Verificador do 1° Dígito:

        # Passando os 9 primeiros dígitos para a tabela_cpf:

    for cont in range(0, 9, 1):
        tabela_cpf.append(dicionario['cpf'][cont])

        # Fazendo a multiplicação e a soma para gerar o Primeiro Dígito Verificador:

    for cont in range(0, 9, 1):
        aux = float(tabela_cpf[cont])
        soma = soma + aux * aux_verificador1[cont]

        # Divisão do número gerado anteriormente por 11 e definição do Primeiro Dígito:

    rest = soma % 11
    if rest < 2:
        pri_digito = 0
    else:
        pri_digito = 11 - rest

        # Verificador do 2º Dígito:

        # Zerando a variável soma e adicionando o pri_digito a tabela_cpf:
    soma = 0
    tabela_cpf.append(int(pri_digito))

        # Fazendo a multiplicação e a soma para gerar o Segundo Dígito Verificador:

    for cont in range(0,10,1):
        aux = float(tabela_cpf[cont])
        soma = soma + aux * aux_verificador2[cont]

        # Divisão do número gerado anteriormente por 11 e definição do Segundo Dígito:

    rest = soma % 11
    if rest < 2:
        seg_digito = 0
    else:
        seg_digito = 11 - rest
    tabela_cpf.append(int(seg_digito))

        # Gerando o CPF com o primeiro e segundo dígito na variável CPF:

    for cont in range (0,11,1):
        CPF = f'{CPF}{tabela_cpf[cont]}'

        # Determinação da validação do CPF:

    if dicionario['cpf'] == CPF:
        dicionario['Condição'] = "Válido"

    else:
        dicionario['Condição'] = "Inválido"

    return dicionario['Condição']

