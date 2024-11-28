from flask import Flask, request, send_file, jsonify
import cv2
from flask_cors import CORS
import torch
import json
from io import BytesIO
import base64
import pandas as pd
from metrics_app import plot_detection_metrics

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
    _, buffer = cv2.imencode('.jpg', annotated_frame) 
    encoded_image = base64.b64encode(buffer).decode('utf-8') 
    location = request.form.get('location', "{}") 
    gps_info = json.loads(location) # Use json.loads() for safety 
    print(f"GPS Info: {gps_info}") 
    ##TESTEEEE
    # Log results to a CSV file 
    df = pd.DataFrame({ 
         'class': results.pred[0][:, -1].cpu().numpy(), 
         'confidence': results.pred[0][:, 4].cpu().numpy(), 
         'x1': results.pred[0][:, 0].cpu().numpy(), 
         'y1': results.pred[0][:, 1].cpu().numpy(), 
         'x2': results.pred[0][:, 2].cpu().numpy(), 
         'y2': results.pred[0][:, 3].cpu().numpy() 
    }) 
    df.to_csv('detection_results.csv', mode='a', header=False, index=False)

    return jsonify({ 'image': encoded_image, # Send base64 encoded image
                     'gps_info': gps_info 
                     }) 

@app.route('/plot_metrics', methods=['GET']) 
def plot_metrics(): 
    plot_detection_metrics() 
    with open('detection_metrics.png', 'rb') as f: 
        encoded_image = base64.b64encode(f.read()).decode('utf-8') 
        return jsonify({'plot': encoded_image})

if __name__ == '__main__': 
        print("Running Flask app...") 
        app.run(debug=True)