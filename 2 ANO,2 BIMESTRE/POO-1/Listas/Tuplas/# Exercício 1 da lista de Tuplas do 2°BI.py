# Exercício 1 da lista de Tuplas do 2°Bimestre
# Laurent Chaves Assis Feliciano
# Kaiky Augusto Bedim
# Renato Minoru Nishikawa
# Alberson Wander de Sá
# 2°F - Informática
# 1) Guardar numa tupla números entre 0 e 10 em extenso. Solicite ao usuário para digitar um número pelo teclado
# e mostre o número equivalente por extenso. Exija do usuário a digitação do número no intervalo definido. 

Numeros_em_extenso= ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez')
numero= int(input('Digite um numero entre 0 e 10:'))
while numero >10 or numero <0:
    numero= int(input('Digite um numero entre 0 e 10:'))
for contador in range(11): 
    if numero==contador: print(Numeros_em_extenso[contador])