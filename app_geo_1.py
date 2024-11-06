from flask import Flask, request, send_file, jsonify
import cv2
from flask_cors import CORS
import torch
import numpy as np

app = Flask(__name__)
CORS(app)

@app.route('/detect', methods=['POST'])
def detect_fire():
    print("Received POST request...")

    file = request.files['image']
    file_path = 'input.jpg'
    file.save(file_path)
    print("Image saved...")

    frame = cv2.imread(file_path)
    print("Image loaded...")

    frame = cv2.resize(frame, (640, 640))
    print("Image resized...")

    model = torch.hub.load('ultralytics/yolov5', 'custom', path='yolov5s.pt', force_reload=False)
    print("Model loaded...")

    model.conf = 0.25
    model.iou = 0.45

    results = model([frame])
    print("Detection done...")

    results.render()

    if hasattr(results, 'ims'):
        annotated_frame = results.ims[0]
    elif hasattr(results, 'imgs'):
        annotated_frame = results.imgs[0]
    else:
        print("Erro: Imagem renderizada não encontrada")
        return "Erro ao processar a imagem", 500

    annotated_frame = cv2.cvtColor(annotated_frame, cv2.COLOR_RGB2BGR)

    temp_file = 'detected.jpg'
    cv2.imwrite(temp_file, annotated_frame)
    print("Annotated image saved...")

    location = request.form.get('location', "{}")  # Obtém a localização do formulário
    gps_info = eval(location)  # Avalia a string JSON como um dicionário

    print(f"GPS Info: {gps_info}")

    return jsonify({
        'image': temp_file,
        'gps_info': gps_info
    })

if __name__ == '__main__':
    print("Running Flask app...")
    app.run(debug=True)
