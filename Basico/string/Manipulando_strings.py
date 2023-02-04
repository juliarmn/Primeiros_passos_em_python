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
#Outra forma:
texto = 'O valor do produto é {}'
print(texto.format(valor))

#Udo do %:
print('O valor do produto é: %f; \nO custo de produção é: %f' % (valor, custo))
#%s para string

#Ver se existe substring dentro da string:
print('AAAA' in 'aaAAAAbbBBBb')
#retorna true ou false - no caso acima é true

#Métodos das strings:
#capitalize(): Coloca a primeira em maiúscula
nome = 'júlia'
print(nome.capitalize())

#casefold(): Coloca todo o texto em minúsculo
nome_2 = 'JULIA'
print(nome_2.casefold())#pode usar o lower tbm - melhor casefold

#count(): quantas vezes aparece na string essa substring
simbolos = '$$566665555%%%%##'
print(simbolos.count('%'))

#endswith(): Verifica se o texto acaba com aquela substring
email_2 = 'Marta.Silva@gmail.com'
print(email_2.endswith('.com'))
#Retorna true ou false
#É para verificações

#find():
#Procura um texto dentro de outro texto e dá como resposta a posição em que aparece
print(email_2.find('@'))

#isalnum():
#Verifica se a string tem numero e letras
texto_2 = 'Jua123'
print(texto_2.isalnum())#retorna true ou false

#isalpha():
#Verifica se o texto é todo composto de letras:
texto_3 = 'asdasd'
print(texto_3.isalpha())#retorna true ou false

#isnumeric():
#Verifica se o texto é todo composto de letras:
texto_4 = '12323'
print(texto_4.isnumeric())#retorna true ou false

#replace():
#Troca um texto por outro
numero = '1090.80'
print(numero.replace('.', ','))#dois argumentos

#split():
#Separa a string de acordo com algum delimitador
codigo = 'BABABA%123'
print(codigo.split('%'))
#resultado:
#['BABABA', '123']

#Textos de mais de uma linha:
texto_grande = '''
                 Olá, bom dia

                 Como está?
                 '''

#splitlines():
#Divide textos de mais de uma linha no enter
print(texto_grande.splitlines())

#stratswith():
#Verifica se começa com um texto -> como endswith

#strip():
#Retira caracteres "indesejados"
nome_user = ' Julia.rm '
print(nome_user.strip())#retira os espaços extra - retira antes e no final

#title():
#Coloca cada caracter inicial da palavra em maiúsculo
nome_e_sobrenome = 'júlia rodrigues marques do nascimento'
print(nome_e_sobrenome.title())

#upper():
#Texto todo em letra maiúscula:
cod = 'asdasdasdasd'
print(cod.upper())


#Formatações com o format: pode combinar eles
#{:<tam_texto} texto alinhado à esquerda do tam_texto caracteres
#{:>tam_texto} texto alinhado à direita do tam_texto caracteres
#{:^tam_texto} texto alinhado no centro de acordo com o tam_texto
#{:+} coloca sempre o sinal do número (+ ou -)
#{:,} coloca a vírgula como separador de milhar
#{:2f} coloca 2 casas decimais em f -> número float
#{:2%} coloca em formato de percentual, com 2 casas decimais
#{:,.2f} formato de moeda


#Função round():
#Faz arredondamento
#round(valor, 2) -> arredonda o valor em 2 casas decimais
