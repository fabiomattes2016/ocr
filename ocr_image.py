import pytesseract
import os
import pandas as pd
from PIL import Image, ImageEnhance

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\fabio_mattes\AppData\Local\Tesseract-OCR\tesseract.exe'

arquivo = 'image.jpg'
extensao_arquivo = os.path.splitext(arquivo)

if extensao_arquivo == '.pdf':
    print('Arquivo PDF')
else:
    print('Arquivo de Imagem')

image = Image.open('image.jpg')
image = image.convert('L')
enhancer = ImageEnhance.Contrast(image)
image = enhancer.enhance(2)

image.save('realcada.png')

image = Image.open('realcada.png')

# esquerda, superior, direita, inferior
retangulo = (275, 290, 1080, 350)
imagem_cortada = image.crop(retangulo)

imagem_cortada.show()

data = pytesseract.image_to_string(imagem_cortada, output_type = pytesseract.Output.DICT)
# df = pd.DataFrame(data)

# df
print(data['text'])
