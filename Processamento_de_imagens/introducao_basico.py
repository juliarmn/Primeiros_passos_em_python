#Uma imagem é composta por 3 canais de cores:
#RGB(Red, Green and Blue)
import cv2
#0: nada da cor
#255: maximo da cor
#Uso de listas para representar as cores:
[255, 0, 0]#Forma a cor vermelha
[0, 255, 0]#forma a cor verde
[0, 0, 255]#Forma a cor azul
#A imagem será uma matriz em que para cada pixel, teremos um valor RGB
#É uma matriz tridimensional
#Método imread() -> cv2:
#Pega a imagem e transforma ela em uma matriz tridimensional RGB
