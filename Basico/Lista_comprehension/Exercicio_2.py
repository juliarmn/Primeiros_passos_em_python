#Achar clientes inadimplentes:
#cpf, dinheiro, dias
#Devem mais de 5000 com mais de 20 dias
clientes = [('560.035.850-48', 5000, 21), ('605.289.020-75', 6000, 20), ('489.058.220-70', 700, 39), ('943.245.470-33', 7000, 30)]

lista_inadimplentes = [(cpf, quantidade, dias) for cpf, quantidade, dias in clientes if quantidade > 5000 and dias > 20]
print(lista_inadimplentes)
