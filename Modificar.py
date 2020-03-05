import cv2
import glob
i=1
for x in glob.glob("C:/Users/alber/Desktop/Classificador/Neg/*.jpg"):
    imagem = cv2.imread(x, cv2.IMREAD_GRAYSCALE)
    if imagem is not None:
        tamanho_novo = (100, 100)
        img= cv2.resize(imagem,tamanho_novo, interpolation = cv2.INTER_AREA) 
        nome='c:/Users/alber/Desktop/Classificador/Negative/'+str(i)+'.jpg'
        cv2.imwrite(nome,img)
        print(i)
        i=i+1







