#Tratamento básico de strings - lembrando que python é case sensitive
#Concatenação simples:
print('Meu nome é ' + 'Jua')
#Verifica se a substring existe na string:
print('J' in 'Jua')
#Retorna 'true' ou 'false'

#Input do usuario:
name = input('Qual seu nome?')

#Tipos de variáveis:
#Mostrar o tipo:
gain = 200
type(gain) #Indica que é um tipo interiro
bool_type = False
type(bool_type) #Indica um tipo booleano
number = '100001.1'
type(number) #Indica que é uma string

#Tranformar um valor em string:
gain = 90
print('O lucro foi ' + str(gain))

#Método format:
gain = 90
cost = 50
print('O lucro foi {} e o custo foi {}'. format(gain, cost))

#Uso de f-string:
gain = 90
cost = 50
print(f'O lucro foi {gain} e o custo foi {cost}')

#Casting de variáveis:
