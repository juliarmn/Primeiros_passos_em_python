#Código simples e introdutório do algoritmo do tipo Perceptron
x_input = [0.3, 0.9, 0.8, 0.4]
w_weight = [0.2, 0.1, 0.5, 0.7]
bias = 0.6

#Funções:
#Função para y (saída):
def y_output(sum_weight):
  if sum_weight > bias:
    return 1
  else:
    return 0
  
def perceptron():
  sum_weight = 0
  for x, w in zip(x_input, w_weight):#zip = retorna uma lista de tuplas contendo os pares ordenados
    sum_weight += x * w
  return sum_weight

print('A soma total é {}'.format(perceptron()))
print('A saída é {}'.format(y_output(perceptron())))
