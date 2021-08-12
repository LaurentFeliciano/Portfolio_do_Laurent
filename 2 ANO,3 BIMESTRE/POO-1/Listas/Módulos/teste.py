def valida_cpf(cpf):
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

    dicionario['cpf'] = cpf

    for cont in range(0, 9, 1):
        tabela_cpf.append(dicionario['cpf'][cont])

    for cont in range(0, 9, 1):
        aux = float(tabela_cpf[cont])
        soma = soma + aux * aux_verificador1[cont]

    rest = soma % 11
    if rest < 2:pri_digito = 0
    else:pri_digito = 11 - rest

    soma = 0
    tabela_cpf.append(int(pri_digito))

    for cont in range(0,10,1):
        aux = float(tabela_cpf[cont])
        soma = soma + aux * aux_verificador2[cont]

    rest = soma % 11
    if rest < 2:seg_digito = 0
    else:seg_digito = 11 - rest
    tabela_cpf.append(int(seg_digito))

    for cont in range (0,11,1):
        CPF = f'{CPF}{tabela_cpf[cont]}'

    if dicionario['cpf'] == CPF:dicionario['Condição'] = "Válido"
    else:dicionario['Condição'] = "Inválido"
    return dicionario["Condição"]