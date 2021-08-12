import teste

lista=[]
cpf=int(input('Digite seu CPF'))
while len(cpf) != 11:
        cpf = (input('\033[4;31mCPF com proporções inválidas, digite novamente:\033[m '))
lista.append(cpf)
print(f'O CPF é {teste.valida_cpf(cpf)}!')
