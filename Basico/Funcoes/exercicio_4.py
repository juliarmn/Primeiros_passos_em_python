#Modelo de precisão
precos = [2.17, 1.54, 1.454, 1.94, 2.37, 2.3, 1.79, 1.8, 2.25, 1.37]
tam = [207, 148, 130, 201, 257, 228, 160, 194, 232, 147]
#Fator de divisão da lista
fator = 0.4
i = int((1 - fator) * len(tam))
precos_1 = precos[:i]
precos_2 = preco[i:]
print(precos_1'\n'precos_2)

 #Função:
 def separar_lista(fator, precos, tamanhos)
    if len(precos) == len(tamanhos):
      i = int((1 - fator) * len(precos))
        preco_1 = precos[:i]
        preco_2 = precos[i:]
        tamanho_1 = tamanhos[:i]
        tamanho_2 = tamanhos[i:]
        return preco_1, preco_2, tamanho_1, tamanho_2
      return
    else:
      print('Listas de tamanhos diferentes')
      return
#Chama essa função e imprime depois os resultados
