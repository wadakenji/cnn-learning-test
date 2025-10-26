import numpy as np
import _pickle,random
from PIL import Image
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D
from tensorflow.keras.layers import Flatten, Dense, Dropout, BatchNormalization

IMAGE_SHAPE = (32, 32, 3)
BATCH_SIZE = 495

# ファイルを読み込む
# cf. https://qiita.com/lumbermill/items/010920d264806b903e5f
def unpickle(file):
    fo = open(file, 'rb')
    dict = _pickle.load(fo, encoding='latin-1')
    fo.close()
    return dict

# 長さ1024の配列の配列
# ↓
# 長さ(32,32,3)の3次元配列の配列
def vectors_to_images(vector_arr):
    image_data_arr = []

    for index, vector in enumerate(vector_arr):
        if index % 3 != 0 : continue
        r = vector_arr[index]
        g = vector_arr[index+1]
        b = vector_arr[index+2]
        data = np.array([r,g,b]).T.reshape(32,32,3)
        image_data_arr.append(data)

    return image_data_arr

# データセットのファイルを画像データとラベルにフォーマット
def get_images_and_labels(filename):
    file_data = unpickle(filename)
    labels = file_data['labels']
    vectors = file_data['data']
    images = vectors_to_images(vectors)
    return [images, labels]

# 以下の記事で使用されていたモデル
# https://www.yakupro.info/entry/cnn-regression
def sample_cnn(input_shape):
    model = Sequential()
    model.add(Conv2D(16, (3, 3), activation='relu', input_shape=input_shape))
    model.add(Conv2D(32, (3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Conv2D(64, (3, 3),activation='relu'))
    model.add(Dropout(0.3))
    model.add(Flatten())
    model.add(Dense(500, activation='relu'))
    model.add(BatchNormalization())
    model.add(Dropout(0.3))
    model.add(Dense(10, activation='relu'))
    model.add(Dense(1, activation='linear'))
    model.summary()
    return model

if __name__ == "__main__":
    # images_1, labels_1 = get_images_and_labels('src/data/cucumber-9-python/data_batch_1')
    # images_2, labels_2 = get_images_and_labels('src/data/cucumber-9-python/data_batch_2')
    # images_3, labels_3 = get_images_and_labels('src/data/cucumber-9-python/data_batch_3')
    # images_4, labels_4 = get_images_and_labels('src/data/cucumber-9-python/data_batch_4')
    # images_5, labels_5 = get_images_and_labels('src/data/cucumber-9-python/data_batch_5')
    print(tf.__version__)
    model = sample_cnn(IMAGE_SHAPE)
    print(model)
