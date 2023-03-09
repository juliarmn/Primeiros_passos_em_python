#Forma de iterar itens da lista de forma mais direta
#única linha de código
#É um extra
#Exemplo
preco_livro = [20, 50, 80, 60]
livro = ['Hamlet', 'Metamorfose', 'Mobby Dick', 'Crime e Castigo']
#Colocando imposto de 40% com for:
imposto = []
for unidade in preco_livro:
    imposto.append(unidade * 0.4)
print(imposto)
#Lista Comprehension:
imposto = [unidade * 0.4 for unidade in preco_livro]
print(imposto)
#Pode usar uma function também:
#Criar uma sequência a partir de uma sequência numérica
def calcular_prox (n):
  return (5 * n) + 3

elem = [1, 2, 3, 4, 5, 6, 7, 8]
sequencia = [calcular_prox(elemento) for elemento in elem]
print(sequencia)
#Se a lista for muito grande, o list comprehension pode ser lento!!! -> prejudica a otimização

#Unpacking com list comprehension:
vendas = [200, 800, 700, 600, 900]
vendedores = ['Lucas', 'Júlia', 'Marta', 'Diego', 'Vanessa']
#Criar uma lista de tuplas para podermos ordenar sem perder nenhum dado:
lista_ordenada = list(zip(vendas, vendedores))
#Ordenar decrescente:
lista_ordenada.sort(reverse=True)
#Unpacking com list comprehension, retornar ao original, mas ordenado:
vendedores = [vendedores for vendas, vendedores in lista_ordenada]
print(vendedores)

#Filtrando com if:
idade = [30, 70, 80, 60, 40, 20]
#Com o for:
isento = []
idade_min = 60

for i, item in enumerate(idade):
    if idade[i] >= idade_min:
        isento.append(idade[i])
print(isento)

#list comprehension:
isento_2 = [item for i,item in enumerate(idade) if idade[i] >= idade_min]
print(isento)
#Não esquecer da estrutura:
#list = [item if condição else outro_item for item in iterable]

#List comprehension não serve só para criar listas
