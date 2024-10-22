""" import tensorflow as tf
import numpy as np
from PIL import Image

def classify_image(image_path):
    model = tf.keras.models.load_model('path_to_your_model.h5')

    # Cargar la imagen y procesarla
    img = Image.open(image_path).resize((224, 224))  # Ajusta el tamaño según lo que requiera tu modelo
    img_array = np.array(img) / 255.0  # Normalizar la imagen
    img_array = np.expand_dims(img_array, axis=0)  # Agregar una dimensión extra para lotes

    predictions = model.predict(img_array)
    predicted_class = np.argmax(predictions[0])  # Clase con mayor probabilidad
    confidence = np.max(predictions[0])  # Confianza de la predicción

    return {"class": predicted_class, "confidence": confidence}
 """