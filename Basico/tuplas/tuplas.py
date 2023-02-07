#Listas de valores entre parênteses
#Pode usar sem parênteses (não recomendado)
#Lista imutável
vendas = ('Coca', 2000, 'nome')#Imutável -> pouco flexível
#Vantagem para proteger os dados
# Acessando valores de uma tupla:
produto = vendas[0]
numero = vendas[1]
nome = vendas[3]
#A tupla não pode ser modificada
#Uso de valores heterogêneos

#Unpacking:
#Desmembra os valores da tupla
produto, numero, nome = vendas#Pega cada valor inicial da tupla e atribui a cada variável

#Criar a tupla:
num_vendas = [100, 10, 80, 99]
funcionários = ['A', 'B', 'C', 'D']
for item in enumerate(num_vendas):
  print(item)
#Com unpacking:
num_vendas = [100, 10, 80, 99]
funcionários = ['A', 'B', 'C', 'D']
for item in enumerate(num_vendas):
  i, venda = item 
  print(i)
  print(venda)
#Ou seja, o enumerate transforma os valores em uma tupla

#Lista de tuplas
