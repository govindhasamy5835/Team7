import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array

model = load_model("model/skin_cancer_cnn.h5")

def predict_skin_cancer(image):
    image = image.resize((64, 64))
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0) / 255.0
    prediction = model.predict(image)
    return "Malignant" if prediction[0][0] > 0.5 else "Benign"