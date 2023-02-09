#dicionario = {chave: valor, chave: valor ...}
mais_vendidos = {'livros': 'Os Demônios', ' tecnologia': 'iphone', 'eletrodomestico': 'geladeira'}
#Pode usar tipos de dados diferentes entre chave e valor
#O índice é a chave
vendas = {'Dostoiévsky': '300', 'Dante Alighieri': '200', 'Machado de Assis': '550'}
print(vendas['Machado de Assis'])#Pega a informção pelo valor da chave
#Não podemos ter mais de um item em uma chave
#Antes dicionários não tinham uma ordem, hoje tem, porém, melhor não confiar
#Podia variar a ordem na hora de compilar
#Melhor trabalhar com as chaves
print(mais_vendidos['livros'])#Usa a chave
vendas.get('Dante Alighieri')#Método get para pegar uma informação no dicionário

#A diferença entre usar o get e o índice como chave:
#Se escrever o nome errado, o get dá como r4esposta none(não encontrou nada-> nome da chave errado)
#Usando a chave, dá o erro-> não encontrou a chave

#Verificar se o item está  no dicionário:
if 'Nikolai Gógol' in vendas:
  print(vendas['Nikolai Gógol'])
else:
  print('Não há vendas de livros de Nikolai Gógol')
#Verifica se está no dicionário pelas chaves

#Com .get, usa if 'vendas.get('chave')' == None:

#Adicionar itens no dicionário
#Criação de um dicionário vazio:
dicionario = {}
dicionario[chave] = valor
#Outra opção:
dicionario.update({chave: valor, chave: valor})#Adiciona mais de um valor

#Se adicionar com uma chave já existente, o valor é atualizado apenas

#Remover um item:
del vendas['Machado de Assis']#Retira e joga o item fora
#Ou, ainda:
venda_livro = vendas.pop('Machado de Assis')#Retira do dicionário e guarda em outra variável

#Excluir o dicionário inteiro:
del vendas
#Deletar os índices, mas dicionário ainda existe:
vendas.clear()

#for com dicionários:
for chave in dicionario:
  #comandos

#Métodos dos dicionários:
#Método items:
itens_dicionario = dicionario.items()#Pega todos os itens de um dicionário
#Ou:
for item in dicionario.items():
  print(item)
#Ou, com unpacking:
for produto, preco in vendas.items():
  print('{}; {}'.format(produto, preco))
#keys:
chaves = dicionario.keys()
#Apresenta só as chaves
#Ao adicionar ou retirar valores, as chaves também são atualizadas e modicficadas -> não aplica todos os métodos da lista em python
#Se precisar transformar em lista, usa o .list()

#Values:
valores = dicionario.values()
#Para transformar em lista faz
print(list(valores))#idem para chaves

#Transformando listas em dicionários:
#1-Dicionarios com valores padrões:
#Método from keys:
produtos = ['a', 'b', 'c', 'd', 'e', 'f']
dicionario = dict.fromkeys(produtos, 0)#Valor padrão para os valores
#2- Dicionários a partir de uma lista de tupla:
#Método dict:
dicionario = dict(lista_tuplas)
#3-Duas listas:
#Primeiro transforma as duas listas em uma única lista de tuplas
#Segundo usa o dict
produtos = ['a', 'b', 'c', 'd', 'e', 'f']
vendas = [11, 12, 13, 14, 15, 16]
#Transformar em tupla:
lista_de_tuplas = zip(produtos, vendas)#Método zip
#Tranforma com dict em dicionário
dicionario_vendas = dict(lista_de_tuplas)
#Por dicionário, acessamos dois valores de uma vez só (vantagem)
