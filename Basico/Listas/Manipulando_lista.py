#Estrutura básica
lista_de_frutas = ['maçã', 'laranja', 'goiaba', 'banana']
#Recomendado ser listahomogênea

#Manipular um índice da lista:
print(lista_de_frutas[0])

#Obs: string é imutável, não é possível pegar um item da string e mudar ele, trocar a letra
#Usa a função replace, porém ela muda todas os símbolos iguais ao longo da string:
#Error:
email = 'jua.rod@gmail.com'
email[1] = 'a'
#Mudaria todas iguais:
email = 'jua.rod@gmail.com'
print(email.replace('a', 'i'))


#Descobrindo o índice de um elemento da lista:
lista = ['a', 'b', 'c']
i = lista.index('a')
