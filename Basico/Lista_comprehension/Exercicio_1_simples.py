#A lista abaixo apresenta os produtos, a qauntidade vendida em 2019 e, por fim, a vendida em 2020
#Faça por list compreension apenas os produtos de 2019 -> ideia de exercício da hashtag treinamentos
vendas = [('A', 456, 890), ('B', 780, 880), ('C', 900, 809)]

lista_2019 = [prod_2019 for prod, prod_2019, prod_2020 in vendas]
print(lista_2019)
#Descubra o valor mais vendido em 2019:
lista_2019_2 = [(prod, prod_2019) for  prod, prod_2019, prod_2020 in vendas]
print(max(lista_2019_2))
