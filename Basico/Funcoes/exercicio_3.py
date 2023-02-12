#Vendedores que bateram a meta em percentual:
def calculo_meta(vendas, meta):
  lista_vendedores = []
  total = len(vendas)
  total_meta = 0
  for item in vendas:
    if vendas[item] >= meta:
      lista_vendedores.append(item)
  return (lista_vendedores, (len(lista_vendedores)/total)*100)
      
  
vendas = {
  'Julia': 1300,
  'Diego': 1222,
  'Rafael': 1223,
  'Maria': 1555
}

meta = int(input('Qual era a meta? '))
print(calculo_meta(vendas, meta))
