import cv2

def obter_coordenadas(evento, x, y, flags, parametros):
    if evento == cv2.EVENT_LBUTTONDOWN:
        print(f"Coordenada inicial: {x}, {y}")
        
        parametros['x_inicial'],
        parametros['y_inicial'] = x, y
    elif evento == cv2.EVENT_LBUTTONUP:
        print(f"Coordenada final: {x}, {y}")
        parametros['x_final'],
        parametros['y_final'] = x, y
        
        x1, y1 = parametros['x_inicial'], parametros['y_inicial']
        x2, y2 = parametros['x_final'], parametros['y_final']
        
        # x1, x2 = min(x1, x2), max(x1, x2)
        # y1, y2 = min(y1, y2), max(y1, y2)
        
        print(f"{x1}, {x2}, {y1}, {y2}")
        
        # cv2.rectangle(imagem, (x1, y1), (x2, y2), color=(255,0,0), thickness=2)

        # cv2.imshow("Imagem", imagem)


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

print(f"""Coordenadas selecionadas: 
    {coordenadas['x_inicial']}, {coordenadas['y_inicial']} até
    {coordenadas['x_final']}, {coordenadas['y_final']}
""")