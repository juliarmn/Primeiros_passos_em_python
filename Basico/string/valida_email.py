email = input('Digite seu email: ')
arroba = email.find('@')
servidor = email[arroba:]
if arroba != -1 and '.' in  servidor:
  print('Email válido \nCadastro concluído.')
else:
  print('Digite um email válido!')
