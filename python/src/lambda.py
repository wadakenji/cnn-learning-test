import numpy as np
from tensorflow.keras.models import load_model

def predict(image, model_type = 'sample_cnn'):
   model_dir = 'src/models/sample_cnn'
   model = load_model(model_dir + '/model.keras')
   predicted = model.predict(np.array([image]))
   return predicted[0][0]

def handler(event, context):
    #     data = np.zeros((32,32,3))
    #     value = predict(data)

    print('##################################')
    print(event)
    print('##################################')
    print(context)
    print('##################################')

    return 'hello world'