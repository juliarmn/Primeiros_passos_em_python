#Estocagem:
#Menos de 100 unidades pedimos 50
#Menos de 20 unidades pedimos 100
estoque = [('A', 90), ('B', 70), ('C', 4), ('D', 20), ('E', 800)]
pedido = [100 if num < 20 else 50 for produto, num in estoque]
print(pedido)
