from flask import Flask, request, send_file
import cv2
from flask_cors import CORS
import torch
import numpy as np

app = Flask(__name__)
CORS(app)

@app.route('/detect', methods=['POST'])
def detect_fire():
    print("Received POST request...")  # Log para verificar recebimento do pedido

    # Receber a imagem do pedido
    file = request.files['image']
    file.save('input.jpg')
    print("Image saved...")  # Log para verificar salvamento da imagem

    # Carregar a imagem
    frame = cv2.imread('input.jpg')
    print("Image loaded...")  # Log para verificar carregamento da imagem

    # Pré-processamento da imagem
    frame = cv2.resize(frame, (640, 640))
    print("Image resized...")  # Log para verificar redimensionamento da imagem

    # Lógica de detecção de fogo
    model = torch.hub.load('ultralytics/yolov5', 'custom', path='yolov5s.pt', force_reload=False)  # Desabilitar force_reload temporariamente
    print("Model loaded...")  # Log para verificar carregamento do modelo

    model.conf = 0.25  # Confidence threshold
    model.iou = 0.45   # IOU threshold for NMS

    results = model([frame])
    print("Detection done...")  # Log para verificar finalização da detecção

    # Anotar a imagem
    results.render()  # Modifica a imagem original

    # Verificar se a imagem renderizada está no atributo 'ims' ou 'imgs'
    if hasattr(results, 'ims'):
        annotated_frame = results.ims[0]
    elif hasattr(results, 'imgs'):
        annotated_frame = results.imgs[0]
    else:
        print("Erro: Imagem renderizada não encontrada")
        return "Erro ao processar a imagem", 500

    # Converter o formato da imagem de volta para BGR se necessário
    annotated_frame = cv2.cvtColor(annotated_frame, cv2.COLOR_RGB2BGR)

    # Salvar imagem anotada em um arquivo temporário
    temp_file = 'detected.jpg'
    cv2.imwrite(temp_file, annotated_frame)
    print("Annotated image saved...")  # Log para verificar salvamento da imagem anotada

    # Retornar a imagem anotada como resposta
    return send_file(temp_file, mimetype='image/jpeg')

if __name__ == '__main__':
    print("Running Flask app...")  # Log para verificar início da execução do Flask
    app.run(debug=True)
