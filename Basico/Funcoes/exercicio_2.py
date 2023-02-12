#Análise de indicadores
#Percentual de stockout:
def calcula_stockout(vendas):
  num = 0
  den = 0
  for item in vendas:
    val, status, motivo = vendas[item]
    if status == 'Concluído':
     den += val
    else:
     if motivo == 'Cancelado por falta de estoque':
       den += val
       num += val      
  return (num / den)

vendas = {
          'V0001': (1555, 'Concluído', ''),
          'V0002': (1000, 'Cancelado', 'Cancelado pelo cliente'),
          'V0003': (111, 'Cancelado', 'Cancelado por falta de estoque'),
          'V0004': (14567, 'Concluído', ''),
          'V0005': (1423, 'Cancelado', 'Cancelado pelo cliente')
         }
print('O stockout é {:.2%}'.format(calcula_stockout(vendas)))

#Clientes inadimplentes:
#Deve mais de 1000 reais por 20 dias
def inadimplentes(devedores):
  total = []
  for item in devedores:
    cpf, qtd, dias = item
    if qtd >= 1000 and dias >= 20:
      total.append(cpf)
  return total

devedores = [('053.772.888-99', 1000, 3), 
             ('099.768.999-78', 999, 31), 
             ('021.619.776-29', 5000, 21), 
             ('453.789.448-75', 3000, 12), 
             ('980.778.772-09', 1000, 23)]
print(inadimplentes(devedores))
