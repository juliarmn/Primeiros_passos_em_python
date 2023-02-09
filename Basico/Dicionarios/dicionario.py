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

