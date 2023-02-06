#Exercicio 1
#Qual foi o valor de vendas do melhor mês do Ano? E valor do pior mês do ano?
meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
vendas_1sem = [25000, 29000, 22200, 17750, 15870, 19900]
vendas_2sem = [19850, 20120, 17540, 15555, 49051, 9650]
pior_1 = min(vendas_1sem)
pior_2 = min(vendas_2sem)
if pior_1 < pior_2:
  mes_pior = vendas_1sem.index(pior_1)
  print('O menor valor de vendas foi no mes {}, valendo {}'.format(meses[mes_pior], pior_1))
else:
  mes_pior = vendas_2sem.index(pior_2)
  print('O menor valor de vendas foi no mes {}, valendo {}'.format(meses[mes_pior], pior_2))
maior_1 = max(vendas_1sem)
maior_2 = max(vendas_2sem)
if maior_1 < maior_2:
  mes_melhor = vendas_1sem.index(maior_1)
  print('O maior valor de vendas foi no mes {}, valendo {}'.format(meses[mes_melhor],maior_1))
else:
  mes_melhor = vendas_2sem.index(maior_2)
  print('O maior valor de vendas foi no mes {}, valendo {}'.format(meses[mes_melhor], maior_2))
