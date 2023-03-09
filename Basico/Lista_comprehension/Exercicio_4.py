#% das vendas totais dos top 3 produtos:
form collections import Counter
produtos = [('A', 300), ('B', 789), ('C', 726), ('D', 908), ('E', 33), ('F', 456), ('G', 890)]
top_3 = Counter(produtos).most_common(3)
print(top_3)
