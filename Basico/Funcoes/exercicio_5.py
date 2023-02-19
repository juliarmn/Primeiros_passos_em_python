#Descobre o servidor do email
def servidor_email(email)
  try:
    indice = email.index('@')
    servidor = email[indice:]
    if 'gmail' in servidor:
      return 'gmail'
    elif 'hotmail' in servidor:
      return 'hotmail'
    elif 'yahoo' in servidor:
      return 'yahoo'
    else:
      print('Servidor não encontrado')
      return
  exception:
    raise Exception('Não tem @-> inválido')
  
      
#raise TypeError: erro do tipo de variável
#raise ValueError: valor errado
#raise ZeroDivisionError
