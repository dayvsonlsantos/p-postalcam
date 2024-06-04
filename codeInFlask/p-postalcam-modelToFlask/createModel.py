import cv2
import numpy as np
import os
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense, Dropout, GlobalAveragePooling2D
from keras.src.legacy.preprocessing.image import ImageDataGenerator
from keras.applications import MobileNetV2
from keras.optimizers import Adam

# Função para carregar e pré-processar as imagens
def load_images_from_folder(folder, label):
    images = []
    labels = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder, filename))
        if img is not None:
            img = cv2.resize(img, (224, 224))  # Redimensionar a imagem para o tamanho desejado
            images.append(img)
            labels.append(label)
    return images, labels

# Carregar as imagens de cada classe
pessoa_images, pessoa_labels = load_images_from_folder("Dataset/train/Pessoas", 0)
pacote_images, pacote_labels = load_images_from_folder("Dataset/train/Pacotes", 1)
pessoas_e_pacotes_images, pessoas_e_pacotes_labels = load_images_from_folder("Dataset/train/Pessoas_e_Pacotes", 2)

# Concatenar todas as imagens e rótulos
images = np.array(pessoa_images + pacote_images + pessoas_e_pacotes_images)
labels = np.array(pessoa_labels + pacote_labels + pessoas_e_pacotes_labels)

# Dividir os dados em conjuntos de treinamento e teste
train_images, test_images, train_labels, test_labels = train_test_split(images, labels, test_size=0.2, random_state=42)

# Normalizar os valores dos pixels das imagens para o intervalo [0, 1]
train_images = train_images / 255.0
test_images = test_images / 255.0

# Data augmentation
datagen = ImageDataGenerator(
    rotation_range=30,
    width_shift_range=0.2,
    height_shift_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    vertical_flip=True
)
datagen.fit(train_images)

# Usar MobileNetV2 pré-treinado como base
base_model = MobileNetV2(include_top=False, input_shape=(224, 224, 3))
base_model.trainable = False  # Congelar as camadas convolucionais pré-treinadas

# Definir a arquitetura do modelo
model = Sequential([
    base_model,
    GlobalAveragePooling2D(),
    Dense(256, activation='relu'),
    Dropout(0.5),
    Dense(3, activation='softmax')
])

# Criar o otimizador Adam
optimizer = Adam(learning_rate=1e-4)

# Compilar o modelo com o otimizador criado
model.compile(optimizer=optimizer,
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Treinar o modelo com data augmentation
history = model.fit(datagen.flow(train_images, train_labels, batch_size=32),
                    epochs=50,
                    validation_data=(test_images, test_labels))

# Avaliar o modelo
test_loss, test_acc = model.evaluate(test_images, test_labels)
print('Acurácia do teste:', test_acc)

# Fazer previsões
predictions = model.predict(test_images)

# Salvar o modelo treinado como um arquivo .h5
model.save("Model/modelo5.h5")