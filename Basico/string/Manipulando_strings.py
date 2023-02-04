#Inicialização da string:
str_1 = input('Digite a string: ')
str_2 = 'Julia Rodrigues'

#Tamanho da string - número de caracteres:
str_3 = 'mandarim'
print(len(str_3))

#Pegar/analizar um caracter específico:
texto = 'Hoje é sábado'
indice = 1
print(texto[indice])

#Índice negativo:
#Pega o texto de trás para frente
email = 'maria.h@gmail.com'
print(email[-3])
#printa o caractere na posição 3 de trás para frente, iniciando no -1

#Imprimir o texto até uma posicao
print(email[:-4]) #imprime o texto até o índice -4, não pega o índice -4
#Pode também fazer com o número de índice positivo, o da sua preferência:
print(email[:-13])#Mesma coisa do de cima

#Imprimir o texto de uma posição específica até o final:
print(email[7:]) #Nesse caso inclui a posição 7
#Saída = @gmail.com

#Delimitar o texto, imprimindo do indice x até o índice y
print(email[7:13])#Imprime do índice 7 até o índice 12

#Operações com string:
#Transformar em string:
Valor = 5.5
print('O valor do produto é ' + str(valor))
#Sinal de +: concatenar as strings

#Format:
print('O valor do produto é {}'.format(valor))
custo = 2.5
print('O valor do produto é {} e o custo de produção é {}'.format(valor, custo))
#Outra forma:
print('{0}  {1}  {0} '.format(valor, custo))#Imprime valor custo valor

#Udo do %:
print('O valor do produto é: %f; \nO custo de produção é: %f' % (valor, custo))
#%s para string

#Ver se existe substring dentro da string:
print('AAAA' in 'aaAAAAbbBBBb')
#retorna true ou false - no caso acima é true

#Métodos das strings:

