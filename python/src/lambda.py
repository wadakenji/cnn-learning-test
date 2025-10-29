import base64
from io import BytesIO
from PIL import Image
import numpy as np
from tensorflow.keras.models import load_model

def predict(image, model_type = 'sample_cnn'):
   model_dir = 'src/models/sample_cnn'
   model = load_model(model_dir + '/model.keras')
   predicted = model.predict(np.array([image]))
   return predicted[0][0]

def base64_to_ndarray(b64_data):
    binary = base64.b64decode(b64_data)
    pil_image = Image.open(BytesIO(binary))
    return np.array(pil_image)

def handler(event, context):
    b64_data = event['body']
    image = base64_to_ndarray(b64_data)
    value = predict(image)

    return {'body': value.item()}