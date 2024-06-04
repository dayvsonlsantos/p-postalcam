from flask import Flask, render_template, Response, jsonify
from keras.models import load_model
import cv2
import numpy as np
from datetime import datetime
import json
from time import sleep

app = Flask(__name__)

# Carregar o modelo treinado
model = load_model("Model/modelo5.h5")

# Lista para armazenar as previsões
predictions_log = []

# Função para pré-processar uma imagem da câmera
def preprocess_frame(frame):
    img = cv2.resize(frame, (224, 224))  # Atualizar para 224x224 para compatibilidade com MobileNetV2
    img = img / 255.0
    return img.reshape(1, 224, 224, 3)

# Função para prever a classe de uma imagem
def predict_class(frame):
    img = preprocess_frame(frame)
    prediction = model.predict(img)
    class_index = np.argmax(prediction)
    if class_index == 0:
        return "Pessoa"
    elif class_index == 1:
        return "Pacote"
    elif class_index == 2:
        return "Pessoas e Pacotes"

def generate_frames():
    camera = cv2.VideoCapture(0)
    while True:
        success, frame = camera.read()
        if not success:
            print("Erro ao ler frame da câmera")
            break
        else:
            # Fazer a previsão
            predicted_class = predict_class(frame)
            # print("Classe prevista:", predicted_class)
            
            # Adicionar previsão ao log
            if predicted_class == "Pessoas e Pacotes":
                print("Uma possível encomenda, pode ter sido detectada em sua porta")
                # Adicionar previsão ao log
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                predictions_log.append((timestamp, "Uma possível encomenda, pode ter sido detectada em sua porta"))

            # Codificar o frame em JPEG
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()

            # Usar o frame como um gerador de bytes
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/predictions_stream')
def predictions_stream():
    def generate():
        while True:
            sorted_predictions = sorted(predictions_log, key=lambda x: x[0], reverse=True)
            yield 'data: %s\n\n' % json.dumps(sorted_predictions)
    return Response(generate(), mimetype='text/event-stream')

if __name__ == "__main__":
    app.run(debug=True)
