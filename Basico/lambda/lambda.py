#Funções em iterables:
#Método para aplicar a função em cada item do iterable
#função map
#list_2 = list(map(função, iterable incial))
def padronizar_cpf(cpf):
    cpf = '{}.{}.{}-{}'.format(cpf[:3], cpf[3:6], cpf[6:9], cpf[9:])
    return cpf
  
cpf = ['02874334472', '33518043420', '55621733100', '54261536390', '97564615273']
for i, item in enumerate(cpf):
  cpf[i] = padronizar_cpf(item)
print(cpf)
#Usando o map
cpf = list(map(padronizar_cpf, cpf))
print(cpf)

#Usando function no iterable no sort:
#sort aplica uma function em cada elemento da lista
#sort modifica a lista inicial
#sorted cria uma nova lista
#no sort temos o key (chave para ordenar) como parâmetro
#Podemos usar a key para ordenar tudo como se fosse letra minúscula sem modificar a lista, por exemplo
celulares = ['apple', 'Samsung', 'Iphone', 'galaxy']
#Com o sort apenas, sem a key (usa ASCII):
celulares.sort()
print(celulares)
#Com a key:
celulares.sort(key = str.casefold)
print(celulares)[
#Ordenar uma lista de tuplas pelo segundo valor
dicionario = {'gato': 7, 'cachorro': 5, 'passarinho': 8}
lista_dici = list(dicionario.items())
print(lista_dici)
#Lá em cima cria uma função que devolve o segundo valor da tupla
def segundo(tupla):
    return tupla[1]
lista_dici.sort(key=segundo)
print(lista_dici)

#Lambda expressions:
#Funções anônimas
#Ação única -> evitar fazer funções só para isso
#minha_function = lambda parâmetro: expressão
def multiplica_por_2(num):
    return num * 2
#Lambda:
multiplica_por_2 = lambda num: num * 2
#Aplicações da Lambda expression:
#Usar como parâmetro dentro de uma função
#Passar como parâmetro uma função para um método

#Função filter: filtra uma lista, ou tupla, etc
#Resposta é todos os itens do iterable cuja a função retorna true
#filter(function, iterable)
#list(filter(lambda num: num > 2000, dicionario.items()))
