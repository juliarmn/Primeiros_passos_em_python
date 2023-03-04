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
