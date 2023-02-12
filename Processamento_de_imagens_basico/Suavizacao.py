#Suavização - blur:
import cv2

imagem = cv2.imread("imagem.jpg")

#Mudar o foco:
#Definir o tamanho do blur - sempre ímpar para ter um pixel central:
#Pela média aritmética:
for i in range(0, imagem.shape[0], 20):
    for j in range(0, imagem.shape[1], 20):
        imagem[i:i+3, j:j+3] = (255, 255, 255)

blur_img = cv2.blur(imagem, (15,21))#tamanho da suavização

cv2.imshow("Imagem", blur_img)
cv2.waitKey(0)
#Observe que o pixel branco não é mais totalmmente branco

#---------------------------Próximo código------------------

#Suavização pela mediana -diminui a distorção da imagem por pixels foora do padrão:
#Faz o sort e acha a mediana
#Não cria valor novo, mas usa um valor já existente

import cv2

imagem = cv2.imread("imagem.jpg")

for i in range(0, imagem.shape[0], 20):
    for j in range(0, imagem.shape[1], 20):
        imagem[i:i+3, j:j+3] = (255, 255, 255)

blur_img_1 = cv2.medianblur(imagem, 6)
blur_img_2 = cv2.medianblur(imagem, 11)

cv2.imshow("Imagem", blur_img_1)
cv2.imshow("Imagem 2", blur_img_2)
cv2.waitKey(0)
