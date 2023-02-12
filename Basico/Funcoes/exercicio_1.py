#Função que calcula a carga tributária sobre um produto:
def carga_tributaria(custo, lucro, preco):
    imposto = preco - custo - lucro
    return (imposto / preco)

preco = int(input('Digite o preço: '))
custo = int(input('Digite o custo de fabricação: '))
lucro = int(input('Digite o lucro que conseguiu: '))
valor = carga_tributaria(custo, lucro, preco)
print('A carga tributária total foi {:.2%}'.format(valor))
