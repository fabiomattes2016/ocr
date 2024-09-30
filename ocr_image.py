import pytesseract
import os
import pandas as pd
import cv2
from PIL import Image, ImageEnhance

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\fabio_mattes\AppData\Local\Tesseract-OCR\tesseract.exe'

def obter_coordenadas(evento, x, y, flags, parametros):
    if evento == cv2.EVENT_LBUTTONDOWN:
        print(f"Coordenada inicial: {x}, {y}")
        
        parametros['x_inicial'] = x
        parametros['y_inicial'] = y
    elif evento == cv2.EVENT_LBUTTONUP:
        print(f"Coordenada final: {x}, {y}")
        parametros['x_final'] = x
        parametros['y_final'] = y
        
        x1 = parametros['x_inicial']
        y1 = parametros['y_inicial']
        x2 = parametros['x_final']
        y2 =  parametros['y_final']
        
        # x1, x2 = min(x1, x2), max(x1, x2)
        # y1, y2 = min(y1, y2), max(y1, y2)
        
        # print(f"{x1}, {x2}, {y1}, {y2}")
        
        cv2.rectangle(imagem, (x1, y1), (x2, y2), color=(255,0,0), thickness=2)

        cv2.imshow("Imagem", imagem)
        
        arquivo = 'image.jpg'
        extensao_arquivo = os.path.splitext(arquivo)

        if extensao_arquivo == '.pdf':
            print('Arquivo PDF')
        else:
            print('Arquivo de Imagem')

        image = Image.open('image.jpg')
        image = image.convert('L')
        enhancer = ImageEnhance.Contrast(image)
        image = enhancer.enhance(1)

        image.save('realcada.png')

        image = Image.open('realcada.png')

        # esquerda, superior, direita, inferior
        retangulo = (x1, y1, x2, y2)

        imagem_cortada = image.crop(retangulo)

        imagem_cortada.show()

        data = pytesseract.image_to_string(imagem_cortada, output_type = pytesseract.Output.DICT)
        # df = pd.DataFrame(data)

        # df
        print(data['text'])
        
coordenadas = {
    'x_inicial': 0,
    'y_inicial': 0,
    'x_final': 0,
    'y_final': 0
}

imagem = cv2.imread("image.jpg")
cv2.imshow("Imagem", imagem)
cv2.setMouseCallback("Imagem", obter_coordenadas, coordenadas)
cv2.waitKey(0)
cv2.destroyAllWindows()
