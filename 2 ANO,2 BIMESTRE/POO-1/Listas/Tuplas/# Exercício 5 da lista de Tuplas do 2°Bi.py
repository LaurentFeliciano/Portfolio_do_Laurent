# Exercício 5 da lista de Tuplas do 2°Bimestre
# Laurent Chaves Assis Feliciano
# Kaiky Augusto Bedim
# Renato Minoru Nishikawa
# Alberson Wander de Sá
# 2°F - Informática
# Criar uma tupla contendo produtos e seus respectivos preços (tudo numa só tupla). Logo depois imprima para o
# usuário uma lista exatamente formatada como no exemplo abaixo:
tabela_de_preços=('Pai rico,Pai pobre',44.88,'Quem pensa, enriquece',19.90,'O homem mais rico da babilônia',15.89,'O segredo',44.90,
'O maior segredo',29.89,'Os segredos da mente milionária',29.90,'O poder do hábito',29.89,'Mais esperto que o diabo',24.50,
'O milagre da manhã',20.30,'Trabalhe 4 horas por dia',35.46)
print("="*50)
print("{:^50}".format("LISTAGEM DE PREÇOS"))
print("="*50)
for contador in range(0, len(tabela_de_preços), 2):
    print(f"{tabela_de_preços[contador]:.<40}", f" R$ {tabela_de_preços[contador+1]:>7.2f}")
print("="*50)