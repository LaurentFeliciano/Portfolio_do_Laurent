Arquivo= open('exercicio.alg', 'r+')

Codigo = input('Digite o código do algoritmo:')

while Codigo!= '':
    Arquivo.write(f'{Codigo}\n')
    Codigo = input('Digite o código do algoritmo:')
Leitura =Arquivo.readline()
for Ler in Leitura:
    print(Ler)