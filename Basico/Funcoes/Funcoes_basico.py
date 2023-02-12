#Funções são criadas e definidas pelo def
def acha_seq(nome):
  if 'ana' in nome:
    return True
  else:
    return False
#Uma função não necessariamente precisa retornar um valor
#O código principal fica embaixo da função
#Subdivisão de tarefas

#Funções com parâmetro de valor padrão, exemplo:
def padroniza_cod(codigos, padrao = 'M'):#padroniza tudo para letra maiuscula
  #Já tem o valor default
  #item = no for modifica só a variável item, não lista, devemos usar também o index para mudar
  for item, i in enumerate(codigos):
    item.replace(' ', '')
    item = item.replace
    item = item.strip()
    if padrao == 'M':
      item = item.upper()
    elif padrao == 'm':
      item = item.casefold()
    lista[i] = item
return codigos
     
#Lembre, com return, a function encerra imediatamente

#Return com mais de um objeto:
#Coloca os valores em uma tupla e devolde ela como resposta
def multiplicacao_divisao (num_1, num_2):
  multiplicacao = num_1 * num_2
  divisao = num_1 * num_2
  return(multiplicacao, divisao)#Retornou uma tupla -> não precisa dos (), pois por padrão ele retorna uma tupla


