# Algoritmo Bubble Sort em Python
# Feito por:
# Laurent Chaves Assis Feliciano
# 2°F informática- Colégios Univap
# 02/08/21

# Variáveis globais:
numero=list()
# Determinando quantos números vamos comparar do vetor:

quantidade_de_números= int(input('Digite quantos números serão comparados:'))
for contador in range(quantidade_de_números):   numero[contador]=int(input(f'Digite o {contador+1}° número :'))

# Determinando quantas vezes vamos comparar os números do vetor:       
    

while quantidade_de_números >1:
    for contador in quantidade_de_vezes:    
        if numero[contador] > numero[contador+1]:   
            auxiliar=numero[contador]
            numero[contador]=numero[contador+1]
            numero[contador+1]=auxiliar
    quantidade_de_númeross-=1
print(f'Vetor ordenado:{numero[len(numero)+1]}')