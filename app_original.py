from flask import Flask, request, jsonify
import cv2
from flask_cors import CORS
import torch

app = Flask(__name__)
CORS(app)

@app.route('/detect', methods=['POST'])
def detect_fire():
    # Receber a imagem do pedido
    file = request.files['image']
    file.save('input.jpg')

    # Carregar a imagem
    frame = cv2.imread('input.jpg')

    # Pré-processamento da imagem
    frame = cv2.resize(frame, (640, 640))
    frame = frame / 255.0

    # Lógica de detecção de fogo
    model = torch.hub.load('ultralytics/yolov5', 'custom', path='yolov5s.pt', force_reload=True)
    model.conf = 0.25  # Confidence threshold
    model.iou = 0.45   # IOU threshold for NMS

    results = model([frame])
    # # Anotar a imagem
    # results.render() 
    # annotated_frame = results.imgs[0] 
    # # Salvar imagem anotada em um arquivo temporário 
    # temp_file = 'detected.jpg' 
    # cv2.imwrite(temp_file, annotated_frame) 
    # # # Retornar a imagem anotada como resposta 
    # return send_file(temp_file, mimetype='image/jpeg')
    
    # Extrair resultados
    annotated_frame = results.render()[0]
    _, encoded_img = cv2.imencode('.jpg', annotated_frame)
    encoded_img = encoded_img.tobytes()

    # Retornar a imagem anotada como resposta
    return encoded_img

if __name__ == '__main__':
    app.run(debug=True)
