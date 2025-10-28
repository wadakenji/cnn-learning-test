import numpy as np
import argparse
from PIL import Image
from utils.plot import plot_history
from models.sample_cnn.model import sample_cnn
from data.get_data import images_train, labels_train

IMAGE_SHAPE = (32, 32, 3)
BATCH_SIZE = 495

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--model')
    parser.add_argument('--epochs')
    args = parser.parse_args()

    if (args.model is None or args.model == 'sample_cnn'):
        model = sample_cnn(IMAGE_SHAPE)
        model_dir = 'src/models/sample_cnn'
    else:
        raise Exception('invalid model arg')

    epochs = 100
    if (args.epochs is not None):
        epochs = int(args.epochs)

    model.compile(optimizer='Adam',
                  loss='mean_squared_error',
                  metrics=['mean_absolute_error'])

    result = model.fit(images_train, labels_train,
                       batch_size=BATCH_SIZE,
                       epochs=epochs,
                       verbose=1,
                      )

    model.save(model_dir + '/model.keras')

    plot_history(result, model_dir)
    
