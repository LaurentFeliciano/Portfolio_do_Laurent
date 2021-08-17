# Exercício 1 da lista de Tuplas do 2°Bimestre
# Laurent Chaves Assis Feliciano
# Kaiky Augusto Bedim
# Renato Minoru Nishikawa
# Alberson Wander de Sá
# 2°F - Informática
# 1) Guardar numa tupla números entre 0 e 10 em extenso. Solicite ao usuário para digitar um número pelo teclado
# e mostre o número equivalente por extenso. Exija do usuário a digitação do número no intervalo definido. 
NumerosExtenso= ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez')
N= int(input('Digite um numero entre 0 e 10:'))
while N >10 or N <0:
    N= int(input('Digite um numero entre 0 e 10:'))
for C in range(11): 
    if N==C: print(NumerosExtenso[C])