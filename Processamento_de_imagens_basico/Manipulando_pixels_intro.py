import cv2

imagem = cv2.imread("imagem.jpg")#BGR - open cv
print(imagem)
cv2.imshow("Imagem", imagem)
cv2.waitKey(0)

#Alterando valores de pixels:
imagem[0][0] = (255, 255, 255) #tupla
#todos 255: cor branca
#Modifica só 1 pixel

#Mudar mais de um pixel
imagem[0:10, 0:10] = (255, 255, 255)
cv2.imshow("Imagem", imagem)
cv2.waitKey(0)

#Alterar dinamicamente os pixels com estruturas de repetição:
branco = (255, 255, 255)
preto = (0, 0, 0)
