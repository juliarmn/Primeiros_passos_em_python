#Estrutura básica
lista_de_frutas = ['maçã', 'laranja', 'goiaba', 'banana']
#Recomendado ser listahomogênea

#Manipular um índice da lista:
print(lista_de_frutas[0])

#Obs: string é imutável, não é possível pegar um item da string e mudar ele, trocar a letra
#Usa a função replace, porém ela muda todas os símbolos iguais ao longo da string:
#Error:
email = 'jua.rod@gmail.com'
email[1] = 'a'
#Mudaria todas iguais:
email = 'jua.rod@gmail.com'
print(email.replace('a', 'i'))


#Descobrindo o índice de um elemento da lista:
lista = ['a', 'b', 'c']
i = lista.index('a')

#Adicionar itens em uma lista:
item_adicionado = 'abacate'
lista_de_frutas.append(item_adicionado)
indice_item_removido = 2
lista_de_frutas.pop(indice_item_removido)
#Ou ainda, para remover:
lista_de_frutas.remove('laranja')
#Tratamento de erros:
#Verificar com if else se o item existe na lista antes de remover com remove

#try e except:
lista_animais = ['urso', 'macaco', 'elefante']
try:
  lista_animais.remove('leão')
except:
  print('Leão não existe na lista')
  
#Comando pass: tipo um continue do C
#Ex: Se der erro no try, não faz nada no except

#Tamanho da lista:
produtos = ['comida', 'bebida', 'roupa']
tamanho = len(produtos)
print('O tamanho é {}'.format(tamanho))

#Maior e menor valor:
vendas = [100, 345, 44, 2]
mais_vendido = max(vendas)
menos_vendido = min(vendas)
print('Mais vendido: {} unidades;\nMenos  vendido: {} unidades'.format(mais_vendido, menos_vendido))

#Juntar 2 listas:
lista_comidas = ['macarrao', 'arroz', 'bolo', 'carne']
novas_comiidas = ['feijão', 'biscoito']
#Método extend:
lista_comidas.extend(novas_comidas)
print(lista_comidas)
#Método +:
todas_comidas = lista_comidas + novas_comidas
print(todas_comidas)
#No append colocaria uma lista dentro de uma lista

