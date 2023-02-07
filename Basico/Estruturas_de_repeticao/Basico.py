#for: repetição do comando
produtos = ['coca', 'guaraná', 'suco', 'cerveja']
producao = [100, 2000, 550, 3200]
tamanho = len(produtos)
for i in range(tamanho):
  print('Produto: {};\nProdução: {}\n\n'.format(produtos[i], producao[i]))
  print('---------------------------------------------')
#i é o índice e é incrementado a cada iteração

#for each: forma de manipular cada item da lista, sem o uso do índice:
for produto in produtos:
  print('O produto é {}'.format(produto))#Printa cada item

#Enumerate:
#Pega o item e variável
funcionarios = ['Júlia', 'Gabriel', 'Paula', 'Diego']
for func,i in enumerate(funcionarios):
  print('Nome: {};\nÍndice: {}\n\n'.format(func, i))
  print('---------------------------------------------')
  
#Continue e break:
#break: interrompe e sai do laço
fruta = ['maçã', 'abacate', 'abacaxi', 'melancia'] 
for item in fruta:
  if item == 'abacaxi':
    break
tam = len(fruta)
for i in range(tam):
  if fruta[i] == 'abacate':
    continue
  else: 
    print(fruta[i])

    
#while:
#while(condição): -> executa o codigo enquanto for satisfeito
#Deve incrementar o índice
cor = input('Digite uma cor: ')
cores = []
while cor != '':
  cores.append(cor)
  cor = input('Digite outra cor: (Para sair basta não inserir cor nenhuma e dar enter)\n')
print('As cores foram: ')
print(cores)
