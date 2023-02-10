import cv2
#Recortar a imagem:
#Perde parte da imagem
imagem = cv2.imread("imagem.jpg")
imagemRecortada = imagem[555:100, 100:500]#limita a imagem
cv2.imshow("Imagem Recortada", imagem_recortada)
cv2.imshow("Imagem Original", imagem)
cv2.waitKey(0)

#Redimensionando a imagem:
#Não perde a informação
#Sem arrumar a proporção, a imagem fica modificada:
imagem = cv2.imread("imagem.jpg")
largura_nova = 300
altura_nova = 500
imagem = cv2.resize(imagem, (largura_nova, altura_nova))
cv2.imshow("Imagem Original", imagem)
cv2.waitKey(0)
#Para não perder a proporção:
largura = imagem.shape[1]
altura = imagem.shape[0]
prop = float(altura/largura)#Definir a proporção da imagem
