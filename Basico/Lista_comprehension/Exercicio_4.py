#% das vendas totais dos top 3 produtos:
i = 0
top_3 = []
total = 0
produtos = [(300, 'A'), (789, 'B'), (756, 'C'), (908, 'D'), (33, 'E'), (456, 'F'), (890, 'G')]
for num, prod in produtos:
    total += num
print(total)
produtos.sort(reverse=True)
while i < 3:
    top_3.append(produtos[i])
    i += 1
print(top_3)
total_top_3 = 0
total_top_3 = sum(num for num, produto in top_3)
print(total_top_3)
print('% Top 3 do total: {:0.2%}'.format(total_top_3 / total))
