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
#shift + tab: mostra dados sobre a função
#Docstrings e annotations: organização do código
#Docstrings dizem o que a função faz e seus argumentos/parâmetros
#Coloca entre 3 aspas: explica o que ela faz, ''' ''', parâmetros e por fim os argumentos->organizado
#Annotations: focado nos parâmetros e resposta da função

#Lembre de tratar erros em funçẽs -> pode usar try, except
#except (tipo específico except) ('')
#Uso do else após o try e except: isola a linha de código que pode dar erro
#finaly: faz independente de dar erro

#Position argument:
#Uso do asterisco: * -> passa quantos argumentos quiser (indefinido)
def soma(*num):
  soma = 0
  for numero in num:
    soma += numero
  return soma

print(soma(1, 2, 44, 55, 6, 77, 8, 90))

#O argumento se torna uma tupla
# **: indica que pode passar quantos argumentos de palavra chave quiser

def preco_prod(preco, **adicional)
  if 'desconto' in adicional:
    preco += 1 - adicional['desconto']
  elif 'imposto' in adicional:
    preco += (1 + adicional['imposto'])
  return preco

print('preco_prod(1000, desconto = 0.1))
#Trabalhou com o dicionário
#Primeiro passa os argumentos de posição e depois os de keywords 
#Sempre argumentos individuais vêm antes e depois os múltiplos

      
      
