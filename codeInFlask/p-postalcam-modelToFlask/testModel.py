import cv2
import numpy as np
from keras.models import load_model

# Carregar o modelo treinado
model = load_model("Model/modelo5.h5")

# Função para pré-processar uma imagem de teste
def preprocess_image(image_path):
    img = cv2.imread(image_path)
    img = cv2.resize(img, (224, 224))  # Atualizar para 224x224 para compatibilidade com MobileNetV2
    img = img / 255.0
    return img.reshape(1, 224, 224, 3)

# Função para prever a classe de uma imagem
def predict_class(image_path):
    img = preprocess_image(image_path)
    prediction = model.predict(img)
    class_index = np.argmax(prediction)
    if class_index == 0:
        return "Pessoa"
    elif class_index == 1:
        return "Pacote"
    elif class_index == 2:
        return "Pessoas e Pacotes"

# Testar o modelo com uma imagem de teste
image_path = "Dataset/test/imgPePa2.png"
predicted_class = predict_class(image_path)
print("Classe prevista:", predicted_class)
