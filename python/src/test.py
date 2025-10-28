import argparse
from tensorflow.keras.models import load_model
from data.get_data import images_test, labels_test

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--model')
    args = parser.parse_args()

    if (args.model is None or args.model == 'sample_cnn'):
        model_dir = 'src/models/sample_cnn'
    else:
        raise Exception('invalid model arg')

    model = load_model(model_dir + '/model.keras')
    score = model.evaluate(images_test, labels_test, verbose=1)
    print('Test loss: ', score[0])
    print('Test mae: ', score[1])
    