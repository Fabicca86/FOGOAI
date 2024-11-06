from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.graphics.texture import Texture
import cv2
import torch

class MyFireDetectionApp(App):
    def build(self):
        self.img = Image()
        layout = BoxLayout(orientation='vertical')
        button = Button(text="Detect Fire", on_press=self.detect_fire)
        layout.add_widget(self.img)
        layout.add_widget(button)
        return layout

    def detect_fire(self, instance):
        # Capturar a imagem da câmera
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        cap.release()

        # Pré-processamento da imagem
        frame = cv2.resize(frame, (640, 640))
        frame = frame / 255.0

        # Lógica de detecção de fogo
        model = torch.hub.load('ultralytics/yolov5', 'custom', path='yolov5s.pt', force_reload=True)
        model.conf = 0.25  # Confidence threshold
        model.iou = 0.45   # IOU threshold for NMS

        results = model(frame)

        # Renderizar a imagem com detecções
        annotated_frame = results.render()[0]

        # Converter a imagem anotada para textura Kivy
        buf1 = cv2.flip(annotated_frame, 0)
        buf = buf1.tobytes()  # Usar tobytes() em vez de tostring()
        texture = Texture.create(size=(annotated_frame.shape[1], annotated_frame.shape[0]), colorfmt='bgr')
        texture.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
        self.img.texture = texture

if __name__ == '__main__':
    MyFireDetectionApp().run()
