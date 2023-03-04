#Tudo é um objeto no Python
#Objetos: possuem características específicas e métodos nele
#Uso de bibliotecas prontas
#Módulos são arquivos com códigos com objetos já prontos, junto com seus métodos
#Estrutura:
import numpy #numpy = nome do módulo
import numpy as np #np = nome para referenciar
#Abrir um site específico na internet:
import webbrowser
webbrowser.open("https://google.com")
#Pode importar tudo:
from numpy import *
#Pode importar só uma função específica também
#Uso em automações: módulo selenium


#Módulo time
import time
#marco zero: EPOCH (01/01/1970)
#contagem em segundos desde o marco 0
segundos_passados = time.time()
data_hoje = time.ctime()#data de hoje formatada - formato UTC
#Medir o tempo que uma ação leva:
tempo_inicio = time.time()
for i in range(1000000000):
  pass
tempo_final = time.time()
duracao = tempo_final - tempo_inicio
print(duracao)
#Código esperando alguhns segundos:
time.sleep(6)#espera 6 segundos para rodar
#Pegar informações de data atual:
data = time.gmtime()
#OU:
ano = data_atual.tm_year
mes = data_atual.tm_mon
#etc: tm_mday, tm_hour, tm_wday
#Nenhum parâmetro -> data atual

#Pegar os maiores valores de um dicionário
from collections import Counter
cores = {'azul': 300, 'rosa': 1900, 'vermelho': 550, 'amarelo': 980, 'lilás': 3900}

aux = Counter(cores).most_common(3)
print(aux)#Retorna uma lista com as tuplas dos 3 maiores

#Gráficos:
import matplotlib.pyplot as plt
vendas = [2000, 345, 6665, 890, 998]
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio']
plt.plot(meses, vendas)
plt.ylabel('Vendas')
plt.xlabel('Meses')
plt.axis([0, 5, 0, 7000])                         
plt.show()
#Podemos importar o numpy para gerar números e dados
import numpy as np
vendas = np.random.randit(1000, 8000, 10)#gera um número inteiro entre o min, max e quantidade
meses = np.arange(1, 11)
#Tipo de gráfico
plt.plot(meses, vendas, 'g^')
plt.plot(meses, vendas, 'bo')
plt.plot(meses, vendas, 'ro')#Vários tipos diferentes
